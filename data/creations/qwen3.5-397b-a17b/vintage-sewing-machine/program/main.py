from pixelbench_api import *

# Create 48x48 canvas with transparent background
c = new_canvas(48, 48, background=None, name="sewing_machine")

# Define color palette (staying under 86 visible colors)
body_dark = c.color("#2a2a2a", "body_dark")
body_mid = c.color("#5a5a5a", "body_mid")
body_light = c.color("#7a7a7a", "body_light")
metal = c.color("#b8b8b8", "metal")
metal_bright = c.color("#d0d0d0", "metal_bright")
gold = c.color("#c9a227", "gold")
red_fabric = c.color("#c41e3a", "fabric")
red_dark = c.color("#8b0000", "fabric_shadow")
needle_color = c.color("#e0e0e0", "needle")
black_detail = c.color("#1a1a1a", "black_detail")
highlight = c.color("#f0f0f0", "highlight")

# === BASE (bottom platform) ===
# Main base body
c.rect(6, 36, 36, 8, body_dark, fill=True)
c.rect(6, 38, 36, 4, body_mid, fill=True)
c.rect(6, 40, 36, 2, body_light, fill=True)
# Base edge highlight
c.line(6, 40, 41, 40, highlight)

# === MAIN BODY (vertical column and arm) ===
# Vertical column on left
c.rect(8, 14, 14, 24, body_dark, fill=True)
c.rect(10, 14, 10, 24, body_mid, fill=True)
c.rect(12, 14, 6, 24, body_light, fill=True)

# Top arm extending right
c.rect(18, 12, 22, 6, body_dark, fill=True)
c.rect(18, 13, 22, 4, body_mid, fill=True)
c.rect(18, 14, 22, 2, body_light, fill=True)

# Head (right end of arm where needle is)
c.rect(38, 10, 6, 10, body_dark, fill=True)
c.rect(39, 11, 4, 8, body_mid, fill=True)

# === HANDWHEEL (right side, circular) ===
# Outer wheel
c.circle(42, 22, 5, body_dark, fill=True)
c.circle(42, 22, 4, body_mid, fill=True)
c.circle(42, 22, 3, body_light, fill=True)
# Center hub
c.circle(42, 22, 2, metal, fill=True)
c.circle(42, 22, 1, black_detail, fill=True)
# Wheel spokes/handle
c.line(42, 17, 42, 19, metal_bright)
c.line(42, 25, 42, 27, metal_bright)
c.line(37, 22, 39, 22, metal_bright)
c.line(45, 22, 47, 22, metal_bright)

# === NEEDLE BAR (vertical, going down from head) ===
c.rect(40, 20, 2, 14, metal, fill=True)
c.rect(40, 34, 2, 4, needle_color, fill=True)

# Needle point
c.set(41, 37, needle_color)
c.set(41, 38, needle_color)

# === PRESSER FOOT (holds fabric down) ===
# Presser foot holder
c.rect(38, 32, 6, 3, metal, fill=True)
# Presser foot itself
c.rect(37, 35, 8, 2, metal_bright, fill=True)
c.rect(38, 37, 6, 1, metal, fill=True)

# === RED FABRIC (under presser foot) ===
# Main fabric
c.rect(28, 41, 18, 4, red_fabric, fill=True)
# Fabric fold/shadow
c.rect(28, 43, 18, 2, red_dark, fill=True)
# Fabric edge highlight
c.line(28, 41, 45, 41, c.color("#e8586e"))
# Stitch line
c.line(30, 42, 44, 42, c.color("#a01028"))

# === STITCH PLATE (under needle) ===
c.rect(36, 39, 10, 2, metal_bright, fill=True)
c.rect(37, 40, 8, 1, metal, fill=True)
# Needle hole
c.set(41, 40, black_detail)

# === DECORATIVE DETAILS ===
# Gold trim on head
c.rect(39, 12, 4, 1, gold, fill=True)
c.rect(39, 17, 4, 1, gold, fill=True)

# Thread spool pin on top
c.rect(26, 6, 2, 6, metal, fill=True)
# Thread spool
c.rect(24, 4, 6, 4, red_dark, fill=True)
c.rect(25, 3, 4, 1, gold, fill=True)

# Thread guide
c.set(27, 10, metal_bright)
c.set(27, 11, metal_bright)

# Tension dial on front
c.circle(15, 20, 3, metal_bright, fill=True)
c.circle(15, 20, 2, metal, fill=True)
c.set(15, 20, black_detail)

# Bobbin area indicator
c.rect(20, 30, 8, 5, body_dark, fill=True)
c.rect(21, 31, 6, 3, body_mid, fill=True)

# === HIGHLIGHTS AND SHADING ===
# Body highlights
c.line(12, 15, 12, 37, highlight)
c.line(20, 13, 39, 13, highlight)

# Base shadow
c.rect(6, 43, 36, 1, black_detail, fill=True)

# === THREAD PATH (from spool to needle) ===
c.line(27, 8, 27, 14, c.color("#f5f5dc"))
c.line(27, 14, 35, 14, c.color("#f5f5dc"))
c.line(35, 14, 35, 20, c.color("#f5f5dc"))
c.line(35, 20, 40, 20, c.color("#f5f5dc"))
c.line(40, 20, 40, 34, c.color("#f5f5dc"))

# Check stats
print(c.stats_text())

# Submit
finish(c)
