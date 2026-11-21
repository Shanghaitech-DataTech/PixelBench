from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64, name="female_elf_archer")

def col(spec, name=None):
    return c.color(spec, name)

OUT = col((20,24,20), "outline")
SKIN = col((244,198,160), "skin")
SKIN_S = col((222,170,132), "skin_shadow")
SKIN_H = col((252,226,196), "skin_hi")
EYE = col((34,36,44), "eye")
LIPS = col((198,136,128), "lips")
HAIR_D = col((16,60,34), "hair_dark")
HAIR = col((46,128,60), "hair")
HAIR_H = col((100,182,106), "hair_light")
HAIR_L = col((164,216,146), "hair_lite")
OUTFIT = col((172,226,158), "outfit")
OUTFIT_D = col((116,182,110), "outfit_dark")
OUTFIT_H = col((214,244,194), "outfit_hi")
OUTFIT_X = col((84,142,92), "outfit_deep")
BELT = col((58,94,56), "belt")
BELT_B = col((184,148,86), "buckle")
BOOT = col((116,76,48), "boot")
BOOT_D = col((66,44,30), "boot_dark")
BOW = col((164,110,62), "bow")
BOW_D = col((104,64,32), "bow_dark")
BOW_H = col((214,174,110), "bow_hi")
SHAFT = col((198,158,100), "shaft")
SHAFT_D = col((142,106,62), "shaft_dark")
FLETCH = col((222,98,74), "fletch")
FLETCH_W = col((242,236,216), "fletch_white")
QUIVER = col((130,88,48), "quiver")
QUIVER_D = col((82,54,32), "quiver_dark")
SHADOW = col((14,32,22,96), "shadow")

def quad(p0, p1, p2, n=24):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        pts.append((round(u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]),
                    round(u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1])))
    return pts

def vline(x, y0, y1, co):
    for y in range(y0, y1 + 1):
        c.set(x, y, co)

def hline(y, x0, x1, co):
    for x in range(x0, x1 + 1):
        c.set(x, y, co)

# 1. ground shadow
c.ellipse(32, 57, 16, 3, SHADOW)

# 2. bow slung across the back: big arc bulging far to the left
outer = quad((51, 1), (-24, 25), (10, 54))
inner = quad((42, 8), (-8, 27), (16, 54))
high  = quad((49, 3), (-20, 25), (12, 53))
c.poly(outer + inner[::-1], BOW)
c.poly(outer + high[::-1], BOW_H)   # highlight along the outer face
c.set(51, 1, BOW_D); c.set(50, 2, BOW_D)   # dark tips
c.set(10, 54, BOW_D); c.set(11, 53, BOW_D)

# 3. quiver + arrows on the right side, behind the back
c.rect(45, 28, 5, 10, QUIVER)
c.rect(45, 28, 5, 2, QUIVER_D)
c.rect(45, 28, 1, 10, QUIVER_D)
for x in (46, 47, 48):
    vline(x, 11, 29, SHAFT)
    c.set(x, 10, SHAFT_D)
    c.set(x - 1, 28, FLETCH)
    c.set(x + 1, 28, FLETCH_W)
    c.set(x, 27, FLETCH)

# 4. long hair behind the body
c.ellipse(32, 15, 12, 13, HAIR_D)      # mass behind the head
c.rect(20, 18, 3, 22, HAIR_D)         # long hair down the left of the back
c.rect(40, 18, 4, 16, HAIR_D)         # long hair right of the back
vline(43, 30, 40, HAIR_D)
vline(20, 38, 44, HAIR_D)

# 5. legs and boots
c.rect(27, 42, 4, 6, OUTFIT_D)
c.rect(33, 42, 4, 6, OUTFIT)
c.rect(25, 47, 7, 6, BOOT)
c.rect(33, 47, 7, 6, BOOT)
c.rect(25, 53, 7, 1, BOOT_D)
c.rect(33, 53, 7, 1, BOOT_D)
hline(48, 26, 31, BOOT_D)
hline(48, 34, 39, BOOT_D)

# 6. neck and torso (light green tunic with skirt)
c.rect(30, 19, 4, 5, SKIN)                                # neck
c.poly([(23, 24), (41, 24), (40, 35), (24, 35)], OUTFIT)   # torso
c.poly([(24, 34), (40, 34), (42, 43), (22, 43)], OUTFIT)   # skirt
c.rect(22, 42, 21, 2, OUTFIT_D)                            # hem
c.line(40, 24, 30, 33, OUTFIT_X)                            # stitching
hline(27, 27, 30, OUTFIT_D)

# 7. belt and arms
c.rect(27, 35, 10, 2, BELT)
c.rect(30, 35, 4, 2, BELT_B)
c.rect(21, 24, 4, 10, OUTFIT_D)      # left sleeve
c.rect(22, 34, 3, 2, SKIN)           # left hand
c.rect(39, 24, 4, 10, OUTFIT)        # right sleeve
c.rect(39, 34, 3, 2, SKIN)           # right hand
c.line(46, 33, 30, 23, QUIVER_D)     # quiver strap over the shoulder

# 8. hair cap behind the face
c.ellipse(32, 12, 9, 8, HAIR)

# 9. face
c.ellipse(32, 15, 6, 6, SKIN)

# 10. pointed ears
c.poly([(20, 10), (25, 12), (25, 17), (21, 18)], SKIN)
c.poly([(44, 10), (39, 12), (39, 17), (43, 18)], SKIN)
c.set(23, 14, SKIN_S)
c.set(23, 15, SKIN_S)
c.set(40, 14, SKIN_S)
c.set(40, 15, SKIN_S)

# 11. bangs over the forehead
c.rect(27, 7, 10, 3, HAIR)
c.set(26, 8, HAIR); c.set(26, 9, HAIR)
c.set(37, 8, HAIR); c.set(37, 9, HAIR)

# 12. face features
c.set(28, 11, HAIR_D); c.set(29, 11, HAIR_D)   # brows
c.set(35, 11, HAIR_D); c.set(36, 11, HAIR_D)
c.set(28, 13, EYE); c.set(29, 13, EYE)
c.set(34, 13, EYE); c.set(35, 13, EYE)
c.set(32, 16, SKIN_S)                          # nose
c.set(31, 19, LIPS); c.set(32, 19, LIPS); c.set(33, 19, LIPS)
c.set(32, 20, SKIN_S)

# 13. front locks over the shoulders
c.rect(23, 14, 4, 13, HAIR)
c.rect(38, 14, 4, 13, HAIR)
vline(23, 16, 26, HAIR_H)
vline(41, 16, 26, HAIR_H)
c.set(24, 27, HAIR_L)
c.set(41, 27, HAIR_L)
c.set(24, 28, HAIR)
c.set(40, 28, HAIR)
c.set(25, 17, HAIR_L); c.set(39, 17, HAIR_L)

# 14. small highlights and hair strands
c.set(29, 5, HAIR_H); c.set(32, 4, HAIR_H); c.set(35, 5, HAIR_H)
c.set(28, 26, OUTFIT_H)
c.set(18, 20, BOW_H)
c.set(15, 33, BOW_H)
c.set(21, 40, HAIR_L); c.set(22, 42, HAIR_L)
c.set(42, 36, HAIR_L); c.set(41, 38, HAIR_L)

# 15. outline pass (soft ground shadow stays un-outlined)
for y in range(64):
    for x in range(64):
        idx = c.get(x, y)
        if idx == 0 or idx == SHADOW:
            continue
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= 64 or ny < 0 or ny >= 64 or c.get(nx, ny) == 0:
                c.set(x, y, OUT)
                break

# 16. nudge everything right so the bow is not flush with the edge
c.shift(3, 0)

print(c.stats_text())
print("COLORS:", len(c.palette()))
print(c.matrix_text(region=(2, 0, 54, 34)))
print(c.matrix_text(region=(2, 34, 54, 62)))
finish(c)
