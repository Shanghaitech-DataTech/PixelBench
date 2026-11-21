from pixelbench_api import *
import random

C = new_canvas(64, 64)

def R(h): return C.color(h)

# ---- palette ----
night    = R("#0b1133")
sky      = R("#0e153f")
dist     = R("#0f1538")
dbuild   = R("#151b3c")
dbwin    = R("#b8c89a")
build    = R("#332a44")
buildl   = R("#463a58")
sign     = R("#a8e8f0")
signtxt  = R("#18304c")
awning_d= R("#1c1c2c")
awnr     = R("#c04a52")
awnw     = R("#e8e0d8")
awnsh    = R("#7c3038")
gwarm    = R("#ffd868")
gbright  = R("#ffe9a8")
gshadow = R("#d8a850")
glare    = R("#fff6cc")
shelf    = R("#b8843c")
# product accent colors stored to reuse
R("#e86848"); R("#3aa06a"); R("#3a78c8"); R("#3a78c8")
prodA = R("#e86848"); prodB = R("#3aa06a"); prodC = R("#3a88c8")
frame   = R("#241c30")
dglass  = R("#ffcf5c")
handle  = R("#d8bc7c")
sidew   = R("#8a8894")
sidewarm= R("#c8b080")
doorlit = R("#e8c868")
street  = R("#20242e")
streetL = R("#3c3844")
puddle  = R("#3a4a6a")
prefl   = R("#d8a848")
gamerefl= R("#8ac8e8")
ripple  = R("#9ab8d8")
rain    = R("#7aa4cc")
rainb   = R("#b8d4ec")
lamp    = R("#16161e")
lamph   = R("#c8e8ec")
ub      = R("#3a88c8")
ug      = R("#3aa06a")
ur      = R("#c84a4a")
rackd   = R("#2c2438")
ubar    = R("#d8d0a8")
rdark   = R("#3a2a34")
coat    = R("#ffd23c")
coats   = R("#d8a828")
hood    = R("#e8b828")
face    = R("#8a6040")
boot    = R("#3a3a44")
bik     = R("#e07a34")
bikd    = R("#b05a20")
wheelc  = R("#26303c")
cub     = R("#a0a8b8")

# ---- background ----
C.rect(0, 0, 64, 64, night)

# distant city silhouettes on right
C.rect(50, 20, 7, 24, dist)
C.rect(50, 22, 7, 1, dbuild)
C.rect(59, 16, 5, 28, dist)
C.rect(59, 18, 5, 1, dbuild)
# distant lit windows
for wx, wy in [(51,30),(53,36),(60,26),(62,32)]:
    C.set(wx, wy, dbwin); C.set(wx+1, wy, dbwin); C.set(wx, wy+1, dbwin)

# faint ground base beneath far area
C.rect(49, 44, 15, 20, night)

# ---- store wall ----
C.rect(3, 5, 45, 40, build)          # wall x=3..47, y=5..44
C.rect(3, 5, 45, 1, buildl)          # parapet top

# neon sign
C.rect(16, 6, 20, 6, sign)           # sign box x=16..35, y=6..11
C.text(20, 8, "24H", signtxt)

# awning
C.rect(2, 12, 47, 2, awning_d)        # canopy underside y=12..13
for i in range(2, 48, 8):
    C.rect(i, 12, 4, 1, awnr)         # front stripes red band
    C.rect(i+4, 12, 4, 1, awnw)       # white band
    C.rect(i, 13, 4, 1, awnsh)
    C.rect(i+4, 13, 4, 1, awnw)
    C.rect(i+2, 13, 2, 1, awnr)        # scallop bump
    C.rect(i+6, 13, 2, 1, awnw)

# ---- left window ----
C.rect(5, 14, 16, 22, gwarm)          # interior x=5..20, y=14..35
C.rect(5, 15, 16, 2, gbright)        # bright ceiling light band
C.rect(5, 20, 16, 2, gshadow)        # shelving shadow
C.rect(5, 26, 16, 2, shelf)
C.rect(5, 32, 16, 2, shelf)
# product silhouettes on shelves
for px in (6,9,12,15,18):
    C.set(px, 22, prodA); C.set(px, 23, prodA)
    C.set(px, 29, prodB); C.set(px, 30, prodB)
# glare streaks on glass
C.line(7, 14, 12, 5, glare)
C.line(5, 20, 10, 16, gbright)

# ---- right window ----
C.rect(32, 14, 14, 22, gwarm)
C.rect(32, 15, 14, 2, gbright)
C.rect(32, 20, 14, 2, gshadow)
C.rect(32, 26, 14, 2, shelf)
C.rect(32, 32, 14, 2, shelf)
for px in (34,38,42):
    C.set(px, 29, prodC); C.set(px, 30, prodC)
C.line(34, 14, 40, 5, glare)
C.line(44, 14, 46, 24, gbright)

# ---- door ----
C.rect(22, 16, 9, 29, frame)          # door frame x=22..30, y=16..44
C.rect(22, 16, 9, 1, buildl)
C.rect(23, 17, 7, 27, dglass)         # door glass
C.rect(23, 26, 7, 1, gshadow)
C.rect(25, 17, 1, 27, gshadow)        # divider
C.rect(29, 32, 1, 4, handle)
C.rect(23, 17, 7, 3, gbright)

# ---- sidewalk / street ----
C.rect(0, 44, 64, 7, night)           # fill lane
C.rect(0, 46, 64, 5, sidew)           # sidewalk y=46..50
C.rect(3, 46, 45, 5, sidewarm)        # store-lit patch of walk y46..50
C.rect(0, 51, 64, 13, street)         # street y=51..63
C.rect(24, 47, 7, 3, doorlit)         # doorway light spill on walk
C.rect(33, 45, 6, 6, sidewarm)
# low wall base shadow
C.rect(3, 44, 45, 2, build)

# ---- puddles ----
C.rect(2, 48, 60, 16, street)
# big street puddle
C.ellipse(27, 57, 19, 5, puddle)      # across street under store
C.ellipse(52, 59, 8, 4, puddle)       # puddle under lamplight
C.ellipse(30, 48, 16, 2, puddle)      # sidewalk puddle
# reflections in street puddle
for rx in (10, 24, 38):
    C.rect(rx, 54, 4, 3, prefl)
    C.rect(rx, 58, 4, 2, prefl)
C.rect(40, 54, 4, 2, prefl)
C.rect(49, 58, 6, 1, gamerefl)
# ripple rings
C.circle(24, 58, 2, ripple, fill=False)
C.circle(38, 55, 2, ripple, fill=False)
C.circle(53, 56, 2, ripple, fill=False)
C.circle(15, 58, 2, ripple, fill=False)

# lamp light pool already via streetL? draw glow near pole
# ---- streetlamp ----
C.rect(56, 22, 2, 30, lamp)           # pole x=56..57, y=22..51
C.rect(54, 20, 6, 2, lamph)           # lamp head
C.rect(55, 21, 4, 1, lamp)
C.ellipse(56, 56, 6, 3, streetL)      # lamp pool
C.rect(52, 57, 10, 1, lamph)

# ---- umbrella rack (left of door) ----
C.rect(19, 30, 2, 13, rackd)          # umbrella bodies holder x=19..20
C.rect(19, 41, 3, 2, rackd)          # base
C.rect(17, 30, 2, 12, ub)             # third umbrella
C.rect(17, 29, 2, 1, ub)
C.rect(17, 40, 2, 1, ub)
C.rect(19, 33, 2, 3, ug)              # green umbrella mid

# ---- bicycle (right, leaning on wall) ----
C.circle(37, 47, 3, wheelc)
C.circle(44, 47, 3, wheelc)
C.circle(37, 47, 1, cub)
C.circle(44, 47, 1, cub)
C.line(37, 47, 44, 43, bik)           # top tube
C.line(37, 47, 40, 43, bik)           # seat tube
C.line(40, 43, 44, 45, bik)           # front fork
C.line(44, 47, 43, 44, bik)
C.line(37, 45, 42, 43, bikd)
C.rect(39, 42, 3, 1, bikd)            # seat
C.rect(44, 41, 1, 3, bikd)            # handlebar stem
C.rect(45, 40, 2, 1, bikd)            # handlebar
C.rect(41, 47, 2, 1, bikd)            # pedal / stand
C.line(37, 47, 35, 49, bikd)          # kickstand
# spokes
C.line(38, 45, 36, 49, rackd)
C.line(43, 45, 45, 49, rackd)

# ---- person in raincoat entering door ----
# umbrella above
C.ellipse(26, 26, 7, 3, ur)           # open umbrella tilted
C.line(26, 28, 27, 33, rain)          # pole to hand
C.line(27, 33, 27, 34, rain)
# boots
C.rect(25, 41, 2, 3, boot)
C.rect(28, 41, 2, 3, boot)
# raincoat legs
C.rect(25, 39, 2, 2, coats)
C.rect(28, 39, 2, 2, coat)
# coat body
C.rect(25, 32, 5, 7, coat)
C.rect(25, 31, 6, 5, coat)            # shoulders
C.rect(24, 27, 4, 5, hood)            # hood/back
C.rect(26, 29, 4, 3, face)            # open front
C.rect(28, 27, 3, 5, hood)
C.rect(26, 27, 3, 5, coats)           # hood top
# arm holding umbrella
C.rect(27, 32, 2, 3, coat)
C.line(25, 34, 28, 34, coat)

# ---- rain streaks over scene ----
rng = random.Random(11)
for _ in range(60):
    x = rng.randrange(0, 63)
    y = rng.randrange(0, 61)
    col = rain if rng.random() < 0.7 else rainb
    if rng.random() < 0.6:
        C.line(x, y, x, y+2, col)
    else:
        C.line(x, y, x+1, y+1, col)

result = C
print(C.stats_text())
print("colors_used:", C.stats()["colors_used"])

print(C.matrix_text(region=(18,16,34,44), indices=False))

print(C.matrix_text(region=(0,44,63,63), indices=False))

finish(result)
