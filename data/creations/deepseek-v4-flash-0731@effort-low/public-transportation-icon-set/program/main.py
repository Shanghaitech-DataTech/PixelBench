from pixelbench_api import *

c = new_canvas(64, 64, name="transport")

# palette
cream  = c.color('#F4EFE3')
tile   = c.color('#2A4159')
white  = c.color('#FFFFFF')
accent = c.color('#84C0F0')
dark   = c.color('#16263B')

# whole background
c.rect(0, 0, 64, 64, cream)

def rr(X0, Y0, X1, Y1, r, outline=None, fillcol=None):
    d = (f"M {X0+r} {Y0} L {X1-r} {Y0} A {r} {r} 0 0 1 {X1} {Y0+r} "
         f"L {X1} {Y1-r} A {r} {r} 0 0 1 {X1-r} {Y1} "
         f"L {X0+r} {Y1} A {r} {r} 0 0 1 {X0} {Y1-r} "
         f"L {X0} {Y0+r} A {r} {r} 0 0 1 {X0+r} {Y0} Z")
    if fillcol is not None:
        c.path(d, fillcol, fill=True)
    if outline is not None:
        c.path(d, outline, fill=False)

# ---- tiles (2x2, each 32x32), consistent framing ----
rr(3, 3, 28, 28, 5, white, tile)
rr(35, 3, 60, 28, 5, white, tile)
rr(3, 35, 28, 60, 5, white, tile)
rr(35, 35, 60, 60, 5, white, tile)

# ===== BUS (top-left) =====
ox, oy = 0, 0
c.rect(ox+7,  oy+21, 6, 5, dark)   # rear wheel
c.rect(ox+19, oy+21, 6, 5, dark)   # front wheel
rr(ox+4, oy+5, ox+27, oy+20, 3, None, white)  # body
for wx in (6, 12, 18):
    c.rect(ox+wx, oy+9, 5, 5, accent)  # windows

# ===== SUBWAY (top-right) =====
ox, oy = 32, 0
c.line(ox+4, oy+24, ox+28, oy+24, accent)      # rail
c.rect(ox+6, oy+23, 20, 2, dark)
rr(ox+4, oy+7, ox+27, oy+21, 4, None, white)   # train car
c.rect(ox+6,  oy+11, 13, 4, accent)            # side windows
c.rect(ox+19, oy+11, 5, 6, accent)             # windshield
c.rect(ox+11, oy+4, 10, 2, accent)             # roof detail

# ===== BICYCLE (bottom-left) =====
ox, oy = 0, 32
c.circle(ox+10, oy+18, 6, white, True); c.circle(ox+10, oy+18, 3, dark, True)   # rear
c.circle(ox+22, oy+18, 6, white, True); c.circle(ox+22, oy+18, 3, dark, True)   # front
c.line(ox+13, oy+9,  ox+17, oy+9,  white)   # saddle
c.rect(ox+13, oy+9,  2, 5,  white)          # seat post
c.line(ox+12, oy+14, ox+18, oy+14, white)   # top tube
c.line(ox+13, oy+9,  ox+13, oy+19, white)   # seat tube
c.line(ox+13, oy+19, ox+18, oy+9,  white)   # down tube
c.line(ox+13, oy+19, ox+10, oy+18, white)   # chainstay
c.line(ox+18, oy+9,  ox+22, oy+18, white)   # fork
c.rect(ox+16, oy+6,  6, 2,  white)          # handlebar
c.line(ox+22, oy+6,  ox+22, oy+9,  white)   # head tube

# ===== PEDESTRIAN (bottom-right) =====
ox, oy = 32, 32
c.circle(ox+16, oy+9, 4, white, True)    # head
c.line(ox+15, oy+14, ox+11, oy+11, white)  # left arm
c.line(ox+17, oy+14, ox+21, oy+11, white)  # right arm
c.rect(ox+15, oy+13, 2, 7, white)        # torso
c.line(ox+15, oy+20, ox+14, oy+26, white) # left leg
c.line(ox+17, oy+20, ox+18, oy+26, white) # right leg
c.rect(ox+13, oy+26, 3, 2,  white)       # left foot
c.rect(ox+17, oy+26, 3, 2,  white)       # right foot

finish(c)
