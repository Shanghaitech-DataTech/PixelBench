from pixelbench_api import *

# Create output canvases that are large enough to hold the rotated house
# The input is 112x157. When rotated 45 degrees, the bounding box expands.
# For a 45-degree rotation, the new dimensions are approximately:
# new_w = w * cos(45) + h * sin(45) = 112 * 0.707 + 157 * 0.707 ≈ 190
# new_h = w * sin(45) + h * cos(45) = same ≈ 190
# For 90-degree rotation: 157x112

# Let's create canvases that can hold both rotations comfortably
# We'll use 256x256 to be safe

# First, let's copy the input to work with
output = input_canvas.copy(name='output')

# Create two canvases for the two views
# We need to center the house and rotate it
# Let's create canvases of 256x256 for both frames

c1 = new_canvas(256, 256, name='frame1_45deg')
c2 = new_canvas(256, 256, name='frame2_90deg')

# Copy the input canvas to the center of each frame canvas
# Input is 112x157, canvas is 256x256
# Center offset: (256-112)//2 = 72, (256-157)//2 = 49
offset_x = (256 - 112) // 2
offset_y = (256 - 157) // 2

c1.blit(input_canvas, offset_x, offset_y)
c2.blit(input_canvas, offset_x, offset_y)

print("Frame 1 after blit:", c1.stats_text())
print("Frame 2 after blit:", c2.stats_text())

# Now we need to rotate the house
# The task says:
# - 45-degree frame shows front door, front wall, window and wall on right-hand side
# - 90-degree frame shows only right-hand wall and its window

# We need to use selection and rotation
# First, let's select the entire house content from the input

# Select the house from the original input
sel = input_canvas.select(0, 0, 112, 157)

# For frame 1: rotate by 45 degrees
# The selection recipe allows rotation
sel_45 = sel.rotate(45, algorithm="rotsprite")
print("Selection 45 deg size:", sel_45.size)

# For frame 2: rotate by 90 degrees  
sel_90 = sel.rotate(90, algorithm="nearest")
print("Selection 90 deg size:", sel_90.size)

# Now let's create fresh canvases and paste the rotated selections
# Clear the canvases first
c1.clear()
c2.clear()

# Calculate center positions for pasting
# sel_45.size gives us the expanded output dimensions
w45, h45 = sel_45.size
w90, h90 = sel_90.size

# Center the rotated content in the 256x256 canvas
x1 = (256 - w45) // 2
y1 = (256 - h45) // 2
x2 = (256 - w90) // 2
y2 = (256 - h90) // 2

print(f"Paste 45deg at: ({x1}, {y1}), size: {w45}x{h45}")
print(f"Paste 90deg at: ({x2}, {y2}), size: {w90}x{h90}")

# Copy the rotated selections to the frame canvases
sel_45.copy_to(x1, y1, c1, mode="over")
sel_90.copy_to(x2, y2, c2, mode="over")

print("Frame 1 after rotation:", c1.stats_text())
print("Frame 2 after rotation:", c2.stats_text())

# Let's view the results to check
print("\nFrame 1 matrix (center region):")
print(c1.matrix_text(region=(50, 50, 200, 200)))

print("\nFrame 2 matrix (center region):")
print(c2.matrix_text(region=(50, 50, 200, 200)))

# Submit both frames
finish([c1, c2])
