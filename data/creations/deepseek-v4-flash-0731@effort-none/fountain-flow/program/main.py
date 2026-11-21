from pixelbench_api import *

# Waterless fountain -> add running water
output = input_canvas.copy(name='output')

WATER      = '#2090D0'   
WATER_LIGHT = '#60C8F0'  
WATER_BRIGHT = '#B0EFFF' 
WATER_DEEP  = '#0A76B8'  

# =========================================================
# WATER IN THE FOUNTAIN - STRATEGY:
# 1. A sharp water jet shoots from the top spout
# 2. A clear dome/umbrella of water from the top
# 3. Water falls from the top bowl in visible streams
# 4. Water collects in the main basin as a pool
# =========================================================

# =========================================================
# 1. WATER JET FROM TOP SPOUT
# =========================================================

# Clear jet from the top spout going up
output.set(31, 0, WATER_BRIGHT)
output.set(30, 0, WATER_LIGHT)
output.set(32, 0, WATER_LIGHT)
output.set(31, 1, WATER_BRIGHT)
output.set(30, 1, WATER_BRIGHT)
output.set(32, 1, WATER_BRIGHT)
output.set(29, 1, WATER_LIGHT)
output.set(33, 1, WATER_LIGHT)

# Jet rising and expanding into a dome spray
for y in range(0, 8):
    w = y // 2  # the jet widens as it rises
    for dx in range(w + 1):
        output.set(31 - dx, y, WATER_BRIGHT)
        output.set(31 + dx, y, WATER_BRIGHT)

# The dome/umbrella shape where water arcs outward
# Water arcs from the peak of the jet back down
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

# The top bowl area fills with water spray
# Sprinkling/cascading water at the top of the fountain
for y in range(5, 12):
    for x in range(20, 44):
        if 0 <= x < 64:
            output.set(x, y, WATER)

# Lighter surface with wave highlights
for x in range(22, 42):
    for y in range(5, 10):
        if 0 <= x < 64:
            if (x * 7 + y * 13) % 6 < 3:
                output.set(x, y, WATER_LIGHT)
            else:
                output.set(x, y, WATER)

# Water peaks/splashes at the top edge
for x in range(23, 41):
    if (x * 3) % 4 == 0:
        output.set(x, 4, WATER_BRIGHT)
    if (x * 3) % 4 == 2:
        output.set(x, 5, WATER_BRIGHT)

# =========================================================
# 2. WATER STREAMS FALLING BETWEEN TIERS
# =========================================================

# Water cascades down both sides as curtains/streams
# The left side has falling water streams

# Main cascade streams on the left
left_stream_cols = [13, 15, 17, 19]
right_stream_cols = [44, 46, 48, 50]

for y in range(13, 37):
    for x in left_stream_cols:
        output.set(x, y, WATER)
    for x in right_stream_cols:
        output.set(x, y, WATER)

# Intermittent splash bits on the left streams
for i, y in enumerate(range(14, 36)):
    if i % 2 == 0:
        output.set(left_stream_cols[0] - 1, y, WATER_BRIGHT)
        output.set(left_stream_cols[-1] + 1, y, WATER_BRIGHT)
        output.set(right_stream_cols[0] - 1, y, WATER_BRIGHT)
        output.set(right_stream_cols[-1] + 1, y, WATER_BRIGHT)
    if i % 3 == 1:
        output.set(left_stream_cols[1] + 1, y, WATER_LIGHT)
        output.set(right_stream_cols[1] - 1, y, WATER_LIGHT)

# =========================================================
# 3. WATER POOL IN THE MAIN BASIN
# =========================================================
# The main/lower basin accumulates the water

# Fill the main basin with water - the lower basin pool area
# The basin floor spans the wide middle section of the fountain

# Fill with water
for y in range(38, 52):
    for x in range(6, 58):
        if 0 <= x < 64:
            if (x + y) % 2:
                output.set(x, y, WATER)
            else:
                output.set(x, y, WATER_LIGHT)

# Some darker deep spots
for y in range(42, 50):
    for x in range(15, 49):
        if (x + y) % 4 == 0:
            output.set(x, y, WATER_DEEP)

# Ripple rings from where water falls
# Central ripples
output.ellipse(31, 42, 22, 3, WATER_LIGHT, fill=False)
output.ellipse(31, 45, 18, 3, WATER_BRIGHT, fill=False)
output.ellipse(31, 48, 13, 2, WATER_LIGHT, fill=False)

# Bright shimmer lines on the pool
for x in range(8, 56):
    if (x * 5) % 7 == 0:
        output.set(x, 41, WATER_BRIGHT)
        output.set(x + 2, 43, WATER_BRIGHT)
        output.set(x + 5, 45, WATER_BRIGHT)

# =========================================================
# 4. SPLASHES AT CASCADE BASES
# =========================================================

# Where the falling water hits the pool surface
# Left impact zone
for y in range(36, 43):
    for x in range(5, 20):
        if 0 <= x < 64:
            if (x + y) % 2:
                output.set(x, y, WATER_BRIGHT)
            else:
                output.set(x, y, WATER_LIGHT)

# Right impact zone
for y in range(36, 43):
    for x in range(44, 59):
        if 0 <= x < 64:
            if (x + y) % 2:
                output.set(x, y, WATER_BRIGHT)
            else:
                output.set(x, y, WATER_LIGHT)

# Spray points flying from the impact
for x, y in [(6, 34), (9, 33), (12, 32), (16, 31), (48, 31), (52, 32),
             (55, 33), (58, 34), (7, 36), (57, 36)]:
    if 0 <= x < 64 and 0 <= y < 76:
        output.set(x, y, WATER_BRIGHT)

# =========================================================
# 5. WATER OVERFLOWING THE MAIN RIM
# =========================================================

# Water spilling over the main rim on both sides
for y in range(44, 50):
    out_l = 4 + (y - 44) // 2
    if 0 <= out_l < 64:
        output.set(out_l, y, WATER)
    out_r = 59 - (y - 44) // 2
    if 0 <= out_r < 64:
        output.set(out_r, y, WATER)

# =========================================================
# Extra water beads and droplets
# =========================================================
for x, y in [(20, 15), (44, 15), (22, 18), (42, 18), (24, 22), (40, 22),
             (21, 20), (43, 20), (10, 28), (54, 28), (19, 26), (45, 26)]:
    if 0 <= x < 64 and 0 <= y < 76:
        output.set(x, y, WATER_LIGHT)

print(output.stats_text())
