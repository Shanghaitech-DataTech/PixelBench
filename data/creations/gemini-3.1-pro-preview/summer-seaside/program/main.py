import random
from pixelbench_api import *

c = new_canvas(128, 128)

# Sky
c.rect(0, 0, 128, 25, "#63B8FF")
c.rect(0, 25, 128, 20, "#87CEFA")

# Sun
c.circle(110, 20, 12, "#FFD700")
c.circle(110, 20, 9, "#FFFF00")
c.circle(110, 20, 6, "#FFFFE0")

# Clouds
def cloud(cx, cy, r, color="#FFFFFF"):
    c.circle(cx, cy, r, color)
    c.circle(cx - int(r*1.2), cy + int(r*0.5), int(r*0.8), color)
    c.circle(cx + int(r*1.2), cy + int(r*0.5), int(r*0.8), color)
    c.rect(cx - int(r*1.2), cy + int(r*0.5), int(r*2.4), int(r*0.8) + 1, color)

cloud(30, 15, 6)
cloud(70, 10, 5)
cloud(95, 30, 4)
cloud(15, 35, 3)

# Gulls
def gull(gx, gy):
    c.path(f"M {gx} {gy} Q {gx+3} {gy-3} {gx+6} {gy} Q {gx+9} {gy-3} {gx+12} {gy} Q {gx+9} {gy-1} {gx+6} {gy+1} Q {gx+3} {gy-1} {gx} {gy} Z", "#FFFFFF")
    c.set(gx, gy, "#696969")
    c.set(gx+12, gy, "#696969")

gull(40, 25)
gull(60, 20)

# Sea
c.rect(0, 45, 128, 10, "#0055A4") # Deep blue
c.rect(0, 55, 128, 10, "#1E90FF") # Mid blue
c.rect(0, 65, 128, 10, "#20B2AA") # Teal
c.rect(0, 75, 128, 8, "#48D1CC")  # Lighter teal

# Sea highlights
random.seed(42)
for _ in range(40):
    x = random.randint(0, 120)
    y = random.randint(46, 80)
    w = random.randint(4, 12)
    if y < 55:
        color = "#1E90FF"
    elif y < 65:
        color = "#48D1CC"
    else:
        color = "#E0FFFF"
    c.line(x, y, x+w, y, color)

# Waves (Foam)
for i in range(-5, 130, 15):
    c.ellipse(i, 82, 10, 3, "#E0FFFF")
    c.ellipse(i+7, 84, 9, 2, "#FFFFFF")

# Sand
c.rect(0, 85, 128, 43, "#FFE4B5") # Base sand
c.rect(0, 100, 128, 28, "#DEB887")
c.rect(0, 115, 128, 13, "#D2B48C")

# Sand texture
for _ in range(150):
    x = random.randint(0, 127)
    y = random.randint(85, 127)
    c.set(x, y, "#CD853F")

# Umbrella shadow
c.ellipse(30, 112, 18, 6, "#CDA066")

# Sailboat
c.poly([(90, 48), (96, 48), (94, 51), (88, 51)], "#F5F5F5") # Hull
c.line(92, 48, 92, 36, "#A9A9A9") # Mast
c.poly([(91, 47), (91, 37), (86, 46)], "#FFFFFF") # Left sail
c.poly([(93, 47), (93, 38), (99, 46)], "#FFFFFF") # Right sail

# Beach Umbrella
# Pole
c.line(40, 90, 40, 115, "#8B4513")
c.line(41, 90, 41, 115, "#A0522D")

# Canopy
c.path("M 15 90 Q 40 60 65 90 Z", "#FF0000")
c.path("M 25 90 Q 40 68 55 90 Z", "#FFFFFF")
c.path("M 35 90 Q 40 75 45 90 Z", "#FF0000")

# Scallops
for i in range(15, 65, 10):
    if i in [15, 35, 55]:
        color = "#FF0000"
    else:
        color = "#FFFFFF"
    c.circle(i + 5, 90, 5, color)

# Towel
c.poly([(65, 105), (85, 98), (100, 110), (80, 117)], "#32CD32")
c.poly([(70, 103), (75, 101), (90, 113), (85, 115)], "#FFFFFF")
c.poly([(77, 100), (82, 98), (97, 110), (92, 112)], "#FFFFFF")

# Flip-flops
c.ellipse(55, 115, 3, 5, "#FF1493")
c.ellipse(63, 113, 3, 5, "#FF1493")
# Straps
c.line(55, 113, 53, 116, "#FFFFFF")
c.line(55, 113, 57, 116, "#FFFFFF")
c.line(63, 111, 61, 114, "#FFFFFF")
c.line(63, 111, 65, 114, "#FFFFFF")

finish(c)
