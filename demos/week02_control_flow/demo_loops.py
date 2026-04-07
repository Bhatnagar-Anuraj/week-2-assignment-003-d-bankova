"""
DIGM 131 - Week 2 Demo: Loops in Maya
=======================================
INSTRUCTOR NOTES:
    This demo covers for loops with range(), nested loops for grids, while loops,
    circular arrangements with sin/cos, and a spiral staircase as a capstone.
    Run in Maya's Script Editor (Python tab).
"""

import maya.cmds as cmds
import math  # INSTRUCTOR: We need math for sin, cos, and pi

# Start fresh
cmds.file(new=True, force=True)

# =============================================================================
# SECTION 1: for loop with range() — a row of columns
# =============================================================================
# INSTRUCTOR: "range(n) gives us the numbers 0, 1, 2, ... n-1.
# We can use each number to calculate a position."

num_columns = 6
column_spacing = 3.0
column_radius = 0.3
column_height = 4.0

for i in range(num_columns):
    col_name = "column_{}".format(i)
    col = cmds.polyCylinder(name=col_name, radius=column_radius, height=column_height)[0]
    x_position = i * column_spacing  # 0, 3, 6, 9, 12, 15
    cmds.move(x_position, column_height / 2.0, 0, col)

# INSTRUCTOR: "Each pass through the loop, i takes the next value: 0, 1, 2, 3, 4, 5.
# Multiplying i by spacing spreads the columns evenly."

# =============================================================================
# SECTION 2: Nested loops — a grid of cubes
# =============================================================================
# INSTRUCTOR: "Put one loop inside another and you get a 2D grid."

rows = 4
cols = 5
grid_spacing = 2.5
cube_size = 0.8

for row in range(rows):
    for col in range(cols):
        cube_name = "gridCube_{}_{}".format(row, col)
        cube = cmds.polyCube(name=cube_name, width=cube_size, height=cube_size, depth=cube_size)[0]
        x = col * grid_spacing
        z = row * grid_spacing + 8  # offset behind the columns
        cmds.move(x, cube_size / 2.0, z, cube)

# INSTRUCTOR: "The outer loop controls the row (Z), the inner loop controls the column (X).
# For a 4x5 grid we create 4 * 5 = 20 cubes total."

# =============================================================================
# SECTION 3: Using the loop variable for varied properties
# =============================================================================
# INSTRUCTOR: "The loop variable isn't just for position — use it to change size, color, anything."

for i in range(8):
    sphere_name = "growSphere_{}".format(i)
    # Each sphere is slightly larger than the last
    radius = 0.3 + i * 0.15
    sphere = cmds.polySphere(name=sphere_name, radius=radius)[0]
    cmds.move(i * 2.0, radius, -5, sphere)

# =============================================================================
# SECTION 4: while loop — grow until a limit
# =============================================================================
# INSTRUCTOR: "A while loop repeats as long as a condition is True.
# Use it when you don't know how many iterations you need in advance."

current_height = 1.0
stack_y = 0.0
stack_index = 0

while current_height < 10.0:
    block_name = "stackBlock_{}".format(stack_index)
    block_h = 0.5 + stack_index * 0.3  # each block is taller than the last
    block = cmds.polyCube(name=block_name, width=2, height=block_h, depth=2)[0]
    cmds.move(-8, stack_y + block_h / 2.0, 0, block)
    stack_y += block_h  # move up for the next block
    current_height = stack_y  # update our running total
    stack_index += 1

print("Stacked {} blocks to height {:.1f}".format(stack_index, current_height))

# INSTRUCTOR: "IMPORTANT: A while loop can run forever if the condition never becomes False.
# Always make sure something inside the loop moves you toward the exit condition."

# =============================================================================
# SECTION 5: Circular arrangement using sin and cos
# =============================================================================
# INSTRUCTOR: "To place objects in a circle we need trigonometry. Don't panic!
# sin gives us the Z position, cos gives us the X position on a circle of a given radius."

num_pillars = 10
circle_radius = 6.0
pillar_height = 3.0

for i in range(num_pillars):
    # Convert the index to an angle in radians (full circle = 2*pi)
    angle = (2 * math.pi / num_pillars) * i
    x = math.cos(angle) * circle_radius
    z = math.sin(angle) * circle_radius

    pillar_name = "pillar_{}".format(i)
    pillar = cmds.polyCylinder(name=pillar_name, radius=0.25, height=pillar_height)[0]
    cmds.move(x, pillar_height / 2.0, z + 20, pillar)  # offset Z so it doesn't overlap the grid

# INSTRUCTOR: Draw a unit circle on the board. Show that cos = X, sin = Z.
# Multiplying by circle_radius scales the circle to the size we want.

# =============================================================================
# SECTION 6: Capstone — Spiral staircase
# =============================================================================
# INSTRUCTOR: "Let's combine loops, math, and incremental changes to build something cool."

num_steps = 30
stair_width = 2.5
stair_depth = 1.0
stair_height = 0.3
staircase_radius = 3.0
height_per_step = 0.4
rotation_per_step = 15.0  # degrees each step rotates

for i in range(num_steps):
    step_name = "stair_{}".format(i)
    step = cmds.polyCube(name=step_name, width=stair_width, height=stair_height, depth=stair_depth)[0]

    # Calculate position on the spiral
    angle_rad = math.radians(rotation_per_step * i)
    step_x = math.cos(angle_rad) * staircase_radius + 15  # offset to the right
    step_z = math.sin(angle_rad) * staircase_radius + 20
    step_y = i * height_per_step + stair_height / 2.0

    cmds.move(step_x, step_y, step_z, step)
    # Rotate the step to face outward from the center
    cmds.rotate(0, -rotation_per_step * i, 0, step)

# Add a center pole for the staircase
total_stair_height = num_steps * height_per_step
pole = cmds.polyCylinder(name="centerPole", radius=0.2, height=total_stair_height)[0]
cmds.move(15, total_stair_height / 2.0, 20, pole)

# Frame everything
cmds.viewFit(allObjects=True)

print("Demo complete: row, grid, growing spheres, stack, circle, and spiral staircase.")

# INSTRUCTOR: Recap:
#   1. for i in range(n) — repeat n times, i counts from 0 to n-1.
#   2. Nested loops — outer loop * inner loop = total iterations.
#   3. while — repeat until a condition becomes False.
#   4. math.sin/cos — place objects in circles and spirals.
#   5. The loop variable can drive position, size, rotation, or any attribute.
