from pixelbench_api import *

W = H = 64
c = new_canvas(W, H, name="combo")

SH = (0, 0, 0, 95)


def rrect(c, x, y, w, h, r, colr):
    c.rect(x + r, y, w - 2 * r, h, colr)
    c.rect(x, y + r, w, h - 2 * r, colr)
    for cx, cy in [(x + r, y + r), (x + w - r - 1, y + r), (x + r, y + h - r - 1), (x + w - r - 1, y + h - r - 1)]:
        c.circle(cx, cy, r, colr)


def loose_fry(sx, sy):
    c.line(sx - 1, sy, sx + 2, sy + 3, "#5A3A08")
    c.line(sx, sy, sx + 3, sy + 3, "#E8A52F")
    c.line(sx + 1, sy, sx + 4, sy + 3, "#5A3A08")
    c.set(sx + 1, sy, "#FFE28A")


# ---------------- table (checkered) ----------------
for ty in range(8):
    for tx in range(8):
        c.rect(tx * 8, ty * 8, 8, 8, "#F3EAD6" if (tx + ty) % 2 == 0 else "#EDE1C6")

# ---------------- tray ----------------
rrect(c, 6, 7, 56, 56, 8, SH)
rrect(c, 4, 4, 56, 56, 7, "#2E0A0A")
rrect(c, 5, 5, 54, 54, 6, "#B03434")
c.rect(6, 5, 52, 1, "#C94848")
rrect(c, 7, 7, 50, 50, 5, "#9E2C2C")
rrect(c, 9, 9, 46, 46, 5, "#B98F5C")
rrect(c, 10, 10, 44, 44, 4, "#FBF3DE")
c.rect(13, 50, 38, 4, "#E4D5AE")
c.rect(13, 11, 36, 2, "#FFF9EC")

# ---------------- cheeseburger ----------------
c.ellipse(24, 26, 13, 12, SH)
# lettuce
c.ellipse(23, 24, 12, 11, "#1E3A0E")
c.ellipse(23, 24, 11, 10, "#63B43C")
for (bx, by) in [(12, 18), (12, 25), (12, 31), (19, 34), (27, 34), (33, 29), (33, 21), (33, 16), (20, 14), (28, 14)]:
    c.circle(bx, by, 2, "#4C9A2F")
c.ellipse(19, 19, 5, 4, "#7BD054")
# melted cheese drips
c.ellipse(23, 23, 10, 9, "#7A520A")
c.ellipse(23, 23, 9, 8, "#F5C542")
for (bx, by) in [(18, 33), (24, 35), (29, 33)]:
    c.circle(bx, by, 2, "#7A520A")
    c.circle(bx, by, 1, "#F5C542")
    c.set(bx, by + 2, "#F5C542")
    c.set(bx, by + 3, "#F5C542")
    c.set(bx - 1, by + 1, "#FFD96A")
# bun
c.ellipse(23, 23, 11, 10, "#3A2208")
c.ellipse(23, 23, 10, 9, "#E8A33D")
c.ellipse(25, 25, 6, 5, "#C67E1F")
c.ellipse(20, 19, 5, 4, "#F0B957")
c.ellipse(20, 18, 3, 2, "#FBD988")
for (sx, sy) in [(19, 20), (22, 17), (26, 17), (30, 19), (31, 23), (29, 27), (25, 29), (21, 29)]:
    c.set(sx, sy, "#FFF3D6")
for (gx, gy) in [(16, 17), (27, 18), (20, 25)]:
    c.set(gx, gy, "#7BD054")
for (cx, cy) in [(37, 16), (39, 19), (36, 26), (38, 29)]:
    c.set(cx, cy, "#A86A1F")

# ---------------- fries carton ----------------
rrect(c, 41, 12, 17, 16, 2, SH)
rrect(c, 39, 9, 18, 17, 3, "#3A0E0E")
rrect(c, 40, 10, 16, 15, 2, "#D94040")
c.rect(53, 11, 3, 12, "#A92A2A")
c.rect(41, 11, 2, 11, "#E85555")
FRIES = [(42, 7, 7), (44, 5, 9), (46, 4, 10), (48, 4, 10), (50, 5, 9), (52, 4, 10), (54, 6, 8),
        (43, 10, 7), (45, 9, 8), (47, 9, 9), (49, 9, 9), (51, 9, 8), (53, 9, 7), (55, 9, 6)]
for (fx, fy, fh) in FRIES:
    c.rect(fx, fy, 3, fh, "#5A3A08")
    c.rect(fx, fy, 2, fh, "#E8A52F")
    c.set(fx, fy, "#FFE28A")
    c.set(fx + 1, fy, "#F2BE3C")
c.rect(41, 18, 14, 6, "#F8F1E4")
c.text(46, 18, "F", "#D94040", font="5x7")

# loose fries on tray
loose_fry(33, 20)
loose_fry(35, 29)

# ---------------- cola cup ----------------
rrect(c, 42, 40, 15, 15, 2, SH)
rrect(c, 40, 36, 17, 19, 3, "#330A0A")
rrect(c, 41, 37, 15, 17, 3, "#C22F2F")
c.rect(53, 38, 3, 13, "#962323")
c.rect(42, 38, 2, 13, "#D84343")
c.ellipse(49, 38, 8, 7, "#330A0A")
c.ellipse(49, 38, 7, 6, "#3B1F0C")
c.ellipse(47, 35, 3, 2, "#5E3A1E")
for (ix, iy) in [(45, 35), (49, 33), (52, 37), (46, 40), (50, 38)]:
    c.rect(ix, iy, 3, 3, "#3A6E88")
    c.rect(ix + 1, iy + 1, 2, 2, "#DDF2FC")
    c.set(ix + 1, iy + 1, "#FFFFFF")
    c.set(ix + 2, iy + 2, "#8FBFD8")
c.rect(41, 45, 14, 3, "#F8F1E4")

# straw (red with white stripes, leaning from cup toward the burger)
for i in range(12):
    bx = 34 + i
    by = 28 + i
    c.rect(bx, by, 2, 2, "#4A0E0E")
    if i % 3 == 2:
        c.rect(bx, by, 2, 2, "#F8F1E4")
    else:
        c.rect(bx, by, 2, 2, "#E23333")
    c.set(bx, by, "#F05050")

# ---------------- chicken nuggets ----------------
nugs = [(13, 45, 3), (18, 43, 3), (22, 46, 3), (15, 50, 3), (11, 51, 2)]
for (nx, ny, nr) in nugs:
    c.circle(nx + 1, ny + 1, nr, SH)
    c.circle(nx, ny, nr + 1, "#40220A")
    c.circle(nx, ny, nr, "#D99A3D")
    c.circle(nx - 1, ny - 1, nr - 1, "#EFC06E")
    c.set(nx - 1, ny - 1, "#F8D48A")

# ---------------- dipping sauce cups ----------------
for (sx, sy, sauce, sl) in [(32, 50, "#D63A2A", "#E85530"), (28, 45, "#8A4A1A", "#A86226")]:
    c.circle(sx, sy, 3, "#2A1A10")
    c.circle(sx, sy, 2, "#F0E6D0")
    c.circle(sx, sy, 1, sauce)
    c.set(sx - 1, sy - 1, "#FFF4DC")

print(c.stats_text())
finish(c)
