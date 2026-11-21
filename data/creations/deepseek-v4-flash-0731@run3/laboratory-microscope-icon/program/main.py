from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32)

OUT     = c.color("#14171c")
METAL_D = c.color("#38424e")
METAL   = c.color("#5e6c7d")
METAL_L = c.color("#9aabb8")
STAGE   = c.color("#263039")
STAGE_L = c.color("#4c5a67")
GLASS   = c.color("#6fcfe3")
GLASS_L = c.color("#b9eef5")
KNOB    = c.color("#e59a2f")
KNOB_L  = c.color("#f7c067")

# --- base ---
c.rect(4, 27, 24, 4, METAL_D)      # x=4..27, y=27..30
c.rect(4, 26, 24, 1, METAL)        # top surface
c.rect(5, 26, 9, 1, METAL_L)       # top highlight

# --- arm pillar ---
c.rect(23, 13, 4, 15, METAL)       # x=23..26, y=13..27
c.rect(23, 14, 1, 13, METAL_L)     # left edge highlight
c.rect(25, 24, 2, 3, METAL_D)      # lower shading

# --- connector ---
c.rect(14, 9, 13, 4, METAL)        # x=14..26, y=9..12
c.rect(14, 9, 13, 1, METAL_L)

# --- body tube (slanted, three-quarter) ---
c.poly([(9, 3), (13, 3), (16, 15), (12, 15)], METAL)
c.rect(10, 4, 1, 7, METAL_L)       # tube highlight
c.rect(12, 4, 1, 8, METAL_D)       # tube shading

# --- eyepiece ---
c.rect(8, 0, 7, 2, METAL_D)        # flare x=8..14, rows 0..1
c.rect(8, 0, 7, 1, METAL)          # flare top rim
c.rect(9, 1, 5, 3, METAL)          # eyepiece cylinder rows 1..3
c.rect(10, 1, 3, 1, METAL_L)
c.rect(8, 3, 7, 1, METAL_D)         # flare lip under rim

# --- objective ---
c.rect(13, 15, 5, 5, METAL_D)      # x=13..17, rows 15..19
c.rect(13, 15, 5, 1, METAL)        # knurled ring
c.rect(14, 19, 3, 2, METAL)        # tip, rows 19..20
c.rect(14, 15, 1, 4, METAL_L)      # objective highlight

# --- stage bracket ---
c.rect(19, 23, 7, 3, METAL)        # x=19..25, rows 23..25

# --- stage ---
c.rect(6, 20, 16, 4, STAGE)        # platform x=6..21, rows 20..23
c.rect(6, 20, 16, 1, STAGE_L)      # stage top face
c.rect(6, 20, 3, 1, METAL_D)       # front overhang lip

# --- slide on stage ---
c.rect(9, 20, 6, 1, GLASS)
c.rect(10, 20, 3, 1, GLASS_L)

# --- knobs ---
c.circle(10, 28, 1, KNOB)
c.set(10, 28, KNOB_L)
c.circle(20, 28, 1, KNOB)
c.set(20, 28, KNOB_L)

# --- unified dark outline ---
c.outline(OUT)

# keep the slide glass readable on top after outlining
c.rect(9, 20, 6, 1, GLASS)
c.rect(10, 20, 2, 1, GLASS_L)

print(c.stats_text())
print(c.matrix_text())
finish(c)
