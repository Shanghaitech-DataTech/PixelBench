from pixelbench_api import *

NAVY = "#2B3A55"
BLUE = "#3D7DD8"
WHITE = "#FFFFFF"
BG = "#E8ECF1"

c = new_canvas(64, 64, background=BG, name="transport_icons")

def tile(qx, qy):
    # consistent framing: 24x24 rounded tile centered in each 32px quadrant
    c.rect(qx+4, qy+4, 24, 24, WHITE)
    # rounded corners: knock out corners, then border
    c.set(qx+4, qy+4, None); c.set(qx+27, qy+4, None)
    c.set(qx+4, qy+27, None); c.set(qx+27, qy+27, None)
    for (x, y, w, h) in [(qx+5,qy+4,22,1),(qx+5,qy+27,22,1),
                         (qx+4,qy+5,1,22),(qx+27,qy+5,1,22)]:
        c.rect(x, y, w, h, NAVY)

def thick_line(x0,y0,x1,y1,col):
    c.line(x0,y0,x1,y1,col)
    c.line(x0+1,y0,x1+1,y1,col)

# ---- Bus (top-left quadrant) ----
qx, qy = 0, 0
tile(qx, qy)
x, y = qx, qy
c.rect(x+9, y+12, 15, 9, NAVY)              # body
c.rect(x+11, y+14, 4, 4, WHITE)             # window L
c.rect(x+17, y+14, 4, 4, WHITE)             # window R
c.rect(x+9, y+19, 15, 1, BLUE)              # stripe
c.circle(x+13, y+22, 2, NAVY)               # wheel L
c.circle(x+20, y+22, 2, NAVY)               # wheel R
c.set(x+13, y+22, BLUE); c.set(x+20, y+22, BLUE)
c.rect(x+23, y+14, 1, 2, BLUE)              # mirror

# ---- Subway (top-right quadrant) ----
qx, qy = 32, 0
tile(qx, qy)
x, y = qx, qy
c.rect(x+10, y+11, 13, 12, NAVY)            # car front
c.set(x+10,y+11,None); c.set(x+22,y+11,None)
c.set(x+10,y+22,None); c.set(x+22,y+22,None)
c.rect(x+12, y+13, 9, 4, WHITE)             # windshield
c.rect(x+10, y+19, 13, 1, BLUE)             # stripe
c.set(x+13, y+21, BLUE); c.set(x+20, y+21, BLUE)  # lights
c.line(x+8, y+25, x+25, y+25, NAVY)         # rail
for i in range(4):
    c.line(x+9+i*4, y+24, x+9+i*4, y+25, NAVY)

# ---- Bicycle (bottom-left quadrant) ----
qx, qy = 0, 32
tile(qx, qy)
x, y = qx, qy
c.circle(x+12, y+20, 4, NAVY, fill=False)   # rear wheel
c.circle(x+21, y+20, 4, NAVY, fill=False)   # front wheel
c.set(x+12, y+20, BLUE); c.set(x+21, y+20, BLUE)
c.line(x+12, y+20, x+16, y+14, NAVY)        # seat tube
c.line(x+16, y+14, x+21, y+20, NAVY)        # down tube
c.line(x+12, y+20, x+17, y+20, NAVY)        # chainstay
c.line(x+16, y+14, x+18, y+12, NAVY)        # seat post
c.rect(x+16, y+11, 4, 1, NAVY)              # seat
c.line(x+16, y+14, x+20, y+13, NAVY)        # top tube
c.line(x+20, y+13, x+21, y+16, NAVY)        # fork
c.line(x+19, y+11, x+22, y+11, NAVY)        # handlebar

# ---- Pedestrian (bottom-right quadrant) ----
qx, qy = 32, 32
tile(qx, qy)
x, y = qx, qy
c.circle(x+17, y+11, 2, NAVY)               # head
c.line(x+17, y+14, x+17, y+19, NAVY)        # torso
c.line(x+16, y+14, x+16, y+19, NAVY)
c.line(x+17, y+19, x+13, y+24, NAVY)        # leg 1
c.line(x+16, y+19, x+13, y+24, NAVY)
c.line(x+17, y+19, x+21, y+22, NAVY)        # leg 2
c.line(x+16, y+19, x+20, y+22, NAVY)
c.line(x+16, y+15, x+12, y+18, NAVY)        # arm 1
c.line(x+17, y+15, x+21, y+17, NAVY)        # arm 2
c.line(x+16, y+15, x+13, y+18, NAVY)
c.rect(x+21, y+16, 2, 3, BLUE)              # bag accent

print(c.stats_text())
save("transport_icons", c)
finish(c)
