from pixelbench_api import new_canvas, finish
import math

c = new_canvas(64, 64, name="result")


def blade(hx, hy, ang, L, w2, col, seam):
    a = math.radians(ang)
    tip = (int(round(hx + L * math.cos(a))), int(round(hy + L * math.sin(a))))
    p1 = (int(round(hx - w2 * math.sin(a))), int(round(hy + w2 * math.cos(a))))
    p2 = (int(round(hx + w2 * math.sin(a))), int(round(hy - w2 * math.cos(a))))
    c.poly([p1, p2, tip], col)
    c.line(hx, hy, tip[0], tip[1], seam)


def distant(cx, tt, L, nw):
    # tower (above water only; ocean painted after)
    c.rect(cx - 1, tt, 2, 48 - tt + 1, "#7EA4C6")
    blade(cx, tt - 1, -90, L, 1, "#CDDFEB", "#B7CFE1")
    blade(cx, tt - 1, 30, L, 1, "#CDDFEB", "#B7CFE1")
    blade(cx, tt - 1, 150, L, 1, "#CDDFEB", "#B7CFE1")
    c.rect(cx - 1, tt - 2, nw, 2, "#9FBBD3")
    c.set(cx, tt - 1, "#C6D8E6")


# ---------------- sky ----------------
c.rect(0, 0, 64, 8, "#6BB3DD")
c.rect(0, 8, 64, 8, "#7DBFE4")
c.rect(0, 16, 64, 8, "#90CAEA")
c.rect(0, 24, 64, 8, "#A4D4EF")
c.rect(0, 32, 64, 8, "#B9DEF2")
c.rect(0, 40, 64, 6, "#CBE7F5")
c.rect(0, 46, 64, 2, "#DCEFF8")

# sun
c.circle(12, 6, 4, "#F0DA9F")
c.circle(12, 6, 3, "#FFE9AC")

# clouds
c.circle(6, 15, 2, "#FFFFFF")
c.circle(9, 16, 3, "#FFFFFF")
c.circle(13, 15, 2, "#FFFFFF")
c.circle(36, 18, 2, "#FFFFFF")
c.circle(39, 19, 3, "#FFFFFF")
c.circle(43, 18, 2, "#FFFFFF")

# ---------------- distant turbines ----------------
distant(44, 34, 8, 6)
distant(57, 38, 7, 5)

# ---------------- ocean ----------------
c.rect(0, 48, 64, 1, "#83B4D6")
c.rect(0, 49, 64, 2, "#5F98C2")
c.rect(0, 51, 64, 3, "#4282B4")
c.rect(0, 54, 64, 4, "#2E6CA2")
c.rect(0, 58, 64, 3, "#26598E")
c.rect(0, 61, 64, 3, "#1F4C7C")

# ---------------- maintenance deck ----------------
c.rect(7, 42, 31, 2, "#71889E")
c.rect(7, 44, 31, 2, "#576D84")
c.rect(7, 44, 31, 1, "#D9A72B")
c.rect(7, 46, 31, 1, "#485E74")
c.rect(7, 40, 31, 1, "#8FA6BC")
for px in (9, 13, 18, 24, 31, 36):
    c.rect(px, 40, 1, 3, "#71889E")

# deck legs + braces
c.rect(10, 44, 2, 12, "#64798F")
c.rect(31, 44, 2, 12, "#64798F")
c.line(10, 46, 31, 53, "#485E75")
c.line(31, 46, 10, 53, "#485E75")
c.rect(10, 50, 2, 6, "#4273A4")
c.rect(31, 50, 2, 6, "#4273A4")

# ---------------- tower ----------------
c.poly([(21, 44), (30, 44), (28, 13), (24, 13)], "#93ABC1")
c.poly([(26, 13), (28, 13), (30, 44), (27, 44)], "#7B96B0")
c.rect(22, 17, 1, 27, "#AEC2D3")

# ladder on tower
c.rect(24, 15, 1, 30, "#C2D4E2")
c.rect(27, 15, 1, 30, "#C2D4E2")
for y in range(16, 45, 2):
    c.rect(24, y, 4, 1, "#C2D4E2")

# ---------------- rotor ----------------
blade(25, 12, -90, 12, 2, "#E3EDF5", "#BFD3E3")
blade(25, 12, 30, 12, 2, "#E3EDF5", "#BFD3E3")
blade(25, 12, 150, 12, 2, "#E3EDF5", "#BFD3E3")
c.rect(18, 11, 16, 4, "#AFC5D8")
c.rect(18, 11, 16, 1, "#CFDEE9")
c.rect(18, 14, 16, 1, "#8FA7BC")
c.rect(29, 12, 3, 2, "#274E78")
c.circle(25, 12, 2, "#CFDEE9")
c.circle(25, 12, 1, "#EAF2F8")

# ---------------- technician on ladder ----------------
c.set(25, 27, "#EE7D1E")          # helmet
c.set(24, 28, "#F6B41F")          # hi-vis vest
c.set(25, 28, "#F6B41F")
c.set(26, 28, "#F6B41F")          # hand on rail
c.set(24, 29, "#3A4A60")          # trousers
c.set(25, 29, "#3A4A60")
c.set(25, 30, "#2E3D52")           # boot

# ---------------- water details ----------------
# shadow of deck on water
c.rect(9, 49, 27, 2, "#4A87B8")
# reflections
c.rect(24, 50, 4, 3, "#6DA3C9")
c.rect(25, 53, 2, 4, "#4E89B8")

dashes = [
    (49, "#7FB0D2", [(2, 5), (15, 4), (27, 6), (41, 5), (53, 4)]),
    (49, "#DCEFF4", [(8, 3), (30, 3), (48, 3)]),
    (51, "#5D96C0", [(6, 4), (20, 5), (35, 4), (50, 5), (60, 3)]),
    (51, "#8FBFDA", [(12, 2), (25, 2), (44, 3)]),
    (53, "#4A88B8", [(10, 4), (28, 4), (46, 4), (58, 3)]),
    (53, "#7CB2D3", [(17, 2), (38, 2)]),
    (55, "#3F7FB2", [(6, 3), (22, 5), (36, 3), (52, 4)]),
    (57, "#3470A6", [(14, 4), (30, 3), (47, 4)]),
    (59, "#2C6398", [(8, 3), (25, 4), (42, 3), (56, 3)]),
    (61, "#255789", [(16, 3), (34, 3), (50, 3)]),
]
for y, col, segs in dashes:
    for x, l in segs:
        c.rect(x, y, l, 1, col)

print(c.stats_text())
print("colors used:", len(c.palette()))

finish(c)
