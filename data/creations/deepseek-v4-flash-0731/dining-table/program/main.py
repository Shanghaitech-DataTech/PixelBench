from pixelbench_api import new_canvas, finish

W = H = 64
c = new_canvas(W, H, name="dining-table")

def col(spec, name=None):
    return c.color(spec, name)

OUT   = col((26, 18, 12))
FLOOR = col((236, 214, 170))
FLOORL= col((222, 196, 150))
RUG   = col((178, 74, 63))
RUGD  = col((140, 54, 48))
RUGL  = col((242, 226, 192))
SHAD  = col((124, 52, 46))
WOODL = col((224, 164, 98))
WOODM = col((200, 136, 66))
WOODD = col((156, 94, 38))
GRAIN = col((122, 72, 28))
CW    = col((150, 90, 40))
SEAT1 = col((198, 112, 84))
SEAT1D= col((168, 88, 66))
SEAT2 = col((88, 126, 124))
SEAT2D= col((68, 102, 100))
PLATE = col((245, 238, 222))
RIM   = col((204, 194, 168))
BOWL  = col((240, 232, 214))
BSH   = col((220, 204, 174))
BAN   = col((240, 196, 56))
BAN2  = col((198, 148, 38))
ORG   = col((242, 154, 46))
ORG2  = col((198, 108, 30))
RED   = col((210, 58, 44))
RED2  = col((150, 36, 32))
GRN   = col((128, 176, 62))
GRN2  = col((92, 132, 44))
HIL   = col((255, 242, 214))

c.rect(0, 0, 64, 64, FLOOR)
for y in range(4, 64, 8):
    c.line(0, y, 63, y, FLOORL)
for x in range(4, 64, 16):
    c.line(x, 0, x, 63, FLOORL)

c.circle(32, 32, 28, OUT)
c.circle(32, 32, 26, RUG)
c.circle(32, 32, 23, RUGL)
c.circle(32, 32, 21, RUG)
c.circle(32, 32, 18, RUGL, fill=False)
for cx, cy in ((8, 8), (56, 8), (8, 56), (56, 56)):
    c.set(cx, cy, RUGD)

c.ellipse(32, 33, 19, 18, SHAD)

c.rect(24, 5, 16, 4, OUT); c.rect(25, 6, 14, 2, CW)
c.rect(24, 8, 16, 10, OUT); c.rect(25, 9, 14, 8, SEAT1)
c.rect(26, 10, 12, 6, SEAT1D, fill=False)
c.rect(24, 46, 16, 10, OUT); c.rect(25, 47, 14, 8, SEAT2)
c.rect(26, 48, 12, 6, SEAT2D, fill=False)
c.rect(24, 56, 16, 4, OUT); c.rect(25, 57, 14, 2, CW)
c.rect(3, 24, 4, 16, OUT); c.rect(4, 25, 2, 14, CW)
c.rect(6, 24, 10, 16, OUT); c.rect(7, 25, 8, 14, SEAT2)
c.rect(8, 26, 6, 12, SEAT2D, fill=False)
c.rect(48, 24, 10, 16, OUT); c.rect(49, 25, 8, 14, SEAT1)
c.rect(50, 26, 6, 12, SEAT1D, fill=False)
c.rect(58, 24, 4, 16, OUT); c.rect(59, 25, 2, 14, CW)

c.rect(16, 19, 32, 26, OUT)
for cx, cy in ((20, 23), (43, 23), (20, 40), (43, 40)):
    c.circle(cx, cy, 4, OUT)
c.rect(17, 20, 30, 24, WOODL)
for cx, cy in ((20, 23), (43, 23), (20, 40), (43, 40)):
    c.circle(cx, cy, 3, WOODL)
for y in (23, 29, 35, 41):
    c.line(17, y, 46, y, WOODM)
c.rect(18, 21, 28, 22, WOODD, fill=False)
c.circle(24, 27, 3, GRAIN, fill=False)
c.circle(39, 37, 3, GRAIN, fill=False)
c.line(40, 26, 44, 25, GRAIN)
c.line(20, 37, 23, 38, GRAIN)

for px, py in ((21, 22), (43, 22), (21, 39), (43, 39)):
    c.circle(px, py, 2, OUT)
    c.circle(px, py, 1, PLATE)
    c.set(px, py, RIM)

c.circle(32, 32, 8, OUT)
c.ellipse(32, 32, 7, 6, BOWL)
c.ellipse(32, 32, 6, 5, BSH, fill=False)
c.ellipse(29, 28, 3, 2, BAN)
c.set(26, 29, BAN2); c.set(32, 27, BAN2)
c.circle(28, 33, 2, OUT); c.circle(28, 33, 1, ORG)
c.set(27, 32, ORG2); c.set(27, 32, HIL)
c.circle(35, 32, 2, OUT); c.circle(35, 32, 1, RED)
c.set(36, 33, RED2); c.set(34, 32, HIL)
c.set(35, 29, GRN)
c.circle(32, 36, 2, OUT); c.circle(32, 36, 1, GRN)
c.set(31, 37, GRN2); c.set(32, 35, HIL)
c.set(34, 37, BAN2)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63)))
finish(c)
