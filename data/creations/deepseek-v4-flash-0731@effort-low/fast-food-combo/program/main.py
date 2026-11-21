from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64, name="combo")

# ---------- palette ----------
def col(s): return c.color(s)
OUT   = col("#1a1a1a")
SHAD  = col("#00000055")
TRAY  = col("#efeadd")
TRAY2 = col("#e2dcc8")
BUN   = col("#a8662a")
BUNL  = col("#c07e38")
BUNB  = col("#c99868")
SES   = col("#f5e8cc")
LETD  = col("#3f7d26")
LET   = col("#5aa832")
LETB  = col("#7cc74a")
CHS   = col("#f5b71e")
CHSD  = col("#e0981a")
PATTY = col("#5a3220")
PATD  = col("#3d1f0e")
FRY   = col("#f2c14e")
FRYL  = col("#f8d97c")
FRYD  = col("#d99c2b")
CART  = col("#d21f1f")
CARTD = col("#a51515")
CARTW = col("#f0ede6")
NUG   = col("#d99a3c")
NUGL  = col("#eeb469")
NUGD  = col("#a86a20")
CPW   = col("#f2efe8")
COLA  = col("#4a2a14")
COLD  = col("#2e1a0c")
ICE   = col("#cfe8f4")
ICEL  = col("#a8cfe0")
SAU   = col("#c62828")
SAUL  = col("#e53935")
SAUO  = col("#f58a2e")
SAC   = col("#f7f1e2")
STR   = col("#e02020")
STRL  = col("#ff5a5a")
TRANSP = None

def rr(x, y, w, h, colr, fill=True):
    c.rect(x, y, w, h, colr, fill=fill)
    if fill:
        c.clear(x, y, 1, 1); c.clear(x+w-1, y, 1, 1)
        c.clear(x, y+h-1, 1, 1); c.clear(x+w-1, y+h-1, 1, 1)
    return c

# ---------- tray + shadow ----------
rr(4, 5, 58, 58, SHAD)
rr(2, 2, 59, 59, TRAY)
rr(3, 3, 57, 57, TRAY)
c.rect(2, 2, 59, 59, OUT, fill=False)
c.rect(4, 4, 55, 55, TRAY2, fill=False)
rr(6, 6, 51, 51, TRAY)

# ---------- sauce cups (top-left) ----------
def sauce_cup(cx, cy, r, sauce, hi, rim):
    c.ellipse(cx, cy, r, r, SAC)          # cup
    c.ellipse(cx, cy, r-2, r-2, sauce)    # sauce
    c.ellipse(cx, cy, r-3, r-3, hi)
    c.circle(cx, cy, r, OUT, fill=False)
    # small highlight
    c.ellipse(cx-1, cy-1, r-1, r-1, OUT, fill=False)

sauce_cup(14, 13, 7, SAU, SAUL, SAC)
sauce_cup(28, 13, 7, SAUO, CHS, SAC)

# ---------- french fries (top-right) ----------
fx0, fy0, fw, fh = 41, 7, 16, 15
# shadow
c.rect(fx0+1, fy0+2, fw, fh, SHAD)
# carton
c.rect(fx0, fy0, fw, fh, CART)
c.rect(fx0+1, fy0+1, fw-2, fh-1, CART)
# inner red
c.rect(fx0+2, fy0+2, fw-4, fh-2, CARTD)
# carton front band
c.rect(fx0+2, fy0+9, fw-4, 4, CART)
c.rect(fx0+3, fy0+11, fw-6, 2, CARTW)
# fries inside (top opening)
c.rect(fx0+3, fy0+2, fw-6, 7, FRYD)
# fry tips sticking above
for (a,(ox,oy)) in enumerate([(45,4),(48,3),(52,3),(55,4),(50,5),(43,5),(57,6),(46,4),(54,4)]):
    c.set(ox, oy, FRY)
    c.set(ox, oy+1, FRYL)
# fries texture
for y in range(fy0+3, fy0+8):
    for x in range(fx0+3, fx0+fw-3):
        if (x+y)%3!=0:
            c.set(x, y, FRY)
c.rect(fx0+2, fy0+2, fw-4, fh-2, OUT, fill=False)
# highlight on carton edge
c.rect(fx0, fy0, 1, fh, STRL) if False else None
c.set(fx0+1, fy0+3, CART)
# fry tips highlight dots
c.set(45,4,FRYL); c.set(48,3,FRYL); c.set(52,3,FRYL); c.set(55,4,FRYL)

# ---------- cheeseburger (center) ----------
bx, by = 33, 29
# shadow
c.ellipse(bx, by+10, 16, 6, SHAD)
# bottom bun
c.ellipse(bx, by+10, 15, 6, BUNB)
c.ellipse(bx, by+10, 15, 6, OUT, fill=False)
c.ellipse(bx, by+10, 12, 4, BUN)
# patty
c.ellipse(bx, by+6, 13, 5, PATTY)
c.ellipse(bx, by+6, 13, 5, OUT, fill=False)
for (px,py) in [(bx-6,by+6),(bx+6,by+6),(bx-3,by+7),(bx+2,by+7),(bx,by+5),(bx-8,by+5),(bx+8,by+4)]:
    c.set(px,py,PATD)
# cheese (melty)
c.ellipse(bx-1, by+3, 13, 5, CHS)
c.ellipse(bx-1, by+3, 13, 5, OUT, fill=False)
for (px,py) in [(bx-9,by+4),(bx+10,by+4),(bx-11,by+5),(bx+12,by+5),(bx-5,by+6),(bx+6,by+6)]:
    c.set(px,py,CHSD)
c.rect(bx-12, by+2, 3, 2, CHS); c.rect(bx+10, by+2, 3, 2, CHS)
# lettuce
c.ellipse(bx-1, by-1, 14, 6, LET)
c.ellipse(bx-1, by-1, 14, 6, OUT, fill=False)
c.ellipse(bx-2, by-2, 11, 4, LETB)
c.ellipse(bx-2, by-2, 8, 2, LET)
for (px,py) in [(bx-8,by-3),(bx+7,by-3),(bx,by-4),(bx-4,by-2),(bx+4,by-2)]:
    c.set(px,py,LETD)
# top bun
c.ellipse(bx-1, by-7, 15, 7, BUN)
c.ellipse(bx-1, by-7, 15, 7, OUT, fill=False)
c.ellipse(bx-2, by-6, 11, 5, BUNL)
# sesame seeds
for (sx,sy) in [(bx-8,by-8),(bx-3,by-10),(bx+4,by-10),(bx+8,by-8),(bx-1,by-7),(bx-6,by-6),(bx+5,by-6),(bx+1,by-9),(bx-10,by-6),(bx+9,by-5),(bx-5,by-4),(bx+2,by-4)]:
    c.set(sx,sy,SES)

c.shift(1,1,None)

# ---------- chicken nuggets (bottom-left) ----------
def nugget(cx, cy, rw, rh):
    c.ellipse(cx+1, cy+2, rw, rh, SHAD)
    c.ellipse(cx, cy, rw, rh, NUG)
    c.ellipse(cx, cy, rw, rh, OUT, fill=False)
    c.ellipse(cx-1, cy-1, rw-1, rh-1, NUGL)
    c.ellipse(cx+1, cy, rw-2, rh-2, NUG)
    c.set(cx+2, cy-1, NUGD); c.set(cx-3, cy+1, NUGD); c.set(cx, cy+3, NUGD)

nugget(13, 40, 6, 4)
nugget(22, 38, 7, 5)
nugget(9, 47, 7, 5)
nugget(19, 48, 6, 4)

# ---------- cola cup (bottom-right) ----------
cx0, cy0 = 52, 44
c.ellipse(cx0+1, cy0+2, 9, 8, SHAD)
# cup wall (visible portion toward bottom-left)
c.ellipse(cx0, cy0, 9, 8, CART)
c.ellipse(cx0, cy0, 9, 8, OUT, fill=False)
c.ellipse(cx0-1, cy0-1, 7, 6, CARTW)
c.ellipse(cx0-1, cy0-1, 6, 5, COLA)
# ice cubes
for (ix,iy,ic) in [(cx0-4,cy0-3,ICE),(cx0,cy0-2,ICE),(cx0+2,cy0+1,ICEL),(cx0-1,cy0+2,ICE),(cx0+3,cy0-1,ICEL),(cx0-2,cy0,ICEL)]:
    c.set(ix,iy,ic)
# straw (down through cup center, red with white stripes)
for y in range(28, 50):
    x = 52
    c.set(x, y, STR); c.set(x-1, y, STRL)
    if y % 4 == 0:
        c.set(x, y, CPW); c.set(x-1, y, CPW)

# ---------- outlines / finish ----------
c.outline(OUT)

finish(c)
print(c.stats_text())
