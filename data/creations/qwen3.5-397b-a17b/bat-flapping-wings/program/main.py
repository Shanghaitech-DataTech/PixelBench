from pixelbench_api import *

# The input is 27x22. For the wing flap animation, raised wings need more vertical space.
# Create a larger canvas: 27x35 (13 pixels extra at top for raised wings)
W, H = 27, 35
OFFSET_Y = 13  # Position original bat starting at row 13

# Register colors from the input palette
colors = {
    'body_dark': '#1d181e',  # a - main body
    'wing_light': '#7784a2',  # b - wing highlights
    'wing_purple': '#b572b1',  # c - wing accent
    'wing_dark': '#432f53',  # d - main wing color
    'wing_mid': '#5f5f7b',  # e - wing midtone
    'eye': '#ae0000',  # f - eyes
    'teeth': '#fff9d6',  # g - teeth
    'wing_shadow': '#5c436f',  # h - wing shadow
}

for name, hex_val in colors.items():
    input_canvas.color(hex_val, name)

# Create frame canvases
frame1 = new_canvas(W, H, name='frame1')
frame2 = new_canvas(W, H, name='frame2')

# Copy input to frame1 at offset position
frame1.blit(input_canvas, 0, OFFSET_Y)

# For frame2: Draw wings first (raised position), then body on top
# Define color indices
c0 = input_canvas.color('#1d181e')  # body dark
c1 = input_canvas.color('#7784a2')  # wing light
c2 = input_canvas.color('#b572b1')  # wing purple  
c3 = input_canvas.color('#432f53')  # wing dark (main)
c4 = input_canvas.color('#5f5f7b')  # wing mid
c5 = input_canvas.color('#ae0000')  # eyes
c6 = input_canvas.color('#fff9d6')  # teeth
c7 = input_canvas.color('#5c436f')  # wing shadow

wing_dark = c3
wing_shadow = c7
wing_light = c1

# Draw left raised wing first
left_wing_points = [
    (9, OFFSET_Y-5),   # wing tip high
    (5, OFFSET_Y-2),
    (2, OFFSET_Y+2),
    (0, OFFSET_Y+6),
    (0, OFFSET_Y+10),
    (1, OFFSET_Y+14),
    (3, OFFSET_Y+17),
    (6, OFFSET_Y+19),
    (9, OFFSET_Y+20),
    (11, OFFSET_Y+18),
    (12, OFFSET_Y+15),
    (12, OFFSET_Y+12),
    (12, OFFSET_Y+9),
    (12, OFFSET_Y+6),
    (11, OFFSET_Y+3),
    (10, OFFSET_Y+0),
]

frame2.poly(left_wing_points, wing_dark, fill=True)

# Add wing vein details
frame2.line(9, OFFSET_Y-4, 11, OFFSET_Y+10, wing_shadow)
frame2.line(6, OFFSET_Y-1, 10, OFFSET_Y+8, wing_shadow)
frame2.line(3, OFFSET_Y+3, 8, OFFSET_Y+12, wing_shadow)

# Draw right raised wing
right_wing_points = [
    (17, OFFSET_Y-5),  # wing tip high
    (21, OFFSET_Y-2),
    (24, OFFSET_Y+2),
    (26, OFFSET_Y+6),
    (26, OFFSET_Y+10),
    (25, OFFSET_Y+14),
    (23, OFFSET_Y+17),
    (20, OFFSET_Y+19),
    (17, OFFSET_Y+20),
    (15, OFFSET_Y+18),
    (14, OFFSET_Y+15),
    (14, OFFSET_Y+12),
    (14, OFFSET_Y+9),
    (14, OFFSET_Y+6),
    (15, OFFSET_Y+3),
    (16, OFFSET_Y+0),
]

frame2.poly(right_wing_points, wing_dark, fill=True)

# Add wing vein details
frame2.line(17, OFFSET_Y-4, 15, OFFSET_Y+10, wing_shadow)
frame2.line(20, OFFSET_Y-1, 16, OFFSET_Y+8, wing_shadow)
frame2.line(23, OFFSET_Y+3, 18, OFFSET_Y+12, wing_shadow)

# Add highlights to wings
frame2.set(6, OFFSET_Y, wing_light)
frame2.set(7, OFFSET_Y+1, wing_light)
frame2.set(20, OFFSET_Y, wing_light)
frame2.set(19, OFFSET_Y+1, wing_light)

# NOW draw body on top (copy from input)
# Body region: x=10-16 in original, y=0-21
for y in range(22):
    for x in range(10, 17):
        color_idx = input_canvas.get(x, y)
        if color_idx is not None:
            frame2.set(x, y + OFFSET_Y, color_idx)

# View results
print("Frame 1 stats:", frame1.stats_text())
print("Frame 2 stats:", frame2.stats_text())

print("\nFrame 2 matrix (region with content):")
print(frame2.matrix_text(region=(0, 8, 26, 34)))

view(frame1, scale=8)
view(frame2, scale=8)

# Submit both frames
finish([frame1, frame2])
