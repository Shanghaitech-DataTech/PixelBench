from pixelbench_api import *

W, H = 32, 32
c = new_canvas(W, H, background=None, name="microscope")

# Palette
INK    = c.color((38, 44, 60))     # dark outline / shadow
BODY   = c.color((96, 105, 124))   # main body mid grey
BODY_D = c.color((70, 78, 94))     # darker body (shadow side)
BODY_L = c.color((142, 152, 172))  # lit body
LENS   = c.color((80, 195, 232))   # glass lens
LENS_D = c.color((26, 118, 158))   # dark glass
STAGE  = c.color((86, 96, 116))    # stage
STAGE_L= c.color((155, 165, 188))  # stage lit edge
BASE   = c.color((64, 71, 88))     # base
BASE_L = c.color((130, 140, 162))  # base lit
ACCENT = c.color((205, 135, 62))   # brass knobs
SLIDE  = c.color((205, 214, 232))  # glass slide

# ---- Eyepiece (top, center) ----
c.rect(10, 0, 5, 2, INK)
c.rect(11, 0, 3, 1, (160, 225, 250))
c.rect(11, 1, 3, 1, LENS)
c.rect(10, 2, 5, 5, INK)
c.rect(11, 2, 3, 5, BODY_D)
c.rect(11, 2, 1, 5, BODY_L)
c.rect(9, 7, 7, 1, INK)
c.rect(10, 7, 5, 1, BODY)

# ---- Head ----
c.rect(8, 8, 8, 2, INK)
c.rect(9, 8, 6, 2, BODY)
c.rect(9, 8, 2, 1, BODY_L)

# ---- Arm ----
c.rect(4, 9, 4, 16, INK)
c.rect(5, 9, 2, 16, BODY_D)
c.rect(5, 9, 1, 16, BODY_L)
c.rect(4, 9, 5, 1, INK)

# ---- Body tube (diagonal down-right) ----
c.poly([(11, 10), (15, 10), (23, 18), (23, 20), (16, 20), (11, 12)], INK, fill=True)
c.poly([(12, 11), (14, 11), (21, 18), (21, 19), (15, 19), (12, 12)], BODY, fill=True)
for dx, dy in [(12,11),(12,12),(13,13),(14,14),(15,15),(17,16)]:
    c.set(dx, dy, BODY_L)

# ---- Coarse focus knob ----
c.rect(7, 15, 4, 5, INK)
c.rect(8, 15, 2, 5, ACCENT)
c.rect(8, 15, 1, 5, (240, 165, 80))
# Fine focus knob
c.rect(7, 21, 3, 3, INK)
c.rect(8, 21, 2, 3, ACCENT)

# ---- Objective ----
c.rect(15, 19, 9, 2, INK)
c.rect(16, 19, 7, 2, BODY)
c.rect(16, 19, 2, 2, BODY_L)
c.rect(16, 21, 7, 1, INK)
c.rect(17, 21, 5, 1, BODY)
c.poly([(17, 22), (21, 22), (20, 25), (18, 25)], INK, fill=True)
c.poly([(18, 23), (20, 23), (19.5, 24), (18, 24)], LENS, fill=True)
c.rect(19, 24, 1, 1, LENS_D)

# ---- Stage ----
c.rect(7, 25, 18, 3, INK)
c.rect(8, 25, 16, 1, STAGE_L)
c.rect(8, 26, 16, 1, STAGE)
c.rect(8, 27, 16, 1, BODY_D)
c.rect(16, 26, 7, 2, SLIDE)
c.rect(16, 26, 7, 1, (225, 232, 246))

# ---- Base ----
c.rect(6, 28, 22, 4, INK)
c.rect(7, 28, 21, 3, BASE)
c.rect(7, 28, 21, 1, BASE_L)
c.rect(8, 31, 18, 1, INK)

print(c.stats_text())
finish(c)
