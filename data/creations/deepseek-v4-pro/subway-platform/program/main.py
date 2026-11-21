from pixelbench_api import *

W, H = 64, 64

# ---- palette ----
CEIL      = '#0a0c11'
WALL      = '#161a23'
WALL_TOP  = '#202636'
SIGN      = '#10131c'
ACCENT_R  = '#e0483a'
ACCENT_C  = '#3fa7d8'
SIGN_TXT  = '#cfd8e6'
T_ROOF    = '#32485c'
T_BODY    = '#243a4e'
T_BODY_D  = '#162534'
T_WIN     = '#eaf6fc'
T_WIN_DIM = '#9fc6d8'
T_DIV     = '#1b2c3c'
STREAK    = '#ffffff'
HEADLIGHT = '#fff3c2'
D_FRAME   = '#2b303b'
D_GLASS   = (138, 194, 214, 72)
D_HL      = (232, 248, 255, 96)
FLOOR     = '#6b665e'
FLOOR_FAR = '#7d7870'
FLOOR_D   = '#4e4a44'
JOINT     = '#3a3733'
YELLOW    = '#e6b32c'
YELLOW_D  = '#c08f1f'
BENCH_M   = '#32363f'
BENCH_W   = '#9c6b46'
P1        = '#131a25'
P2        = '#1a222f'
P3        = '#2c3a52'
PHONE     = '#c4ecff'
BAG       = '#8a4a34'

# ---- layers ----
bg    = new_canvas(W, H, name='bg')
train = new_canvas(W, H, name='train')
doors = new_canvas(W, H, name='doors')
floor = new_canvas(W, H, name='floor')
fg    = new_canvas(W, H, name='fg')

# ---------- background: tunnel wall + ceiling + station signs ----------
bg.rect(0, 0, W, H, WALL)
bg.rect(0, 0, W, 4, CEIL)
bg.rect(0, 4, W, 8, WALL_TOP)

# left sign (abstract, no brand name)
bg.rect(6, 5, 18, 7, SIGN)
bg.rect(6, 5, 18, 1, ACCENT_R)
bg.rect(8, 7, 9, 1, SIGN_TXT)
bg.rect(8, 9, 13, 1, SIGN_TXT)
bg.rect(8, 10, 6, 1, SIGN_TXT)

# right sign
bg.rect(38, 5, 20, 7, SIGN)
bg.rect(38, 5, 20, 1, ACCENT_C)
bg.rect(40, 7, 11, 1, SIGN_TXT)
bg.rect(40, 9, 8, 1, SIGN_TXT)

# ---------- train (arriving, moving right, front cab on right) ----------
train.rect(0, 14, W, 3, T_ROOF)
train.rect(0, 17, W, 26, T_BODY)
train.rect(0, 43, W, 3, T_BODY_D)

# bright window band with vertical dividers
train.rect(0, 19, W, 15, T_WIN)
for x in range(6, 46, 8):
    train.rect(x, 19, 2, 15, T_DIV)
# a couple of dim windows suggest blur
train.rect(20, 19, 4, 15, T_WIN_DIM)
train.rect(36, 19, 3, 15, T_WIN_DIM)

# front cab at right: dark body + slanted windshield facing right
train.rect(46, 17, 17, 29, T_BODY_D)
train.poly([(46, 19), (46, 33), (61, 33), (53, 19)], T_WIN)
train.rect(60, 22, 2, 2, HEADLIGHT)

# horizontal speed streaks
for y, x0, x1 in [(21, 2, 18), (24, 10, 32), (27, 4, 20), (31, 14, 42), (38, 12, 54), (41, 26, 60)]:
    train.line(x0, y, x1, y, STREAK)

# ---------- platform screen doors ----------
DOOR_TOP, DOOR_BOT = 13, 46
posts = [2, 17, 32, 47, 62]
doors.rect(2, DOOR_TOP, 60, 2, D_FRAME)          # top rail
doors.rect(2, 34, 60, 2, D_FRAME)                # mid rail
doors.rect(2, DOOR_BOT, 60, 2, D_FRAME)          # bottom rail
for x in posts:
    doors.rect(x, DOOR_TOP, 2, DOOR_BOT - DOOR_TOP + 1, D_FRAME)

for i in range(4):
    gx = posts[i] + 2
    gw = posts[i + 1] - posts[i] - 2
    doors.rect(gx, 15, gw, 19, D_GLASS)          # upper glass
    doors.rect(gx, 36, gw, 10, D_GLASS)          # lower glass
    doors.rect(gx + 1, 16, 1, 16, D_HL)          # highlight
    doors.rect(gx + 1, 37, 1, 8, D_HL)

# ---------- platform floor with perspective ----------
floor.rect(0, 47, W, 2, YELLOW)
floor.rect(0, 47, W, 1, YELLOW_D)
for x in range(4, 64, 8):
    floor.rect(x, 48, 2, 1, YELLOW_D)
floor.rect(0, 49, W, 15, FLOOR)
floor.rect(0, 49, W, 1, FLOOR_D)
floor.rect(0, 50, W, 3, FLOOR_FAR)
for y in [53, 56, 59, 62]:
    floor.line(0, y, W - 1, y, JOINT)

vp = (32, 40)
for xb in [0, 12, 24, 36, 48, 63]:
    xi = xb + (vp[0] - xb) * 14.0 / 23.0
    floor.line(xb, 63, int(round(xi)), 49, JOINT)

# ---------- foreground: bench + three passengers ----------
# bench
fg.rect(6, 42, 20, 1, BENCH_M)   # backrest bar
fg.rect(8, 43, 1, 5, BENCH_M)
fg.rect(23, 43, 1, 5, BENCH_M)
fg.rect(6, 48, 20, 2, BENCH_W)   # seat
fg.rect(8, 50, 2, 7, BENCH_M)
fg.rect(22, 50, 2, 7, BENCH_M)

# passenger 2: sitting on bench, facing right (near)
c = fg
col = P2
c.ellipse(13, 33, 2, 2, col)   # head y31..35
c.rect(12, 36, 5, 9, col)      # torso y36..44
c.rect(12, 45, 7, 2, col)      # thigh y45..46
c.rect(18, 47, 2, 9, col)      # lower leg y47..55
c.rect(17, 56, 4, 2, col)      # shoe y56..57
c.rect(12, 38, 4, 1, col)      # arm on lap

# passenger 1: standing, facing left, looking at phone (near)
col = P1
c.ellipse(29, 29, 2, 2, col)   # head y27..31
c.rect(26, 32, 7, 13, col)     # torso y32..44
c.rect(27, 45, 2, 12, col)     # front leg y45..56
c.rect(30, 45, 2, 12, col)     # back leg
c.rect(26, 57, 4, 2, col)      # front shoe
c.rect(29, 57, 4, 2, col)      # back shoe
c.rect(25, 34, 2, 1, col)      # upper arm
c.rect(24, 34, 1, 5, col)      # forearm
c.rect(23, 36, 2, 4, PHONE)    # phone glow

# passenger 3: walking far side, smaller (depth), carrying bag
col = P3
c.ellipse(53, 41, 2, 1, col)   # head y40..42
c.rect(51, 43, 5, 7, col)      # torso y43..49
c.rect(54, 50, 2, 4, col)      # front leg y50..53
c.rect(50, 50, 2, 4, col)      # back leg
c.rect(55, 54, 4, 1, col)      # front shoe
c.rect(48, 54, 4, 1, col)      # back shoe
c.rect(56, 45, 3, 1, col)      # arm
c.rect(58, 46, 2, 2, BAG)      # bag

# ---------- composite ----------
result = flatten([bg, train, doors, floor, fg], name='subway')

print(result.stats_text())
print(result.matrix_text(region=(0, 0, 63, 63), indices=False))

finish(result)
