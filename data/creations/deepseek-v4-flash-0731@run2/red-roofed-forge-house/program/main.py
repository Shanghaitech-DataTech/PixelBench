from pixelbench_api import new_canvas, finish
import random

rng = random.Random(11)
c = new_canvas(128, 128)

def reg(h, n):
    return c.color(h, n)

ground  = reg('#4A4030', 'ground')
gdark   = reg('#3A3225', 'gdark')
glite   = reg('#574B37', 'glite')
shadow  = reg('#262012', 'shadow')
wall    = reg('#D8B48C', 'wall')
wshade  = reg('#B98F62', 'wshade')
timber  = reg('#4A2E16', 'timber')
tdark   = reg('#301E0E', 'tdark')
roof_l  = reg('#9E2F1E', 'roof_l')
roof_r  = reg('#D2422B', 'roof_r')
rl_dark = reg('#7C2417', 'rl_dark')
rr_dark = reg('#A93420', 'rr_dark')
ridgec  = reg('#E8603C', 'ridgec')
gable   = reg('#6E4226', 'gable')
door    = reg('#3A2210', 'door')
doorf   = reg('#5C3A1E', 'doorf')
iron    = reg('#333333', 'iron')
fire_d  = reg('#A63A0E', 'fire_d')
fire_m  = reg('#E8621A', 'fire_m')
fire_b  = reg('#FFA02A', 'fire_b')
core    = reg('#FFEDB0', 'core')
glow    = reg('#B05014', 'glow')
gdim    = reg('#7E3A10', 'gdim')
brick   = reg('#8A4A2E', 'brick')
brick_d = reg('#65351F', 'brick_d')
brick_l = reg('#A85C3A', 'brick_l')
smoke   = reg('#9C9484', 'smoke')
smoke_l = reg('#C9C0AC', 'smoke_l')
sign    = reg('#7C5028', 'sign')
sigd    = reg('#553416', 'sigd')
cream   = reg('#EDD9AE', 'cream')
ban     = reg('#9E6A3C', 'ban')
bandd   = reg('#4E2F1A', 'bandd')
win     = reg('#FFB450', 'win')
stone   = reg('#6E6048', 'stone')

# ---- ground ----
c.rect(0, 0, 128, 128, ground)
for _ in range(470):
    c.set(rng.randrange(0, 128), rng.randrange(48, 128), gdark if rng.random() < 0.55 else glite)
for _ in range(30):
    c.set(rng.randrange(0, 128), rng.randrange(92, 128), stone)

# ---- early shadows & warm pool ----
c.rect(30, 120, 62, 8, shadow)               # shadow under the house front
c.poly([(88, 119), (113, 94), (115, 91), (90, 116)], shadow)
c.ellipse(19, 122, 9, 4, shadow)              # under barrels
c.ellipse(100, 121, 12, 5, shadow)            # under furnace
c.ellipse(100, 120, 20, 7, gdim)               # dim warm pool on the ground

# ---- house: side walls, front wall, gable ----
c.poly([(86, 58), (109, 35), (109, 101), (86, 124)], wshade)   # right side wall
c.poly([(34, 58), (57, 35), (57, 101), (34, 124)], gable)      # left side wall
c.rect(34, 58, 52, 66, wall)                                   # front wall
c.poly([(34, 58), (86, 58), (60, 36)], gable)                  # front gable

# ---- roof planes (clean 45-degree wedge) ----
c.poly([(86, 58), (60, 36), (83, 13), (109, 35)], roof_r)      # right roof plane
c.poly([(34, 58), (60, 36), (83, 13), (57, 35)], roof_l)       # left roof plane

# tile coursing (courses run across the slope, along lines of constant x+y)
for y in range(13, 59):
    for x in range(34, 110):
        p = c.get(x, y)
        if p == roof_l and (x - y) % 6 == 0:
            c.set(x, y, rl_dark)
        elif p == roof_r and (x + y) % 8 in (0, 1):
            c.set(x, y, rr_dark)

# timber beams on the gable
c.line(42, 50, 78, 50, tdark)
c.line(48, 43, 72, 43, tdark)

# roof dark outline (crisp RTS edge)
c.poly([(34, 58), (60, 36), (83, 13), (57, 35)], tdark, fill=False)
c.poly([(86, 58), (60, 36), (83, 13), (109, 35)], tdark, fill=False)
c.line(60, 36, 83, 13, ridgec)                # ridge highlight
c.rect(34, 123, 52, 1, tdark)                 # base trim
c.line(86, 123, 109, 100, timber)             # right corner edge

# ---- chimney on the roof ----
c.rect(67, 14, 15, 17, brick)
c.rect(65, 10, 19, 4, brick_d)
c.line(65, 10, 83, 10, brick_l)
c.rect(66, 14, 1, 17, brick_d)                # chimney shade side

# smoke wisp
c.rect(63, 6, 5, 5, smoke)
c.rect(57, 2, 6, 5, smoke)
c.rect(51, 0, 5, 4, smoke)
c.rect(45, 0, 4, 3, smoke_l)
c.rect(58, 4, 1, 1, smoke_l)
c.set(52, 3, smoke_l)
c.set(64, 8, smoke_l)

# ---- windows ----
c.rect(37, 71, 12, 14, tdark)
c.rect(38, 72, 10, 12, win)
c.line(43, 72, 43, 83, tdark)
c.line(38, 77, 47, 77, tdark)
c.rect(37, 84, 12, 1, timber)                 # sill
c.rect(73, 71, 12, 14, tdark)
c.rect(74, 72, 10, 12, win)
c.line(79, 72, 79, 83, tdark)
c.line(74, 77, 83, 77, tdark)
c.rect(73, 84, 12, 1, timber)

# ---- door ----
c.rect(46, 86, 28, 36, tdark)
c.rect(48, 88, 24, 34, door)
for sx in (52, 56, 60, 64, 68):
    c.line(sx, 88, sx, 121, tdark)
c.rect(46, 86, 3, 5, doorf)                   # frame top
c.rect(46, 88, 3, 2, doorf)
c.set(45, 90, iron)
c.rect(46, 94, 2, 6, iron)
c.rect(45, 92, 2, 1, iron)
c.rect(48, 122, 24, 2, stone)                 # door step

# ---- wooden sign ----
c.rect(10, 54, 24, 3, timber)
c.line(16, 56, 16, 60, iron)
c.line(28, 56, 28, 60, iron)
c.rect(6, 60, 30, 15, sigd)
c.rect(6, 60, 30, 2, sign)
c.text(10, 63, "FORGE", cream, font="5x7")

# ---- stacked barrels ----
# lower barrel
c.rect(14, 99, 14, 22, ban)
for bx in range(15, 28):
    c.set(bx, 119, bandd)
    c.set(bx, 120, bandd)
for sx in (16, 19, 22, 25):
    c.line(sx, 100, sx, 118, bandd)
c.rect(14, 104, 14, 3, bandd)
c.rect(14, 111, 14, 3, bandd)
c.rect(14, 98, 14, 2, brick_l)
# upper barrel
c.rect(14, 79, 14, 20, ban)
for sx in (16, 19, 22, 25):
    c.line(sx, 81, sx, 97, bandd)
c.rect(14, 85, 14, 3, bandd)
c.rect(14, 92, 14, 3, bandd)
c.rect(14, 77, 14, 2, brick_l)
c.ellipse(21, 78, 6, 2, ban)

# ---- furnace with glow ----
c.rect(90, 96, 20, 24, brick)
c.ellipse(100, 97, 10, 5, brick)
c.ellipse(100, 106, 10, 8, glow, fill=False)   # glow rim around the mouth
c.rect(94, 107, 12, 13, door)
c.rect(96, 107, 8, 13, fire_d)
c.rect(98, 109, 4, 11, fire_m)
c.rect(99, 111, 2, 3, fire_b)
c.ellipse(100, 121, 15, 5, glow)               # bright spill
c.rect(96, 115, 8, 5, fire_b)
c.rect(98, 117, 4, 3, core)
c.line(96, 118, 103, 118, tdark)               # grate bars
c.line(96, 120, 103, 120, tdark)
c.rect(90, 96, 20, 24, tdark, fill=False)
c.rect(90, 96, 20, 4, brick_l)
c.rect(95, 96, 10, 1, brick_l)                 # top lip highlight
c.rect(100, 120, 1, 3, fire_b)
c.rect(102, 122, 4, 1, fire_b)
c.rect(96, 122, 4, 1, fire_m)

print(c.stats_text())
print(c.stats())
finish(c)
