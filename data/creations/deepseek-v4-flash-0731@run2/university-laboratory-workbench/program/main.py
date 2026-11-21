from pixelbench_api import *

c = new_canvas(64, 64, name="lab_bench")

# ---------------------------------------------------------------- palette
wall = c.color("#e6eaf0", "wall")
wall_shadow = c.color("#d3dae5", "wall_shadow")
shelf = c.color("#7a4d26", "shelf")
bench_top = c.color("#c08a52", "bench_top")
bench_top_hl = c.color("#d29a63", "bench_top_hl")
bench_front = c.color("#8f5d2a", "bench_front")
bench_dark = c.color("#764a1f", "bench_dark")
bench_handle = c.color("#b07c46", "bench_handle")
shadow = c.color("#96642f", "shadow")
scope_dark = c.color("#30364a", "scope_dark")
scope_mid = c.color("#49526b", "scope_mid")
scope_black = c.color("#1c2130", "scope_black")
scope_light = c.color("#8e99b3", "scope_light")
scope_hl = c.color("#c6cfe4", "scope_hl")
glass = c.color("#a9c6de", "glass")
glass_hl = c.color("#e0eef8", "glass_hl")
liquid_blue = c.color("#4480b2", "liquid_blue")
liquid_green = c.color("#4d9e52", "liquid_green")
amber = c.color("#d29a3a", "amber")
amber_hl = c.color("#e6b65f", "amber_hl")
cap_red = c.color("#c23b4a", "cap_red")
cap_green = c.color("#3a7d44", "cap_green")
bulb_hl = c.color("#d95b5f", "bulb_hl")
label = c.color("#f4ecd8", "label")
label_line = c.color("#c9bfa8", "label_line")
page = c.color("#f7f4ea", "page")
page_shade = c.color("#e4dfd0", "page_shade")
spine = c.color("#cdc8ba", "spine")
ring = c.color("#9aa3b5", "ring")
ink = c.color("#5d6273", "ink")
red_ink = c.color("#c2554a", "red_ink")
tube_red = c.color("#d95b50", "tube_red")
tube_yellow = c.color("#e0b63e", "tube_yellow")

# ---------------------------------------------------------------- wall + shelf
c.rect(0, 0, 64, 49, wall)
c.rect(4, 10, 56, 2, shelf)
c.rect(4, 12, 56, 1, wall_shadow)

# flask on the shelf
c.rect(13, 4, 5, 1, glass)          # rim
c.rect(14, 5, 3, 3, glass)          # neck
c.rect(14, 5, 1, 3, glass_hl)
c.circle(16, 7, 3, glass)            # bulb
c.rect(14, 8, 5, 3, liquid_green)   # liquid
# beaker on the shelf
c.rect(25, 4, 8, 6, glass)
c.rect(25, 4, 1, 6, glass_hl)
c.rect(26, 6, 6, 4, liquid_blue)

# ---------------------------------------------------------------- bench
c.rect(0, 49, 64, 3, bench_top)
c.rect(0, 49, 64, 1, bench_top_hl)
c.rect(0, 52, 64, 12, bench_front)
c.rect(0, 58, 64, 6, bench_dark)
c.rect(8, 59, 20, 2, bench_handle)
c.rect(36, 59, 20, 2, bench_handle)

# shadows on the bench
c.ellipse(11, 50, 8, 1, shadow)      # microscope
c.ellipse(23, 50, 4, 1, shadow)      # amber bottle
c.ellipse(31, 50, 4, 1, shadow)      # clear bottle
c.rect(39, 50, 13, 1, shadow)        # notebook
c.ellipse(58, 50, 5, 1, shadow)      # rack

# ---------------------------------------------------------------- microscope
c.rect(4, 47, 14, 3, scope_dark)     # base
c.rect(4, 47, 14, 1, scope_mid)
c.rect(8, 14, 5, 1, scope_black)     # eyepiece lens
c.rect(8, 15, 5, 4, scope_dark)      # eyepiece
c.rect(9, 19, 9, 10, scope_dark)     # head
c.rect(12, 22, 4, 10, scope_dark)    # tube
c.rect(12, 23, 1, 8, scope_mid)      # tube shading
c.rect(13, 31, 3, 3, scope_mid)      # objective
c.rect(13, 34, 3, 1, scope_black)
c.rect(13, 28, 4, 21, scope_dark)    # arm (continues down to the base)
c.circle(10, 30, 2, scope_black)      # focus knobs
c.circle(18, 30, 2, scope_black)
c.rect(10, 35, 10, 2, scope_light)   # stage
c.rect(10, 35, 10, 1, scope_hl)

# ---------------------------------------------------------------- amber bottle
c.rect(20, 32, 7, 3, cap_red)
c.rect(20, 32, 2, 1, bulb_hl)
c.rect(22, 35, 3, 3, amber)          # neck
c.rect(20, 38, 7, 12, amber)         # body
c.rect(20, 38, 1, 12, amber_hl)
c.rect(21, 40, 5, 6, label)           # label
c.rect(24, 40, 1, 6, label_line)
c.set(22, 42, cap_red)

# ---------------------------------------------------------------- clear bottle
c.rect(28, 34, 7, 3, cap_green)
c.rect(28, 34, 2, 1, glass_hl)
c.rect(29, 37, 3, 3, glass)          # neck
c.rect(28, 40, 7, 10, glass)         # body
c.rect(28, 40, 1, 10, glass_hl)
c.rect(29, 45, 5, 4, liquid_blue)    # liquid
c.rect(29, 41, 5, 3, label)
c.rect(31, 41, 1, 3, label_line)
c.set(32, 42, cap_green)

# ---------------------------------------------------------------- open notebook
c.rect(38, 41, 15, 9, page)
c.rect(38, 41, 1, 9, page_shade)
c.rect(45, 41, 1, 9, page_shade)
c.rect(45, 41, 1, 9, spine)
for yy in (42, 44, 46):
    c.set(38, yy, ring)
c.rect(39, 43, 5, 1, page_shade)
c.rect(39, 45, 5, 1, page_shade)
c.rect(46, 43, 5, 1, page_shade)
c.rect(46, 45, 5, 1, page_shade)
c.set(40, 43, ink)
c.set(41, 45, ink)
c.set(47, 43, ink)
c.set(48, 45, red_ink)

# ---------------------------------------------------------------- test-tube rack
for x, col in ((55, tube_red), (57, liquid_blue), (59, liquid_green), (61, tube_yellow)):
    c.rect(x, 35, 2, 8, glass)
    c.rect(x + 1, 38, 1, 3, col)
    c.rect(x, 35, 1, 8, glass_hl)
c.rect(54, 41, 10, 1, shelf)          # top plate
c.rect(54, 43, 10, 1, shelf)          # bottom plate
c.rect(54, 41, 1, 9, shelf)           # posts
c.rect(63, 41, 1, 9, shelf)

# ---------------------------------------------------------------- dropper lying in front
c.circle(23, 49, 1, cap_red)          # rubber bulb
c.set(22, 49, bulb_hl)
c.rect(25, 48, 10, 2, glass)         # glass tube
c.rect(35, 48, 3, 1, glass)          # fine tip
c.rect(25, 48, 1, 2, glass_hl)
c.rect(38, 48, 1, 1, glass)          # tip end
c.set(38, 48, glass_hl)

print(c.stats_text())
finish(c)
