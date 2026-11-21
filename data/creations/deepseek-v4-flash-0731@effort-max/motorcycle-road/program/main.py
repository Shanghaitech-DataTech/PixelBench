from pixelbench_api import *

c = input_canvas.copy(name="output")

white = c.get(0, 0)
sky   = c.color("#a5d4f7")
sky2  = c.color("#bcdcf6")
far   = c.color("#9ed07a")
near  = c.color("#6db84c")
dark  = c.color("#4f9a36")
gravel = c.color("#868686")
roadc = c.color("#a3a3a3")
road2 = c.color("#8f8f8f")
edge  = c.color("#6a6a6a")
line  = c.color("#e8c44a")
shadowc = c.color("#333333")
sun   = c.color("#ffe873")

def far_bottom(x):
    b = 33
    if 8 <= x <= 20: b = 34
    if 28 <= x <= 40: b = 35
    if 46 <= x <= 58: b = 34
    return b

def put(x, y, col, guards):
    if 0 <= x < 64 and 0 <= y < 64 and c.get(x, y) in guards:
        c.set(x, y, col)

# 1) paint the country scene on the white background only
for y in range(64):
    for x in range(64):
        if c.get(x, y) != white:
            continue
        fb = far_bottom(x)
        if y < 30:
            col = sky if y < 23 else sky2
        elif y < fb:
            col = far
        elif y < 37:
            col = near
        elif y < 40:
            col = gravel
        elif y > 61:
            col = edge
        elif y > 53:
            col = road2
        else:
            col = roadc
        c.set(x, y, col)

# 2) sun
for y in range(6, 15):
    for x in range(46, 55):
        if (x - 50) ** 2 + (y - 10) ** 2 <= 17:
            put(x, y, sun, (sky, sky2))

# 3) clouds
for cx, cy, rx, ry in [(12, 8, 7, 2), (30, 15, 5, 2), (45, 5, 4, 2), (57, 12, 3, 1), (4, 13, 4, 2)]:
    for y in range(cy - ry, cy + ry + 1):
        for x in range(cx - rx, cx + rx + 1):
            if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1:
                put(x, y, white, (sky, sky2))

# 4) trees / bushes in the fields
for cx, cy, r, col in [(15, 32, 2, dark), (4, 35, 2, dark), (60, 33, 2, dark),
                      (2, 30, 1, dark), (63, 36, 1, dark), (57, 35, 1, dark)]:
    for y in range(cy - r, cy + r + 1):
        for x in range(cx - r, cx + r + 1):
            if (x - cx) ** 2 + (y - cy) ** 2 <= r * r:
                put(x, y, col, (far, near))

# 5) soft shadow beneath the motorcycle on the road
for y in range(43, 51):
    for x in range(12, 55):
        if ((x - 33) / 20.0) ** 2 + ((y - 46) / 3.4) ** 2 <= 1.0:
            put(x, y, shadowc, (roadc, road2, gravel))

# 6) dashed centre line
for s in range(-2, 64, 12):
    for x in range(max(0, s), min(s + 7, 64)):
        for y in (49, 50):
            put(x, y, line, (roadc, road2))

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 26)))
print(c.matrix_text(region=(0, 27, 63, 63)))
finish(c)
