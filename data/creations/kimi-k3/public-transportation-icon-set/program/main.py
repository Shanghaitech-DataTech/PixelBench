from pixelbench_api import *

# ---------------------------------------------------------------- palette ---
BG    = '#DCE5EB'   # page background
TILE  = '#F7FAFC'   # tile face
TBORD = '#B9C7D2'   # tile border
INK   = '#22384A'   # dark navy linework
BLUE  = '#2E86DE'   # transit blue accent
WHITE = '#FFFFFF'   # glass / highlights

c = new_canvas(64, 64, background=BG, name='transit_icons')

# ---------------------------------------------------------------- helpers ---
def rrect(cv, x, y, w, h, r, color):
    """Filled rounded rect covering pixels x..x+w-1, y..y+h-1.
    (path fill excludes the bottom edge row, so the bottom edge is at y+h)."""
    d = (f"M {x+r} {y} H {x+w-1-r} Q {x+w-1} {y} {x+w-1} {y+r} "
         f"V {y+h-r} Q {x+w-1} {y+h} {x+w-1-r} {y+h} "
         f"H {x+r} Q {x} {y+h} {x} {y+h-r} V {y+r} Q {x} {y} {x+r} {y} Z")
    cv.path(d, color)

def tile(cv, ox, oy):
    rrect(cv, ox+2, oy+2, 28, 28, 4, TBORD)
    rrect(cv, ox+3, oy+3, 26, 26, 3, TILE)

for ox, oy in [(0, 0), (32, 0), (0, 32), (32, 32)]:
    tile(c, ox, oy)

# ------------------------------------------------------------------- bus ---
def bus(cv, cx, cy):
    rrect(cv, cx-8, cy-10, 17, 20, 3, INK)      # body outline
    rrect(cv, cx-7, cy-9, 15, 18, 2, BLUE)      # body
    cv.rect(cx-3, cy-6, 6, 2, WHITE)            # destination sign
    cv.rect(cx-5, cy-4, 11, 5, WHITE)           # windshield
    cv.line(cx, cy-4, cx, cy, BLUE)             # windshield split
    cv.rect(cx-6, cy+3, 2, 2, WHITE)            # headlight L
    cv.rect(cx+5, cy+3, 2, 2, WHITE)            # headlight R
    cv.line(cx-4, cy+6, cx+4, cy+6, INK)        # grille
    cv.rect(cx-7, cy+10, 4, 2, INK)             # wheel L
    cv.rect(cx+3, cy+10, 4, 2, INK)             # wheel R
    cv.rect(cx-10, cy-3, 2, 1, INK)             # mirror stubs
    cv.rect(cx+9, cy-3, 2, 1, INK)

# ---------------------------------------------------------------- subway ---
def subway(cv, cx, cy):
    ink_d = (f"M {cx-8} {cy+10} V {cy-4} Q {cx-8} {cy-10} {cx} {cy-10} "
             f"Q {cx+8} {cy-10} {cx+8} {cy-4} V {cy+10} Z")
    cv.path(ink_d, INK)
    blue_d = (f"M {cx-7} {cy+9} V {cy-4} Q {cx-7} {cy-9} {cx} {cy-9} "
              f"Q {cx+7} {cy-9} {cx+7} {cy-4} V {cy+9} Z")
    cv.path(blue_d, BLUE)
    rrect(cv, cx-5, cy-6, 11, 5, 1, WHITE)      # windshield
    cv.rect(cx-6, cy+2, 2, 2, WHITE)            # headlight L
    cv.rect(cx+4, cy+2, 2, 2, WHITE)            # headlight R
    cv.line(cx-3, cy+5, cx+3, cy+5, INK)        # lower stripe

# --------------------------------------------------------------- bicycle ---
def bicycle(cv, cx, cy):
    A  = (cx-6, cy+7)   # rear hub
    B  = (cx+6, cy+7)   # front hub
    S  = (cx-3, cy-1)   # seat cluster
    H  = (cx+4, cy)     # head tube
    P  = (cx-2, cy+7)   # bottom bracket
    # frame first, so the black wheel rings stay unbroken on top
    cv.line(*A, *S, BLUE)
    cv.line(*S, *H, BLUE)
    cv.line(*H, *B, BLUE)
    cv.line(*A, *P, BLUE)
    cv.line(*P, *S, BLUE)
    cv.line(*P, *H, BLUE)
    # seat and seatpost
    cv.line(S[0], S[1], cx-3, cy-2, BLUE)
    cv.line(cx-5, cy-3, cx-2, cy-3, INK)
    # handlebar and stem
    cv.line(H[0], H[1], cx+5, cy-4, BLUE)
    cv.line(cx+3, cy-4, cx+6, cy-4, INK)
    # wheels on top
    cv.circle(A[0], A[1], 4, INK, fill=False)
    cv.circle(B[0], B[1], 4, INK, fill=False)
    cv.set(*A, INK)
    cv.set(*B, INK)

# ------------------------------------------------------------ pedestrian ---
def pedestrian(cv, cx, cy):
    # solid 3x3 head
    cv.rect(cx, cy-8, 3, 3, INK)
    cv.line(cx+1, cy-5, cx, cy+2, BLUE)         # torso
    cv.line(cx+1, cy-3, cx-3, cy, BLUE)         # back arm
    cv.line(cx+1, cy-3, cx+4, cy-1, BLUE)       # front arm
    cv.line(cx, cy+2, cx+5, cy+7, BLUE)         # front leg
    cv.line(cx+5, cy+7, cx+7, cy+7, BLUE)       # front foot
    cv.line(cx, cy+2, cx-4, cy+7, BLUE)         # back leg
    cv.line(cx-4, cy+7, cx-6, cy+7, BLUE)       # back foot

bus(c, 16, 16)
subway(c, 48, 16)
bicycle(c, 16, 45)
pedestrian(c, 48, 48)

view(c)
finish(c)
