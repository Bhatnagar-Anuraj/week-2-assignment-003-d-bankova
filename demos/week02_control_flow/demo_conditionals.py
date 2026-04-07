"""
DIGM 131 - Week 2 Demo: Conditionals in Maya
==============================================
    This demo teaches if/elif/else using Maya scene queries. We create objects,
    read their attributes with getAttr, and make decisions: coloring objects
    based on height, checking positions, and combining conditions with logical operators.
    Run in Maya's Script Editor (Python tab).
"""

import maya.cmds as cmds

# Start fresh
cmds.file(new=True, force=True)

# =============================================================================
# SECTION 1: Simple if/else — Is a value above a threshold?
# =============================================================================
# and runs the indented code only if the condition is True."

# Create a tall cube
tower_height = 7.0
tower = cmds.polyCube(name="tower", height=tower_height, width=1.5, depth=1.5)[0]
cmds.move(0, tower_height / 2.0, 0, tower)

# Query the height back from the scene to demonstrate getAttr
actual_height = cmds.getAttr(tower + ".scaleY") * tower_height
print("Tower height:", actual_height)

if actual_height > 5.0:
    print("This tower is TALL (over 5 units).")
else:
    print("This tower is SHORT (5 units or under).")

# =============================================================================
# SECTION 2: if / elif / else — Multiple categories
# =============================================================================

# Create three buildings at different heights and color them by category
# We'll do each one individually -- no loops yet!

# Shaders for three height categories
short_shader = cmds.shadingNode("lambert", asShader=True, name="shortMat")
cmds.setAttr(short_shader + ".color", 0.2, 0.7, 0.2, type="double3")  # green

medium_shader = cmds.shadingNode("lambert", asShader=True, name="mediumMat")
cmds.setAttr(medium_shader + ".color", 0.9, 0.7, 0.1, type="double3")  # yellow

tall_shader = cmds.shadingNode("lambert", asShader=True, name="tallMat")
cmds.setAttr(tall_shader + ".color", 0.8, 0.15, 0.15, type="double3")  # red

# Building 0 — short
building_0_height = 2.0
building_0 = cmds.polyCube(name="building_0", height=building_0_height, width=1.5, depth=1.5)[0]
cmds.move(-4.5, building_0_height / 2.0, 0, building_0)

if building_0_height < 4.0:
    cmds.select(building_0)
    cmds.hyperShade(assign=short_shader)
    print("building_0 is short")
elif building_0_height < 9.0:
    cmds.select(building_0)
    cmds.hyperShade(assign=medium_shader)
    print("building_0 is medium")
else:
    cmds.select(building_0)
    cmds.hyperShade(assign=tall_shader)
    print("building_0 is tall")

# Building 1 — medium
building_1_height = 5.0
building_1 = cmds.polyCube(name="building_1", height=building_1_height, width=1.5, depth=1.5)[0]
cmds.move(-1.5, building_1_height / 2.0, 0, building_1)

if building_1_height < 4.0:
    cmds.select(building_1)
    cmds.hyperShade(assign=short_shader)
    print("building_1 is short")
elif building_1_height < 9.0:
    cmds.select(building_1)
    cmds.hyperShade(assign=medium_shader)
    print("building_1 is medium")
else:
    cmds.select(building_1)
    cmds.hyperShade(assign=tall_shader)
    print("building_1 is tall")

# Building 2 — tall
building_2_height = 12.0
building_2 = cmds.polyCube(name="building_2", height=building_2_height, width=1.5, depth=1.5)[0]
cmds.move(1.5, building_2_height / 2.0, 0, building_2)

if building_2_height < 4.0:
    cmds.select(building_2)
    cmds.hyperShade(assign=short_shader)
    print("building_2 is short")
elif building_2_height < 9.0:
    cmds.select(building_2)
    cmds.hyperShade(assign=medium_shader)
    print("building_2 is medium")
else:
    cmds.select(building_2)
    cmds.hyperShade(assign=tall_shader)
    print("building_2 is tall")

# Notice the repetition? Next week we'll learn LOOPS to eliminate this copy-paste!

# =============================================================================
# SECTION 3: Comparison operators review
# =============================================================================

# Demonstrate with getAttr — query an object's X position
obj_x = cmds.getAttr("building_0.translateX")
print("building_0 is at X =", obj_x)

if obj_x < 0:
    print("building_0 is on the LEFT side of the scene (negative X).")
elif obj_x == 0:
    print("building_0 is at the CENTER.")
else:
    print("building_0 is on the RIGHT side (positive X).")

# =============================================================================
# SECTION 4: Logical operators — and, or, not
# =============================================================================

# Create a sphere and check multiple properties at once
test_sphere = cmds.polySphere(name="testSphere", radius=1.0)[0]
cmds.move(3, 6, 0, test_sphere)

sphere_x = cmds.getAttr(test_sphere + ".translateX")
sphere_y = cmds.getAttr(test_sphere + ".translateY")

# AND — both must be True
if sphere_x > 0 and sphere_y > 5:
    print("Sphere is in the upper-right area of the scene.")

# OR — at least one must be True
if sphere_x > 10 or sphere_y > 10:
    print("Sphere is far from the origin on at least one axis.")
else:
    print("Sphere is reasonably close to the origin.")

# NOT — flips True/False
is_visible = cmds.getAttr(test_sphere + ".visibility")
if not is_visible:
    print("The sphere is hidden!")
else:
    print("The sphere is visible.")

# =============================================================================
# SECTION 5: Practical example — tag an object by position quadrant
# =============================================================================
# Combine and/or to classify where an object sits in the scene.

# Check building_0's position
b0_x = cmds.getAttr("building_0.translateX")
b0_z = cmds.getAttr("building_0.translateZ")

if b0_x >= 0 and b0_z >= 0:
    quadrant = "front-right"
elif b0_x < 0 and b0_z >= 0:
    quadrant = "front-left"
elif b0_x < 0 and b0_z < 0:
    quadrant = "back-left"
else:
    quadrant = "back-right"

print("building_0 is in the {} quadrant".format(quadrant))

# Check building_2's position
b2_x = cmds.getAttr("building_2.translateX")
b2_z = cmds.getAttr("building_2.translateZ")

if b2_x >= 0 and b2_z >= 0:
    quadrant_2 = "front-right"
elif b2_x < 0 and b2_z >= 0:
    quadrant_2 = "front-left"
elif b2_x < 0 and b2_z < 0:
    quadrant_2 = "back-left"
else:
    quadrant_2 = "back-right"

print("building_2 is in the {} quadrant".format(quadrant_2))

# See how we had to repeat the same quadrant logic twice?
# Next week: functions will let us write it once and reuse it.

# Frame everything nicely
cmds.viewFit(allObjects=True)

