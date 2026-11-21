from pixelbench_api import new_canvas, finish, view, save

c = new_canvas(64, 64, name="tavern")

# ---- palette ----
# warm darks
OUT   = (30,18,12)          # dark outline
WALL  = (74,44,30)
WALLD = (54,32,22)
WLIT  = (96,58,38)
CEIL  = (38,24,16)
FLOOR = (60,36,24)
FLOORD= (46,28,19)
W_LIT = (120,76,46)
W_MD  = (88,54,34)
W_HI  = (150,98,58)
LAMP  = (255,215,110)
LAMPHI= (255,230,150)
GLOW  = (255,205,110,70)
SMOKE = (255,208,120,55)
SMOKE2= (255,214,130,40)
AMBER = (226,168,70)
GREEN = (120,150,80)
RED   = (150,60,45)
BLUE  = (80,110,150)
CLEAR = (200,220,225)
BROWN = (120,78,48)
CAP   = (70,48,32)
LIQ   = (240,190,90)
LIQD  = (196,140,60)
GLASS = (215,225,230,120)
GLASS2= (235,240,240,180)
METAL = (70,58,48)
SHADE = (52,42,34)
PALE  = (180,150,120)

# ---- background ----
# ceiling
c.rect(0,0,64,6,CEIL)
# back wall
c.rect(0,5,64,30,WALL)
# wood plank lines on wall
for y in (9,12,15,18,21,27,30,33):
    c.line(0,y,63,y,WALLD)
c.line(2,7,61,7,WLIT)

# ---- shelf with bottles ----
# shelf board
c.rect(3,24,58,4,W_LIT)
c.line(3,27,60,27,OUT)
c.line(3,24,60,24,W_HI)

bottles = [
    (8, AMBER), (15, GREEN), (22, RED), (29, BLUE),
    (36, AMBER), (43, GREEN), (50, BROWN),
]
for (bx, col) in bottles:
    h = 9 if bx != 22 else 10
    top = 23 - h
    # cap
    c.rect(bx+2, top-2, 3, 2, CAP)
    # neck
    c.rect(bx+2, top, 3, 3, col)
    # body
    c.rect(bx, top+3, 7, 8, col)
    # highlight
    c.rect(bx+1, top+3, 1, 6, GLASS2)
    # outline
    c.rect(bx, top+3, 7, 8, OUT, fill=False)
    c.rect(bx+2, top, 3, 4, OUT, fill=False)

# ---- bar counter ----
# heavy counter behind bar stools, spans width
c.rect(0,36,64,3,W_HI)     # top surface
c.line(0,38,63,38,OUT)
c.rect(0,39,64,9,W_MD)     # front
c.line(0,43,63,43,OUT)
# counter skirt
c.rect(0,48,64,3,WALLD)
c.line(0,50,63,50,OUT)

# --- items on counter ---
# glass left
gx=9
c.rect(gx,31,5,6,GLASS)
c.rect(gx,32,5,5,LIQ)
c.rect(gx,31,5,6,OUT,fill=False)
c.line(gx+1,32,gx+1,36,GLASS2)
# glass right
gx=54
c.rect(gx,31,5,6,GLASS)
c.rect(gx,32,5,5,LIQD)
c.rect(gx,31,5,6,OUT,fill=False)
# on-counter barrel, center-left
bx, by = 28, 29
c.ellipse(bx+5, by, 5, 2, W_HI)
c.circle(bx+5, by, 2, W_HI)
c.rect(bx, by+1, 11, 7, W_MD)
c.line(bx, by+2, bx+10, by+2, OUT)
c.line(bx, by+6, bx+10, by+6, OUT)
c.rect(bx, by+2, 11, 6, OUT, fill=False)
# small glass on barrel
c.rect(bx+2, by-4, 3, 4, GLASS)
c.rect(bx+2, by-3, 3, 3, LIQ)
c.rect(bx+2, by-4, 3, 4, OUT, fill=False)

# ---- floor ----
c.rect(0,51,64,13,FLOOR)
c.line(0,51,63,51,W_LIT)
for x in range(4,64,8):
    c.line(x,52,x,63,FLOORD)

# ---- barrels on floor (sides) ----
def barrel(px, py, wcol):
    c.ellipse(px+wcol//2, py, wcol//2, 2, W_LIT)
    c.circle(px+wcol//2, py, wcol//4, W_HI)
    c.rect(px, py+2, wcol, 9, W_MD)
    c.line(px, py+3, px+wcol-1, py+3, OUT)
    c.line(px, py+3, px+wcol-1, py+5, OUT)
    c.line(px, py+8, px+wcol-1, py+8, OUT)
    c.line(px, py+8, px+wcol-1, py+10, OUT)
    c.rect(px, py+1, wcol, 10, OUT, fill=False)
    c.rect(px+wcol-3, py+2, 1, 9, W_HI)
barrel(3, 47, 11)
barrel(50, 47, 11)

# ---- stools ----
for sx in (16, 32, 48):
    # seat
    c.ellipse(sx+3, 50, 5, 1, W_LIT)
    c.ellipse(sx+3, 50, 5, 1, OUT, fill=False)
    # legs
    c.line(sx+2, 50, sx+4, 56, OUT)
    c.rect(sx+3, 50, 1, 2, METAL)
    # cross bar
    c.line(sx+1, 54, sx+5, 54, METAL)

# ---- hanging lamps ----
for cx in (16, 48):
    c.rect(cx-1, 4, 3, 5, OUT)            # cord
    c.rect(cx, 4, 1, 5, METAL)
    # glow
    c.circle(cx, 15, 6, GLOW)
    c.circle(cx, 15, 3, SMOKE)
    # shade (trapezoid)
    c.poly([(cx-3,8),(cx+3,8),(cx+8,13),(cx-8,13)], SHADE)
    c.poly([(cx-3,8),(cx+3,8),(cx+8,13),(cx-8,13)], OUT, fill=False)
    c.rect(cx-2,8,4,5,METAL)
    # bulb
    c.circle(cx, 15, 2, LAMP)
    c.circle(cx, 15, 1, LAMPHI)

# ---- smoky atmosphere (upper haze) ----
c.circle(16, 20, 9, SMOKE)
c.circle(48, 20, 9, SMOKE)
c.circle(32, 14, 6, SMOKE2)
c.path("M6 40 q6 -8 10 0 q4 -6 9 -2", SMOKE2, fill=False)
c.path("M46 42 q5 -7 9 -1 q5 -6 8 -1", SMOKE2, fill=False)

# ---- warm foreground glow floor ----
c.circle(16, 50, 7, SMOKE2)
c.circle(48, 50, 7, SMOKE2)

# submit single output
finish(c)
save("tavern_interior", c)
print(c.stats_text())
