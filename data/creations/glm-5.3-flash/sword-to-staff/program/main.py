BG = '#ffffffff'

out = input_canvas.copy(name='output')

# ---------------- palette ----------------
WOOD_L = out.color('#c09257', 'staff_wood_light')
WOOD_M = out.color('#96613a', 'staff_wood_mid')     # reuses existing c2
WOOD_D = out.color('#5f4025', 'staff_wood_dark')
WOOD_G = out.color('#6b4423', 'staff_wood_grain')   # reuses existing c15
GOLD   = out.color('#c9a227', 'gold')               # reuses existing c17
GEM_R  = out.color('#17707f', 'gem_rim')
GEM_B  = out.color('#4ec3dc', 'gem_body')
GEM_D  = out.color('#2b9cb5', 'gem_deep')
GEM_H  = out.color('#d8f7fd', 'gem_highlight')
SPARK  = out.color('#6fd0e6', 'gem_spark')
INK    = '#2e1f12'                                  # the drawing's outline colour

# ---------------- 1. remove the sword ----------------
for y in (39, 40):                      # gold crossguard + its edge pixels
    for x in range(40, 47):
        out.set(x, y, BG)
for y in range(41, 56):                 # silver blade
    for x in range(42, 45):
        out.set(x, y, BG)

# ---------------- 2. wooden shaft (x = 43 light | 44 mid | 45 dark) ----
keep_light = {34, 35, 36, 37}           # sleeve corner + fist stay in front
for y in range(12, 55):
    if y not in keep_light:
        out.set(43, y, WOOD_L)
    out.set(44, y, WOOD_M)
    out.set(45, y, WOOD_D)
out.set(44, 55, WOOD_M)                 # tip planted on the ground line
for y in (16, 23, 30, 44, 51):          # grain ticks
    out.set(44, y, WOOD_G)

# ---------------- 3. gold collar / socket ----------------
for x in range(42, 47):
    out.set(x, 10, GOLD)
for x in range(43, 46):
    out.set(x, 11, GOLD)

# ---------------- 4. the orb (7x7, centred on 44,6) ----------------
orb = [
    (3,  [(43, GEM_R), (44, GEM_R), (45, GEM_R)]),
    (4,  [(42, GEM_R), (43, GEM_H), (44, GEM_B), (45, GEM_B), (46, GEM_R)]),
    (5,  [(41, GEM_R), (42, GEM_H), (43, GEM_H), (44, GEM_B), (45, GEM_B), (46, GEM_B), (47, GEM_R)]),
    (6,  [(41, GEM_R), (42, GEM_B), (43, GEM_B), (44, GEM_B), (45, GEM_B), (46, GEM_D), (47, GEM_R)]),
    (7,  [(41, GEM_R), (42, GEM_B), (43, GEM_B), (44, GEM_B), (45, GEM_D), (46, GEM_D), (47, GEM_R)]),
    (8,  [(42, GEM_R), (43, GEM_B), (44, GEM_D), (45, GEM_D), (46, GEM_R)]),
    (9,  [(43, GEM_R), (44, GEM_R), (45, GEM_R)]),
]
for y, px in orb:
    for x, col in px:
        out.set(x, y, col)

# ---------------- 5. two small sparkles ----------------
for x, y in [(51, 4), (50, 4), (52, 4), (51, 3), (51, 5),
             (39, 2), (38, 2), (40, 2), (39, 1), (39, 3)]:
    out.set(x, y, SPARK)

# ---------------- 6. keep the fist's right edge ----------------
for y in (35, 36, 37):
    out.set(44, y, INK)

# ---------------- verify ----------------
print(out.stats_text())
print(out.matrix_text(region=(36, 0, 54, 20)))
print(out.matrix_text(region=(36, 30, 52, 58)))

finish(out)
