# Render Visibility Tools

A small Blender addon for quickly isolating objects for rendering in large scenes by synchronizing viewport visibility with render visibility.

It was created from a real Blender project that became heavy, with hundreds of objects and an Outliner that was not always as clean as originally planned.

> For Blender scenes that start well organized... and somehow end up with 400 objects and an Outliner telling another story.

## Why this addon?

In large Blender scenes, preparing a render can become tedious when hundreds of objects are involved.

Render Visibility Tools lets you use the viewport as a quick render setup:

1. Hide everything you do not need in the viewport.
2. Keep only the object or group you want to render visible.
3. Run **Sync All Viewport → Render**.
4. Start the render.

This makes it possible to render individual objects or small groups without manually searching through hundreds of entries in the Outliner or changing each render visibility setting one by one.

The addon is especially useful during creative work, when organizing every object and collection immediately would interrupt the workflow.

**Create first, organize when needed, and keep control of the render.**

Blender already provides several ways to manage render visibility, including the Outliner, visibility icons, shortcuts, and context operations.

This addon does not try to replace Blender's native tools. Its purpose is to group a few practical render visibility commands into one simple menu.

## Features

The addon adds a submenu here:

`Object > Render Visibility Tools`

![Render Visibility Tools menu](menu_screenshot.jpg)

### Selected Objects

#### Hide Selected in Render

Disables render visibility for the selected objects.

#### Show Selected in Render

Enables render visibility for the selected objects.

### Entire Scene

#### Sync All Viewport → Render

Sets the render visibility of all scene objects according to their current viewport visibility.

Objects hidden in the viewport are hidden from rendering, while visible objects remain enabled for rendering.

#### Show All Objects and Collections in Render

Restores render visibility for every object and collection in the current scene.

This provides a quick way to reset the scene after preparing individual or temporary renders.

## Collections

The addon does not hide collections from rendering.

The **Sync All Viewport → Render** command synchronizes object visibility only. Collection render visibility remains controlled through Blender's native collection tools in the Outliner.

However, the **Show All Objects and Collections in Render** command restores render visibility for every object and collection in the current scene.

This choice keeps the addon simple and avoids duplicating Blender's existing collection visibility controls.

## Installation

### From a ZIP file

For installation, download the addon package from the Releases section.

1. Download the ZIP file from the GitHub Release page.
2. Open Blender.
3. Go to `Edit > Preferences > Add-ons`.
4. Click `Install`.
5. Select the downloaded ZIP file.
6. Enable **Render Visibility Tools**.

### From the Python file

1. Download `render_visibility_tools.py`.
2. Open Blender.
3. Go to `Edit > Preferences > Add-ons`.
4. Click `Install`.
5. Select `render_visibility_tools.py`.
6. Enable **Render Visibility Tools**.

## Usage example

Imagine a scene containing several hundred objects, but you only need a clean render of one component.

Instead of finding every unwanted object in the Outliner and disabling its render icon individually:

1. isolate the required object visually in the viewport;
2. hide the other objects using Blender's normal viewport tools;
3. choose `Object > Render Visibility Tools > Sync All Viewport → Render`;
4. launch the render;
5. use **Show All Objects and Collections in Render** when you want to restore the full scene.

## Keyboard shortcuts

The addon does not install any keyboard shortcuts by default.

This avoids conflicts with existing Blender shortcuts and lets each user decide whether a shortcut is useful.

Custom shortcuts can be assigned through Blender's keymap preferences or by right-clicking a menu command and choosing **Assign Shortcut**.

## Compatibility

Designed for Blender 3.6 and later.

The addon may also work with newer Blender versions, but each major Blender release should be tested before compatibility is formally confirmed.

## Current scope

The addon intentionally remains small and focused.

It currently manages:

* selected-object render visibility;
* scene-object viewport-to-render synchronization;
* restoration of render visibility for all objects and collections.

Possible future improvements may include additional collection tools or checks involving modifier dependencies, depending on real-world use and user feedback.

## Known limitations

* Viewport-to-render synchronization acts on objects, not collections.
* Collection exclusion and View Layer configuration remain managed by Blender.
* The addon does not modify modifier settings or dependency relationships.
* Linked or externally managed scene data may behave according to Blender's own restrictions.

## License

Released under the MIT License.

See `LICENSE.txt` for details.

## Issues and contributions

Bug reports, suggestions, and feedback are welcome through the GitHub Issues page.

When reporting a problem, please include:

* the Blender version;
* the addon version;
* a short description of the expected behavior;
* the steps required to reproduce the issue.

## Author

Created by **3DLP**, with AI assistance.
