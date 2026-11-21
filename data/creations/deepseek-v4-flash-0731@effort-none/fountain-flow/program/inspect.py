from pixelbench_api import *

output = input_canvas.copy(name='output')

WATER      = '#2090D0'   
WATER_LIGHT = '#60C8F0'  
WATER_BRIGHT = '#B0EFFF' 
WATER_DEEP  = '#0A76B8'  

# Top jet spray
output.set(31, 0, WATER_BRIGHT)
output.set(30, 0, WATER_LIGHT)
output.set(32, 0, WATER_LIGHT)
output.set(31, 1, WATER_BRIGHT)
output.set(32, 1, WATER_BRIGHT)
output.set(31, 1, WATER_BRIGHT)
output.set(29, 1, WATER_LIGHT)
output.set(33, 1, WATER_LIGHT)

for y in range(0, 8):
    w = y // 2
    for dx in range(w + 1):
        output.set(31 - dx, y, WATER_BRIGHT)
        output.set(31 + dx, y, WATER_BRIGHT)

for y in range(0, 6):
    for dx in [-7, -5, -3, -1, 0, 1, 3, 5, 7]:
        if y >= 1 and y <= 5:
            out_x = 31 + dx
            if 0 <= out_x < 64:
                output.set(out_x, y, WATER_BRIGHT)
        if y >= 2 and y <= 6:
            for ex in [-8, -4, -2, 2, 4, 8]:
                out_x = 31 + ex
                if 0 <= out_x < 64:
                    output.set(out_x, y, WATER_LIGHT)

for y in range(5, 12):
    for x in range(20, 44):
        output.set(x, y, WATER)

for x in range(22, 42):
    for y in range(5, 10):
        if (x * 7 + y * 13) % 6 < 3:
            output.set(x, y, WATER_LIGHT)
        else:
            output.set(x, y, WATER)

for x in range(23, 41):
    if (x * 3) % 4 == 0:
        output.set(x, 4, WATER_BRIGHT)
    if (x * 3) % 4 == 2:
        output.set(x, 5, WATER_BRIGHT)

# Left/right cascade streams
left_stream_cols = [13, 15, 17, 19]
right_stream_cols = [44, 46, 48, 50]

for y in range(13, 37):
    for x in left_stream_cols:
        output.set(x, y, WATER)
    for x in right_stream_cols:
        output.set(x, y, WATER)

for i, y in enumerate(range(14, 36)):
    if i % 2 == 0:
        output.set(left_stream_cols[0] - 1, y, WATER_BRIGHT)
        output.set(left_stream_cols[-1] + 1, y, WATER_BRIGHT)
        output.set(right_stream_cols[0] - 1, y, WATER_BRIGHT)
        output.set(right_stream_cols[-1] + 1, y, WATER_BRIGHT)
    if i % 3 == 1:
        output.set(left_stream_cols[1] + 1, y, WATER_LIGHT)
        output.set(right_stream_cols[1] - 1, y, WATER_LIGHT)

# Main pool
for y in range(38, 52):
    for x in range(6, 58):
        if (x + y) % 2:
            output.set(x, y, WATER)
        else:
            output.set(x, y, WATER_LIGHT)

for y in range(42, 50):
    for x in range(15, 49):
        if (x + y) % 4 == 0:
            output.set(x, y, WATER_DEEP)

output.ellipse(31, 42, 22, 3, WATER_LIGHT, fill=False)
output.ellipse(31, 45, 18, 3, WATER_BRIGHT, fill=False)
output.ellipse(31, 48, 13, 2, WATER_LIGHT, fill=False)

for x in range(8, 56):
    if (x * 5) % 7 == 0:
        output.set(x, 41, WATER_BRIGHT)
        output.set(x + 2, 43, WATER_BRIGHT)
        output.set(x + 5, 45, WATER_BRIGHT)

# Splashes
for y in range(36, 43):
    for x in range(5, 20):
        if (x + y) % 2:
            output.set(x, y, WATER_BRIGHT)
        else:
            output.set(x, y, WATER_LIGHT)
    for x in range(44, 59):
        if (x + y) % 2:
            output.set(x, y, WATER_BRIGHT)
        else:
            output.set(x, y, WATER_LIGHT)

for x, y in [(6, 34), (9, 33), (12, 32), (16, 31), (48, 31), (52, 32),
             (55, 33), (58, 34), (7, 36), (57, 36)]:
    output.set(x, y, WATER_BRIGHT)

# Rim overflow
for y in range(44, 50):
    out_l = 4 + (y - 44) // 2
    if 0 <= out_l < 64:
        output.set(out_l, y, WATER)
    out_r = 59 - (y - 44) // 2
    if 0 <= out_r < 64:
        output.set(out_r, y, WATER)

# Water beads
for x, y in [(20, 15), (44, 15), (22, 18), (42, 18), (24, 22), (40, 22),
             (21, 20), (43, 20), (10, 28), (54, 28), (19, 26), (45, 26)]:
    output.set(x, y, WATER_LIGHT)

# Print the output
print(output.matrix_text(region=(0,0,63,40)))
print("\nLegend:")
s = output.stats()
print(s)  # to get color legend
