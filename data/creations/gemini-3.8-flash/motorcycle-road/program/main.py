from collections import deque
import math

w, h = 64, 64

# 1. Identify exterior pixels of input_canvas (white background)
exterior = set()
q = deque([(0,0), (0, h-1), (w-1, 0), (w-1, h-1)])
visited = set(q)
while q:
    x, y = q.popleft()
    if input_canvas.get(x, y) == 1:
        exterior.add((x, y))
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                visited.add((nx, ny))
                if input_canvas.get(nx, ny) == 1:
                    q.append((nx, ny))

# 2. Build the Country Road Background
bg = new_canvas(64, 64, background="#4a88c8")

# --- SKY GRADIENT ---
sky_colors = [
    (0, 3, "#3a7ec2"),
    (4, 7, "#5294d4"),
    (8, 11, "#72aee6"),
    (12, 14, "#94c8f2"),
    (15, 17, "#bce0fa"),
]
for y0, y1, col in sky_colors:
    bg.rect(0, y0, 64, y1 - y0 + 1, col)

# --- CLOUDS ---
# Cloud 1 (top left)
bg.rect(5, 3, 8, 3, "#ffffff")
bg.rect(7, 2, 5, 2, "#ffffff")
bg.rect(4, 4, 11, 2, "#ffffff")
bg.rect(3, 5, 13, 2, "#f0f6fc")
bg.rect(4, 6, 11, 1, "#d0e4f4")

# Cloud 2 (top right)
bg.rect(46, 5, 11, 4, "#ffffff")
bg.rect(48, 4, 7, 2, "#ffffff")
bg.rect(44, 6, 15, 3, "#ffffff")
bg.rect(43, 7, 17, 2, "#f0f6fc")
bg.rect(45, 8, 14, 2, "#d0e4f4")

# Tiny distant birds in sky
bg.set(25, 6, "#345678")
bg.set(27, 6, "#345678")
bg.set(26, 7, "#345678")

bg.set(31, 8, "#406284")
bg.set(33, 8, "#406284")
bg.set(32, 9, "#406284")

# --- DISTANT MOUNTAINS (y=12..21) ---
mountains = [
    (0, 16), (4, 15), (9, 13), (13, 14), (18, 16), (23, 15), 
    (28, 13), (33, 14), (39, 16), (45, 13), (50, 12), (56, 14), (63, 16)
]
m_ridge = {}
for i in range(len(mountains)-1):
    x0, y0 = mountains[i]
    x1, y1 = mountains[i+1]
    for x in range(x0, x1+1):
        t = (x - x0) / (x1 - x0)
        m_ridge[x] = int(y0 + t * (y1 - y0) + 0.5)

for x in range(64):
    yr = m_ridge[x]
    for y in range(yr, 22):
        if y == yr:
            bg.set(x, y, "#94acca")
        elif (x + y) % 3 == 0:
            bg.set(x, y, "#728aa8")
        else:
            bg.set(x, y, "#607896")

# --- MIDGROUND ROLLING HILLS (y=18..28) ---
for x in range(64):
    y_hill = int(21 - 3 * math.cos((x - 10) * 0.08) - 2 * math.sin((x - 30) * 0.06))
    for y in range(y_hill, 32):
        if y == y_hill:
            bg.set(x, y, "#7ec454")
        elif y == y_hill + 1:
            bg.set(x, y, "#64aa3e")
        else:
            bg.set(x, y, "#4c8a2e")

# Clumps of trees on the hills
def draw_tree(canvas, cx, cy, rx, ry):
    for dy in range(-ry, ry+1):
        for dx in range(-rx, rx+1):
            if (dx*dx)/(rx*rx + 0.1) + (dy*dy)/(ry*ry + 0.1) <= 1.0:
                px, py = cx + dx, cy + dy
                if 0 <= px < 64 and 0 <= py < 64:
                    if dy < -ry//2:
                        canvas.set(px, py, "#589c44")
                    elif dy < 0:
                        canvas.set(px, py, "#3e7c32")
                    else:
                        canvas.set(px, py, "#2a5c24")

draw_tree(bg, 5, 19, 4, 3)
draw_tree(bg, 9, 20, 3, 3)
draw_tree(bg, 23, 23, 3, 2)
draw_tree(bg, 56, 20, 4, 3)
draw_tree(bg, 60, 21, 2, 2)

# Little country barn on the left hill (x=14..20, y=18..25)
bg.rect(14, 21, 6, 4, "#a43232")
bg.poly([(13, 21), (17, 18), (20, 21)], "#4a444a")
bg.rect(16, 23, 2, 2, "#e8e8e8")
bg.set(15, 22, "#e8e8e8")
bg.set(18, 22, "#e8e8e8")

# --- ROADSIDE MEADOW & GRASS (y=28..39) ---
for y in range(28, 40):
    for x in range(64):
        if y < 32:
            col = "#5ca638" if (x+y)%4 != 0 else "#6db844"
        elif y < 36:
            col = "#68b440" if (x*3+y)%5 != 0 else "#549e34"
        else:
            col = "#5aa436" if (x+y*2)%3 != 0 else "#72c248"
        bg.set(x, y, col)

# Meadow wildflowers
flowers = [
    (3, 30, "#e83434"), (7, 34, "#ffcc22"), (11, 31, "#ffffff"),
    (18, 35, "#e83434"), (22, 32, "#ffcc22"), (27, 36, "#ffffff"),
    (32, 33, "#ffcc22"), (36, 37, "#e83434"), (41, 32, "#ffffff"),
    (48, 35, "#ffcc22"), (54, 31, "#e83434"), (60, 34, "#ffcc22"),
]
for fx, fy, fcol in flowers:
    bg.set(fx, fy, fcol)

# --- RUSTIC WOODEN FENCE (y=32..38) ---
fence_posts_x = [2, 14, 26, 38, 50, 62]
for rx in range(64):
    bg.set(rx, 34, "#8a5c36")
    bg.set(rx, 37, "#7a4e2a")

for px in fence_posts_x:
    bg.rect(px, 32, min(2, 64-px), 7, "#6a4020")
    bg.rect(px, 32, 1, 7, "#9c683e")
    bg.set(px, 31, "#9c683e")
    if px+1 < 64:
        bg.set(px+1, 31, "#6a4020")
    if 0 <= px-1 < 64:
        bg.set(px-1, 38, "#3e7c28")
    if 0 <= px+2 < 64:
        bg.set(px+2, 38, "#3e7c28")

# --- FAR SHOULDER / GRAVEL (y=39..42) ---
for y in range(39, 43):
    for x in range(64):
        if y == 39:
            bg.set(x, y, "#7ea442" if (x+y)%2 == 0 else "#a88c5a")
        elif y == 40:
            bg.set(x, y, "#b09462" if (x*2+y)%3 != 0 else "#8c7246")
        elif y == 41:
            bg.set(x, y, "#9a8052" if (x+y)%2 == 0 else "#7c6440")
        else:
            bg.set(x, y, "#5a4e44")

pebbles = [(5, 40), (12, 41), (25, 40), (34, 41), (47, 40), (58, 41)]
for px, py in pebbles:
    bg.set(px, py, "#d8cca8")
    bg.set(px+1, py, "#483c30")

# --- THE ASPHALT COUNTRY ROAD (y=43..56) ---
for y in range(43, 57):
    for x in range(64):
        if y == 43:
            col = "#444046"
        elif y == 56:
            col = "#403c42"
        else:
            val = (x * 7 + y * 13) % 11
            if val < 2:
                col = "#545058"
            elif val > 8:
                col = "#64606a"
            else:
                col = "#5c5862"
        bg.set(x, y, col)

# Road Center Dashed Yellow Line (y=44..45)
for x in range(64):
    if (x % 12) < 6:
        if 20 <= x <= 45: # shaded under the motorcycle
            bg.set(x, 44, "#8c6c18")
            bg.set(x, 45, "#705414")
        else:
            bg.set(x, 44, "#f0be30")
            bg.set(x, 45, "#c49420")

# --- MOTORCYCLE CONTACT SHADOWS ON ROAD ---
for x in range(11, 22):
    bg.set(x, 47, "#242026")
    bg.set(x, 48, "#322e36")

for x in range(45, 56):
    bg.set(x, 47, "#242026")
    bg.set(x, 48, "#322e36")

for x in range(22, 45):
    bg.set(x, 47, "#302c34")
    bg.set(x, 48, "#38343e")

# --- NEAR ROAD SHOULDER & FOREGROUND VERGE (y=57..63) ---
for x in range(64):
    bg.set(x, 57, "#8c7246" if x % 2 == 0 else "#a88c5a")

for y in range(58, 64):
    for x in range(64):
        if y == 58:
            bg.set(x, y, "#488226" if (x+y)%3 != 0 else "#62a836")
        elif y < 61:
            bg.set(x, y, "#5aa032" if (x*3+y)%4 != 0 else "#72b840")
        else:
            bg.set(x, y, "#447822" if (x+y)%2 == 0 else "#56942c")

for gx in [3, 8, 14, 19, 27, 33, 40, 48, 55, 60]:
    bg.set(gx, 57, "#62a836")
    if gx+1 < 64:
        bg.set(gx+1, 56, "#72b840")

fg_flowers = [
    (5, 60, "#ffdd22"), (6, 60, "#ffe855"),
    (16, 61, "#e83030"), (17, 61, "#ff5555"),
    (24, 59, "#ffffff"), (25, 59, "#ffffff"),
    (36, 61, "#4088e8"), (37, 61, "#66aaff"),
    (44, 60, "#ffdd22"), (45, 60, "#ffe855"),
    (52, 62, "#e83030"),
    (58, 60, "#ffffff"), (59, 60, "#ffffff")
]
for fx, fy, fcol in fg_flowers:
    bg.set(fx, fy, fcol)

# 3. Composite the motorcycle on top of the background
output = bg.copy(name="output")
for y in range(64):
    for x in range(64):
        if (x, y) not in exterior:
            output.set(x, y, input_canvas.get(x, y))

view(output)
finish(output)
