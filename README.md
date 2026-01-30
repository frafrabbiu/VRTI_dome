# VRTI_dome

## Setup Steps

- Download the ZIP folder from GitHub.
- Unzip the downloaded folder.

After unzipping, you will find:
- `assets` folder
- `rti_script`

## Opening the Workspace

- Inside the `assets` you'll find `VRTI_workspace.blend`.
- Open the `.blend` file in Blender.

## Preparing the Scene

- Import the 3D model of interest. If the pivot is not already set by default, move the object’s origin to the centre of its geometry (`Object → Set Origin → Origin to Geometry`). Then position the model so that it is correctly aligned under the camera, with the following coordinates:
  - x = 0  
  - y = 0  
  - z = 0
    
- Arrange the spheres along the X and Y axes, position them around the object (so they remain within the camera view). Ensure the Z-axis plane matches the object's plane.
  
- Scale the light sources (`lights1`, `lights2`, `lights3`) according to the size of your object or sample.
  - **Important:** if you scale the lights, keep their proportions consistent (do not move or scale them separately).
  
- Adjust the camera focal length if needed (default: **38 mm**).
- Go to **Properties** → **Camera Settings** → **Depth of Field** and, in the **Focus on Object** field, select the object to focus on.
  
- When running the script, the camera must remain perpendicular to the object.
  - Recommended: adjust only the Z-axis.

## Configuring the Output

- In the Blender workspace, the output resolution has been set to 8K. If you wish to change it, adjust the format settings in `Output Properties → Format`, located in the third section from the bottom on the right-hand side (Blender 4.3.2).

In Blender's Text Editor, you will find:

```python
# Set the output folder
output_folder = 'your file path'

```
- Replace the text inside the quotes with the local file path where you want the output files saved.
- Ensure the path uses the correct slash direction for your OS (\\ or /), otherwise Blender may return a syntax error.
- This script is the same as the one in rti_script.

**Key features**:

- Sequential rendering: The script produces one image per active light, automatically turning off all other lights, resulting in a complete set of images where each is lit by a single source at a time.
- Light group organization: The script uses the light folder structure present in the .blend file (lights1, lights2, lights3) to identify and manage the light sources.

## Running the Script

- Click Play in the Blender Text Editor.
- While the script is running, the Blender workspace will be unresponsive. Normal operation will resume once the process is complete.

## Final Output

- The script generates .jpg render files, ready for import into Relight or any other RTI processing software.



