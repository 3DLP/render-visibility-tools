bl_info = {
    "name": "Render Visibility Tools",
    "author": "3DLP, with AI assistance",
    "version": (1, 2, 0),
    "blender": (3, 6, 0),
    "location": "Object > Render Visibility Tools",
    "description": "Quickly manage render visibility for selected objects, scene objects and collections.",
    "category": "Object",
}

import bpy


def get_selected_objects(context):
    return [obj for obj in context.selected_objects if obj is not None]


def get_scene_objects(context):
    return [obj for obj in context.scene.objects if obj is not None]


def get_scene_collections(context):
    collections = []

    def walk_collection(collection):
        collections.append(collection)
        for child in collection.children:
            walk_collection(child)

    walk_collection(context.scene.collection)
    return collections


class RVT_OT_hide_selected_render(bpy.types.Operator):
    bl_idname = "rvt.hide_selected_render"
    bl_label = "Hide Selected in Render"
    bl_description = "Disable render visibility for selected objects"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        objects = get_selected_objects(context)
        if not objects:
            self.report({"WARNING"}, "No selected objects")
            return {"CANCELLED"}
        for obj in objects:
            obj.hide_render = True
        self.report({"INFO"}, f"{len(objects)} selected object(s) hidden from render")
        return {"FINISHED"}


class RVT_OT_show_selected_render(bpy.types.Operator):
    bl_idname = "rvt.show_selected_render"
    bl_label = "Show Selected in Render"
    bl_description = "Enable render visibility for selected objects"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        objects = get_selected_objects(context)
        if not objects:
            self.report({"WARNING"}, "No selected objects")
            return {"CANCELLED"}
        for obj in objects:
            obj.hide_render = False
        self.report({"INFO"}, f"{len(objects)} selected object(s) shown in render")
        return {"FINISHED"}


class RVT_OT_sync_all_viewport_to_render(bpy.types.Operator):
    bl_idname = "rvt.sync_all_viewport_to_render"
    bl_label = "Sync All Viewport -> Render"
    bl_description = "Set render visibility according to viewport visibility for all objects in the scene"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        objects = get_scene_objects(context)
        if not objects:
            self.report({"WARNING"}, "No objects in scene")
            return {"CANCELLED"}

        hidden_count = 0
        visible_count = 0

        for obj in objects:
            should_hide_in_render = obj.hide_get() or obj.hide_viewport
            obj.hide_render = should_hide_in_render
            if should_hide_in_render:
                hidden_count += 1
            else:
                visible_count += 1

        self.report({"INFO"}, f"Viewport synced to render: {visible_count} visible, {hidden_count} hidden")
        return {"FINISHED"}


class RVT_OT_show_all_scene_render(bpy.types.Operator):
    bl_idname = "rvt.show_all_scene_render"
    bl_label = "Show All Objects and Collections in Render"
    bl_description = "Enable render visibility for all objects and collections in the current scene"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        objects = get_scene_objects(context)
        collections = get_scene_collections(context)

        if not objects and not collections:
            self.report({"WARNING"}, "No objects or collections in scene")
            return {"CANCELLED"}

        for obj in objects:
            obj.hide_render = False

        for collection in collections:
            collection.hide_render = False

        self.report({"INFO"}, f"{len(objects)} object(s) and {len(collections)} collection(s) shown in render")
        return {"FINISHED"}


class RVT_MT_render_visibility_tools(bpy.types.Menu):
    bl_label = "Render Visibility Tools"
    bl_idname = "RVT_MT_render_visibility_tools"

    def draw(self, context):
        layout = self.layout

        layout.label(text="Selected Objects")
        layout.operator("rvt.hide_selected_render", icon="HIDE_ON")
        layout.operator("rvt.show_selected_render", icon="HIDE_OFF")

        layout.separator()

        layout.label(text="All Scene")
        layout.operator("rvt.sync_all_viewport_to_render", icon="FILE_REFRESH")
        layout.operator("rvt.show_all_scene_render", icon="RESTRICT_RENDER_OFF")


def draw_object_menu(self, context):
    self.layout.separator()
    self.layout.menu(RVT_MT_render_visibility_tools.bl_idname, icon="RESTRICT_RENDER_OFF")


classes = (
    RVT_OT_hide_selected_render,
    RVT_OT_show_selected_render,
    RVT_OT_sync_all_viewport_to_render,
    RVT_OT_show_all_scene_render,
    RVT_MT_render_visibility_tools,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_object.append(draw_object_menu)


def unregister():
    bpy.types.VIEW3D_MT_object.remove(draw_object_menu)
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
