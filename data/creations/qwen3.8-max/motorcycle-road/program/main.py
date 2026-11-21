from pixelbench_api import *

# ---- extract motorcycle sprite with transparent background ----
sp = input_canvas.copy(name="sprite")
sp.fill_at(0, 0, None)                      # outer white background -> transparent
wi = sp.color('#ffffffff')
# enclosed white pockets inside the wheels are see-through too
for (x0, x1) in ((6, 21), (43, 58)):
    for y in range(33, 48):
        for x in range(x0, x1 + 1):
            if sp.get(x, y) == wi:
                sp.set(x, y, None)

# ---- colours ----
SKY      = '#87ceeb'
SUN      = '#ffd93b'
CLOUD    = '#ffffff'
BIRD     = '#4a4a4a'
HILL1    = '#a3cd7a'
HILL2    = '#8bbf68'
FIELD1   = '#74b258'
FIELD2   = '#61a04b'
HEDGE    = '#3f7f37'
TRUNK    = '#7a4a21'
LEAF     = '#3f7f37'
LEAF2    = '#2f6b2f'
FENCE_P  = '#8a5a2b'
FENCE_R  = '#a06a35'
SHOULDER = '#4c8a3f'
EDGE     = '#a8a8a8'
ASPHALT  = '#6e6e6e'
SP1      = '#626262'
SP2      = '#7a7a7a'
DASH     = '#e8d44d'
SHADOW   = '#5a5a5a'

# ---- scene ----
out = new_canvas(64, 64, name="output")
out.rect(0, 0, 64, 64, SKY)

# sun, clouds, birds
out.circle(52, 7, 4, SUN, fill=True)
out.ellipse(13, 8, 7, 2, CLOUD)
out.ellipse(17, 6, 4, 2, CLOUD)
out.ellipse(36, 13, 6, 2, CLOUD)
for bx, by in ((24, 9), (25, 8), (26, 9), (40, 6), (41, 5), (42, 6)):
    out.set(bx, by, BIRD)

# rolling hills
out.ellipse(14, 30, 20, 8, HILL1)
out.ellipse(46, 31, 24, 9, HILL2)

# fields with a hedge between two plots
out.rect(0, 30, 26, 13, FIELD1)
out.rect(26, 30, 2, 13, HEDGE)
out.rect(28, 30, 36, 13, FIELD2)

# trees
out.rect(6, 30, 2, 12, TRUNK)
out.circle(7, 27, 5, LEAF)
out.rect(57, 29, 2, 13, TRUNK)
out.circle(58, 26, 5, LEAF2)

# fence along the field edge
out.rect(0, 36, 64, 1, FENCE_R)
out.rect(0, 39, 64, 1, FENCE_R)
for px in (2, 12, 22, 32, 42, 52, 60):
    out.rect(px, 35, 2, 8, FENCE_P)

# grass shoulder + road
out.rect(0, 43, 64, 2, SHOULDER)
out.rect(0, 45, 64, 1, EDGE)
out.rect(0, 46, 64, 18, ASPHALT)
for i in range(46):
    x = (i * 17 + 3) % 64
    y = 46 + ((i * 29) % 18)
    out.set(x, y, SP1 if i % 2 else SP2)
for x0 in range(1, 64, 13):
    out.rect(x0, 55, 7, 2, DASH)

# wheel shadows, then the motorcycle (wheels land on row 53)
out.rect(5, 54, 17, 1, SHADOW)
out.rect(42, 54, 17, 1, SHADOW)
out.blit(sp, 0, 6)

view(out)
save("motorcycle-road", out)
finish(out)
