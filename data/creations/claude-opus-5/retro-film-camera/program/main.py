c = new_canvas(32, 32, name="output")

# ---- palette ----
OUT = c.color("#140e10", "outline")
LTH_D = c.color("#2a1e1d", "leather_dark")
LTH = c.color("#3e2d29", "leather")
LTH_M = c.color("#342523", "leather_mid")
LTH_L = c.color("#55403a", "leather_light")
CHR_D = c.color("#55555f", "chrome_dark")
CHR = c.color("#8a8a97", "chrome")
CHR_L = c.color("#c9c9d6", "chrome_light")
GLASS_D = c.color("#0f1c2e", "glass_dark")
GLASS = c.color("#26497c", "glass")
GLASS_L = c.color("#3f72a4", "glass_light")
GLASS_H = c.color("#cbe8f8", "glass_hi")
RED = c.color("#a83331", "red")
RED_L = c.color("#dd6a5a", "red_light")

# ---- round disc helper (hand-tuned half widths) ----
HW = {5: [5, 5, 5, 4, 3, 2],
      4: [4, 4, 4, 3, 2],
      3: [3, 3, 2, 1],
      2: [2, 2, 1],
      1: [1, 1]}


def disc(cx, cy, r, col):
    for dy in range(-r, r + 1):
        hw = HW[r][abs(dy)]
        c.rect(cx - hw, cy + dy, 2 * hw + 1, 1, col)


def ring_shade(cx, cy, r_out, r_in, hi, mid, lo):
    """Shade the annulus between two discs by light direction (upper-left)."""
    for dy in range(-r_out, r_out + 1):
        hw = HW[r_out][abs(dy)]
        for dx in range(-hw, hw + 1):
            inside = abs(dy) <= r_in and abs(dx) <= HW[r_in][abs(dy)]
            if inside:
                continue
            t = dx + dy
            c.set(cx + dx, cy + dy, hi if t <= -3 else (lo if t >= 3 else mid))


# ================= outline silhouette (1px oversize) =================
c.rect(11, 3, 11, 5, OUT)      # prism hump
c.rect(5, 4, 7, 4, OUT)        # rewind knob block
c.rect(20, 4, 7, 4, OUT)       # shutter / wind block
c.rect(3, 6, 26, 5, OUT)       # top plate
c.rect(2, 9, 28, 18, OUT)      # body

# ================= top deck =================
# prism (viewfinder hump)
c.rect(12, 4, 9, 3, CHR_D)
c.rect(13, 4, 7, 2, CHR)
c.line(13, 4, 15, 4, CHR_L)

# rewind knob, left
c.rect(6, 5, 5, 2, CHR_D)
c.line(6, 5, 8, 5, CHR)

# shutter button + wind lever, right
c.rect(21, 5, 5, 2, CHR_D)
c.line(21, 5, 25, 5, CHR)
c.rect(22, 3, 3, 2, OUT)
c.rect(22, 3, 3, 1, RED)
c.set(22, 3, RED_L)

# top plate
c.rect(4, 7, 24, 3, CHR_D)
c.rect(4, 7, 24, 2, CHR)
c.line(5, 7, 26, 7, CHR_L)

# ================= body (leather) =================
c.rect(3, 10, 26, 16, LTH_D)
c.rect(4, 11, 24, 13, LTH)
c.line(4, 11, 27, 11, LTH_L)

# leather grain: fine checker on the two front panels, lens area left clear
c.dither(4, 12, 7, 12, [LTH, LTH_M], pattern="checker")
c.dither(22, 12, 6, 12, [LTH, LTH_M], pattern="checker")
# a few lighter flecks for texture variation
for (gx, gy) in [(5, 14), (8, 17), (6, 19), (9, 22), (23, 16),
                 (26, 18), (24, 20), (27, 13)]:
    c.set(gx, gy, LTH_L)

# bottom plate
c.rect(3, 24, 26, 2, CHR_D)
c.line(4, 24, 27, 24, CHR)

# ================= lens =================
disc(16, 17, 5, OUT)
disc(16, 17, 4, CHR)
ring_shade(16, 17, 4, 3, CHR_L, CHR, CHR_D)
disc(16, 17, 3, GLASS_D)
disc(16, 17, 2, GLASS)
# a clean crescent highlight on the upper-left of the glass
c.line(14, 16, 15, 15, GLASS_L)
c.set(16, 15, GLASS_L)
c.set(15, 16, GLASS_H)
# shaded lower-right of the glass
c.line(17, 18, 18, 18, GLASS_D)
c.set(17, 19, GLASS_D)

# ================= front furniture =================
# rangefinder window, left of lens
c.rect(5, 12, 4, 3, OUT)
c.rect(5, 12, 4, 2, GLASS_L)
c.set(5, 12, GLASS_H)
# self-timer lever, right of lens
c.rect(23, 12, 4, 3, OUT)
c.rect(23, 12, 4, 2, CHR_D)
c.set(26, 12, CHR)
# strap lugs on the shoulders
c.rect(1, 10, 2, 3, OUT)
c.rect(29, 10, 2, 3, OUT)
c.set(1, 11, CHR)
c.set(30, 11, CHR)

# small nameplates
c.line(23, 21, 26, 21, CHR_D)
c.line(5, 21, 8, 21, CHR_D)

view(c)
save("retro-film-camera", c)
finish(c)
