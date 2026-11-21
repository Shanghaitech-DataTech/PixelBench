from pixelbench_api import new_canvas, finish

W = H = 128
scene = new_canvas(W, H, name="standoff")

# ---------------- background ----------------
for y0, y1, hx in [
    (0, 6, "#0f0d24"),
    (6, 14, "#15132e"),
    (14, 24, "#201d45"),
    (24, 36, "#332a5c"),
    (36, 50, "#553e6e"),
    (50, 66, "#8a547b"),
    (66, 84, "#c26d6d"),
    (84, 100, "#ef9a56"),
]:
    scene.rect(0, y0, W, y1 - y0, hx)

# thin anime cloud wisps
scene.rect(6, 9, 26, 3, "#1c1a38")
scene.rect(88, 7, 30, 3, "#181630")

# sun between them
scene.circle(64, 34, 17, "#ffd27a")
scene.circle(64, 34, 11, "#ffe9b0")
for (rx, ry) in [(64, 13), (64, 55), (43, 34), (85, 34),
                (49, 19), (79, 19), (49, 49), (79, 49)]:
    scene.set(rx, ry, "#ffd27a")

# distant mountains
scene.poly([(0, 90), (18, 66), (34, 78), (52, 70), (66, 90), (54, 97), (0, 97)], "#241f3d")
scene.poly([(64, 90), (80, 72), (100, 82), (114, 74), (128, 90), (128, 97), (64, 97)], "#241f3d")

# ground
scene.rect(0, 100, W, 3, "#33283a")
scene.rect(0, 103, W, 25, "#191322")
scene.rect(50, 100, 28, 4, "#ef9a56")  # sun reflection

# wind streaks in the gap between the rivals
for (sx, sy, ln) in [(52, 26, 8), (56, 34, 10), (50, 44, 5), (58, 76, 4)]:
    scene.rect(sx, sy, ln, 1, "#ef9a56")

# ground cast shadows
scene.ellipse(20, 107, 27, 4, "#0a0813")
scene.ellipse(106, 107, 27, 4, "#0a0813")

# ---------------- knight (left, red armor) ----------------
k = new_canvas(W, H, name="knight")
# plume flowing back
k.poly([(20, 10), (33, 13), (38, 22), (33, 32), (25, 30), (15, 28), (12, 20)], "#e86a5a")
k.poly([(22, 15), (31, 17), (34, 23), (27, 27), (19, 24)], "#f08a6a")
# helmet
k.ellipse(32, 44, 11, 10, "#c83a3a")
k.rect(26, 39, 16, 5, "#5a6472")
k.set(32, 40, "#ffd27a")
k.set(33, 41, "#ffd27a")
k.set(38, 40, "#ffd27a")
k.set(39, 41, "#ffd27a")
# neck
k.rect(29, 49, 7, 7, "#5a6472")
# pauldrons
k.ellipse(20, 56, 9, 7, "#8f2228")
k.ellipse(42, 56, 9, 7, "#8f2228")
# torso
k.poly([(16, 60), (44, 60), (40, 86), (20, 86)], "#c83a3a")
k.rect(25, 62, 12, 16, "#e86a5a")
k.circle(31, 69, 3, "#e8b64c")
k.rect(20, 78, 21, 4, "#e8b64c")
# legs + boots
k.rect(22, 82, 7, 13, "#5a6472")
k.rect(35, 82, 7, 13, "#5a6472")
k.rect(20, 93, 11, 7, "#14101c")
k.rect(33, 93, 11, 7, "#14101c")
# shield
k.poly([(6, 53), (17, 51), (19, 64), (16, 83), (8, 83)], "#8f2228")
k.poly([(8, 57), (16, 55), (17, 63), (14, 79), (9, 79)], "#c83a3a")
k.circle(11, 66, 2, "#cfd6e0")
# sword (point down at his side)
k.circle(46, 51, 2, "#e8b64c")
k.rect(45, 53, 3, 7, "#14101c")
k.rect(41, 60, 10, 4, "#e8b64c")
k.rect(43, 64, 4, 32, "#cfd6e0")
k.rect(46, 64, 1, 32, "#eef4fa")
k.poly([(43, 96), (47, 96), (45, 100)], "#cfd6e0")

# ---------------- rogue (right, green cloak) ----------------
r = new_canvas(W, H, name="rogue")
# hood + pointed tip
r.ellipse(96, 44, 11, 10, "#3fae5a")
r.poly([(84, 40), (76, 50), (87, 54)], "#2c8a4a")
r.ellipse(93, 45, 7, 6, "#123c24")
r.set(85, 42, "#c8ffae")
r.set(86, 43, "#c8ffae")
r.set(92, 42, "#c8ffae")
r.set(93, 43, "#c8ffae")
# scarf tail
r.poly([(108, 50), (123, 56), (119, 70), (106, 64)], "#2c8a4a")
# cloak body
r.poly([(80, 56), (112, 56), (117, 72), (113, 94), (98, 102), (82, 94), (77, 72)], "#3fae5a")
r.rect(86, 60, 3, 28, "#22663a")
r.rect(94, 62, 3, 30, "#22663a")
r.rect(102, 60, 3, 26, "#22663a")
r.rect(78, 58, 2, 30, "#6fd47f")
# arm + hand
r.rect(78, 56, 8, 8, "#22663a")
r.circle(77, 61, 3, "#123c24")
# dagger
r.poly([(80, 58), (70, 70), (73, 75), (81, 61)], "#cfd6e0")
r.poly([(80, 58), (70, 70), (72, 72), (79, 60)], "#eef4fa")
# boots
r.rect(84, 94, 10, 7, "#4a3626")
r.rect(98, 94, 10, 7, "#4a3626")


def outlined(src, dark):
    w2, h2, data = src.to_rgba()
    d = new_canvas(w2, h2)
    for yy in range(h2):
        off = yy * w2 * 4
        for xx in range(w2):
            if data[off + xx * 4 + 3] > 0:
                d.set(xx, yy, dark)
    out = new_canvas(w2, h2)
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            t = d.copy()
            t.shift(dx, dy)
            out.blit(t, 0, 0)
    out.blit(src, 0, 0)
    return out


scene.blit(outlined(k, "#0d0b16"), 0, 0)
scene.blit(outlined(r, "#0d0b16"), 0, 0)

# embers rising in the gap
for x, y in [(58, 70), (63, 58), (67, 68), (56, 50), (68, 46), (60, 94), (67, 90),
            (55, 84), (69, 80), (61, 100)]:
    scene.set(x, y, "#ff9d3c")

print(scene.stats_text())
print(scene.matrix_text(region=(44, 22, 84, 58)))
finish(scene)
