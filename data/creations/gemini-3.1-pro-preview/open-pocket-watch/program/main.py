import math
from pixelbench_api import *

c = new_canvas(64, 64)

# Palette
colors = {
    "bg": "#0a0a0c",
    "black": "#050505",
    "dark_brown": "#1a0f00",
    "gold_shadow": "#332200",
    "gold_dark": "#593d00",
    "gold_base": "#8c6200",
    "gold_light": "#c6930a",
    "gold_highlight": "#f2cc49",
    "white_highlight": "#ffffff",
    "silver_shadow": "#2a2d34",
    "silver_base": "#6c727a",
    "silver_light": "#aab0b8",
    "silver_highlight": "#e5e7eb",
    "dial_bg": "#f4f1ea",
    "dial_shadow": "#d0c8b0",
    "ruby": "#d91a36",
    "ruby_dark": "#660011",
    "hand_color": "#0d131f",
    "hand_highlight": "#2d3748"
}
for k, v in colors.items():
    c.color(v, k)

c.rect(0, 0, 64, 64, "bg")

cx, cy = 40, 38
r_outer = 21

# Shadow under the watch and lid
c.ellipse(cx + 4, cy + 4, r_outer + 2, r_outer - 2, "black")
c.ellipse(14, cy + 6, 10, 17, "black")

# Chain
for i in range(15):
    tx = 40 + i * 1.8
    ty = 8 - i * 1.2
    if ty < -2: continue
    c.circle(int(tx), int(ty), 1, "gold_light", fill=False)
    c.set(int(tx)-1, int(ty), "gold_dark")

# Bow
c.circle(cx, 9, 6, "gold_shadow")
c.circle(cx, 9, 5, "gold_base")
c.circle(cx, 9, 4, "bg")
c.circle(cx, 9, 3, "bg")
c.set(cx-4, 9, "gold_highlight")
c.set(cx-5, 8, "gold_highlight")
c.set(cx+4, 9, "gold_highlight")

# Stem
c.rect(cx-3, 15, 7, 4, "gold_shadow")
c.rect(cx-2, 15, 5, 4, "gold_base")
c.rect(cx-1, 15, 2, 4, "gold_highlight")
c.rect(cx-2, 13, 5, 2, "gold_dark")
c.rect(cx-1, 13, 3, 2, "gold_light")

# Lid
hinge_x = cx - r_outer + 1
c.rect(hinge_x - 2, cy - 4, 4, 9, "gold_dark")
c.rect(hinge_x - 1, cy - 3, 2, 7, "gold_highlight")

lid_cx = hinge_x - 8
lid_rx = 8
lid_ry = 21
c.ellipse(lid_cx, cy, lid_rx, lid_ry, "gold_shadow")
c.ellipse(lid_cx, cy, lid_rx-1, lid_ry-1, "gold_dark")
c.ellipse(lid_cx-1, cy, lid_rx-2, lid_ry-2, "gold_base")
c.ellipse(lid_cx-2, cy, lid_rx-4, lid_ry-3, "gold_light")
c.ellipse(lid_cx-3, cy, lid_rx-5, lid_ry-5, "gold_highlight")
c.ellipse(lid_cx-4, cy, lid_rx-6, lid_ry-7, "white_highlight")
c.rect(lid_cx - lid_rx - 2, cy - 2, 3, 5, "gold_base")
c.rect(lid_cx - lid_rx - 2, cy - 1, 1, 3, "gold_highlight")

# Main Case
c.circle(cx, cy, r_outer, "gold_shadow")
c.circle(cx, cy, r_outer-1, "gold_dark")
c.circle(cx, cy, r_outer-2, "gold_base")
c.circle(cx, cy, r_outer-3, "gold_light")
c.circle(cx, cy, r_outer-4, "gold_highlight")
c.circle(cx, cy, r_outer-5, "gold_base")
c.circle(cx, cy, r_outer-6, "gold_dark")
c.circle(cx, cy, r_outer-7, "gold_shadow")

# Case highlights and shadows
c.path(f"M {cx-r_outer+2} {cy-5} A {r_outer-2} {r_outer-2} 0 0 1 {cx-5} {cy-r_outer+2}", "white_highlight", fill=False)
c.path(f"M {cx-r_outer+3} {cy-5} A {r_outer-3} {r_outer-3} 0 0 1 {cx-5} {cy-r_outer+3}", "gold_highlight", fill=False)
c.path(f"M {cx+5} {cy+r_outer-2} A {r_outer-2} {r_outer-2} 0 0 0 {cx+r_outer-2} {cy+5}", "black", fill=False)
c.path(f"M {cx+5} {cy+r_outer-3} A {r_outer-3} {r_outer-3} 0 0 0 {cx+r_outer-3} {cy+5}", "gold_shadow", fill=False)

# Dial ring
r_dial_outer = r_outer - 7
r_dial_inner = r_outer - 12
c.circle(cx, cy, r_dial_outer, "dial_shadow")
c.circle(cx, cy, r_dial_outer-1, "dial_bg")
c.circle(cx, cy, r_dial_inner, "black")

# Tick marks
for i in range(60):
    if i % 5 != 0:
        angle = i * math.pi / 30 - math.pi/2
        x1 = cx + math.cos(angle) * 12
        y1 = cy + math.sin(angle) * 12
        x2 = cx + math.cos(angle) * 13
        y2 = cy + math.sin(angle) * 13
        c.line(int(x1), int(y1), int(x2), int(y2), "dial_shadow")

for i in range(12):
    angle = i * math.pi / 6 - math.pi/2
    x1 = cx + math.cos(angle) * 10
    y1 = cy + math.sin(angle) * 10
    x2 = cx + math.cos(angle) * 13
    y2 = cy + math.sin(angle) * 13
    c.line(int(x1), int(y1), int(x2), int(y2), "black")
    if i % 3 == 0:
        x3 = cx + math.cos(angle+0.05) * 13
        y3 = cy + math.sin(angle+0.05) * 13
        c.line(int(x1), int(y1), int(x3), int(y3), "black")

# Skeleton internals
c.circle(cx, cy, r_dial_inner-1, "dark_brown")

def draw_gear(x, y, r, color_base, color_light, color_shadow, teeth=True, spokes=False):
    if teeth:
        c.circle(x, y, r, color_shadow)
        c.circle(x, y, r-1, color_base)
        for i in range(int(r*3)):
            angle = i * 2 * math.pi / int(r*3)
            tx = x + math.cos(angle) * r
            ty = y + math.sin(angle) * r
            c.set(int(tx), int(ty), color_light)
    else:
        c.circle(x, y, r, color_base)
        
    if spokes and r >= 4:
        c.circle(x, y, r-2, "dark_brown")
        for i in range(8):
            angle = i * math.pi / 4
            c.line(x, y, int(x + math.cos(angle)*(r-1)), int(y + math.sin(angle)*(r-1)), color_base)
    else:
        c.circle(x, y, r-1, color_base)
        c.circle(x-1, y-1, r//2, color_light)
        
    c.circle(x, y, 1, color_shadow)
    c.set(x, y, "ruby")

draw_gear(cx - 3, cy - 3, 5, "gold_base", "gold_highlight", "gold_shadow", spokes=True)
draw_gear(cx + 4, cy - 4, 4, "silver_base", "silver_highlight", "silver_shadow", spokes=True)
draw_gear(cx + 3, cy + 4, 4, "gold_dark", "gold_light", "gold_shadow", spokes=False)
draw_gear(cx - 4, cy + 4, 3, "silver_base", "silver_light", "silver_shadow", spokes=False)

# Bridges
b1_pts = [(cx-7, cy-2), (cx-3, cy-7), (cx+1, cy-7), (cx+4, cy-2), (cx-1, cy+2)]
c.poly(b1_pts, "gold_base")
c.poly([(px, py-1) for px, py in b1_pts], "gold_light")
c.set(cx-2, cy-5, "silver_highlight")
c.set(cx, cy-4, "ruby")
c.set(cx+1, cy-4, "ruby_dark")

b2_pts = [(cx+2, cy+2), (cx+7, cy-2), (cx+7, cy+5), (cx+3, cy+7)]
c.poly(b2_pts, "silver_base")
c.poly([(px, py-1) for px, py in b2_pts], "silver_light")
c.set(cx+5, cy+3, "ruby")
c.set(cx+4, cy+5, "gold_highlight")

# Center pinion
draw_gear(cx, cy, 2, "gold_base", "gold_highlight", "gold_shadow", teeth=False)

# Hands
angle_h = -math.pi * 5 / 6
hx = cx + int(math.cos(angle_h) * 6)
hy = cy + int(math.sin(angle_h) * 6)
c.line(cx, cy, hx, hy, "hand_color")
c.line(cx, cy-1, hx, hy-1, "hand_highlight")

angle_m = -math.pi * 1 / 6
mx = cx + int(math.cos(angle_m) * 11)
my = cy + int(math.sin(angle_m) * 11)
c.line(cx, cy, mx, my, "hand_color")
c.line(cx, cy-1, mx, my-1, "hand_highlight")

angle_s = math.pi / 2
sx = cx + int(math.cos(angle_s) * 12)
sy = cy + int(math.sin(angle_s) * 12)
c.line(cx, cy, sx, sy, "ruby_dark")
c.circle(cx, cy, 1, "ruby")

finish(c)
