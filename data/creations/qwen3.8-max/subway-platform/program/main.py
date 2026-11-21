# Subway platform, side view, 64x64 -- train arriving behind platform screen doors.
# Three composited layers: bg (structure + train), fx (glass tint / headlight / speed), front (doors, platform, people).
# Palette budget: <=86 visible colours, so alpha overlays are few and deliberate.

W = H = 64

bg = new_canvas(W, H, background='#0a0c12', name="bg")
fx = new_canvas(W, H, name="fx")
fr = new_canvas(W, H, name="front")

# ---------------------------------------------------------------- palette (42 opaque)
VOID = '#0a0c12'
WALL = '#1c2333'; WALL2 = '#232c40'; WALLN = '#2c3750'
CEIL = '#151a27'
TUN2 = '#141b28'; TUN3 = '#101724'; TUN4 = '#0c111b'
MD = '#232b3c'; MM = '#333e55'; ML = '#4d5b78'; MH = '#6b7c9e'
BODY = '#cdd7e4'; BODY2 = '#a9b6c8'; SHADE = '#7d8a9e'; LOW = '#4a5568'
WIN = '#ffe3a1'; WARMHI = '#fff6d8'; WF = '#2b3a4d'
STR = '#2f7fbf'; STR2 = '#57a8dd'
FLOOR = '#333c4e'; FLOOR2 = '#2b3342'
TAC = '#c99a2e'; TACL = '#e8bd55'; TACD = '#8f6c1c'
FIG = '#141a26'; FIG2 = '#1d2635'; RIM = '#8fa8c8'
ACC = '#c0563f'; ACC2 = '#e07a5f'
BN = '#7d5735'; BNL = '#96693f'; BND = '#5d3f26'
SCRN = '#dff0ff'
SIGNBG = '#16233a'; SIGNBD = '#3d5f8c'; SIGNSD = '#2a4364'; SIGNTX = '#e8f2ff'
SIL2 = '#6f7f96'
GREEN = '#5fd07a'; AMBER = '#ff9d3c'

GLASS = (146, 194, 214, 52)      # screen-door glazing tint
CONE = (255, 236, 180, 64)       # headlight wash
GLOW = (255, 246, 208, 90)       # headlight bloom
STREAK = (255, 255, 255, 55)     # motion blur on the train tail

# ================================================================ BG LAYER
# ---- ceiling
bg.rect(0, 0, 64, 6, CEIL)
bg.rect(0, 5, 64, 1, WALL2)
for lx in (4, 26, 48):
    bg.rect(lx - 1, 1, 14, 1, MD)
    bg.rect(lx, 2, 12, 2, WIN)
    bg.rect(lx + 1, 2, 10, 1, WARMHI)

# ---- back wall band above the screen-door header
bg.rect(0, 6, 64, 4, WALL)
for x in range(0, 64, 6):
    bg.set(x, 7, WALLN); bg.set(x, 8, WALLN)
bg.line(0, 8, 63, 8, WALL2)

# ---- tunnel / track bed behind the doors
bg.rect(0, 15, 64, 30, TUN2)
bg.rect(44, 15, 4, 30, WALL)      # receding tunnel bands (depth, right)
bg.rect(48, 15, 5, 30, TUN2)
bg.rect(53, 15, 6, 30, TUN3)
bg.rect(59, 15, 5, 30, TUN4)
bg.rect(44, 15, 20, 4, TUN3)       # soffit shadow
bg.rect(44, 41, 20, 4, VOID)       # track bed
bg.line(44, 42, 63, 42, MD)
bg.line(44, 44, 63, 44, ML)        # far rail
for x in range(45, 62, 4):
    bg.rect(x, 43, 2, 1, FIG)
bg.set(57, 24, GREEN); bg.set(57, 25, GREEN)   # distant signal
bg.set(51, 18, AMBER)                           # distant tunnel lamp

# ---- the train: nose at right, tail blurring out of frame at left
bg.rect(0, 42, 44, 3, VOID)                     # underframe shadow
bg.rect(0, 15, 40, 2, SHADE)                    # roof
bg.poly([(39, 15), (41, 16), (43, 20), (43, 22), (39, 22)], SHADE)
bg.rect(0, 15, 40, 1, MH)
bg.rect(0, 17, 40, 20, BODY)                    # body
bg.poly([(40, 17), (42, 19), (43, 23), (43, 37), (40, 37)], BODY)
bg.rect(0, 17, 40, 1, WARMHI)                   # top highlight
bg.rect(0, 34, 43, 3, BODY2)                    # lower panel
bg.rect(0, 37, 43, 3, SHADE)
bg.rect(0, 40, 44, 2, LOW)                      # skirt
bg.rect(0, 31, 43, 3, STR)                      # livery stripe
bg.rect(0, 31, 43, 1, STR2)
bg.rect(3, 42, 9, 3, FIG)                       # bogies
bg.rect(24, 42, 9, 3, FIG)
for wx in (5, 9, 26, 30):
    bg.circle(wx, 43, 1, LOW)
    bg.set(wx, 43, MD)

def train_window(x0, x1, y0=20, y1=27):
    bg.rect(x0, y0, x1 - x0 + 1, y1 - y0 + 1, WIN)
    bg.rect(x0, y0, x1 - x0 + 1, 1, WARMHI)
    bg.rect(x0, y0, 1, y1 - y0 + 1, WF)
    bg.rect(x1, y0, 1, y1 - y0 + 1, WF)
    bg.line(x0, y0 - 1, x1, y0 - 1, SHADE)
for (a, b) in ((2, 8), (11, 16), (21, 27), (30, 35)):
    train_window(a, b)
# seated passengers inside the train (depth)
bg.rect(4, 24, 2, 3, SIL2); bg.set(4, 23, SIL2)
bg.rect(13, 24, 2, 3, SIL2)
bg.rect(24, 24, 2, 3, SIL2)
bg.rect(32, 24, 2, 3, SIL2)
# door bay
bg.rect(17, 18, 3, 22, BODY2)
bg.line(18, 18, 18, 39, SHADE)
bg.rect(17, 20, 3, 6, WIN)
bg.rect(17, 20, 1, 6, WF); bg.rect(19, 20, 1, 6, WF)
# nose: windshield, destination dots, headlight, marker
bg.poly([(40, 19), (42, 21), (42, 27), (40, 27)], WF)
bg.set(41, 21, ML); bg.set(41, 22, ML)
bg.set(39, 17, AMBER); bg.set(41, 17, AMBER)
bg.rect(41, 30, 2, 2, WARMHI)
bg.set(42, 33, ACC2); bg.set(42, 34, ACC2)
bg.rect(40, 35, 3, 2, SHADE)
bg.line(43, 23, 43, 39, MH)                     # nose edge highlight

# ================================================================ FX LAYER
# ---- screen-door glazing tint over every bay
bays = [(2, 10), (13, 21), (24, 32), (35, 43), (46, 54), (57, 61)]
for (a, b) in bays:
    fx.rect(a, 15, b - a + 1, 30, GLASS)
# glare dashes on the glass (opaque, reused colour)
for (a, b) in bays:
    fx.set(a + 2, 40, SCRN); fx.set(a + 3, 38, SCRN); fx.set(a + 4, 36, SCRN)
# ---- headlight wash spilling down the track from the nose
fx.poly([(43, 30), (63, 21), (63, 44), (43, 34)], CONE)
fx.circle(42, 31, 2, GLOW)
fx.rect(43, 30, 2, 2, GLOW)
# ---- air rushing past the nose
fx.rect(46, 18, 12, 1, STREAK)
fx.rect(48, 24, 14, 1, STREAK)
fx.rect(47, 36, 10, 1, STREAK)
# ---- speed: blur streaks trailing off the tail
fx.rect(0, 19, 14, 1, STREAK)
fx.rect(0, 23, 10, 1, STREAK)
fx.rect(0, 29, 17, 1, STREAK)
fx.rect(0, 35, 12, 1, STREAK)

# ================================================================ FRONT LAYER
# ---- screen-door header beam
fr.rect(0, 10, 64, 5, MM)
fr.rect(0, 10, 64, 1, MH)
fr.rect(0, 14, 64, 1, MD)
for x in range(2, 64, 8):
    fr.rect(x, 11, 4, 1, ML)
fr.set(17, 12, GREEN); fr.set(18, 12, GREEN)    # door indicators
fr.set(39, 12, AMBER); fr.set(40, 12, AMBER)

# ---- mullions
for mx in (0, 11, 22, 33, 44, 55, 62):
    fr.rect(mx, 15, 2, 30, MD)
    fr.rect(mx, 15, 1, 30, MM)
# ---- sliding door leaves (bays 2 and 4): centre seam + edge stiles
for (a, b) in ((13, 21), (35, 43)):
    mid = (a + b) // 2
    fr.line(mid, 15, mid, 44, MM)
    fr.line(mid - 1, 15, mid - 1, 44, ML)
    fr.rect(a, 15, 1, 30, ML)
    fr.rect(b, 15, 1, 30, ML)
    fr.rect(a + 1, 40, b - a - 1, 1, ML)
# ---- door sill with hazard marks
fr.rect(0, 45, 64, 5, MD)
fr.rect(0, 45, 64, 1, ML)
fr.rect(0, 49, 64, 1, FIG)
for x in range(1, 61, 4):
    fr.rect(x, 46, 2, 1, TAC)
    fr.rect(x + 2, 46, 2, 1, FIG)

# ---- hanging signs (no brand names)
fr.rect(19, 1, 1, 2, ML); fr.rect(41, 1, 1, 2, ML)
fr.rect(14, 2, 32, 9, SIGNBG)
fr.rect(14, 2, 32, 1, SIGNBD)
fr.rect(14, 10, 32, 1, VOID)
fr.rect(15, 3, 1, 7, SIGNSD); fr.rect(44, 3, 1, 7, SIGNSD)
fr.poly([(19, 6), (17, 5), (17, 7)], SIGNTX)     # left arrow
fr.rect(17, 5, 1, 3, SIGNTX)
fr.text(21, 3, "EXIT", SIGNTX, font="5x7")
# route-map panel
fr.rect(47, 2, 14, 8, SIGNBG)
fr.rect(47, 2, 14, 1, SIGNBD)
fr.rect(48, 4, 12, 1, STR2); fr.set(51, 4, SIGNTX); fr.set(57, 4, SIGNTX)
fr.rect(48, 6, 9, 1, ACC2); fr.set(53, 6, SIGNTX)
fr.rect(48, 8, 11, 1, GREEN); fr.set(56, 8, SIGNTX)

# ---- platform floor
fr.rect(0, 50, 64, 14, FLOOR)
fr.rect(0, 50, 64, 1, MH)
fr.rect(0, 51, 64, 3, TAC)                       # tactile paving
for x in range(1, 63, 3):
    fr.set(x, 51, TACL); fr.set(x + 1, 52, TACL); fr.set(x, 53, TACL)
fr.rect(0, 53, 64, 1, TACD)
for x in range(7, 64, 9):
    fr.line(x, 54, x, 61, FLOOR2)
fr.line(0, 58, 63, 58, FLOOR2)
fr.line(0, 54, 63, 54, WALLN)
fr.rect(0, 62, 64, 2, FIG)                       # foreground grounding

# ---- bench (right)
fr.rect(47, 40, 15, 1, BNL); fr.rect(47, 41, 15, 1, BN)     # backrest
fr.rect(47, 42, 1, 6, BND); fr.rect(59, 42, 1, 6, BND)      # posts
fr.rect(47, 48, 15, 1, BNL); fr.rect(47, 49, 15, 1, BND)    # seat
fr.rect(47, 50, 2, 6, MD); fr.rect(58, 50, 2, 6, MD)        # legs
fr.rect(46, 56, 4, 1, MM); fr.rect(57, 56, 4, 1, MM)        # feet
fr.rect(44, 42, 2, 6, MM); fr.rect(43, 41, 4, 1, ML)        # armrest
fr.rect(44, 57, 20, 1, FIG)                                 # shadow

# ---- passenger 1: standing, phone raised, facing the train
fr.rect(5, 56, 11, 2, FIG)
fr.rect(8, 46, 2, 9, FIG); fr.rect(11, 46, 2, 9, FIG2)
fr.rect(7, 55, 4, 2, FIG); fr.rect(11, 55, 4, 2, FIG)
fr.poly([(7, 37), (12, 37), (13, 46), (6, 46)], FIG2)
fr.line(12, 37, 13, 45, RIM)
fr.rect(9, 36, 2, 1, FIG)
fr.rect(8, 31, 4, 5, FIG2)
fr.rect(8, 31, 4, 2, FIG); fr.rect(7, 32, 1, 3, FIG)
fr.set(12, 32, RIM); fr.set(12, 33, RIM)
fr.rect(11, 38, 2, 4, FIG); fr.rect(12, 35, 2, 3, FIG2)
fr.rect(12, 32, 2, 3, SCRN)                      # phone screen

# ---- passenger 2: striding through, cap + messenger bag
fr.rect(17, 56, 14, 2, FIG)
fr.poly([(22, 45), (25, 45), (21, 54), (19, 54)], FIG)      # back leg
fr.rect(18, 54, 4, 2, FIG)
fr.poly([(25, 45), (28, 45), (30, 54), (28, 54)], FIG2)     # front leg
fr.rect(29, 54, 4, 2, FIG)
fr.poly([(22, 36), (27, 36), (28, 46), (21, 46)], FIG2)     # torso leaning in
fr.line(27, 36, 28, 45, RIM)
fr.rect(21, 38, 2, 5, FIG)                                  # back arm
fr.rect(27, 38, 2, 3, FIG); fr.rect(28, 41, 2, 2, FIG2)     # front arm
fr.line(26, 37, 22, 42, ACC2)                               # bag strap
fr.rect(20, 42, 4, 4, ACC); fr.rect(20, 42, 4, 1, ACC2)
fr.rect(23, 31, 4, 5, FIG2)                                 # head
fr.set(27, 33, RIM); fr.set(27, 34, RIM)
fr.rect(23, 30, 4, 1, ACC2); fr.rect(23, 31, 4, 1, ACC)     # cap
fr.rect(27, 31, 2, 1, ACC)                                  # brim

# ---- passenger 3: seated on the bench, reading, facing left
fr.rect(43, 57, 9, 1, FIG)
fr.rect(46, 49, 2, 6, FIG2); fr.rect(44, 55, 4, 2, FIG)     # shin + foot
fr.rect(47, 46, 6, 2, FIG)                                  # thigh
fr.poly([(51, 40), (57, 40), (57, 48), (50, 48)], FIG2)     # torso
fr.line(51, 40, 51, 47, RIM)
fr.line(57, 40, 57, 47, RIM)                                # backlit by headlight
fr.rect(51, 35, 4, 5, FIG2)                                 # head
fr.rect(50, 34, 6, 3, FIG); fr.rect(55, 35, 2, 3, FIG)      # hair + bun
fr.set(50, 36, RIM); fr.set(50, 37, RIM)
fr.set(56, 35, RIM); fr.set(56, 36, RIM)
fr.rect(52, 43, 2, 3, FIG); fr.rect(48, 45, 4, 2, FIG2)     # arms
fr.rect(45, 41, 3, 4, SCRN)                                 # tablet / book

# ---- foreground pillar (frames the shot, strongest depth cue)
fr.rect(0, 0, 1, 64, FIG)
fr.rect(1, 0, 1, 64, VOID)
fr.rect(2, 0, 1, 64, WALLN)
fr.rect(0, 44, 3, 2, ML)
fr.rect(0, 58, 3, 6, FIG)
fr.rect(3, 58, 1, 6, WALLN)

# ================================================================ compose
out = flatten([bg, fx, fr], name="subway_platform")
print(out.stats_text())
view(out)
save("subway_platform", out)
finish(out)
