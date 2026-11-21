from pixelbench_api import new_canvas, finish
import math

c = new_canvas(32, 32, name="steamer")
S = 1  # horizontal shift (centering tweak)

BAM_RIM  = c.color("#ecc994")
BAM_HL   = c.color("#f9e2b8")
BAM_RIMD = c.color("#d9ab6c")
BAM_SIDE = c.color("#c4914f")
BAM_SDS  = c.color("#a9753a")
BAM_IN   = c.color("#7c4f22")
BAM_IND  = c.color("#56300f")
SHAD     = c.color("#3f2409")
KNOB     = c.color("#9a6a33")
DUMP     = c.color("#f8f2e0")
DUMP_HL  = c.color("#ffffff")
DUMS     = c.color("#e6d6b0")
DUML     = c.color("#c9b084")
STEAM    = c.color("#ffffff")
STEAM2   = c.color("#e9e3d5")

# --- soft ground shadow (before body so the edges show) ---
c.ellipse(16 + S, 29, 13, 3, (74, 48, 22, 110))

# --- steamer body ---
c.rect(3 + S, 15, 27, 13, BAM_SIDE)
c.ellipse(16 + S, 28, 13, 5, BAM_SIDE)
for x in range(6 + S, 28, 4):
    c.line(x, 16, x, 28, BAM_SDS)
c.rect(3 + S, 24, 27, 3, BAM_SDS)

# --- top surface / opening ---
c.ellipse(16 + S, 15, 13, 6, BAM_RIM)
c.ellipse(16 + S, 15, 12, 5, BAM_RIMD, fill=False)
c.ellipse(16 + S, 16, 11, 4, BAM_IN)
for y in range(12, 21):
    t = (y - 16) / 5.0
    if abs(t) < 0.99 and y % 2 == 0:
        dxv = int(11 * math.sqrt(max(0.0, 1 - t * t)))
        c.line(16 + S - dxv, y, 16 + S + dxv, y, BAM_IND)

# --- lid shadow, then tilted lid (left side, partially open) ---
c.ellipse(9 + S, 12, 11, 4.5, SHAD)
c.ellipse(9 + S, 12, 11, 4, BAM_RIMD)
c.ellipse(8 + S, 10, 11, 4, BAM_RIM)
c.ellipse(7 + S, 6, 2, 1.5, KNOB)
c.ellipse(6 + S, 5, 1, 1, BAM_HL)

# --- dumplings ---
def dumpling(cx, cy):
    c.ellipse(cx, cy, 3, 2, DUMP)          # 7x5 dome
    c.ellipse(cx, cy + 1, 2, 1, DUMS)      # lower shading
    c.line(cx - 2, cy - 1, cx - 2, cy + 1, DUML)
    c.line(cx, cy - 1, cx, cy + 1, DUML)
    c.line(cx + 2, cy - 1, cx + 2, cy + 1, DUML)
    c.set(cx, cy - 2, DUML)                 # twist top
    c.set(cx - 1, cy - 2, DUMP_HL)
    c.set(cx - 1, cy - 1, BAM_HL)

dumpling(21, 13)   # back dumpling
dumpling(25, 16)   # front-right
dumpling(18, 18)   # front-left

# --- steam ---
c.circle(19, 8, 1, STEAM2)
c.circle(21, 5, 1, STEAM2)
c.circle(21, 2, 1, STEAM)
c.set(19, 6, STEAM)
c.set(22, 4, STEAM)

# nudge up 1 and right 1 so the bottom rim isn't clipped
c.shift(1, -1)

print(c.stats_text())
print(c.matrix_text())
finish(c)
