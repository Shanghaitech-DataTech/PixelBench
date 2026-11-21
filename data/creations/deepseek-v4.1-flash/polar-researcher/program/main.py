from pixelbench_api import *

W = H = 48
c = new_canvas(W, H, name="polar_researcher")

OUT    = c.color("#12181f", name="outline")
NAVY   = c.color("#1e3050", name="navy")
BLUE   = c.color("#2f5487", name="blue")
MBLUE  = c.color("#3f6ea3", name="mblue")
LBLUE  = c.color("#5c93c4", name="lblue")
PALE   = c.color("#96c8e8", name="pale")
WHITE  = c.color("#dff1fd", name="white")
GLASS  = c.color("#b9e4f8", name="glass")
FUR    = c.color("#e9e3cf", name="fur")
FURD   = c.color("#bcb49b", name="furd")
SKIN   = c.color("#d5a07c", name="skin")
SKIND  = c.color("#a97656", name="skind")
PANTS  = c.color("#2b3345", name="pants")
PANTSL = c.color("#3d475d", name="pantsl")
BOOT   = c.color("#39424f", name="boot")
BOOTL  = c.color("#525d6d", name="bootl")
CASE   = c.color("#6a4f33", name="case")
CASEL  = c.color("#8a6b47", name="casel")
CASED  = c.color("#42301d", name="cased")
METAL  = c.color("#9aa6b2", name="metal")
SCARF  = c.color("#b8402c", name="scarf")
SCARFL = c.color("#dd7048", name="scarfl")

MAP = {OUT: '#', NAVY: 'n', BLUE: 'b', MBLUE: 'm', LBLUE: 'l', PALE: 'p',
       WHITE: 'W', GLASS: 'g', FUR: 'f', FURD: 'F', SKIN: 's', SKIND: 'S',
       PANTS: 't', PANTSL: 'T', BOOT: 'o', BOOTL: 'O', CASE: 'c', CASEL: 'C',
       CASED: 'd', METAL: 'v', SCARF: 'r', SCARFL: 'R'}


def dump(canvas, x0=0, y0=0, x1=47, y1=47):
    pal = {p['index']: p['rgba'] for p in canvas.palette()}
    print('    ' + ''.join(str(x % 10) for x in range(x0, x1 + 1)))
    for y in range(y0, y1 + 1):
        row = ''
        for x in range(x0, x1 + 1):
            i = canvas.get(x, y)
            rgba = pal.get(i)
            if rgba is None or rgba[3] == 0:
                row += '.'
            else:
                row += MAP.get(i, '*')
        print('%3d ' % y + row)


def band(pts, colour, th):
    for i in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        for k in range(th):
            c.line(x0, y0 + k, x1, y1 + k, colour)


# ================================================================ scarf tails
band([(27, 15), (19, 13), (11, 11), (5, 9)], SCARF, 3)
band([(27, 15), (19, 13), (11, 11), (5, 9)], SCARFL, 1)
band([(27, 19), (19, 18), (11, 16), (6, 14)], SCARF, 2)
band([(27, 19), (19, 18), (11, 16), (6, 14)], SCARFL, 1)

# ================================================================ legs
c.poly([(18, 32), (22, 32), (21, 41), (16, 41)], PANTS, fill=True)   # back leg
c.poly([(25, 32), (30, 32), (30, 41), (26, 41)], PANTS, fill=True)   # front leg
c.poly([(18, 32), (20, 32), (19, 41), (16, 41)], PANTSL, fill=True)

# ================================================================ boots
c.rect(16, 40, 6, 2, BOOT)       # back ankle
c.rect(25, 40, 6, 2, BOOT)       # front ankle
c.rect(12, 42, 11, 3, BOOT)      # back foot
c.rect(24, 42, 10, 3, BOOT)      # front foot
c.rect(12, 42, 11, 1, BOOTL)
c.rect(24, 42, 10, 1, BOOTL)
c.rect(12, 44, 11, 1, OUT)
c.rect(24, 44, 10, 1, OUT)

# ================================================================ torso parka
TORSO = [(22, 18), (33, 18), (36, 24), (34, 30), (30, 33), (18, 33), (16, 28), (17, 22)]
c.poly(TORSO, MBLUE, fill=True)
# back shade
c.poly([(22, 18), (20, 19), (17, 22), (16, 28), (18, 33), (21, 33), (20, 27), (21, 21)],
       BLUE, fill=True)
# bottom shade
c.poly([(18, 33), (30, 33), (30, 30), (19, 30)], BLUE, fill=True)
# shoulder rim light
c.line(27, 19, 31, 19, LBLUE)
# chest pocket
c.rect(23, 21, 4, 4, BLUE)
c.rect(23, 21, 4, 1, NAVY)
# zipper
c.line(28, 19, 26, 30, NAVY)
c.set(27, 24, METAL)
# belt
c.rect(19, 30, 12, 2, NAVY)
c.rect(25, 30, 2, 2, METAL)

# ================================================================ case + handle
c.rect(36, 30, 6, 1, OUT)
c.rect(36, 30, 1, 3, OUT)
c.rect(41, 30, 1, 3, OUT)
c.rect(34, 33, 10, 7, CASE)
c.rect(34, 33, 10, 2, CASEL)
c.rect(34, 38, 10, 1, CASED)
c.rect(38, 35, 2, 4, CASED)
c.rect(38, 35, 2, 2, METAL)
c.rect(34, 39, 10, 1, OUT)

# ================================================================ front arm
c.poly([(32, 19), (36, 20), (38, 22), (38, 25), (34, 25), (32, 22)], BLUE, fill=True)
c.poly([(34, 20), (36, 20), (38, 22), (37, 23), (34, 22)], MBLUE, fill=True)
c.line(32, 21, 33, 25, NAVY)

# ================================================================ mitten
c.rect(34, 23, 5, 2, FUR)
c.rect(37, 25, 2, 1, BOOT)
c.rect(36, 26, 4, 3, BOOT)
c.rect(37, 29, 2, 1, BOOT)
c.set(37, 26, BOOTL)
c.set(40, 27, BOOT)

# ================================================================ head / hood
c.ellipse(29, 11, 8, 6, BLUE)
c.ellipse(26, 8, 4, 2, MBLUE)
c.ellipse(29, 12, 6, 5, FUR)
c.ellipse(30, 12, 4, 4, NAVY)
c.ellipse(30, 12, 4, 4, SKIN)
# goggle strap
c.rect(21, 11, 5, 1, NAVY)
c.rect(34, 11, 4, 1, NAVY)
# goggles
c.rect(26, 10, 9, 4, OUT)
c.rect(27, 11, 7, 2, GLASS)
c.rect(30, 11, 1, 2, OUT)
c.set(28, 11, WHITE)
c.set(33, 11, WHITE)
c.set(27, 12, PALE)
c.set(32, 12, PALE)
c.set(29, 12, PALE)
# cheek shade
c.set(33, 14, SKIND)
c.set(32, 14, SKIND)
# fur shading
c.line(23, 14, 24, 16, FURD)
c.line(35, 13, 35, 15, FURD)
c.set(24, 10, FURD)
c.set(24, 11, FURD)

# ================================================================ scarf neck wrap
c.poly([(26, 15), (34, 15), (34, 18), (30, 19), (26, 18)], SCARF, fill=True)
c.poly([(27, 15), (33, 15), (33, 16), (27, 16)], SCARFL, fill=True)

dump(c)
print(c.stats_text())
save("polar_researcher", c)
finish(c)
