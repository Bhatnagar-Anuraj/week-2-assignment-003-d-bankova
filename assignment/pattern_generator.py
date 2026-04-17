"""
DIGM 131 - Assignment 2: Procedural Pattern Generator
======================================================
"""

import maya.cmds as cmds

# Clear the scene.
cmds.file(new=True, force=True)

def generate_pattern():
    # --- Configuration variables ---
    num_rows = 12       # Number of rows in the pattern.
    num_cols = 7        # Number of columns in the pattern.
    spacing = 3.0       # Distance between object centers.

    for row in range (num_rows):
            for col in range(num_cols):
                # Names each building so that each cube has it's own distinct name
                building_name = f"building_{row}_{col}"
                cmds.polyCube(building_name, w=3, h=15, d=3)
                x_pos = col * spacing
                z_pos = row * spacing

                # Changes the height/scale of the buildings in order to add variation to them
                # Each variation has a specific written part to describe what has happened in each variation
                if (row+col) % 2 == 0:
                    cmds.scale(1, 0.5, 1)
                    print (f"{building_name} has been flattened")
                elif (row+col) % 3 == 0: # Adding another variation to the building heights via scale will make the entire grid more appealing/interesting to look at
                    cmds.scale(1, 0.75, 1)
                    print (f"{building_name} has been partially flattened")
                else:
                    cmds.scale(1, 1, 1)
                    print (f"{building_name} remains the same")

                cmds.move(x_pos, 0, z_pos) # Moves each building to be at a set position and keeps each item level
                # Putting the move command after varying the scale guarantees that each object will stay level afterwards

                # Adding the additional maya objects at the end keeps them separate from the main focus, the "buildings" while also giving them distinct positions
                cmds.polySphere(r=3)
                cmds.move (x_pos+0.5, 8, z_pos+0.5)

                cmds.polyCylinder(r= 0.5, hr= 3)
                cmds.move (x_pos+1, 0, z_pos-1)
# ---------------------------------------------------------------------------
# Run the generator
# ---------------------------------------------------------------------------
generate_pattern()

# Frame everything in the viewport.
cmds.viewFit(allObjects=True)
print("Pattern generated successfully!")
