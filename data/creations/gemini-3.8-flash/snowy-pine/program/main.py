import numpy as np
from collections import deque

# 1. Load input
arr = np.zeros((135, 82), dtype=int)
for y in range(135):
    for x in range(82):
        arr[y, x] = input_canvas.get(x, y)

output = input_canvas.copy(name="output")

foliage_mask = (arr >= 1) & (arr <= 4)

# 2. Compute upward sky distance for each column
dist_to_sky = np.full((135, 82), 999)
for x in range(82):
    for y in range(135):
        if foliage_mask[y, x]:
            for dy in range(1, y + 2):
                if y - dy < 0 or arr[y - dy, x] == 0:
                    dist_to_sky[y, x] = dy
                    break

# 3. Base snow detection
snow_mask = np.zeros((135, 82), dtype=bool)

# Tip of tree: solid cap
for y in range(6):
    for x in range(82):
        if foliage_mask[y, x]:
            snow_mask[y, x] = True

# Sky exposed edges (top surface of outer branches)
for y in range(135):
    for x in range(82):
        if foliage_mask[y, x]:
            if dist_to_sky[y, x] <= 2:
                snow_mask[y, x] = True
            elif dist_to_sky[y, x] == 3 and arr[y, x] in (1, 2):
                snow_mask[y, x] = True

# Inner bough tops:
# In each column, detect transitions from dark shadow (3 or 4) to light foliage (1 or 2)
for x in range(82):
    for y in range(6, 135):
        if foliage_mask[y, x] and arr[y, x] in (1, 2):
            for dy in range(1, 5):
                if y - dy >= 0 and arr[y - dy, x] in (0, 3, 4):
                    snow_mask[y, x] = True
                    break

# 4. Fill gaps and make snow layers continuous across boughs
for iteration in range(3):
    new_snow = snow_mask.copy()
    for y in range(135):
        for x in range(1, 81):
            if foliage_mask[y, x] and not new_snow[y, x]:
                left = any(snow_mask[y, max(0, x-2):x])
                right = any(snow_mask[y, x+1:min(82, x+3)])
                if left and right and arr[y, x] in (1, 2, 4):
                    new_snow[y, x] = True
                if y > 0 and y < 134 and snow_mask[y-1, x] and snow_mask[y+1, x]:
                    new_snow[y, x] = True
    snow_mask = new_snow

# Give snow vertical substance (2-3 px pillows)
new_snow = snow_mask.copy()
for y in range(134):
    for x in range(82):
        if snow_mask[y, x] and not snow_mask[y+1, x] and foliage_mask[y+1, x]:
            col_snow_above = sum(snow_mask[max(0, y-2):y+1, x])
            if col_snow_above <= 2 and arr[y+1, x] in (1, 2):
                new_snow[y+1, x] = True
snow_mask = new_snow

# Fill internal holes inside snow (BFS from borders)
outside = np.zeros((135, 82), dtype=bool)
q = deque()
for x in range(82):
    if not snow_mask[0, x]:
        outside[0, x] = True
        q.append((0, x))
    if not snow_mask[134, x]:
        outside[134, x] = True
        q.append((134, x))
for y in range(135):
    if not snow_mask[y, 0]:
        outside[y, 0] = True
        q.append((y, 0))
    if not snow_mask[y, 81]:
        outside[y, 81] = True
        q.append((y, 81))

while q:
    cy, cx = q.popleft()
    for ny, nx in ((cy-1, cx), (cy+1, cx), (cy, cx-1), (cy, cx+1)):
        if 0 <= ny < 135 and 0 <= nx < 82:
            if not snow_mask[ny, nx] and not outside[ny, nx]:
                outside[ny, nx] = True
                q.append((ny, nx))

# Any non-outside pixel inside foliage is an enclosed hole -> fill with snow
for y in range(135):
    for x in range(82):
        if foliage_mask[y, x] and not outside[y, x]:
            snow_mask[y, x] = True

# 5. Remove tiny isolated snow specks (< 6 pixels) using BFS
visited = np.zeros((135, 82), dtype=bool)
for y in range(135):
    for x in range(82):
        if snow_mask[y, x] and not visited[y, x]:
            comp = []
            cq = deque([(y, x)])
            visited[y, x] = True
            while cq:
                py, px = cq.popleft()
                comp.append((py, px))
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        ny, nx = py + dy, px + dx
                        if 0 <= ny < 135 and 0 <= nx < 82:
                            if snow_mask[ny, nx] and not visited[ny, nx]:
                                visited[ny, nx] = True
                                cq.append((ny, nx))
            if len(comp) < 6:
                for py, px in comp:
                    snow_mask[py, px] = False

# Ensure tree tip (y <= 5) is completely snow
for y in range(6):
    for x in range(82):
        if foliage_mask[y, x]:
            snow_mask[y, x] = True

# 6. Proper Shading (gt09 = highlight white, gt08 = shadow periwinkle)
snow_shading = np.full((135, 82), 9, dtype=int)

for y in range(135):
    for x in range(82):
        if not snow_mask[y, x]:
            continue
            
        if y <= 4:
            snow_shading[y, x] = 9
            continue
            
        is_bottom = (y + 1 == 135) or (not snow_mask[y + 1, x])
        
        y_top = y
        while y_top > 0 and snow_mask[y_top - 1, x]:
            y_top -= 1
        strip_height = y - y_top + 1
        
        if is_bottom:
            if strip_height >= 2:
                snow_shading[y, x] = 8
            else:
                if y + 1 < 135 and arr[y + 1, x] in (3, 4):
                    snow_shading[y, x] = 8
                else:
                    snow_shading[y, x] = 9
                    
        if strip_height >= 4 and not is_bottom and y + 1 < 135 and snow_mask[y + 1, x]:
            if y + 2 == 135 or not snow_mask[y + 2, x]:
                if (x > 0 and not snow_mask[y, x - 1]) or (x < 81 and not snow_mask[y, x + 1]):
                    snow_shading[y, x] = 8

# 7. Apply to output canvas
for y in range(135):
    for x in range(82):
        if snow_mask[y, x]:
            c_name = 'gt08' if snow_shading[y, x] == 8 else 'gt09'
            output.set(x, y, c_name)

print(f"Total snow pixels: {np.sum(snow_mask)}, highlight={np.sum(snow_mask & (snow_shading == 9))}, shadow={np.sum(snow_mask & (snow_shading == 8))}")
view(output)
finish(output)
