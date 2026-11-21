from pixelbench_api import *

# Read input pixel data
w, h, indices, _ = input_canvas.to_indexed()
pal = input_canvas.palette()

def src_px(x, y):
    if x < 0 or x >= w or y < 0 or y >= h:
        return None
    idx = indices[y*w+x]
    if idx == 0:
        return None
    p = pal[idx]
    return (p['rgba'][0], p['rgba'][1], p['rgba'][2], p['rgba'][3])

CW, CH = 65, 63

# Frame 1: original content kept as specified
f1 = new_canvas(CW, CH, name='f1')
f1.blit(input_canvas, 0, 0)

# Frame 2: character thrusting fire forward with left foot step
f2 = new_canvas(CW, CH, name='f2')

o = (242, 114, 25, 255)   # orange
g = (244, 163, 12, 255)   # gold
y = (254, 211, 44, 255)   # yellow

# Character transformation for frame 2:
# Head/upper body leans forward (shifts right), left foot steps forward
def get_dx(x, y):
    if y <= 12:    return 5    # head tips forward
    elif y <= 20:  return 5    # shoulders/neck leaning in
    elif y <= 28:  return 5    # chest pushing forward
    elif y <= 36:  return 4    # waist
    elif y <= 44:  return 3    # hips
    elif y <= 48:  return 2    # upper legs
    elif y <= 51:
        if x < 17:  return 4   # left leg begins extending
        else:       return 2
    elif y <= 54:
        if x < 18:  return 8   # left leg mid-step
        else:       return 1
    elif y <= 58:
        if x < 18:  return 14  # left leg extending
        else:       return 1
    else:
        if x < 18:  return 18  # left foot stepped forward
        else:       return 1   # right foot planted

# Copy character with pose transformation
for row_y in range(h):
    for col_x in range(w):
        col = src_px(col_x, row_y)
        if col is None:
            continue
        dx = get_dx(col_x, row_y)
        f2.set(col_x + dx, row_y, col)

# Additional arm thrust - the hand pushes the fire forward
# The arm is at approximately y=19-28, extending from body toward the flame

# Flame thrust with fiery trail: the flame flies forward from the hand
flame_pixels = [
    # Leading edge of the flying flame (far right)
    (59, 12, y), (61, 12, y), (63, 12, y),
    (57, 13, y), (59, 13, y), (61, 13, y), (63, 13, y),
    (56, 14, y), (58, 14, y), (60, 14, y), (62, 14, y),
    (55, 15, y), (57, 15, y), (59, 15, y), (61, 15, y),
    (54, 16, y), (56, 16, y), (58, 16, y), (60, 16, y), (62, 16, y),
    (53, 17, g), (55, 17, y), (57, 17, y), (59, 17, y), (61, 17, y),
    (52, 18, g), (54, 18, y), (56, 18, y), (58, 18, y), (60, 18, y), (62, 18, y),
    (51, 19, g), (53, 19, y), (55, 19, y), (57, 19, y), (59, 19, y), (61, 19, y),
    (50, 20, o), (52, 20, g), (54, 20, y), (56, 20, y), (58, 20, y), (60, 20, y),
    (49, 21, o), (51, 21, g), (53, 21, y), (55, 21, y), (57, 21, y), (59, 21, y),
    (48, 22, o), (50, 22, o), (52, 22, g), (54, 22, y), (56, 22, y), (58, 22, g),
    (47, 23, o), (49, 23, o), (51, 23, g), (53, 23, g), (55, 23, y), (57, 23, g),
    (46, 24, o), (48, 24, g), (50, 24, g), (52, 24, y), (54, 24, y),
    (47, 25, o), (49, 25, g), (51, 25, g), (53, 25, y),
    (48, 26, o), (50, 26, g), (52, 26, g),
    (49, 27, o), (51, 27, o),
    # Fiery trail - fire streaming from hand toward the flying flame
    (44, 23, o), (46, 22, o), (48, 23, o),
    (43, 24, o), (45, 24, o),
    (42, 25, o), (44, 25, o),
    (41, 26, o), (43, 26, o),
    (40, 27, o), (42, 27, o),
    (41, 28, o), (38, 27, o),
    (46, 25, o), (44, 26, o),
    (47, 26, o), (45, 27, o), (43, 28, o),
    (46, 27, o), (44, 28, o), (42, 29, o),
    (48, 28, o), (46, 29, o),
    (50, 29, o), (48, 30, o),
    (54, 27, o), (52, 28, o), (50, 29, y),
    (55, 26, g), (53, 27, o),
    (56, 25, g), (54, 26, o),
    (57, 24, g), (55, 25, o),
    (57, 26, o), (55, 27, o), (53, 28, o),
    (51, 27, o), (49, 28, o),
    # Forward flame edges
    (61, 16, y), (59, 18, y),
    (62, 17, g), (60, 19, y),
    (63, 15, y), (61, 18, y),
    (50, 25, y), (48, 26, g),
    (46, 22, o), (43, 23, o),
    (40, 24, o), (37, 25, o),
    (39, 28, o), (41, 29, o),
    (55, 23, y), (52, 24, y),
    (58, 21, g), (56, 22, y),
    (60, 18, y), (57, 20, y),
    (59, 22, g), (54, 23, y),
    (63, 18, g), (62, 19, g),
    (61, 20, g), (59, 22, o),
    (62, 20, o), (60, 22, g),
]

for px_x, px_y, col in flame_pixels:
    f2.set(px_x, px_y, col)

# Both frames share same dimensions
finish([f1, f2])
