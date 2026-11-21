from pixelbench_api import *

# Final submission - recreate the three frames

w, h = 66, 119

f1 = new_canvas(w, h, name="frame1_left_3q")
f2 = new_canvas(w, h, name="frame2_right_3q")
f3 = new_canvas(w, h, name="frame3_rear")

original = input_canvas.copy(name="original")

# Define face colors
face_colors = {6, 7, 8, 10, 11, 12, 13, 14, 20, 21, 22, 23}
hair_color = 1  # c0

# ============ FRAME 1: LEFT 3/4 VIEW ============
f1.blit(original, 0, 0)

# Shift face pixels left by 2
shifted = {}
for y in range(20, 40):
    for x in range(18, 48):
        idx = f1.get(x, y)
        if idx in face_colors:
            new_x = x - 2
            if new_x >= 0:
                shifted[(new_x, y)] = idx

# Clear and reapply
for y in range(20, 40):
    for x in range(18, 48):
        if f1.get(x, y) in face_colors:
            f1.set(x, y, 0)

for (x, y), idx in shifted.items():
    f1.set(x, y, idx)

# Fill gaps
for y in range(20, 40):
    for x in range(18, 48):
        if f1.get(x, y) == 0:
            neighbors = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < w and 0 <= ny < h:
                    nidx = f1.get(nx, ny)
                    if nidx != 0:
                        neighbors.append(nidx)
            if neighbors:
                non_hair = [n for n in neighbors if n not in {1, 2, 3}]
                f1.set(x, y, non_hair[0] if non_hair else neighbors[0])

# ============ FRAME 2: RIGHT 3/4 VIEW ============
f2.blit(original, 0, 0)

# Shift face pixels right by 2
shifted = {}
for y in range(20, 40):
    for x in range(18, 48):
        idx = f2.get(x, y)
        if idx in face_colors:
            new_x = x + 2
            if new_x < w:
                shifted[(new_x, y)] = idx

for y in range(20, 40):
    for x in range(18, 48):
        if f2.get(x, y) in face_colors:
            f2.set(x, y, 0)

for (x, y), idx in shifted.items():
    f2.set(x, y, idx)

# Fill gaps
for y in range(20, 40):
    for x in range(18, 48):
        if f2.get(x, y) == 0:
            neighbors = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < w and 0 <= ny < h:
                    nidx = f2.get(nx, ny)
                    if nidx != 0:
                        neighbors.append(nidx)
            if neighbors:
                non_hair = [n for n in neighbors if n not in {1, 2, 3}]
                f2.set(x, y, non_hair[0] if non_hair else neighbors[0])

# ============ FRAME 3: REAR VIEW ============
f3.blit(original, 0, 0)

# Replace all face features with hair color
for y in range(h):
    for x in range(w):
        if f3.get(x, y) in face_colors:
            f3.set(x, y, hair_color)

# Submit
finish([f1, f2, f3])
