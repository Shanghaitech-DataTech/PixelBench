from pixelbench_api import *

W, H = 32, 32
c = new_canvas(W, H, name="portable-cassette-player")

BODY = "#2d3a8c"
BODY_L = "#4051b5"
BODY_D = "#1c2456"
EDGE = "#5c6bc0"
SILVER = "#b0bec5"
SILVER_D = "#78909c"
SCREEN = "#0a0a0a"
WINDOW = "#101018"
REEL = "#e8c46a"
REEL_D = "#a8872e"
TAPE = "#3a3a3a"
BUTTON = "#eeeeee"
GRY_D = "#9e9e9e"
RED = "#e53935"
LIT = "#ff8a80"
WIRE = "#1a1a1a"
PLUG = "#808080"
LCD = "#3a3a3a"
GLASS = "#34343a"

def rr(x,y,w,h,cool, r):
    c.rect(x+r, y, w-2*r, h, cool)
    c.rect(x, y+r, w, h-2*r, cool)
    c.circle(x+r, y+r, r, cool)
    c.circle(x+w-1-r, y+r, r, cool)
    c.circle(x+r, y+h-1-r, r, cool)
    c.circle(x+w-1-r, y+h-1-r, r, cool)

# ---- Main body ----
rr(5, 3, 22, 25, BODY, 3)
c.rect(8, 4, 16, 1, EDGE)
c.rect(6, 6, 1, 19, BODY_D)
c.rect(26, 6, 1, 19, BODY_L)
c.rect(7, 26, 18, 1, BODY_D)
c.rect(6, 27, 20, 1, BODY_D)

# ---- Top LCD panel ----
c.rect(8, 5, 16, 3, BODY_L)
c.rect(9, 5, 14, 3, SCREEN)
c.rect(11, 6, 2, 1, LCD)
c.rect(14, 6, 1, 1, LCD)
c.circle(25, 8, 1, RED)          # record indicator

# ---- Cassette window ----
c.rect(9, 10, 14, 11, BODY_D)
c.rect(10, 11, 12, 9, SILVER_D)
c.rect(10, 11, 12, 9, WINDOW)
c.rect(10, 11, 12, 1, GLASS)

# Tape band
c.rect(13, 12, 6, 7, TAPE)

# Reels
for cx in (13, 21):
    c.circle(cx, 15, 3, REEL)
    c.circle(cx, 15, 2, REEL_D)
    c.circle(cx, 15, 1, WINDOW)
    c.rect(cx-1, 15, 3, 1, WINDOW)
    c.rect(cx, 13, 1, 5, WINDOW)

c.rect(13, 17, 6, 1, TAPE)       # lower tape edge

# ---- Right-side controls ----
c.circle(25, 12, 1, SILVER)
c.circle(25, 17, 1, SILVER)
c.circle(25, 22, 1, RED)
c.rect(25, 22, 1, 1, LIT)

# ---- Left volume slider ----
c.rect(5, 10, 1, 11, SCREEN)
c.rect(4, 14, 2, 2, SILVER)
c.rect(4, 14, 2, 1, SILVER_D)
c.rect(4, 10, 1, 1, SILVER_D)
c.rect(4, 20, 1, 1, SILVER_D)

# ---- Bottom controls panel ----
c.rect(8, 22, 16, 5, BODY_L)
c.rect(8, 26, 16, 1, BODY_D)
c.rect(9, 23, 3, 3, BUTTON)
c.rect(14, 23, 3, 3, BUTTON)
c.rect(19, 23, 3, 3, SILVER)
c.rect(9, 25, 3, 1, GRY_D)
c.rect(14, 25, 3, 1, GRY_D)
c.rect(19, 25, 3, 1, GRY_D)
# play
c.poly([(10,24),(12,25),(10,25)], GRY_D)
# pause
c.rect(15, 24, 1, 2, GRY_D)
c.rect(17, 24, 1, 2, GRY_D)
# stop
c.rect(20, 24, 2, 2, GRY_D)

# ---- Headphone cable from right edge ----
# connector jack at right edge
c.rect(27, 11, 1, 2, BODY_D)
c.line(27, 12, 30, 14, WIRE)
c.line(30, 14, 29, 18, WIRE)
c.line(29, 18, 31, 21, WIRE)
c.rect(30, 21, 2, 2, WIRE)
c.rect(31, 23, 1, 1, WIRE)
# plug at end
c.rect(30, 24, 2, 1, PLUG)

# ---- Speaker dots ----
c.rect(10, 21, 2, 1, BODY_D)
c.rect(13, 21, 2, 1, BODY_D)

# ---- Feet ----
c.rect(9, 28, 4, 1, BODY_D)
c.rect(20, 28, 4, 1, BODY_D)

print(c.stats_text())
print(c.matrix_text(region=(0,0,31,31)))

save("portable-cassette-player", c)
finish(c)
