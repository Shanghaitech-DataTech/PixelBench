from pixelbench_api import *

c = new_canvas(32, 32, background=None, name="chainmail")

DARK = c.color("#1a1d26", name="outline")
MID  = c.color("#7d8496", name="mail")
LIGHT= c.color("#aab1c2", name="ring_hi")
SHAD = c.color("#4d5468", name="mail_shade")

sil = new_canvas(32, 32, name="sil")
# torso body
sil.rect(8, 8, 16, 18, MID)
# shoulders
sil.rect(6, 6, 5, 4, MID)
sil.rect(21, 6, 5, 4, MID)
# sleeves (short)
sil.rect(4, 9, 4, 8, MID)
sil.rect(24, 9, 4, 8, MID)
# neck notch
sil.clear(13, 6, 6, 3)

# shading on right side + bottom of torso
for y in range(8, 26):
    for x in range(20, 24):
        sil.set(x, y, SHAD)
for x in range(8, 24):
    sil.set(x, 24, SHAD)

# ring pattern
for row, y in enumerate(range(9, 25, 4)):
    off = 2 if row % 2 else 0
    for x in range(6 + off, 26 + off, 4):
        sil.circle(x, y, 1, LIGHT, fill=False)
for row, y in enumerate(range(10, 17, 3)):
    for x in (6, 25):
        sil.circle(x, y, 1, LIGHT, fill=False)

# dark outline
w = h = 32
def solid(x, y):
    if not (0 <= x < w and 0 <= y < h):
        return False
    return sil.get(x, y) != 0

for y in range(h):
    for x in range(w):
        if solid(x, y):
            if any(not solid(x+dx, y+dy) for dx, dy in ((1,0),(-1,0),(0,1),(0,-1))):
                sil.set(x, y, DARK)

# collar line
for x in range(13, 19):
    sil.set(x, 8, DARK)
sil.set(13, 7, DARK)
sil.set(18, 7, DARK)

result = c
result.blit(sil, 0, 0)

print(result.stats_text())
print(result.matrix_text())
save("chainmail-armor", result)
finish(result)
