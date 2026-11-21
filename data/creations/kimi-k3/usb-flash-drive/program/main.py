# ============================================================
# USB flash drive - 32x32 RPG item portrait
# metal casing / USB connector / keychain strap / dark outline
# transparent background
# ============================================================

c = new_canvas(32, 32, name="usb_flash_drive")

# ---------- palette ----------
OUT      = "#1b1b25"   # dark outline
MET_HI   = "#f2f5f9"   # metal highlight
MET_LT   = "#cbd1da"   # light metal
MET_MD   = "#9aa1ac"   # mid metal
MET_DK   = "#666b77"   # dark metal
CON_LT   = "#dde1e8"   # connector metal light
CON_DK   = "#8d929d"   # connector shade
HOLE     = "#343843"   # connector openings
STRAP    = "#31405f"   # strap navy
STRAP_HI = "#5a6b93"   # strap highlight
ACCENT   = "#45d1a7"   # activity LED

# ---------- USB connector (metal plug, left) ----------
c.rect(2, 14, 8, 7, OUT)          # outline  x2..9  y14..20
c.rect(3, 15, 6, 5, CON_LT)       # interior x3..8  y15..19
c.line(3, 15, 8, 15, MET_HI)      # top sheen
c.line(3, 19, 8, 19, CON_DK)      # bottom shade
c.rect(3, 16, 2, 2, HOLE)         # contact opening A
c.rect(6, 16, 2, 2, HOLE)         # contact opening B
c.set(2, 14, None)                # chamfered plug tip
c.set(2, 20, None)

# ---------- metal casing (body) ----------
c.rect(9, 12, 15, 10, OUT)        # outline  x9..23 y12..21
c.rect(10, 13, 13, 8, MET_MD)     # interior base x10..22 y13..20
c.line(10, 13, 22, 13, MET_HI)    # top highlight
c.line(10, 14, 22, 14, MET_LT)
c.line(10, 15, 22, 15, MET_LT)
c.line(10, 19, 22, 19, MET_DK)    # bottom shade
c.line(10, 20, 22, 20, MET_DK)
c.line(10, 14, 10, 18, MET_HI)    # left edge sheen
# chamfered corners
c.set(9, 12, None)
c.set(23, 12, None)
c.set(9, 21, None)
c.set(23, 21, None)
# eyelet hole where the strap attaches
c.set(22, 16, HOLE)
# activity LED (accent)
c.set(18, 19, ACCENT)
c.set(19, 19, ACCENT)

# ---------- keychain strap (loop at right end) ----------
c.circle(27, 16, 3, OUT)          # outer dark ring
c.circle(27, 16, 2, STRAP)        # navy strap band
c.circle(27, 16, 1, None)         # punch the hole
c.set(26, 14, STRAP_HI)           # strap sheen
c.set(25, 15, STRAP_HI)

view(c)
finish(c)
