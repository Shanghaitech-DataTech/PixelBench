try:
    from pixelbench_api import *
except Exception:
    pass

# ================= palette =================
OUT     = "#2b1a12"   # dark outline
FLR     = "#c79a66"; FLR_D = "#a87a48"; FLR_L = "#d8ae7e"
RUG_B   = "#e9dcc0"; RUG_R = "#b5453c"
TBL_L   = "#dda968"; TBL_M = "#c08c4c"; TBL_D = "#9c6a30"; TBL_E = "#f0c68c"
CH_F    = "#c9954f"; CH_L = "#e0b273"
CUS     = "#f2e3c0"; CUS_D = "#d4bf96"
BOWL    = "#f4e9d3"; BOWL_IN = "#8f7a5c"; BOWL_D = "#cdb691"
PL      = "#f6efdc"; PL_D = "#d8cbb0"
AP_R    = "#d8453a"; AP_D = "#a92f28"; AP_H = "#f28a76"
OR_F    = "#f0912f"; OR_H = "#f8b06a"; OR_D = "#c96f1c"
GR_F    = "#8fb84a"; GR_H = "#b6d97a"; GR_D = "#6a9132"
MG_D    = "#b56450"; MG_L = "#d9927e"; COF = "#5a3a22"
SHDW    = "#b08048"

c = new_canvas(64, 64, background=None, name="dining-table")

# ---------------- floor ----------------
c.rect(0, 0, 64, 64, FLR)
for x in range(5, 64, 6):
    c.rect(x, 0, 1, 64, FLR_D)
for i, x0 in enumerate(range(0, 64, 6)):
    off = (i * 9) % 26
    for y in (off + 2, off + 28, off + 54):
        if 0 <= y < 64:
            c.rect(x0, y, min(5, 64 - x0), 1, FLR_L)
for gx, gy, gl in [
    (1, 4, 3), (8, 1, 4), (15, 5, 3), (46, 2, 4), (53, 4, 3), (60, 1, 3),
    (1, 59, 4), (8, 61, 3), (15, 58, 4), (45, 58, 4), (52, 60, 3), (59, 62, 3),
    (1, 8, 3), (1, 12, 3), (1, 48, 3), (1, 52, 3), (1, 56, 2),
    (59, 8, 3), (59, 12, 3), (59, 48, 3), (59, 52, 3), (62, 56, 2)]:
    c.rect(gx, gy, gl, 1, FLR_L)

# ---------------- rug ----------------
c.rect(6, 6, 52, 52, OUT)      # x6..57  y6..57
c.rect(7, 7, 50, 50, RUG_B)    # x7..56  y7..56
c.rect(9, 9, 46, 46, RUG_R)    # x9..54  y9..54
for x, y, col in [(9, 9, RUG_B), (54, 9, RUG_B), (9, 54, RUG_B), (54, 54, RUG_B)]:
    c.set(x, y, col)

def diamond(cx, cy, col):
    c.set(cx, cy - 1, col); c.set(cx - 1, cy, col); c.set(cx, cy, col)
    c.set(cx + 1, cy, col); c.set(cx, cy + 1, col)

for dx, dy in [(13, 13), (50, 13), (13, 50), (50, 50)]:
    diamond(dx, dy, RUG_B)
for dx, dy in [(18, 11), (45, 11), (18, 52), (45, 52)]:
    c.set(dx, dy, RUG_B)

# ---------------- chairs ----------------
# top chair (backrest at top)
c.rect(20, 1, 24, 6, OUT)     # backrest outline x20..43 y1..6
c.rect(21, 5, 22, 10, OUT)    # seat outline     x21..42 y5..14
c.rect(21, 2, 22, 3, CH_F)    # backrest         x21..42 y2..4
c.rect(21, 2, 22, 1, CH_L)
c.rect(22, 6, 20, 8, CH_F)    # seat             x22..41 y6..13
c.rect(23, 7, 18, 6, CUS)     # cushion          x23..40 y7..12
c.rect(23, 12, 18, 1, CUS_D)  # contact shadow (table side)

# bottom chair (backrest at bottom)
c.rect(21, 49, 22, 10, OUT)   # seat outline     x21..42 y49..58
c.rect(20, 57, 24, 6, OUT)    # backrest outline x20..43 y57..62
c.rect(21, 59, 22, 3, CH_F)   # backrest         x21..42 y59..61
c.rect(21, 59, 22, 1, CH_L)
c.rect(22, 50, 20, 8, CH_F)   # seat             x22..41 y50..57
c.rect(23, 51, 18, 6, CUS)    # cushion          x23..40 y51..56
c.rect(23, 51, 18, 1, CUS_D)

# left chair (backrest at left)
c.rect(1, 20, 6, 24, OUT)     # backrest outline x1..6   y20..43
c.rect(5, 21, 10, 22, OUT)    # seat outline     x5..14  y21..42
c.rect(2, 21, 3, 22, CH_F)    # backrest         x2..4   y21..42
c.rect(2, 21, 1, 22, CH_L)
c.rect(6, 22, 8, 20, CH_F)    # seat             x6..13  y22..41
c.rect(7, 23, 6, 18, CUS)     # cushion          x7..12  y23..40
c.rect(12, 23, 1, 18, CUS_D)

# right chair (backrest at right)
c.rect(57, 20, 6, 24, OUT)    # backrest outline x57..62 y20..43
c.rect(49, 21, 10, 22, OUT)   # seat outline     x49..58 y21..42
c.rect(59, 21, 3, 22, CH_F)   # backrest         x59..61 y21..42
c.rect(59, 21, 1, 22, CH_L)
c.rect(50, 22, 8, 20, CH_F)   # seat             x50..57 y22..41
c.rect(51, 23, 6, 18, CUS)    # cushion          x51..56 y23..40
c.rect(51, 23, 1, 18, CUS_D)

# ---------------- table ----------------
c.rect(14, 14, 36, 36, OUT)   # x14..49 y14..49
c.rect(15, 15, 34, 34, TBL_L) # x15..48 y15..48
c.rect(15, 15, 34, 1, TBL_E)
c.rect(15, 15, 1, 34, TBL_E)
c.rect(15, 48, 34, 1, TBL_M)
c.rect(48, 15, 1, 34, TBL_M)
c.rect(16, 23, 32, 1, TBL_D)  # plank seam
c.rect(16, 40, 32, 1, TBL_D)  # plank seam
for gx, gy, gl in [
    (16, 16, 3), (44, 16, 3), (38, 19, 3), (24, 22, 2),
    (16, 26, 3), (46, 36, 2), (16, 44, 3), (37, 46, 2), (24, 46, 2)]:
    c.rect(gx, gy, gl, 1, TBL_D)

# ---------------- soft shadows ----------------
c.ellipse(33, 33, 7, 5, SHDW)   # bowl
c.circle(22, 22, 2, SHDW)       # mug TL
c.circle(45, 45, 2, SHDW)       # mug BR
c.circle(46, 26, 2, SHDW)       # loose orange
c.circle(21, 41, 2, SHDW)       # loose apple

# ---------------- plates ----------------
def plate(cx, cy):
    c.circle(cx, cy, 3, OUT)
    c.circle(cx, cy, 2, PL)
    c.set(cx - 1, cy + 1, PL_D)
    c.set(cx + 1, cy + 1, PL_D)

for px, py in [(31, 18), (31, 45), (18, 31), (45, 31)]:
    plate(px, py)

# ---------------- cutlery (top & bottom settings) ----------------
c.set(25, 15, OUT); c.set(26, 15, OUT); c.set(27, 15, OUT)   # fork tines
c.rect(26, 16, 1, 5, OUT)                                    # fork stem
c.rect(35, 15, 2, 3, OUT)                                    # knife blade
c.rect(36, 18, 1, 3, OUT)                                    # knife handle
c.set(25, 48, OUT); c.set(26, 48, OUT); c.set(27, 48, OUT)   # fork tines
c.rect(26, 43, 1, 5, OUT)                                    # fork stem
c.rect(36, 43, 1, 3, OUT)                                    # knife handle
c.rect(35, 46, 2, 3, OUT)                                    # knife blade

# ---------------- mugs ----------------
def mug(cx, cy, side):
    c.circle(cx, cy, 3, OUT)
    c.circle(cx, cy, 2, MG_D)
    c.circle(cx, cy, 1, COF)
    c.set(cx - 2, cy - 1, MG_L)
    if side == "r":
        c.set(cx + 4, cy - 1, OUT); c.set(cx + 4, cy, OUT); c.set(cx + 4, cy + 1, OUT)
    else:
        c.set(cx - 4, cy - 1, OUT); c.set(cx - 4, cy, OUT); c.set(cx - 4, cy + 1, OUT)

mug(20, 20, "r")
mug(43, 43, "l")

# ---------------- fruit sprites (5x5 body, optional stem/leaf) ----------------
def fruit(cx, cy, base, hi, sh, top=None):
    if top:
        c.set(cx, cy - 3, top)
    c.set(cx - 1, cy - 2, OUT); c.set(cx, cy - 2, OUT); c.set(cx + 1, cy - 2, OUT)
    c.set(cx - 2, cy - 1, OUT); c.set(cx + 2, cy - 1, OUT)
    c.set(cx - 2, cy, OUT);     c.set(cx + 2, cy, OUT)
    c.set(cx - 2, cy + 1, OUT); c.set(cx + 2, cy + 1, OUT)
    c.set(cx - 1, cy + 2, OUT); c.set(cx, cy + 2, OUT); c.set(cx + 1, cy + 2, OUT)
    c.rect(cx - 1, cy - 1, 3, 3, base)
    c.set(cx - 1, cy - 1, hi)
    c.set(cx + 1, cy + 1, sh)

# ---------------- bowl of fruit ----------------
c.ellipse(31, 31, 8, 6, OUT)      # x23..39 y25..37
c.ellipse(31, 31, 7, 5, BOWL)     # x24..38 y26..36
c.ellipse(31, 31, 6, 4, BOWL_IN)  # x25..37 y27..35
c.set(31, 26, OUT)                # repair rim tips overwritten by inner ellipse
c.set(31, 36, OUT)
c.path("M 25 31 A 6 4 0 0 0 37 31", BOWL_D, fill=False)   # shaded near rim
fruit(31, 30, GR_F, GR_H, GR_D)           # green apple, back centre
fruit(27, 31, AP_R, AP_H, AP_D)           # red apple, front left
fruit(35, 31, OR_F, OR_H, OR_D)           # orange, front right

# ---------------- loose fruit ----------------
fruit(19, 39, AP_R, AP_H, AP_D, COF)      # apple with stem
fruit(44, 24, OR_F, OR_H, OR_D, GR_D)     # orange with leaf

print(c.stats_text())

# ---------------- diagnostic dump ----------------
_pal = c.palette()
_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
_code = {_e["index"]: _letters[_i % len(_letters)] for _i, _e in enumerate(_pal)}
print("LEGEND: " + " ".join(f"{_code[_e['index']]}={_e['rgba'][:7]}" for _e in _pal))

def idx_of(hexc):
    want = tuple(int(hexc[i:i + 2], 16) for i in (1, 3, 5))
    for e in c.palette():
        if tuple(e["rgba"][:3]) == want:
            return e["index"]
    return None

I_OUT = idx_of(OUT); I_AP = idx_of(AP_R); I_OR = idx_of(OR_F); I_GR = idx_of(GR_F)
I_BOWL = idx_of(BOWL); I_BD = idx_of(BOWL_D); I_BIN = idx_of(BOWL_IN)
I_PL = idx_of(PL); I_MGD = idx_of(MG_D); I_COF = idx_of(COF); I_SHDW = idx_of(SHDW)

checks = [
    ("bowl outline left  (23,31)", c.get(23, 31), I_OUT),
    ("bowl outline right (39,31)", c.get(39, 31), I_OUT),
    ("bowl rim top tip   (31,26)", c.get(31, 26), I_OUT),
    ("bowl rim bot tip   (31,36)", c.get(31, 36), I_OUT),
    ("bowl wall          (24,31)", c.get(24, 31), I_BOWL),
    ("bowl inner         (31,33)", c.get(31, 33), I_BIN),
    ("bowl near-rim shade(31,35)", c.get(31, 35), I_BD),
    ("apple centre       (27,31)", c.get(27, 31), I_AP),
    ("orange centre      (35,31)", c.get(35, 31), I_OR),
    ("green apple centre (31,30)", c.get(31, 30), I_GR),
    ("green apple hi     (30,29)", c.get(30, 29), idx_of(GR_H)),
    ("green apple sh     (32,31)", c.get(32, 31), idx_of(GR_D)),
    ("plate top centre   (31,18)", c.get(31, 18), I_PL),
    ("plate bot centre   (31,45)", c.get(31, 45), I_PL),
    ("plate left centre  (18,31)", c.get(18, 31), I_PL),
    ("plate right centre (45,31)", c.get(45, 31), I_PL),
    ("mug TL wall        (22,20)", c.get(22, 20), I_MGD),
    ("mug TL coffee      (20,20)", c.get(20, 20), I_COF),
    ("mug BR wall        (41,43)", c.get(41, 43), I_MGD),
    ("loose apple body   (19,39)", c.get(19, 39), I_AP),
    ("loose apple stem   (19,36)", c.get(19, 36), I_COF),
    ("loose orange body  (44,24)", c.get(44, 24), I_OR),
    ("loose orange leaf  (44,21)", c.get(44, 21), idx_of(GR_D)),
    ("bowl shadow        (33,37)", c.get(33, 37), I_SHDW),
    ("table bevel        (15,15)", c.get(15, 15), idx_of(TBL_E)),
    ("table wood         (21,26)", c.get(21, 26), idx_of(TBL_L)),
    ("table seam         (31,23)", c.get(31, 23), idx_of(TBL_D)),
    ("chair cushion TL   (25,9)",  c.get(25, 9),  idx_of(CUS)),
    ("chair cushion BR   (36,54)", c.get(36, 54), idx_of(CUS)),
    ("chair backrest L   (3,31)",  c.get(3, 31),  idx_of(CH_F)),
    ("chair backrest R   (60,31)", c.get(60, 31), idx_of(CH_F)),
    ("rug inner red      (12,12)", c.get(12, 12), idx_of(RUG_R)),
    ("rug border cream   (8,14)",  c.get(8, 14),  idx_of(RUG_B)),
    ("floor              (2,0)",   c.get(2, 0),   idx_of(FLR)),
]

fails = 0
for name, got, want in checks:
    ok = (got == want)
    if not ok:
        fails += 1
    print(f"  [{'OK ' if ok else 'FAIL'}] {name}: got={got} want={want}")
print(f"CHECKS: {len(checks) - fails}/{len(checks)} passed")

finish(c)
