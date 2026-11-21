from pixelbench_api import *

c = new_canvas(48, 48, name="magic-staff")

WOOD   = c.color("#8a5a2b", "wood")
WOOD_D = c.color("#5c3a17", "wood_dark")
WOOD_L = c.color("#b07c45", "wood_light")
GEM    = c.color("#a855f7", "gem")
GEM_L  = c.color("#d8b4fe", "gem_light")
GEM_D  = c.color("#6b21a8", "gem_dark")
GLOW   = c.color("#c084fc", "glow")
PART   = c.color("#9333ea", "particle")
PART_L = c.color("#e9d5ff", "particle_light")
GOLD   = c.color("#c9a227", "gold")

# --- shaft: diagonal from bottom-left to top-right ---
# main shaft line from (16,44) to (30,12)
for i in range(33):
    t = i / 32
    x = 16 + round(t * 14)
    y = 44 - round(t * 32)
    c.set(x, y, WOOD)
    c.set(x + 1, y, WOOD_D)
    c.set(x, y + 1, WOOD_D) if i % 3 else c.set(x, y + 1, WOOD)
    if i % 5 == 0:
        c.set(x + 1, y - 1, WOOD_L)

# --- curved head: hook curling at top ---
# from top of shaft (30,12) curl up and left, spiral end
c.line(30, 12, 31, 9, WOOD)
c.line(31, 9, 32, 7, WOOD)
c.line(32, 7, 33, 6, WOOD)
# curl left and down (hook)
c.line(33, 6, 35, 6, WOOD)
c.line(35, 6, 37, 7, WOOD)
c.line(37, 7, 38, 9, WOOD)
c.line(38, 9, 38, 11, WOOD)
c.line(38, 11, 37, 13, WOOD)
c.line(37, 13, 36, 14, WOOD)
c.set(35, 14, WOOD_D)
# top edge highlight of the curl
c.set(31, 8, WOOD_L); c.set(32, 6, WOOD_L); c.set(34, 5, WOOD_L); c.set(36, 6, WOOD_L)
c.set(37, 8, WOOD_L)

# second small prong (claw) from the shaft top going up-left
c.line(30, 12, 28, 9, WOOD_D)
c.line(28, 9, 26, 8, WOOD_D)
c.set(25, 8, WOOD)

# --- gem held between the prongs ---
c.circle(30, 6, 3, GEM)
c.circle(30, 6, 2, GEM)  # solid
c.set(29, 5, GEM_L)
c.set(30, 5, GEM_L)
c.set(31, 5, GEM_L)
c.set(29, 4, GEM_L)
c.set(31, 7, GEM_D)
c.set(30, 8, GEM_D)
c.set(28, 6, GEM_D)
c.set(32, 6, GEM_D)

# glow ring around gem
for (x, y) in [(26,6),(27,3),(30,2),(33,3),(34,6),(33,9),(30,10),(27,9)]:
    c.set(x, y, GLOW)

# --- gold band on the shaft ---
c.set(19, 40, GOLD); c.set(20, 40, GOLD)
c.set(20, 39, GOLD); c.set(21, 39, GOLD)

# --- purple particles floating around the head ---
parts = [
    (24, 3, PART_L), (36, 2, PART), (40, 5, PART_L), (41, 12, PART),
    (25, 13, PART), (22, 8, PART_L), (35, 17, PART_L), (42, 9, PART),
    (27, 1, PART), (39, 15, PART_L), (23, 16, PART), (43, 3, PART),
    (20, 5, PART), (26, 18, PART_L), (37, 20, PART),
]
for x, y, col in parts:
    c.set(x, y, col)
    if col is PART_L:
        c.set(x, y - 1, PART)

print(c.stats_text())
save("magic-staff", c)
finish(c)
