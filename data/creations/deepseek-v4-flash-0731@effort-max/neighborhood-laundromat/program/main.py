from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64)

# ---------------- palette ----------------
wall     = (186,200,213)
wall_sh  = (166,181,195)
ceil     = (205,218,231)
blast    = (182,196,210)
floor_l  = (152,166,179)
floor_d  = (140,154,168)
fline    = (126,140,154)
shadow   = (112,128,144)
mach     = (233,237,241)
mach_sh  = (205,213,221)
mach_out = (134,148,162)
glass    = (42,58,76)
glint    = (154,188,214)
dispd    = (24,36,50)
tube     = (243,252,255)
fixture  = (146,162,178)
clockb   = (86,100,114)
clockw   = (240,245,250)
hand     = (56,66,80)
second   = (206,80,70)
b_light  = (194,144,94)
b_mid    = (170,116,72)
b_dark   = (136,88,52)
wood_l   = (218,188,148)
wood     = (176,142,102)
wood_d   = (156,122,84)
cl_white = (242,246,250)
cl_blue  = (84,124,186)
cl_red   = (196,86,76)
cl_green = (96,158,118)
cl_yel   = (226,184,72)

acc1 = (70,130,200)
acc2 = (58,160,140)
acc3 = (224,148,58)
acc4 = (196,88,88)
acc5 = (148,92,188)
acc6 = (70,130,200)

# ---------------- background ----------------
c.rect(0,0,64,64,wall)
c.rect(0,0,64,9,ceil)                 # ceiling
c.rect(5,9,54,3,blast)                # cool light wash on upper wall
c.rect(0,9,64,1,wall_sh)
c.rect(0,10,2,34,wall_sh)
c.rect(62,10,2,34,wall_sh)

for px in (3,23,43):                   # recessed fluorescent fixtures
    c.rect(px,1,18,4,fixture)
    c.rect(px+2,2,14,2,tube)

# ---------------- tiled floor ----------------
for ty,(yy,hh) in enumerate(((44,8),(52,8),(60,4))):
    for tx in range(8):
        if (tx+ty) % 2 == 1:
            c.rect(tx*8, yy, 8, hh, floor_d)
for x in range(0,64,8):
    c.line(x,44,x,63,fline)
c.line(63,52,63,63,fline)
c.line(0,52,64,52,fline)
c.line(0,60,64,60,fline)

# floor shadows under objects
for mx in (3,23,43):
    c.rect(mx,44,18,1,shadow)
c.rect(7,54,8,1,shadow)
c.rect(41,57,16,1,shadow)

# ---------------- machines ----------------
def machine(x, y, accent, load=None):
    c.rect(x, y, 18, 12, mach)
    c.rect(x+1, y+1, 16, 1, mach_sh)
    c.rect(x+1, y+10, 16, 2, mach_sh)
    c.rect(x, y, 18, 12, mach_out, fill=False)
    cx, cy = x+7, y+6
    c.circle(cx, cy, 4, accent)          # door ring
    c.circle(cx, cy, 3, glass)          # porthole
    c.set(cx-2, cy-2, glint)
    c.set(cx-1, cy-2, glint)
    c.set(cx-2, cy-1, glint)
    if load is not None:
        c.set(cx, cy+1, load)
        c.set(cx-1, cy+1, load)
    c.rect(cx+6, y+3, 3, 2, dispd)      # display
    c.set(cx+9, y+5, accent)             # lit indicator

machine(3,  19, acc1, cl_white)
machine(23, 19, acc2, None)
machine(43, 19, acc3, cl_red)
machine(3,  32, acc4, None)
machine(23, 32, acc5, cl_white)
machine(43, 32, acc6, cl_blue)

# ---------------- wall clock ----------------
c.text(6, 12, "24H", clockb)
c.circle(32, 13, 4, clockb)
c.circle(32, 13, 3, clockw)
c.line(32, 13, 32, 11, hand)
c.line(32, 13, 34, 13, hand)
c.line(32, 13, 29, 15, second)

# ---------------- laundry basket ----------------
c.rect(8, 45, 2, 1, cl_blue)            # clothes peeking out
c.rect(11, 45, 2, 1, cl_yel)
c.rect(9, 46, 3, 1, cl_red)
c.rect(6, 47, 8, 1, b_light)            # rim
c.poly([(6,48),(14,48),(12,54),(8,54)], b_mid)
c.poly([(6,48),(14,48),(12,54),(8,54)], b_dark, fill=False)
c.rect(8, 48, 2, 1, cl_green)           # cloth draped over rim
c.rect(7, 49, 6, 1, b_dark)             # weave
c.rect(8, 51, 4, 1, b_dark)
c.rect(9, 53, 2, 1, b_dark)

# ---------------- folding table ----------------
c.rect(40, 50, 18, 2, wood_l)           # top
c.rect(40, 52, 18, 2, wood)
c.rect(44, 54, 12, 2, wood_d)           # front apron
c.rect(42, 50, 2, 7, wood_d)            # legs
c.rect(54, 50, 2, 7, wood_d)
c.rect(43, 47, 7, 1, cl_yel)            # folded stack
c.rect(43, 48, 7, 1, cl_white)
c.rect(43, 49, 7, 1, cl_blue)
c.rect(45, 50, 6, 1, cl_white)          # towel over edge
c.rect(54, 47, 3, 3, cl_red)            # detergent bottle
c.rect(55, 46, 1, 1, cl_blue)

print(c.stats_text())
print("--- machines ---")
print(c.matrix_text(region=(0,16,63,46)))
print("--- clock ---")
print(c.matrix_text(region=(6,9,53,18)))
print("--- table ---")
print(c.matrix_text(region=(36,43,63,60)))
finish(c)
