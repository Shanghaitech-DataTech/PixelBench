from pixelbench_api import new_canvas, finish

W = H = 128


def lerp(c1, c2, t):
    r1 = int(c1[1:3], 16); g1 = int(c1[3:5], 16); b1 = int(c1[5:7], 16)
    r2 = int(c2[1:3], 16); g2 = int(c2[3:5], 16); b2 = int(c2[5:7], 16)
    return "#%02x%02x%02x" % (round(r1 + (r2 - r1) * t),
                             round(g1 + (g2 - g1) * t),
                             round(b1 + (b2 - b1) * t))


stops = [(0.00, "#14102e"), (0.30, "#4e2e74"), (0.55, "#a46a84"),
        (0.75, "#e8a470"), (0.90, "#ffd470"), (1.00, "#ffe8a0")]


def sky(t):
    for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
        if t <= t1:
            return lerp(c0, c1, (t - t0) / (t1 - t0))
    return stops[-1][1]


c = new_canvas(W, H)

# ---- sky gradient ----
n = 16
for i in range(n):
    c.rect(0, i * 4, W, 4, sky((i + 0.5) / n))

# ---- sun + glow (translucent layer composited over the sky) ----
g = new_canvas(W, H)
g.circle(64, 46, 16, (255, 205, 120, 80))
g.circle(64, 46, 11, (255, 226, 148, 70))
g.circle(64, 46, 6, (255, 240, 200, 255))
c.blit(g, 0, 0)

# ---- clouds ----
c.rect(16, 22, 12, 2, "#7c5c8a")
c.rect(20, 20, 6, 2, "#7c5c8a")
c.rect(94, 16, 12, 2, "#7c5c8a")
c.rect(100, 14, 6, 2, "#7c5c8a")

# ---- birds ----
bir = "#2a1a3c"
for bx, by in ((26, 11), (31, 14), (88, 10), (92, 13)):
    c.set(bx, by, bir)
    c.set(bx + 1, by + 1, bir)
    c.set(bx + 2, by, bir)

# ---- distant mountains (hazy purple) ----
c.poly([(0, 56), (8, 50), (16, 54), (24, 40), (30, 50), (40, 56),
       (48, 46), (56, 54), (64, 42), (72, 52), (80, 56), (88, 44),
       (96, 52), (104, 55), (112, 46), (120, 54), (127, 52),
       (127, 64), (0, 64)], "#5e5080")

# ---- mid mountains (blue) ----
c.poly([(0, 66), (10, 58), (18, 64), (28, 52), (38, 62), (48, 55),
       (58, 64), (68, 54), (78, 64), (88, 56), (98, 63), (108, 58),
       (118, 64), (127, 60), (127, 76), (0, 76)], "#40506a")

# ---- back hill (village clearing) ----
c.poly([(0, 84), (14, 79), (30, 77), (64, 75), (98, 77), (114, 79),
       (127, 84), (127, 128), (0, 128)], "#4e6a4c")
c.rect(50, 79, 10, 2, "#58784e")
c.rect(72, 78, 6, 2, "#58784e")
c.rect(42, 82, 8, 2, "#58784e")

# ---- left house ----
c.poly([(38, 75), (31, 88), (45, 88)], "#4a2a18")
c.line(31, 88, 45, 88, "#5e3a22")
c.rect(32, 88, 14, 12, "#8a5c3a")
for x in (34, 38, 42):
    c.line(x, 88, x, 99, "#6e4428")
c.rect(35, 91, 3, 7, "#2e1c10")
c.rect(40, 89, 3, 3, "#ff9a4a")
c.rect(40, 89, 3, 3, "#ffc85a")
c.set(41, 90, "#ffe8a0")
c.rect(33, 72, 5, 2, "#43434e")
c.rect(34, 74, 3, 8, "#565660")
for (sx, sy, sr, sc) in [(34, 71, 2, "#d8d0c8"), (30, 65, 2, "#d8d0c8"),
                        (26, 60, 2, "#c0b8ae")]:
    c.circle(sx, sy, sr, sc)

# ---- centre house (focal point) ----
c.poly([(64, 68), (51, 85), (77, 85)], "#4a2a18")
c.line(51, 85, 77, 85, "#5e3a22")
c.rect(54, 85, 20, 15, "#8a5c3a")
for x in (57, 61, 65, 69, 73):
    c.line(x, 85, x, 99, "#6e4428")
c.rect(62, 91, 4, 8, "#2e1c10")
c.rect(56, 87, 3, 3, "#ff9a4a")
c.rect(56, 87, 3, 3, "#ffc85a")
c.set(57, 88, "#ffe8a0")
c.rect(70, 87, 3, 3, "#ff9a4a")
c.rect(70, 87, 3, 3, "#ffc85a")
c.set(71, 88, "#ffe8a0")
c.rect(70, 72, 5, 2, "#43434e")
c.rect(71, 74, 3, 8, "#565660")
for (sx, sy, sr, sc) in [(72, 70, 2, "#d8d0c8"), (77, 64, 2, "#d8d0c8"),
                        (82, 58, 2, "#d0c8be"), (78, 52, 2, "#c0b8ae"),
                        (84, 48, 1, "#c0b8ae")]:
    c.circle(sx, sy, sr, sc)

# ---- right house ----
c.poly([(89, 76), (78, 88), (99, 88)], "#4a2a18")
c.line(78, 88, 99, 88, "#5e3a22")
c.rect(81, 88, 16, 13, "#8a5c3a")
for x in (84, 88, 92, 95):
    c.line(x, 88, x, 100, "#6e4428")
c.rect(87, 91, 3, 7, "#2e1c10")
c.rect(92, 89, 3, 3, "#ff9a4a")
c.rect(92, 89, 3, 3, "#ffc85a")
c.set(93, 90, "#ffe8a0")
c.rect(93, 78, 5, 2, "#43434e")
c.rect(94, 80, 3, 8, "#565660")
for (sx, sy, sr, sc) in [(95, 77, 2, "#d8d0c8"), (100, 71, 2, "#d8d0c8"),
                        (105, 66, 2, "#c0b8ae"), (101, 61, 2, "#c0b8ae")]:
    c.circle(sx, sy, sr, sc)

# ---- grass strip ----
c.rect(0, 116, 128, 12, "#22301e")

# ---- pine trees ----
def pine(x, ground, h, w, col):
    c.poly([(x, ground - h), (x - w, ground), (x + w, ground)], col)
    c.rect(x - 1, ground, 2, 4, "#2e2214")


# back pines
for (x, gr, h, w) in [(24, 86, 14, 5), (12, 84, 12, 4),
                     (104, 86, 13, 5), (115, 84, 11, 4)]:
    pine(x, gr, h, w, "#36543e")

# mid pines
pine(17, 106, 24, 8, "#1e3a26")
pine(113, 106, 22, 7, "#1e3a26")

# foreground pines (framing)
pine(8, 124, 30, 9, "#162c1c")
pine(121, 124, 29, 9, "#162c1c")

# ---- stone path ----
c.poly([(34, 128), (44, 114), (54, 103), (62, 100), (66, 102),
       (72, 110), (82, 128)], "#6e6a60")

stones = [(58, 123, 4, "#8a8478"), (68, 121, 3, "#a89e8e"),
          (62, 118, 3, "#948e80"), (53, 116, 3, "#7e786c"),
          (66, 112, 3, "#948e80"), (59, 109, 2, "#a89e8e"),
          (73, 124, 3, "#7e786c"), (48, 120, 3, "#8a8478"),
          (63, 104, 2, "#a89e8e"), (58, 110, 2, "#7e786c"),
          (77, 127, 2, "#8a8478"), (66, 106, 1, "#948e80"),
          (70, 104, 1, "#7e786c")]

# ---- grass tufts beside the path ----
for (tx, ty, tw, th) in [(38, 122, 5, 2), (80, 120, 5, 2), (28, 110, 4, 2),
                        (96, 111, 4, 2)]:
    c.rect(tx, ty, tw, th, "#182618")

# ---- final stone details (drawn last) ----
for (sx, sy, sr, sc) in stones:
    c.circle(sx, sy, sr, sc)

print(c.stats_text())
finish(c)
