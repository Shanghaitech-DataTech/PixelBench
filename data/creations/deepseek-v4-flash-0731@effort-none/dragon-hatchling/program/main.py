from pixelbench_api import *

# Create 64x64 canvas - DRAGON HATCHLING
c = new_canvas(64, 64, name="dragon")

# ========== PALETTE ==========
GREEN   = (45, 122, 90)
GREEN_D = (26, 90, 63)
GREEN_L = (63, 156, 119)
BELLY   = (232, 224, 200)
BELLY_S = (200, 192, 168)
HORN    = (232, 216, 160)
HORN_D  = (200, 176, 112)
EYE     = (255, 204, 0)
PUPIL   = (32, 32, 32)
MOUTH_R = (138, 42, 42)
MOUTH_D = (90, 21, 21)
TOOTH   = (248, 248, 240)
CLAW    = (224, 224, 224)
WING    = (90, 74, 138)
WING_L  = (122, 106, 170)
WING_B  = (232, 216, 176)
SPIKE   = (42, 90, 74)
SPIKE_L = (63, 138, 106)
LINE    = (10, 42, 31)

G = c.color(GREEN); GD = c.color(GREEN_D); GL = c.color(GREEN_L)
BE = c.color(BELLY); BS = c.color(BELLY_S)
HO = c.color(HORN); HD = c.color(HORN_D)
EY = c.color(EYE); PU = c.color(PUPIL)
MR = c.color(MOUTH_R); MD = c.color(MOUTH_D); TO = c.color(TOOTH)
CL = c.color(CLAW)
WI = c.color(WING); WL = c.color(WING_L); WB = c.color(WING_B)
SP = c.color(SPIKE); SL = c.color(SPIKE_L)
LN = c.color(LINE)

# ============================================================
# DRAGON HATCHLING - final version
# ============================================================

# ===== LEFT WING (background) =====
c.poly([(28, 17), (23, 9), (14, 5), (4, 6), (1, 13), (8, 20), (17, 21)], WI, fill=True)
c.poly([(28, 17), (23, 9), (14, 5), (4, 6), (1, 13), (8, 20), (17, 21)], LN, fill=False)
c.poly([(23, 14), (19, 9), (10, 8), (6, 15), (12, 17), (18, 16)], WL, fill=True)
c.line(26, 16, 20, 8, WB)
c.line(20, 8, 10, 7, WB)

# ===== TAIL =====
c.poly([(16, 32), (23, 37), (30, 41), (33, 44), (28, 48), (15, 47), (8, 41), (11, 34)], G, fill=True)
c.poly([(16, 32), (9, 35), (5, 33), (4, 29), (9, 26), (12, 28)], G, fill=True)
c.poly([(16, 32), (23, 37), (30, 41), (33, 44), (28, 48), (15, 47), (8, 41), (11, 34)], LN, fill=False)
c.poly([(16, 32), (9, 35), (5, 33), (4, 29), (9, 26), (12, 28)], LN, fill=False)
c.poly([(5, 31), (0, 28), (4, 34)], SP, fill=True)
c.poly([(5, 31), (0, 28), (4, 34)], LN, fill=False)
for (bx, by, tx, ty) in [(14,27,11,22), (19,30,18,25), (24,34,24,29), (29,37,30,33)]:
    c.poly([(bx, by), (tx, ty), (bx+1, by)], SP, fill=True)
c.poly([(10, 31), (7, 26), (11, 33)], SP, fill=True)
for (hx, hy) in [(12,24), (19,27), (25,31), (30,35), (8,28), (1,30)]:
    c.set(hx, hy, SL)

# ===== HIND LEG =====
c.ellipse(25, 43, 5, 4, GD, fill=True)
c.ellipse(25, 43, 5, 4, LN, fill=False)
c.poly([(20, 44), (20, 48), (24, 48), (25, 44)], GD, fill=True)
c.poly([(25, 44), (26, 48), (28, 48), (28, 44)], GD, fill=True)
c.poly([(21, 48), (18, 50), (22, 48)], CL, fill=True)
c.poly([(26, 48), (28, 50), (27, 48)], CL, fill=True)
c.poly([(20, 44), (20, 48), (24, 48), (25, 44)], LN, fill=False)
c.poly([(25, 44), (26, 48), (28, 48), (28, 44)], LN, fill=False)

# ===== BODY =====
c.ellipse(36, 33, 12, 10, G, fill=True)
c.ellipse(36, 38, 9, 6, GD, fill=True)
c.ellipse(30, 36, 6, 5, BE, fill=True)
c.ellipse(30, 38, 4, 3, BS, fill=True)
c.ellipse(36, 33, 12, 10, LN, fill=False)
c.ellipse(30, 36, 6, 5, LN, fill=False)
for (sx, sy) in [(34, 28), (38, 29), (42, 28), (32, 33), (44, 32), (36, 25), (41, 34)]:
    c.set(sx, sy, GL)
for (sx, sy) in [(30, 27), (39, 31), (45, 28), (35, 30)]:
    c.set(sx, sy, GD)
for (sx, sy) in [(32, 36), (40, 35), (45, 34), (28, 36)]:
    c.set(sx, sy, GL)

# ===== BACK SPIKES =====
for (sx, sy) in [(26,27), (30,22), (34,22), (38,23), (42,24)]:
    c.poly([(sx, sy), (sx-1, sy-4), (sx+2, sy-1)], SP, fill=True)
for (hx, hy) in [(27,24), (31,19), (35,19), (39,20), (42,21)]:
    c.set(hx, hy, SL)

# ===== FRONT LEG =====
c.poly([(40, 37), (43, 40), (46, 43), (40, 47), (35, 45), (36, 39)], G, fill=True)
c.poly([(40, 37), (43, 40), (46, 43), (40, 47), (35, 45), (36, 39)], LN, fill=False)
c.poly([(39, 46), (36, 49), (40, 47)], CL, fill=True)
c.poly([(41, 47), (42, 50), (43, 46)], CL, fill=True)

# ===== RIGHT WING =====
c.poly([(44, 16), (51, 8), (58, 5), (62, 12), (58, 18), (52, 22), (45, 20)], WI, fill=True)
c.poly([(44, 16), (51, 8), (58, 5), (62, 12), (58, 18), (52, 22), (45, 20)], LN, fill=False)
c.poly([(49, 12), (53, 9), (58, 8), (60, 14), (54, 18)], WL, fill=True)
c.line(46, 16, 52, 8, WB)
c.line(52, 8, 58, 7, WB)

# ===== NECK =====
c.poly([(31, 15), (36, 21), (42, 21), (45, 15), (43, 11), (34, 11)], G, fill=True)
c.poly([(31, 15), (36, 21), (42, 21), (45, 15), (43, 11), (34, 11)], LN, fill=False)

# ============================================================
# HEAD - drawn as one coherent mass
# ============================================================
# Main head mass
c.ellipse(36, 10, 8, 6, G, fill=True)
c.ellipse(35, 8, 6, 3, G, fill=True)
# Outline
c.ellipse(36, 10, 8, 6, LN, fill=False)
c.ellipse(35, 8, 6, 3, LN, fill=False)

# Snout is a front-facing muzzle
# Fill the snout region solid
c.rect(42, 7, 8, 7, G)
# Snout outline
c.line(42, 7, 48, 7, LN)
c.line(48, 7, 50, 9, LN)
c.line(50, 9, 50, 13, LN)

# ===== FACE =====
# EYE - one big fierce eye
c.circle(35, 9, 2, EY, fill=True)
c.circle(36, 9, 1, PU, fill=True)
# Brow ridge
c.set(33, 6, LN)
c.set(34, 7, LN)
c.set(36, 6, LN)

# ===== OPEN MOUTH =====
# Mouth opening - a clear dark slice
c.rect(43, 11, 6, 3, MR)   # mouth aperture
c.set(44, 12, MD)
c.set(45, 12, MD)
# Upper teeth
c.set(44, 11, TO)
c.set(46, 11, TO)
# Lower jaw
c.poly([(43, 13), (47, 14), (45, 15), (42, 14)], G, fill=True)
# Lower teeth
c.set(44, 14, TO)
c.set(46, 14, TO)
# Jaw boundary
c.line(43, 10, 48, 10, LN)
c.line(44, 15, 42, 14, LN)

# ===== HORNS =====
c.poly([(33, 6), (30, 2), (34, 5)], HO, fill=True)
c.poly([(33, 6), (30, 2), (34, 5)], LN, fill=False)
c.set(31, 3, HD)
c.poly([(38, 5), (37, 1), (40, 4)], HO, fill=True)
c.poly([(38, 5), (37, 1), (40, 4)], LN, fill=False)
c.set(38, 2, HD)

# ===== SCALE HIGHLIGHTS =====
for (sx, sy) in [(35, 13), (39, 13), (37, 15), (31, 17), (37, 7), (40, 12), (33, 14)]:
    c.set(sx, sy, GL)
c.set(29, 35, GL)
c.set(39, 34, GL)
c.set(44, 33, GL)

# ===== Bottom edge =====
c.line(28, 43, 47, 43, LN)
c.line(47, 43, 49, 41, LN)

# ============================================================
# VERIFY and FINISH
# ============================================================
stats = c.stats()
print(f"Canvas: {stats['size']}, Colors: {stats['colors_used']}, Visible: {stats['visible_pixels']}")
print(f"BBox: {stats['bbox']}")
print(c.stats_text())

# Careful head/full check
print("\n=== Final check ===")
print(c.matrix_text(region=(0, 0, 63, 31)))
print(c.matrix_text(region=(0, 32, 63, 50)))

finish(c)
