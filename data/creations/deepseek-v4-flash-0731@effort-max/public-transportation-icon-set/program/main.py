from pixelbench_api import *

BG    = "#161E2E"
TILE  = "#26344F"
W     = "#F4F7FC"
DK    = "#0C1320"
AMBER = "#FFC24B"
CYAN  = "#52D6F0"
PINK  = "#FF8FB2"
GREEN = "#5BE0A0"

c = new_canvas(64, 64, background=BG, name="transport")

def rrect(x, y, w, h, r, col):
    d = (f"M {x+r} {y} H {x+w-1-r} A {r} {r} 0 0 1 {x+w-1} {y+r} "
         f"V {y+h-1-r} A {r} {r} 0 0 1 {x+w-1-r} {y+h-1} H {x+r} "
         f"A {r} {r} 0 0 1 {x} {y+h-1-r} V {y+r} A {r} {r} 0 0 1 {x+r} {y} Z")
    c.path(d, col)

def thick(x0, y0, x1, y1, col):
    c.line(x0, y0, x1, y1, col)
    c.line(x0 + 1, y0, x1 + 1, y1, col)

def tile_at(ox, oy):
    rrect(ox - 15, oy - 15, 30, 30, 6, TILE)

def bus(ox, oy):
    rrect(ox - 11, oy - 8, 23, 17, 3, W)
    rrect(ox - 9, oy - 6, 19, 13, 2, TILE)
    c.rect(ox - 8, oy - 5, 17, 3, W)
    c.line(ox - 3, oy - 5, ox - 3, oy - 3, TILE)
    c.line(ox + 3, oy - 5, ox + 3, oy - 3, TILE)
    c.rect(ox - 8, oy + 3, 17, 3, AMBER)
    c.circle(ox - 6, oy + 7, 2, DK)
    c.circle(ox + 6, oy + 7, 2, DK)

def subway(ox, oy):
    rrect(ox - 11, oy - 8, 23, 17, 3, W)
    rrect(ox - 9, oy - 6, 19, 13, 2, TILE)
    c.rect(ox - 8, oy - 4, 17, 3, W)
    c.line(ox, oy - 4, ox, oy - 2, TILE)
    c.rect(ox - 9, oy - 2, 2, 2, CYAN)
    c.line(ox - 5, oy - 11, ox + 5, oy - 11, W)
    c.line(ox - 5, oy - 11, ox - 2, oy - 8, W)
    c.line(ox + 5, oy - 11, ox + 2, oy - 8, W)
    c.circle(ox - 6, oy + 7, 2, DK)
    c.circle(ox + 6, oy + 7, 2, DK)

def bike(ox, oy):
    c.circle(ox - 6, oy + 5, 4, W)
    c.circle(ox - 6, oy + 5, 2, TILE)
    c.circle(ox + 6, oy + 5, 4, W)
    c.circle(ox + 6, oy + 5, 2, TILE)
    thick(ox - 4, oy - 5, ox + 5, oy - 5, W)
    thick(ox - 4, oy - 5, ox + 0, oy + 4, W)
    thick(ox + 5, oy - 5, ox + 0, oy + 4, W)
    thick(ox - 4, oy - 5, ox - 6, oy + 5, W)
    thick(ox + 0, oy + 4, ox - 6, oy + 5, W)
    thick(ox + 5, oy - 5, ox + 6, oy + 5, W)
    thick(ox + 5, oy - 5, ox + 5, oy - 7, W)
    c.rect(ox - 5, oy - 7, 3, 2, PINK)
    c.rect(ox + 4, oy - 7, 3, 2, PINK)
    c.line(ox, oy + 4, ox, oy + 7, W)
    c.rect(ox - 2, oy + 7, 5, 2, W)

def pedestrian(ox, oy):
    c.circle(ox, oy - 9, 3, W)
    c.circle(ox, oy - 9, 1, TILE)
    c.poly([(ox + 1, oy - 5), (ox + 3, oy - 5), (ox + 4, oy), (ox + 2, oy)], GREEN)
    thick(ox + 3, oy - 4, ox + 5, oy - 1, W)
    thick(ox + 1, oy - 4, ox - 1, oy - 2, W)
    thick(ox + 3, oy, ox + 5, oy + 6, W)
    thick(ox + 1, oy, ox - 2, oy + 6, W)
    c.rect(ox + 4, oy + 6, 3, 1, W)
    c.rect(ox - 3, oy + 6, 3, 1, W)

for ox, oy in ((17, 17), (47, 17), (17, 47), (47, 47)):
    tile_at(ox, oy)

bus(17, 17)
subway(47, 17)
bike(17, 47)
pedestrian(47, 47)

print(c.stats_text())
for (x0, y0) in ((2, 2), (33, 2), (2, 33), (33, 33)):
    print(c.matrix_text(region=(x0, y0, x0 + 29, y0 + 29)))

finish(c)
