import bpy
import os

# =========================================================================
# 1. MANUAL NAME INPUT
# =========================================================================

base_filename = "filename" # change the base filename here

# =========================================================================
# 2. MANUAL PATH CONFIGURATION
# =========================================================================
output_folder = r'C:/Users/<YOUR_USERNAME>/path_outputfolder' # change the output folder path here

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

metadata_file = os.path.join(output_folder, f"{base_filename}_metadata.txt")

# =========================================================================
# LIGHTS AND OBJECT SELECTION
# =========================================================================
collections = [
    bpy.data.collections.get("lights1"),
    bpy.data.collections.get("lights2"),
    bpy.data.collections.get("lights3")
]

lights = [
    obj for collection in collections
    if collection
    for obj in collection.objects
    if obj.type == 'LIGHT'
]

scene = bpy.context.scene
camera = scene.camera


# Save original settings
original_output_path = scene.render.filepath
original_image_format = scene.render.image_settings.file_format

# Force JPEG output
scene.render.image_settings.file_format = 'JPEG'

# =========================================================================
# METADATA GENERATION AND RENDERING LOOP
# =========================================================================
with open(metadata_file, 'w', encoding='utf-8') as f:

    # Write required metadata

    if camera:
        f.write(f"Focal Length: {camera.data.lens} mm\n")
        f.write(f"Sensor Fit: {camera.data.sensor_fit} (Width: {camera.data.sensor_width} mm)\n")
        f.write(f"Camera Position XYZ: {camera.location.x:.6f}, {camera.location.y:.6f}, {camera.location.z:.6f}\n")
    else:
        f.write("Camera: No active camera found\n")

    f.write(f"Render Engine: {scene.render.engine}\n")
    f.write(f"Resolution: {scene.render.resolution_x} x {scene.render.resolution_y}\n")

    # SAFE FIX FOR CYCLES / EEVEE SAMPLES
    if scene.render.engine == 'CYCLES':
        if hasattr(scene.cycles, "render_samples"):
            samples_cycles = scene.cycles.render_samples
        elif hasattr(scene.cycles, "samples"):
            samples_cycles = scene.cycles.samples
        else:
            samples_cycles = "N/A"

        f.write(f"Cycles Samples: {samples_cycles}\n")

    elif scene.render.engine == 'BLENDER_EEVEE':
        if hasattr(scene.eevee, "render_samples"):
            samples_eevee = scene.eevee.render_samples
        elif hasattr(scene.eevee, "taa_render_samples"):
            samples_eevee = scene.eevee.taa_render_samples
        else:
            samples_eevee = "N/A"

        f.write(f"Eevee Samples: {samples_eevee}\n")

    f.write("\n========== EXPORTED IMAGE LIST ==========\n")

    # Rendering loop with progressive renaming (filename_1, filename_2, etc.)
    for index, light in enumerate(lights, start=1):

        # Turn off all lights
        for l in lights:
            l.hide_render = True

        # Turn on only the current light
        light.hide_render = False

        # Generate progressive file name
        image_name = f"{base_filename}_{index}.jpg"
        scene.render.filepath = os.path.join(output_folder, image_name)

        # Execute render
        bpy.ops.render.render(write_still=True)

        # Write associated image file name into metadata
        f.write(f"Image File: {image_name} (Active Light: {light.name})\n")

        # Turn the light off again
        light.hide_render = True

# Restore Blender original state
scene.render.filepath = original_output_path
scene.render.image_settings.file_format = original_image_format

print("Rendering completed and .txt file generated!")