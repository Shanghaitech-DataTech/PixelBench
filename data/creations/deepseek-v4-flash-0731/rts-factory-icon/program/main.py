from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32)

# ---- palette ----
OUTLINE = "#261611"
BRICK   = "#b04a30"
BRICK_D = "#8a3320"
BRICK_L = "#c65c3e"
FRAME   = "#38281e"
WINDOW  = "#ffd773"
WIN_DK  = "#d8a64a"
DOOR    = "#37404f"
DOOR_S  = "#556176"
ROLLER  = "#21242c"
SLAB    = "#3c414d"
SLAB_L  = "#4d5360"
SLAB_D  = "#272b34"
ROOF    = "#3f4450"
ROOF_L  = "#565c6b"
ROOF_D  = "#2b2e38"
CHIM    = "#4a4f5c"
CAP     = "#22252d"
CAP_D   = "#15171c"
VENT    = "#2c3039"
VENT_D  = "#171a20"

# ---- roof slab ----
c.rect(5, 8, 22, 3, ROOF)
c.rect(5, 8, 22, 1, ROOF_L)
c.rect(5, 10, 22, 1, ROOF_D)

# ---- brick wall ----
c.rect(6, 10, 20, 13, BRICK)
c.rect(6, 10, 20, 3, BRICK_L)

# brick seams (before windows/door so they get covered)
for x in (10, 14, 18, 22):
    c.line(x, 10, x, 12, BRICK_D)
for x in (8, 12, 16, 20, 24):
    c.line(x, 13, x, 14, BRICK_D)
for x in (10, 14, 18, 22):
    c.line(x, 16, x, 17, BRICK_D)
for x in (8, 12, 16, 20, 24):
    c.line(x, 19, x, 21, BRICK_D)
for y in (15, 18):
    c.line(6, y, 25, y, BRICK_D)

# ---- windows (two lit factory windows) ----
for fx in (9, 19):
    c.rect(fx, 13, 5, 5, FRAME)
    c.rect(fx + 1, 14, 3, 3, WINDOW)
    c.rect(fx + 1, 16, 3, 1, WIN_DK)
    c.line(fx + 2, 14, fx + 2, 16, WIN_DK)  # mullion

# ---- roll-up door ----
c.rect(12, 17, 8, 2, ROLLER)
c.rect(13, 18, 6, 5, DOOR)
c.rect(13, 20, 6, 1, DOOR_S)
c.rect(13, 22, 6, 1, DOOR_S)

# ---- base slab ----
c.rect(4, 23, 24, 2, SLAB)
c.rect(4, 23, 24, 1, SLAB_L)
c.rect(4, 24, 24, 1, SLAB_D)

# ---- chimney ----
c.rect(9, 1, 6, 2, CAP)      # cap
c.rect(9, 2, 6, 1, CAP_D)    # cap rim shadow
c.rect(10, 3, 4, 5, CHIM)    # stack
c.rect(10, 3, 1, 5, ROOF_L)  # highlight

# ---- roof vents ----
c.rect(18, 6, 4, 2, VENT)
c.rect(18, 7, 4, 1, VENT_D)
c.rect(23, 5, 4, 3, VENT)
c.rect(23, 6, 4, 1, VENT_D)

# ---- clean dark silhouette rim ----
c.outline(OUTLINE)

print(c.matrix_text(region=(0, 0, 31, 31)))
print(c.stats_text())
finish(c)
