# Blender Add-on Metadata
bl_info = {
    "name": "Brooklyn's CarX Tools",
    "version": (1, 0, 0),
    "blender": (3, 6, 1),
    "author": "Brooklyn",
    "location": "View3D",
    "category": "Development",
}

import bpy
from . import BrooklynsTools  # Import the main add-on script

def register():
    try:
        BrooklynsTools.register()  # Register the add-on functionalities
    except Exception as e:
        print(f"Failed to register add-on: {e}")

def unregister():
    try:
        BrooklynsTools.unregister()  # Unregister the add-on functionalities
    except Exception as e:
        print(f"Failed to unregister add-on: {e}")

if __name__ == "__main__":
    register()
