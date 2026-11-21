from pixelbench_api import *

OUT    = (18, 20, 26)   # dark outline
DARK   = (44, 48, 58)   # ring shadow / darkest metal
HOLE   = (66, 72, 82)   # ring inner hole / shadow side
BASEM  = (96, 102, 114) # mid metal
MID2   = (130, 137, 150)
LIGHT  = (168, 175, 188)
BRIGHT = (206, 212, 224)

c = new_canvas(32, 32)

# --- silhouette: broad-shouldered torso, tapering waist ---
torso = [(9,6),(22,6),(27,12),(27,19),(22,26),(18,30),(13,30),(9,26),(4,19),(4,12)]
c.poly(torso, BASEM)

# left shadow zone (depth)
c.poly([(4,12),(7,12),(9,25),(9,26),(4,19)], HOLE)

# belt band
c.rect(8,26,15,2, DARK)
c.rect(13,25,5,1, MID2)   # buckle hint

# --- interlocking chainmail rings over the chest ---
def rings(y0, x0, y1, x1, step=4, shift=2):
    for y in range(y0, y1+1, step):
        off = shift if ((y-y0)//step) % 2 else 0
        for x in range(x0+off, x1+1, step):
            c.circle(x, y, 2, DARK, fill=False)
            c.set(x, y, HOLE)

rings(8, 7, 24, 27)

# highlight some rings near the light source (upper-left diagonal)
for (hx, hy) in [(9,8),(13,8),(9,12),(17,12),(13,16),(21,16)]:
    c.circle(hx, hy, 2, LIGHT, fill=False)
    c.set(hx, hy, HOLE)

# specular sheen across shoulders (upper-left light)
c.poly([(6,7),(13,8),(15,10),(8,9)], LIGHT)
c.poly([(10,6),(16,6),(18,9),(12,9)], MID2)
c.poly([(13,6),(16,6),(17,8),(14,8)], BRIGHT)
c.set(15,7, BRIGHT)

# --- crisp outline around the whole sprite ---
c.outline(OUT)

finish(c)
