from pixelbench_api import *

W = H = 64
c = new_canvas(W, H, name="void-eye")

def col(spec, name=None):
    return c.color(spec, name)

# ---------------- palette ----------------
OUT    = col("#0b0318", "outline")     # near-black edge -> readable silhouette
BODY_D = col("#251040", "body_dark")
BODY_M = col("#331a58", "body_mid")
BODY_L = col("#44276f", "body_light")
BODY_HL = col("#6d4ea6", "body_hl")
IRIS_D = col("#180634", "iris_deep")
IRIS_M = col("#2d1060", "iris_mid")
IRIS_I = col("#4c1e96", "iris_inner")
HALO   = col("#8f5fd6", "glow")
PUPIL  = col("#dcc0ff", "pupil")
CORE   = col("#ffffff", "core")
TEN_D  = col("#150828", "tent_dark")
TEN_M  = col("#2f1352", "tent_mid")
TEN_T  = col("#7350b0", "tent_tip")
AURA_A = col((84, 40, 150, 56), "aura_outer")
AURA_B = col((110, 58, 190, 44), "aura_inner")
SH_A   = col((0, 0, 0, 82),  "shadow_soft")
SH_B   = col((0, 0, 0, 112), "shadow_core")

# ---------------- faint aura behind the eye ----------------
c.ellipse(32, 29, 21, 18, AURA_A)
c.ellipse(32, 29, 17, 14, AURA_B)

# ---------------- soft ground shadow (hover) ----------------
c.ellipse(32, 55, 16, 3, SH_A)
c.ellipse(32, 55, 11, 2, SH_B)

# ---------------- tentacles (behind the body) ----------------
def tent(pts, tip):
    c.poly(pts, TEN_D)
    c.set(tip[0], tip[1], TEN_T)
    c.set(tip[0] - 1, tip[1] - 1, TEN_M)

# side nubs
tent([(13,31),(17,32),(16,38),(13,35),(12,32)], (14,36))
tent([(46,31),(50,32),(49,38),(46,35),(47,32)], (48,36))
# hanging tentacles
tent([(18,40),(22,41),(23,47),(20,52),(17,46)], (20,51))
tent([(24,42),(28,43),(29,49),(26,54),(23,48)], (26,53))
tent([(30,43),(34,43),(35,50),(32,55),(29,49)], (32,54))
tent([(35,42),(39,43),(40,49),(37,54),(34,48)], (37,53))
tent([(41,40),(45,41),(46,46),(43,50),(40,45)], (43,49))

# ---------------- eyeball body ----------------
c.ellipse(32, 29, 19, 17, BODY_D)
c.ellipse(32, 28, 16, 14, BODY_M)
c.ellipse(32, 27, 12, 10, BODY_L)          # sclera band
c.ellipse(32, 29, 19, 17, OUT, fill=False) # strong rim

# ---------------- veins ----------------
c.line(20, 20, 14, 16, OUT)
c.line(21, 30, 14, 33, OUT)
c.line(43, 20, 49, 16, OUT)
c.line(42, 30, 49, 33, OUT)

# ---------------- the eye ----------------
c.ellipse(32, 25, 12, 11, IRIS_D)
c.ellipse(32, 25, 12, 11, OUT, fill=False) # iris rim
c.ellipse(32, 25, 10,  9, IRIS_M)
c.ellipse(32, 25,  8,  7, IRIS_I)
c.circle(32, 25,  5, HALO)
c.circle(32, 25,  3, PUPIL)
c.circle(32, 25,  1, CORE)

# ---------------- highlights ----------------
c.ellipse(28, 14, 2, 1, BODY_HL)   # glossy arc on the eyeball
c.set(32, 24, CORE)                # bright glint in the pupil

# ---------------- floating motes ----------------
c.set(17,  9, (150, 110, 225, 110))
c.set(45,  7, (150, 110, 225,  84))
c.set(11, 24, (140, 100, 215,  72))
c.set(52, 22, (140, 100, 215,  60))

print(c.stats_text())
finish(c)
