from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32, background=None)

def C(hexs):  # convenience register + return index (not needed, just for reference)
    return c.color(hexs)

# palette
ROOF       = "#2a2a33"
ROOF_EDGE  = "#3d3d49"
ROOF_HI    = "#565662"
BRICK      = "#a34b2e"
BRICK_DARK = "#8c3b21"
BRICK_LIT  = "#b95d3b"
MORTAR     = "#d6c5aa"
DOOR       = "#191b21"
DOOR_IN    = "#2e323c"
WINDOW     = "#23262e"
WINDOW_FR  = "#5a6070"
WINDOW_GL  = "#6f8fc4"
VENT       = "#8e93a0"
VENT_DARK  = "#6b6f7a"
CHIM       = "#c2c6d0"
CHIM_DARK  = "#9a9ea9"
CHIM_CAP   = "#767a85"
FOUND      = "#3b3b45"
SMOKE      = (255, 255, 255, 170)
SMOKE_DARK = (255, 255, 255, 120)
GROUND     = (0, 0, 0, 70)

# --- ground shadow ---
c.ellipse(16, 29, 15, 2, GROUND, fill=True)

# --- main building body (brick walls) ---
c.rect(4, 12, 24, 16, BRICK)          # x=4..27, y=12..27

# foundation
c.rect(3, 28, 26, 2, FOUND)          # x=3..28, y=28..29

# brick texture: mortar courses
for yy in (15, 18, 21, 24):
    c.line(4, yy, 27, yy, MORTAR)
# vertical mortar joints (staggered)
c.line(10, 12, 10, 14, MORTAR)
c.line(17, 12, 17, 14, MORTAR)
c.line(24, 12, 24, 14, MORTAR)
c.line(7, 15, 7, 17, MORTAR)
c.line(13, 15, 13, 17, MORTAR)
c.line(20, 15, 20, 17, MORTAR)
c.line(10, 18, 10, 20, MORTAR)
c.line(17, 18, 17, 20, MORTAR)
c.line(24, 18, 24, 20, MORTAR)
# scattered darker bricks
c.rect(5, 16, 2, 1, BRICK_DARK)
c.rect(14, 16, 2, 1, BRICK_DARK)
c.rect(22, 16, 2, 1, BRICK_DARK)
c.rect(8, 19, 2, 1, BRICK_DARK)
c.rect(19, 19, 2, 1, BRICK_DARK)
c.rect(5, 22, 2, 1, BRICK_DARK)
c.rect(14, 22, 2, 1, BRICK_DARK)
c.rect(23, 22, 2, 1, BRICK_DARK)
c.rect(8, 25, 2, 1, BRICK_DARK)
c.rect(19, 25, 2, 1, BRICK_DARK)

# --- flat roof ---
c.rect(2, 10, 28, 2, ROOF)            # x=2..29, y=10..11
c.line(2, 10, 29, 10, ROOF_EDGE)      # top edge
c.line(2, 10, 29, 10, ROOF_EDGE)
# roof overhang shadow below
c.line(3, 10, 28, 10, ROOF_HI)

# --- roof vents ---
c.rect(6, 8, 4, 2, VENT)
c.line(6, 8, 9, 8, VENT_DARK)
c.rect(24, 8, 4, 2, VENT)
c.line(24, 8, 27, 8, VENT_DARK)

# --- chimney ---
c.rect(20, 4, 4, 7, CHIM)             # x=20..23, y=4..10
c.line(20, 4, 20, 10, CHIM_DARK)      # left shade
# chimney cap
c.rect(19, 3, 6, 1, CHIM_CAP)         # x=19..24, y=3

# --- door (factory gate) ---
c.rect(12, 20, 8, 8, DOOR)            # x=12..19, y=20..27
c.line(12, 23, 19, 23, DOOR_IN)
c.line(15, 20, 15, 27, DOOR_IN)

# --- windows ---
for wx in (5, 23):
    c.rect(wx, 15, 4, 4, WINDOW_FR)
    c.rect(wx + 1, 16, 2, 2, WINDOW_GL)

# --- smoke rising from chimney ---
c.circle(0, 1, 2, SMOKE_DARK, fill=True)   # placeholder, reposition below
c.clear(0, 0, 3, 4)                       # clear that spot
c.circle(22, 1, 2, SMOKE, fill=True)
c.circle(25, 0, 1, SMOKE, fill=True)
c.circle(26, 2, 2, SMOKE_DARK, fill=True)

print(c.stats_text())
finish(c)
