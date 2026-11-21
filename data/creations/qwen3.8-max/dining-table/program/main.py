from pixelbench_api import *

c = new_canvas(64, 64, name="dining_table")

# ---------------------------------------------------------------- palette
OUT    = "#231510"   # dark outline
WOOD_D = "#6b4322"
WOOD_M = "#96602e"
WOOD_L = "#b98340"
WOOD_H = "#d8a95f"
TOP_H  = "#dcae6d"
TOP_M  = "#c28d4f"
TOP_E  = "#8e5a2a"
CUSH_D = "#7e2a26"
CUSH_M = "#b34338"
CUSH_L = "#d76a55"
BOWL_D = "#2c5a72"
BOWL_M = "#46809f"
BOWL_L = "#79b2c9"
BOWL_R = "#e2ecef"
APPL_D = "#8d2317"
APPL_M = "#cf3f2c"
APPL_L = "#ef7a5c"
ORNG_D = "#b96a1c"
ORNG_M = "#e08f2e"
ORNG_L = "#f5b85c"
PEAR_D = "#7d8f26"
PEAR_M = "#b6c33f"
PEAR_L = "#dde27f"
LEAF   = "#4f8f36"
STEM   = "#4a3220"
SHAD1  = "#2a1a1240"
SHAD2  = "#2a1a128c"


def rows(cv, spec, color):
    for (y, x0, x1) in spec:
        cv.rect(x0, y, x1 - x0 + 1, 1, color)


# ---------------------------------------------------------------- 1. floor shadow
rows(c, [(52, 16, 47), (53, 10, 53), (54, 7, 56), (55, 5, 58),
         (56, 5, 58), (57, 7, 56), (58, 10, 53), (59, 16, 47)], SHAD1)
rows(c, [(54, 22, 41), (55, 19, 44), (56, 19, 44), (57, 22, 41),
         (58, 26, 37)], SHAD2)

# ---------------------------------------------------------------- 2. back chairs (far side)
def back_chair(x):
    y0 = 10
    c.rect(x, y0, 12, 19, OUT)                 # silhouette y10..28
    c.clear(x + 1, y0 + 1, 10, 17)             # open the frame y11..27
    c.rect(x + 1, y0 + 1, 2, 12, WOOD_M)       # left post
    c.rect(x + 1, y0 + 1, 1, 12, WOOD_L)
    c.rect(x + 9, y0 + 1, 2, 12, WOOD_M)       # right post
    c.rect(x + 10, y0 + 1, 1, 12, WOOD_D)
    for sy in (y0 + 1, y0 + 6, y0 + 10):       # rails / slats
        c.rect(x + 1, sy, 10, 2, WOOD_L)
        c.rect(x + 1, sy + 1, 10, 1, WOOD_M)
    c.rect(x + 1, y0 + 1, 10, 1, WOOD_H)       # top rail light
    c.rect(x + 1, y0 + 13, 10, 5, CUSH_M)      # seat-back cushion
    c.rect(x + 1, y0 + 13, 10, 1, CUSH_L)
    c.rect(x + 1, y0 + 16, 10, 2, CUSH_D)
    c.rect(x + 9, y0 + 14, 1, 2, CUSH_D)
    c.rect(x + 2, y0 + 14, 1, 2, CUSH_L)


back_chair(11)
back_chair(41)

# ---------------------------------------------------------------- 3. table
c.rect(12, 28, 40, 6, OUT)                     # top slab y28..33
c.rect(13, 29, 38, 1, TOP_H)
c.rect(13, 30, 38, 2, TOP_M)
c.rect(13, 32, 38, 1, TOP_E)
for gx in (16, 17, 24, 25, 26, 34, 41, 42, 47):
    c.set(gx, 31, TOP_E)
for gx in (20, 21, 30, 31, 38, 39, 45):
    c.set(gx, 30, TOP_E)

c.rect(17, 33, 30, 5, OUT)                     # apron
c.rect(18, 34, 28, 3, WOOD_M)
c.rect(18, 34, 28, 1, WOOD_L)
c.rect(18, 36, 28, 1, WOOD_D)
c.set(31, 35, WOOD_D); c.set(32, 35, WOOD_D)

for lx in (17, 42):                            # legs
    c.rect(lx, 33, 5, 24, OUT)
    c.rect(lx + 1, 34, 3, 22, WOOD_M)
    c.rect(lx + 1, 34, 1, 22, WOOD_L)
    c.rect(lx + 3, 34, 1, 22, WOOD_D)
    c.rect(lx + 1, 53, 3, 2, WOOD_D)

# ---------------------------------------------------------------- 4. fruit
c.ellipse(32, 11, 4, 5, OUT, fill=True)        # pear, back centre
c.ellipse(32, 11, 3, 4, PEAR_M, fill=True)
c.set(31, 8, PEAR_L); c.set(30, 9, PEAR_L); c.set(30, 10, PEAR_L)
c.set(34, 11, PEAR_D); c.set(33, 13, PEAR_D); c.set(34, 12, PEAR_D)
c.set(32, 5, STEM); c.set(32, 4, STEM)
c.set(33, 4, LEAF); c.set(34, 4, LEAF); c.set(34, 3, LEAF)

c.circle(35, 16, 4, OUT, fill=True)            # orange, right
c.circle(35, 16, 3, ORNG_M, fill=True)
c.set(33, 14, ORNG_L); c.set(34, 14, ORNG_L); c.set(33, 15, ORNG_L)
c.set(37, 18, ORNG_D); c.set(36, 18, ORNG_D); c.set(37, 17, ORNG_D)
c.set(35, 11, STEM)

c.circle(28, 16, 4, OUT, fill=True)            # apple, left front
c.circle(28, 16, 3, APPL_M, fill=True)
c.set(26, 14, APPL_L); c.set(27, 14, APPL_L); c.set(26, 15, APPL_L)
c.set(30, 18, APPL_D); c.set(29, 18, APPL_D); c.set(30, 17, APPL_D)
c.set(28, 11, STEM); c.set(28, 10, STEM)
c.set(27, 10, LEAF); c.set(26, 10, LEAF); c.set(26, 9, LEAF)

# ---------------------------------------------------------------- 5. bowl
rows(c, [(20, 24, 39),
         (21, 24, 24), (21, 39, 39),
         (22, 24, 24), (22, 39, 39),
         (23, 25, 25), (23, 38, 38),
         (24, 25, 25), (24, 38, 38),
         (25, 26, 26), (25, 37, 37),
         (26, 27, 27), (26, 36, 36),
         (27, 27, 27), (27, 36, 36),
         (28, 28, 28), (28, 35, 35),
         (29, 29, 29), (29, 34, 34),
         (30, 30, 33)], OUT)
rows(c, [(21, 25, 38)], BOWL_R)                # rim top
rows(c, [(22, 25, 38)], BOWL_L)                # rim under-lip
rows(c, [(23, 26, 37), (24, 26, 37), (25, 27, 36), (26, 28, 35),
         (27, 28, 35), (28, 29, 34), (29, 30, 33)], BOWL_M)
rows(c, [(25, 28, 35)], BOWL_L)                # glazed band
c.set(27, 23, BOWL_L); c.set(27, 24, BOWL_L); c.set(28, 26, BOWL_L)
c.set(28, 27, BOWL_L); c.set(29, 28, BOWL_L); c.set(30, 29, BOWL_L)
c.set(36, 23, BOWL_D); c.set(36, 24, BOWL_D); c.set(35, 26, BOWL_D)
c.set(35, 27, BOWL_D); c.set(34, 28, BOWL_D); c.set(33, 29, BOWL_D)

# ---------------------------------------------------------------- 5b. plates
for px in (18, 45):
    c.ellipse(px, 31, 4, 1, OUT, fill=True)
    c.rect(px - 3, 30, 7, 1, BOWL_R)
    c.rect(px - 4, 31, 9, 1, BOWL_R)
    c.rect(px - 3, 31, 7, 1, BOWL_L)
    c.rect(px - 2, 30, 5, 1, BOWL_R)
    c.rect(px - 3, 29, 7, 1, OUT)
    c.set(px - 4, 31, OUT); c.set(px + 4, 31, OUT)

# ---------------------------------------------------------------- 6. end chairs (near side)
t = new_canvas(20, 42, name="chair_tmp")
t.rect(2, 2, 5, 37, OUT)                       # back post + back leg
t.rect(3, 3, 3, 35, WOOD_M)
t.rect(3, 3, 1, 35, WOOD_L)
t.rect(5, 3, 1, 35, WOOD_D)
t.rect(3, 36, 3, 2, WOOD_D)
t.rect(1, 2, 8, 5, OUT)                        # top rail
t.rect(2, 3, 6, 3, WOOD_L)
t.rect(2, 3, 6, 1, WOOD_H)
t.rect(2, 5, 6, 1, WOOD_D)
t.rect(3, 17, 14, 5, OUT)                      # cushion
t.rect(4, 18, 12, 3, CUSH_M)
t.rect(4, 18, 12, 1, CUSH_L)
t.rect(4, 20, 12, 1, CUSH_D)
t.rect(15, 18, 1, 3, CUSH_D)
t.rect(2, 21, 16, 4, OUT)                      # seat
t.rect(3, 22, 14, 2, WOOD_M)
t.rect(3, 22, 14, 1, WOOD_H)
t.rect(3, 23, 14, 1, WOOD_D)
t.rect(14, 24, 4, 15, OUT)                     # front leg
t.rect(15, 25, 2, 13, WOOD_M)
t.rect(15, 25, 1, 13, WOOD_L)
t.rect(15, 36, 2, 2, WOOD_D)
t.rect(6, 31, 9, 3, OUT)                       # stretcher
t.rect(7, 32, 7, 1, WOOD_D)

c.blit(t, 0, 18)
t2 = t.copy(name="chair_tmp_r")
t2.mirror(axis="h")
c.blit(t2, 44, 18)

# ---------------------------------------------------------------- preview
print(c.stats_text())
print(view(c))
save("dining_table", c, indexed=True)
finish(c)
