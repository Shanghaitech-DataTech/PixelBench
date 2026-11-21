from pixelbench_api import *

c = new_canvas(48, 48, background=None, name="sewing_machine")

# ---- palette ----
C_OUT   = c.color("#1b1e25", name="outline")
C_DARK  = c.color("#3a4150", name="body_dark")
C_MID   = c.color("#4d5566", name="body_mid")
C_LIGHT = c.color("#6b7488", name="body_light")
C_METAL = c.color("#aab3c2", name="metal")
C_NDL   = c.color("#d8dee8", name="needle")
C_GOLD  = c.color("#d4a72c", name="gold")
C_RED   = c.color("#c8323a", name="fabric_red")
C_REDD  = c.color("#8f2229", name="fabric_dark")
C_BLACK = c.color("#14161b", name="detail_black")

# ---- base (bed) ----
c.rect(2, 44, 45, 4, C_DARK)
c.rect(2, 44, 45, 1, C_MID)          # top edge light
c.rect(2, 47, 45, 1, C_BLACK)        # bottom shade
c.set(1, 45, C_DARK); c.set(1, 46, C_DARK)
c.set(47, 45, C_DARK); c.set(47, 46, C_DARK)
c.rect(4, 46, 41, 1, C_OUT)          # base seam line

# ---- pillar (left vertical body) ----
c.rect(5, 15, 11, 30, C_DARK)
c.rect(5, 15, 2, 30, C_MID)          # left shading
c.rect(13, 15, 3, 30, C_MID)
c.rect(14, 15, 1, 30, C_LIGHT)

# ---- arm (horizontal) ----
c.rect(15, 15, 19, 9, C_DARK)
c.rect(15, 15, 19, 1, C_MID)
c.rect(15, 22, 19, 2, C_MID)
c.rect(15, 23, 19, 1, C_LIGHT)

# ---- head (right vertical) ----
c.rect(33, 15, 9, 24, C_DARK)
c.rect(33, 15, 2, 24, C_MID)
c.rect(39, 15, 3, 24, C_MID)
c.rect(41, 15, 1, 24, C_LIGHT)
c.rect(35, 24, 5, 10, C_MID)         # face plate
c.rect(36, 25, 1, 8, C_LIGHT)

# ---- handwheel (angled: ellipse) ----
c.ellipse(6, 27, 4, 7, C_OUT, fill=True)
c.ellipse(6, 27, 3, 6, C_DARK, fill=True)
c.ellipse(6, 27, 2, 4, C_MID, fill=True)
c.ellipse(6, 27, 1, 2, C_LIGHT, fill=True)
c.set(6, 27, C_METAL)                # hub
# wheel spokes hint
c.line(6, 22, 6, 24, C_OUT)
c.line(6, 30, 6, 32, C_OUT)

# ---- bobbin winder + stitch dial ----
c.circle(13, 12, 2, C_OUT, fill=True)
c.circle(13, 12, 1, C_METAL, fill=True)
c.circle(10, 33, 2, C_OUT, fill=True)
c.circle(10, 33, 1, C_METAL, fill=True)
c.circle(10, 39, 2, C_OUT, fill=True)
c.circle(10, 39, 1, C_METAL, fill=True)

# ---- thread take-up lever ----
c.rect(30, 12, 2, 4, C_OUT)
c.set(30, 12, C_METAL); c.set(31, 12, C_METAL)

# ---- gold decal trim ----
c.rect(17, 19, 14, 1, C_GOLD)
c.rect(7, 20, 1, 6, C_GOLD)
c.rect(7, 36, 1, 5, C_GOLD)
c.set(20, 19, C_GOLD); c.set(24, 19, C_GOLD)

# ---- presser bar + foot ----
c.rect(34, 38, 2, 3, C_MID)          # presser bar
c.rect(32, 40, 6, 2, C_METAL)        # presser foot
c.rect(32, 41, 6, 1, C_OUT)

# ---- needle bar + needle ----
c.rect(38, 36, 1, 4, C_MID)
c.line(38, 40, 38, 43, C_NDL)
c.set(38, 44, C_NDL)

# ---- red fabric ----
c.rect(24, 41, 24, 3, C_RED)         # runs off right edge
c.rect(24, 41, 24, 1, C_REDD)        # fold shadow at top
c.line(28, 42, 34, 42, C_REDD)       # fabric fold
c.line(40, 43, 47, 43, C_REDD)
c.set(24, 44, C_REDD); c.set(25, 44, C_REDD)   # drape over base edge

# ---- unified outline ----
c.outline(C_OUT)

print(c.stats_text())
finish(c)
