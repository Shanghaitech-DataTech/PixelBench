# ============================================================
#  Explosion effect - 64x64, two animation frames on one sheet
#  Frame 1 (left 32x32):  bright yellow fireball at centre
#  Frame 2 (right 32x32): expanding orange-red blast + sparks
#  Background: fully transparent
# ============================================================

c = new_canvas(64, 64, background=None, name="explosion_frames")

# ---- palette ----
WHITE = c.color("#FFFFFF", name="hot_white")
PALE  = c.color("#FFF3A6", name="pale_yellow")
YEL   = c.color("#FFD21F", name="bright_yellow")
ORG   = c.color("#FF8A1E", name="orange")
RED   = c.color("#E8420A", name="red_orange")
DRED  = c.color("#9E1B04", name="deep_red")

# ================= FRAME 1 : bright yellow fireball =================
c.circle(16, 16, 6, ORG)      # outer rim of the fireball
c.circle(16, 16, 5, YEL)      # bright yellow body
c.circle(16, 16, 3, PALE)     # hotter interior
c.rect(15, 15, 2, 2, WHITE)   # white-hot core

# flame licks (cardinal + diagonal tips)
for x, y in [(16, 9), (16, 23), (9, 16), (23, 16),
             (11, 11), (21, 11), (11, 21), (21, 21)]:
    c.set(x, y, ORG)

# stray embers
for x, y, col in [(7, 9, YEL), (25, 11, ORG), (24, 24, YEL), (9, 22, ORG)]:
    c.set(x, y, col)

# ================= FRAME 2 : expanding orange-red blast =================
cx, cy = 48, 16

# radial spikes first - the blast disc will cover their bases
for dx, dy in [(0, -14), (0, 14), (-14, 0), (14, 0),
               (10, -10), (-10, -10), (10, 10), (-10, 10)]:
    c.line(cx, cy, cx + dx, cy + dy, RED)

# blast body (hot core out to cool rim)
c.circle(cx, cy, 10, RED)
c.circle(cx, cy, 8, ORG)
c.circle(cx, cy, 5, YEL)
c.circle(cx, cy, 2, PALE)
c.set(cx, cy, WHITE)

# broken shock-wave ring just outside the blast
for d in ["M 60 20 A 13 13 0 0 1 52 28",
          "M 44 28 A 13 13 0 0 1 36 20",
          "M 36 12 A 13 13 0 0 1 44 4",
          "M 52 4 A 13 13 0 0 1 60 12"]:
    c.path(d, DRED, fill=False)

# sparks flying off
for x, y, col in [(35, 5, YEL), (40, 2, ORG), (46, 1, YEL), (52, 1, ORG),
                  (58, 3, YEL), (62, 7, ORG), (62, 13, RED), (61, 22, YEL),
                  (57, 29, ORG), (50, 30, YEL), (43, 30, RED), (36, 27, ORG),
                  (33, 21, YEL), (33, 12, RED), (37, 7, DRED),
                  (60, 14, YEL), (61, 14, ORG), (35, 18, ORG), (35, 19, YEL),
                  (42, 25, DRED), (43, 26, ORG)]:
    c.set(x, y, col)

# ---- report ----
print(c.stats_text())
print("---- frame 1 ----")
print(c.matrix_text(region=(0, 0, 31, 31)))
print("---- frame 2 ----")
print(c.matrix_text(region=(32, 0, 63, 31)))

save("explosion_effect", c)
finish(c)
