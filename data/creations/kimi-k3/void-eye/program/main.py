# void-eye — 64x64 RPG boss: giant floating single-eye monster

OUT      = '#120826'  # near-black violet outline
BODY     = '#3a2160'  # body base
BODY_D   = '#22103c'  # body shadow
BODY_L   = '#5c3a92'  # body highlight
RIM      = '#8f63e0'  # rim light
GLOWDIM  = '#553199'  # eye socket glow ring
SCLERA   = '#e9e1fb'
SCLERA_D = '#b7a6e4'
VEIN     = '#9a7fd1'
IRIS_D   = '#3c0d7d'
IRIS     = '#7425d6'
IRIS_L   = '#a55cff'
PUPIL    = '#0b0517'
CORE     = '#c77dff'  # glowing pupil core
GLINT    = '#ffffff'
MOTE     = '#9a66ff88'
SH1 = '#0c051733'; SH2 = '#0c051766'; SH3 = '#0c0517a6'

c = new_canvas(64, 64, name='void-eye')

def tentacle(pts, radii, col):
    for (x, y), r in zip(pts, radii):
        if r <= 0:
            c.set(x, y, col)
        else:
            c.circle(x, y, r, col)

CROSS = {}  # (x, y) -> colour index, guarded '+'-shaped writes

def cross(x, y, col):
    idx = c.color(col)
    CROSS[(x, y)] = idx
    c.set(x, y, col)
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        p = (x+dx, y+dy)
        if CROSS.get(p, -1) != idx:
            c.set(p[0], p[1], col)

cross(24, 15, RIM)
cross(44, 34, BODY_L)

# --- tentacles (drawn first, bases hidden under body) ---
tentacle([(22,38),(19,42),(17,45),(16,48),(15,50)], [2,2,1,1,0], BODY_D)  # back left
tentacle([(42,38),(45,42),(47,45),(48,48),(49,50)], [2,2,1,1,0], BODY_D)  # back right
tentacle([(27,40),(25,44),(24,47),(24,50),(25,52)], [2,2,1,1,0], BODY)    # front left
tentacle([(32,42),(32,45),(31,48),(31,51),(32,53)], [2,2,1,1,0], BODY)    # front centre
tentacle([(37,40),(39,44),(40,47),(40,50),(39,52)], [2,2,1,1,0], BODY)    # front right

# --- body sphere with shading ---
c.ellipse(32, 27, 20, 18, BODY_D)   # base (dark)
c.ellipse(31, 25, 19, 17, BODY)     # main mass, leaves dark crescent bottom-right
c.ellipse(27, 20, 11, 9, BODY_L)    # highlight blob top-left
c.ellipse(30, 23, 13, 12, BODY)     # carve highlight into a crescent

# --- the giant eye ---
ex, ey = 32, 25
c.circle(ex, ey, 13, GLOWDIM)        # socket glow ring on body
c.circle(ex, ey, 11, SCLERA)         # sclera
c.circle(ex, ey+1, 10, SCLERA_D)     # lower shade
c.circle(ex, ey-1, 9, SCLERA)        # carve shade to bottom crescent
c.line(22, 19, 25, 21, VEIN)         # veins
c.line(42, 20, 39, 22, VEIN)
c.circle(ex, ey, 7, IRIS_D)          # iris outer ring
c.circle(ex, ey, 6, IRIS)            # deep purple iris
c.circle(ex-1, ey-1, 4, IRIS_L)      # inner light
c.circle(ex, ey, 3, PUPIL)           # pupil
c.circle(ex, ey, 1, CORE)            # faint glowing core
c.set(ex-2, ey-2, GLINT)             # glint
c.set(ex-1, ey-2, GLINT)

# --- silhouette outline ---
c.outline(OUT)

# smooth the crown (kill the 1px antenna the ellipse top creates)
for cx0 in (30, 31, 32):
    c.set(cx0, 8, OUT)

# faint glowing tentacle tips
for tx, ty in [(25, 51), (32, 52), (39, 51)]:
    c.set(tx, ty, RIM)
for tx, ty in [(15, 50), (49, 50)]:
    c.set(tx, ty, BODY_L)

# --- floating motes ---
for mx, my in [(9,22), (54,15), (55,40), (12,44)]:
    c.set(mx, my, MOTE)

# --- soft hover shadow ---
c.ellipse(32, 57, 16, 4, SH1)
c.ellipse(32, 57, 13, 3, SH2)
c.ellipse(32, 57, 7, 2, SH3)

save('void-eye', c)
view(c)
finish(c)
