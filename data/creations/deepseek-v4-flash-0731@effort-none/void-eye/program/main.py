from pixelbench_api import *

W = H = 64
c = new_canvas(W, H, name="void-eye")

# Palette
BLACK     = c.color((6, 4, 10), "black")
DARK      = c.color((15, 12, 24), "dark")
BODY      = c.color((26, 20, 40), "body")
BODY_HI   = c.color((42, 32, 60), "body_hi")
SCLERA    = c.color((76, 52, 100), "sclera")
SCLERA_HI = c.color((104, 78, 134), "sclera_hi")
IRIS      = c.color((92, 30, 148), "iris")
IRIS_DK   = c.color((58, 18, 104), "iris_dk")
PUPIL     = c.color((140, 82, 204), "pupil")
GLOW      = c.color((118, 60, 176), "glow")
GLOW_LT   = c.color((158, 100, 216), "glow_lt")
WHITE     = c.color((225, 212, 246), "white")
TENT      = c.color((62, 42, 84), "tent")
TENT_DK   = c.color((40, 28, 60), "tent_dk")
TENT_MID  = c.color((84, 58, 112), "tent_mid")
SHADOW    = c.color((18, 16, 28), "shadow")
VEIN      = c.color((70, 46, 100), "vein")

# --- Shadow cast below on the ground ---
c.ellipse(32, 58, 18, 4, SHADOW)
c.ellipse(32, 57, 14, 3, SHADOW)

# --- Main body mass (monolith dome) ---
# broad base
c.ellipse(32, 27, 23, 21, DARK)
c.ellipse(32, 26, 21, 19, BODY)
# top sheen of the dome
c.ellipse(32, 15, 14, 6, BODY_HI)
# heavy bottom darkness (creature feels dense below the eye)
c.ellipse(32, 41, 15, 6, DARK)

# --- Sclera (the eye shell) ---
c.ellipse(32, 24, 17, 14, SCLERA)
# light from upper-left on sclera
c.ellipse(28, 20, 10, 7, SCLERA_HI)
# underside shadow on sclera
c.ellipse(32, 30, 14, 5, SCLERA)

# --- Iris: deep purple disc ---
c.ellipse(32, 24, 11, 9, IRIS_DK)
c.ellipse(32, 24, 10, 8, IRIS)
# subtle iris inner shading (darker upper area toward glare)
c.ellipse(32, 21, 8, 4, IRIS_DK)

# --- Faintly glowing vertical-slit pupil ---
c.ellipse(32, 24, 3, 6, PUPIL)
# bright core
c.ellipse(32, 24, 2, 4, GLOW_LT)
# mid glow
c.ellipse(32, 24, 1.5, 3, GLOW)

# glowing aura around the pupil within iris
c.ellipse(32, 24, 5, 7, GLOW, fill=False)
c.ellipse(32, 24, 6, 8, GLOW_LT, fill=False)

# --- Highlight glint ---
c.circle(29, 19, 2, WHITE)
c.circle(28, 18, 1, WHITE)
c.set(30, 20, WHITE)

# --- Veins radiating from iris on sclera (ominous) ---
for (sx, sy, ex, ey) in [(22,27,16,25),(43,27,48,25),(25,32,20,35),(23,18,18,14),(42,18,47,14),(28,33,25,37),(37,33,40,37)]:
    c.line(sx, sy, ex, ey, VEIN)

# --- Tentacles hanging below ---
def tentacle(sx, sy, tx, ty, curve):
    mx = (sx+tx)//2 + curve
    my = (sy+ty)//2 + 2
    pts = []
    steps = 7
    for i in range(steps):
        u = i/(steps-1)
        px = int(round((1-u)*(1-u)*sx + 2*(1-u)*u*mx + u*u*tx))
        py = int(round((1-u)*(1-u)*sy + 2*(1-u)*u*my + u*u*ty))
        pts.append((px,py))
    # main strand (thick - triple line)
    for i in range(len(pts)-1):
        c.line(pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1], TENT)
        c.line(pts[i][0], pts[i][1]+1, pts[i+1][0], pts[i+1][1]+1, TENT)
        c.line(pts[i][0]-1, pts[i][1], pts[i+1][0]-1, pts[i+1][1], TENT)
    # darker tip
    c.set(pts[-1][0], pts[-1][1], TENT_DK)
    c.set(pts[-1][0]+1, pts[-1][1], TENT_DK)
    c.set(pts[-1][0], pts[-1][1]+1, TENT_DK)
    # highlight on one side
    for i in range(2, len(pts)-1):
        c.set(pts[i][0]+1, pts[i][1]+1, TENT_MID)

tents = [
    (18, 37, 13, 48, -3),
    (24, 39, 20, 52, -1),
    (29, 40, 27, 53, 1),
    (36, 40, 37, 53, 2),
    (41, 39, 44, 52, 2),
    (46, 37, 51, 48, 3),
]
for t in tents:
    tentacle(*t)
# base merge blends tentacle tops back into the underbelly
c.ellipse(32, 40, 16, 4, DARK)
c.ellipse(32, 39, 13, 3, BODY)

# --- Body side shading ---
c.ellipse(19, 27, 6, 12, DARK)
c.ellipse(45, 27, 6, 12, DARK)

# subtle sides catching a bit of glow
c.ellipse(17, 27, 3, 9, BODY_HI)

# --- ominous ridge spikes on top of the dome ---
spike_col = BODY
for (sx, sy, tx, ty) in [(12,20,9,12),(15,16,11,8),(20,12,19,5),(26,9,27,3),(38,9,38,3),(44,12,46,5),(49,16,53,8),(52,20,56,12)]:
    c.line(sx, sy, tx, ty, spike_col)

# --- glowing cracks/veins across the dark body (whispering energy) ---
crack = c.color((88, 56, 128), "crack")
for (sx, sy, ex, ey) in [(12,33,8,38),(14,45,9,52),(50,33,55,37),(49,44,55,50),(23,48,19,57),(41,48,45,57)]:
    c.line(sx, sy, ex, ey, crack)

# --- faint outer glow bleed around whole body for ominous mood ---
c.ellipse(32, 26, 25, 24, GLOW, fill=False)
c.ellipse(32, 26, 26, 25, GLOW_LT, fill=False)

print(c.stats_text())
finish(c)
