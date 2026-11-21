from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64, name="subway_platform")

def col(spec):
    return c.color(spec)

# ---------------- palette
TUNNEL   = col("#141828")   # deep tunnel background
CEIL     = col("#202538")  # ceiling beam
LIGHT    = col("#ffdf9e")  # overhead lamp
HOT      = col("#fff6da")  # lamp hot core
SIGN_BG  = col("#0f1119")  # sign board
SIGN_TX  = col("#e9edf3")  # sign text
SIGN_AC  = col("#ff9d6b")  # sign accent
TRAIN    = col("#98a4ba")  # train body
TRAIN_D  = col("#748199")  # train dark
TRAIN_L  = col("#c3cbdd")  # train light streak
STRIPE   = col("#5c687d")  # train stripe
WIN      = col("#ffd784")  # lit window
WIN_D    = col("#c99f5e")  # window dim interior
STREAK   = col("#ffe9b0")  # window light streak
HEAD     = col("#fffdf0")  # headlight
GLOW     = col("#ffd87e")  # headlight glow
FRAME    = col("#333948")  # door frame
GLASS    = col("#4c6882")  # door glass
GLASS_L  = col("#7fa0b8")  # glass reflection
GLASS_D  = col("#3b5268")  # glass lower shade
PF       = col("#4a4f5e")  # platform floor
PF_L     = col("#585e6f")  # floor light
PF_D     = col("#3e4352")  # floor joints
STRIPY   = col("#e8b34a")  # safety strip
EDGE     = col("#232734")  # platform edge / cables
SHAD     = col("#2f2f3b")  # soft shadow
BENCH    = col("#5e7a72")  # bench
BENCH_D  = col("#3d5650")  # bench dark
BENCH_L  = col("#8fb2a6")  # bench highlight
SIL      = col("#12141c")  # passenger silhouettes

# ================= ceiling / tunnel band  (rows 0-11)
c.rect(0, 0, 64, 12, TUNNEL)
c.rect(0, 0, 64, 1, CEIL)

# overhead platform lights
for x in (3, 21, 39, 53):
    c.rect(x, 2, 5, 2, LIGHT)
    c.rect(x + 1, 3, 3, 1, HOT)

# hanging station signs (no brand names)
c.line(32, 1, 32, 3, EDGE)
c.line(48, 1, 48, 3, EDGE)
c.rect(26, 3, 30, 9, SIGN_BG)          # board rows 3-11
c.text(28, 4, "EXIT", SIGN_TX)
c.rect(30, 11, 18, 1, SIGN_AC)

# ================= train band arriving  (rows 12-33)
c.rect(0, 12, 64, 22, TRAIN)           # train body rows 12-33
c.rect(0, 12, 64, 2, TRAIN_D)          # roof
c.rect(0, 15, 64, 2, STRIPE)           # livery stripe
c.rect(0, 33, 64, 1, TRAIN_D)          # skirt shadow

for wx in (2, 10, 18, 26, 34, 42):     # lit windows
    c.rect(wx, 17, 6, 14, WIN)         # rows 17-30
    c.rect(wx, 24, 6, 7, WIN_D)        # interior depth
    c.rect(wx + 1, 19, 4, 1, STREAK)   # speed streak
    c.rect(wx + 2, 27, 3, 1, STREAK)

# front / nose of the arriving train (right)
c.rect(48, 15, 16, 1, STRIPE)
c.rect(48, 33, 16, 1, TRAIN_D)
c.rect(50, 17, 14, 2, TRAIN_D)          # windshield over the nose
c.rect(52, 19, 8, 8, GLOW)             # headlight glow
c.rect(55, 21, 4, 6, HEAD)
c.rect(60, 22, 4, 1, GLOW)             # light beam / motion
c.rect(61, 24, 3, 1, GLOW)
c.rect(60, 26, 4, 1, GLOW)
c.rect(52, 31, 12, 2, TRAIN_L)         # motion streaks on nose
c.rect(14, 32, 24, 1, TRAIN_L)

# ================= platform screen doors  (rows 34-41)
c.rect(0, 34, 64, 1, FRAME)            # top rail
c.rect(0, 41, 64, 1, FRAME)            # bottom rail
c.rect(0, 35, 64, 5, GLASS)            # glass rows 35-39
c.rect(0, 40, 64, 1, GLASS_D)          # glass lower shade
c.rect(0, 35, 64, 1, GLASS_L)          # glass top sheen
for px in (3, 11, 19, 27, 35, 43, 51, 59):
    c.rect(px, 35, 1, 7, FRAME)         # vertical posts
for px in (4, 12, 20, 28, 36, 44, 52):
    c.line(px + 1, 39, px + 6, 35, GLASS_L)
    c.line(px + 3, 39, px + 6, 36, GLASS_L)

# ================= platform  (rows 42-63)
c.rect(0, 42, 64, 22, PF)
c.rect(0, 42, 64, 1, EDGE)             # platform edge lip
c.rect(0, 43, 64, 2, STRIPY)           # yellow safety strip
for tx in range(0, 64, 8):
    c.line(tx, 45, tx, 59, PF_D)
c.line(0, 52, 63, 52, PF_D)
c.line(0, 60, 63, 60, PF_D)

# floor direction chevrons (speed cue)
c.rect(50, 57, 2, 1, PF_L)
c.rect(49, 58, 4, 1, PF_L)
c.rect(50, 59, 2, 1, PF_L)
c.rect(54, 57, 3, 1, PF_L)
c.rect(53, 58, 5, 1, PF_L)
c.rect(54, 59, 3, 1, PF_L)

# ================= bench (left)
c.rect(6, 48, 2, 6, BENCH)             # backrest
c.rect(5, 48, 2, 1, BENCH_L)           # backrest highlight
c.rect(6, 53, 18, 3, BENCH)            # seat rows 53-55
c.rect(8, 56, 2, 4, BENCH_D)           # legs
c.rect(20, 56, 2, 4, BENCH_D)
c.rect(6, 60, 20, 1, SHAD)              # bench shadow

# ================= passengers (three poses, readable silhouettes)
# 1) seated passenger on the bench
c.rect(12, 46, 3, 4, SIL)              # head
c.rect(12, 50, 5, 3, SIL)              # torso (rows 50-52)
c.rect(13, 53, 6, 2, SIL)              # thighs
c.rect(14, 55, 4, 2, SIL)              # shins
c.rect(17, 51, 2, 1, SIL)              # forearm
c.rect(15, 57, 4, 1, SIL)              # feet

# 2) standing passenger, waiting (arms folded)
c.rect(25, 45, 3, 4, SIL)              # head
c.rect(26, 49, 2, 6, SIL)              # torso rows 49-54
c.rect(24, 51, 2, 5, SIL)              # arm behind
c.rect(28, 50, 1, 3, SIL)              # arm front
c.rect(28, 53, 1, 2, SIL)
c.rect(26, 55, 1, 7, SIL)              # legs rows 55-61
c.rect(28, 55, 1, 6, SIL)
c.rect(26, 62, 3, 1, SIL)               # feet
c.rect(25, 62, 5, 1, SHAD)

# 3) walking passenger, striding right
c.rect(42, 45, 3, 4, SIL)              # head, leaning forward
c.rect(41, 49, 3, 5, SIL)              # torso rows 49-53
c.rect(39, 50, 2, 4, SIL)              # arm swung back
c.rect(45, 50, 1, 4, SIL)              # arm swung forward
c.rect(40, 54, 2, 4, SIL)              # back leg
c.rect(43, 54, 2, 7, SIL)              # front leg
c.rect(38, 58, 2, 1, SIL)              # back foot
c.rect(43, 61, 3, 1, SIL)              # front foot
c.rect(41, 62, 6, 1, SHAD)

# ---------------- report
print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 33)))
print(c.matrix_text(region=(0, 34, 63, 63)))

finish(c)
