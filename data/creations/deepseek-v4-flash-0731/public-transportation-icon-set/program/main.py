from pixelbench_api import *

# ---- palette (consistent set) ----
BG    = "#E6ECF2"   # page background, light gray-blue
NAVY  = "#26333F"   # primary icon / frame line colour
WHITE = "#FDFDFE"   # frame fill
ACC   = "#6FA9DB"   # single accent colour used on every icon

c = new_canvas(64, 64, background=BG, name="transport")

# ---- helpers ----
def rr(cv, x0, y0, x1, y1, r, col):
    """Filled rounded rectangle; corners cut by a quarter circle of radius r."""
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            dx = 0
            if x < x0 + r:
                dx = x0 + r - x
            elif x > x1 - r:
                dx = x - (x1 - r)
            dy = 0
            if y < y0 + r:
                dy = y0 + r - y
            elif y > y1 - r:
                dy = y - (y1 - r)
            if dx * dx + dy * dy <= r * r:
                cv.set(x, y, col)

def tile(tx, ty):
    """Consistent frame: 2 px rounded border on a white card."""
    rr(c, tx + 2, ty + 2, tx + 29, ty + 29, 7, NAVY)
    rr(c, tx + 4, ty + 4, tx + 27, ty + 27, 5, WHITE)

def icon_bus(tx, ty):
    # body (2 px outline, white body)
    rr(c, tx + 7,  ty + 8,  tx + 24, ty + 20, 3, NAVY)
    rr(c, tx + 9,  ty + 10, tx + 22, ty + 18, 1, WHITE)
    # windshield, door, side window
    c.rect(tx + 9,  ty + 11, 3, 7, NAVY)   # front windshield
    c.rect(tx + 21, ty + 11, 3, 7, NAVY)   # side window
    c.rect(tx + 13, ty + 15, 3, 3, NAVY)   # door
    c.rect(tx + 13, ty + 17, 8, 2, ACC)    # accent stripe
    # wheels with light hubs
    c.circle(tx + 11, ty + 21, 2, NAVY)
    c.set(tx + 11, ty + 21, WHITE)
    c.circle(tx + 21, ty + 21, 2, NAVY)
    c.set(tx + 21, ty + 21, WHITE)

def icon_subway(tx, ty):
    # pantograph + contact wire
    c.rect(tx + 11, ty + 5, 9, 2, NAVY)
    c.rect(tx + 15, ty + 6, 2, 3, NAVY)
    # car body (2 px outline)
    rr(c, tx + 8,  ty + 10, tx + 23, ty + 21, 3, NAVY)
    rr(c, tx + 10, ty + 12, tx + 21, ty + 19, 1, WHITE)
    # front accent strip, windows, door
    c.rect(tx + 10, ty + 12, 3, 6, ACC)   # front strip
    c.rect(tx + 14, ty + 12, 3, 3, NAVY)  # window
    c.rect(tx + 19, ty + 12, 3, 3, NAVY)  # window
    c.rect(tx + 14, ty + 16, 3, 3, NAVY)  # door
    c.rect(tx + 14, ty + 18, 8, 1, ACC)   # accent underline
    # bogeys + rail
    c.rect(tx + 11, ty + 22, 3, 2, NAVY)
    c.rect(tx + 18, ty + 22, 3, 2, NAVY)
    c.rect(tx + 4,  ty + 24, 24, 2, NAVY)

def icon_bike(tx, ty):
    # wheels: navy rings with white centres
    c.circle(tx + 9,  ty + 21, 4, NAVY)
    c.circle(tx + 9,  ty + 21, 2, WHITE)
    c.set(tx + 9,  ty + 21, NAVY)
    c.circle(tx + 22, ty + 21, 4, NAVY)
    c.circle(tx + 22, ty + 21, 2, WHITE)
    c.set(tx + 22, ty + 21, NAVY)
    # frame: seat tube, top tube, fork, chainstay, down tube, seat stay
    c.line(tx + 9,  ty + 21, tx + 12, ty + 12, NAVY)   # seat tube
    c.line(tx + 12, ty + 12, tx + 20, ty + 11, NAVY)   # top tube
    c.line(tx + 20, ty + 11, tx + 22, ty + 21, NAVY)   # fork
    c.line(tx + 22, ty + 21, tx + 15, ty + 18, NAVY)   # chainstay
    c.line(tx + 15, ty + 18, tx + 12, ty + 12, NAVY)   # down tube
    c.line(tx + 9,  ty + 21, tx + 15, ty + 18, NAVY)   # seat stay
    # chainring, seat (accent), handlebar
    c.circle(tx + 15, ty + 18, 1, NAVY)
    c.rect(tx + 10, ty + 10, 4, 2, ACC)
    c.rect(tx + 18, ty + 9,  5, 2, NAVY)

def icon_ped(tx, ty):
    # head
    c.circle(tx + 16, ty + 8, 3, NAVY)
    c.circle(tx + 16, ty + 8, 2, WHITE)
    c.set(tx + 16, ty + 8, NAVY)
    # scarf (accent)
    c.rect(tx + 13, ty + 11, 5, 2, ACC)
    # torso
    c.rect(tx + 15, ty + 12, 2, 5, NAVY)
    # arms (swing, 2 px stroke each)
    c.line(tx + 17, ty + 13, tx + 21, ty + 16, NAVY)
    c.line(tx + 16, ty + 13, tx + 20, ty + 16, NAVY)
    c.line(tx + 15, ty + 13, tx + 12, ty + 15, NAVY)
    c.line(tx + 14, ty + 13, tx + 11, ty + 15, NAVY)
    # legs (stride, 2 px stroke each)
    c.line(tx + 16, ty + 16, tx + 19, ty + 21, NAVY)
    c.line(tx + 17, ty + 17, tx + 20, ty + 22, NAVY)
    c.line(tx + 15, ty + 16, tx + 12, ty + 21, NAVY)
    c.line(tx + 14, ty + 17, tx + 11, ty + 22, NAVY)
    # feet
    c.rect(tx + 18, ty + 21, 3, 2, NAVY)
    c.rect(tx + 10, ty + 21, 3, 2, NAVY)

# ---- build 2x2 grid: row1 bus | subway ; row2 bike | pedestrian ----
tile(0, 0);  icon_bus(0, 0)
tile(32, 0); icon_subway(32, 0)
tile(0, 32); icon_bike(0, 32)
tile(32, 32); icon_ped(32, 32)

print(c.stats_text())
for name, (rx, ry) in (("bus", (0, 0)), ("subway", (32, 0)), ("bike", (0, 32)), ("ped", (32, 32))):
    print("---", name, "---")
    print(c.matrix_text(region=(rx, ry, rx + 31, ry + 31)))

finish(c)
