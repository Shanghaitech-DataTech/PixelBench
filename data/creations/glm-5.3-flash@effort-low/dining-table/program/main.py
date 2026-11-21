from pixelbench_api import *

c = new_canvas(64, 64, background="#f4e7cf", name="dining_table")

OUT = "#3a2417"    # dark outline
WOOD = "#a9713f"
WOOD_L = "#c68f57"
WOOD_D = "#8a5a2e"
CUSH = "#b8523c"
CUSH_D = "#8f3c2c"
BOWL = "#e9e2d2"
BOWL_D = "#c9c0ac"
RED = "#d94f3d"
ORG = "#e8963c"
GRN = "#5f8f3e"
FLOOR = "#e6d3b0"

def rect(x, y, w, h, col):
    c.rect(x, y, w, h, col)

# --- wall details: window with warm light (right), framed picture (left) ---
c.rect(46, 3, 13, 11, "#9fc4d8")            # window glass
c.rect(46, 3, 13, 11, OUT, fill=False)
c.line(52, 3, 52, 13, OUT)                  # mullions
c.line(46, 8, 58, 8, OUT)
c.rect(45, 2, 15, 1, WOOD_D)                # sill
c.rect(45, 2, 15, 1, OUT, fill=False)
c.rect(5, 5, 9, 8, "#e8d9a8")               # picture
c.rect(5, 5, 9, 8, WOOD_D, fill=False)
c.rect(5, 5, 9, 8, OUT, fill=False)
c.circle(9, 9, 2, GRN)                      # little tree in picture
c.rect(8, 11, 2, 2, WOOD_D)
# string of warm lights across the wall
c.line(0, 4, 63, 4, "#d8c29a")
for lx, ly in [(20, 6), (26, 8), (32, 6), (38, 8)]:
    c.set(lx, ly, "#f2b53c")
    c.set(lx, ly + 1, ORG)

# --- floor hint ---
rect(0, 52, 64, 12, FLOOR)
for x in range(4, 64, 12):
    c.line(x, 52, x, 63, "#d8c29a")
c.line(0, 52, 63, 52, "#d8c29a")
# rug under table
c.ellipse(32, 50, 26, 7, "#c96a5a")
c.ellipse(32, 50, 21, 5, "#e0907e")

# --- back chairs (behind table), drawn first ---
def back_chair(cx):
    # backrest
    rect(cx, 14, 10, 3, WOOD)
    c.rect(cx, 14, 10, 3, OUT, fill=False)
    c.line(cx, 16, cx, 30, OUT)
    c.line(cx + 9, 16, cx + 9, 30, OUT)
    for y in range(18, 30, 4):
        c.line(cx + 1, y, cx + 8, y, WOOD_D)
    # posts continue down (hidden by table later)
    c.line(cx + 1, 16, cx + 1, 31, OUT)
    c.line(cx + 8, 16, cx + 8, 31, OUT)

back_chair(14)
back_chair(40)

# --- side chairs (left and right, facing table) ---
def side_chair(x0, flip):
    # backrest vertical post
    bx = x0 if not flip else x0 + 5
    c.rect(bx, 20, 3, 22, WOOD)
    c.rect(bx, 20, 3, 22, OUT, fill=False)
    # seat
    c.rect(x0, 40, 8, 5, WOOD)
    c.rect(x0, 40, 8, 5, OUT, fill=False)
    c.rect(x0 + 1, 41, 6, 3, CUSH)
    # front legs
    lx = x0 + 1 if not flip else x0 + 6
    c.rect(lx, 45, 2, 11, WOOD_D)
    c.rect(lx, 45, 2, 11, OUT, fill=False)

side_chair(1, False)     # left chair, back on left
side_chair(55, True)     # right chair, back on right

# --- table ---
# top surface
c.rect(9, 30, 46, 8, WOOD)
c.rect(9, 30, 46, 8, OUT, fill=False)
c.rect(10, 31, 44, 3, WOOD_L)          # highlight of tabletop
# apron
c.rect(11, 38, 42, 4, WOOD_D)
c.line(11, 38, 52, 38, OUT)
c.line(11, 41, 52, 41, OUT)
c.line(11, 38, 11, 41, OUT)
c.line(52, 38, 52, 41, OUT)
# legs
c.rect(12, 41, 4, 15, WOOD)
c.rect(12, 41, 4, 15, OUT, fill=False)
c.rect(48, 41, 4, 15, WOOD)
c.rect(48, 41, 4, 15, OUT, fill=False)
# leg shading
c.line(15, 42, 15, 55, WOOD_D)
c.line(51, 42, 51, 55, WOOD_D)
# wood grain on top
for gx in range(14, 50, 8):
    c.line(gx, 33, gx + 3, 33, WOOD_D)
    c.line(gx + 2, 35, gx + 5, 35, WOOD)

# --- fruit bowl on table ---
# bowl body
c.ellipse(32, 34, 9, 4, BOWL)
# rim
c.line(23, 33, 41, 33, BOWL_D)
c.line(23, 34, 23, 35, OUT)
c.line(41, 34, 41, 35, OUT)
c.line(25, 38, 39, 38, OUT)
# fruits peeking above rim
c.circle(27, 32, 2, RED)
c.circle(32, 31, 2, ORG)
c.circle(37, 32, 2, RED)
c.set(32, 28, GRN)
c.set(31, 29, GRN)
c.set(33, 29, GRN)
c.set(27, 29, GRN)
c.set(37, 29, GRN)
c.set(32, 30, "#f2b53c")
# candle + cups on table
c.rect(15, 28, 2, 3, "#f2e6b8")          # candle
c.set(15, 27, "#e8963c")
c.set(16, 27, "#f2b53c")
c.rect(46, 29, 3, 2, BOWL)               # cup right
c.rect(46, 29, 3, 2, OUT, fill=False)
c.rect(15, 29, 3, 2, BOWL)               # cup left
c.rect(15, 29, 3, 2, OUT, fill=False)
c.rect(45, 28, 3, 2, BOWL)
c.rect(45, 28, 3, 2, OUT, fill=False)
# plates
c.ellipse(20, 35, 3, 1, BOWL_D)
c.ellipse(44, 35, 3, 1, BOWL_D)

save("dining_table", c)
finish(c)
