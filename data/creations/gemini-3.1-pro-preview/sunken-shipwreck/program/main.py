import math
from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64)

# Background water gradient
water_colors = [
    c.color('#003B5C'),
    c.color('#003452'),
    c.color('#002D48'),
    c.color('#00253E'),
    c.color('#001E34'),
    c.color('#00172A'),
    c.color('#001020')
]

for y in range(64):
    idx = min(len(water_colors) - 1, int((y / 64.0) * len(water_colors)))
    c.line(0, y, 63, y, water_colors[idx])

# Light rays
ray_color = c.color('#20557740')
c.poly([(0,0), (20,0), (63,40), (63,60)], ray_color)
ray_color2 = c.color('#20557720')
c.poly([(30,0), (45,0), (63,20), (63,35)], ray_color2)

# Shipwreck
wood_dark = c.color('#2C1E16')
wood_mid = c.color('#4A3324')
wood_light = c.color('#684A33')

# Main hull shape
c.path("M 5 60 L 15 40 Q 25 35 45 38 L 55 50 L 55 60 Z", wood_dark)
c.path("M 7 60 L 16 42 Q 25 37 43 40 L 52 50 L 52 60 Z", wood_mid)

# Planking lines
c.path("M 16 42 Q 25 37 43 40", wood_dark, fill=False)
c.path("M 15 46 Q 25 42 45 44", wood_dark, fill=False)
c.path("M 14 50 Q 25 47 48 48", wood_dark, fill=False)
c.path("M 13 54 Q 25 52 50 52", wood_dark, fill=False)

# Broken ribs sticking out
c.line(18, 40, 14, 28, wood_light)
c.line(19, 40, 15, 28, wood_dark)

c.line(24, 38, 22, 25, wood_light)
c.line(25, 38, 23, 25, wood_dark)

c.line(30, 37, 30, 24, wood_light)
c.line(31, 37, 31, 24, wood_dark)

c.line(36, 38, 38, 26, wood_light)
c.line(37, 38, 39, 26, wood_dark)

# Broken mast
c.line(45, 38, 10, 15, wood_dark)
c.line(46, 38, 11, 15, wood_mid)
c.line(47, 39, 12, 16, wood_light)

# Sand
sand_dark = c.color('#6B5B45')
sand_mid = c.color('#8A7855')
sand_light = c.color('#A39065')

for x in range(64):
    y_sand = 48 + int(3 * math.sin(x/8.0) + 2 * math.cos(x/4.0))
    c.line(x, y_sand, x, 63, sand_dark)
    c.line(x, y_sand, x, y_sand+4, sand_mid)
    c.set(x, y_sand, sand_light)

# Anchor and rust
iron_dark = c.color('#222222')
iron_mid = c.color('#444444')
rust1 = c.color('#8A3324')
rust2 = c.color('#B7410E')

c.line(40, 52, 50, 52, iron_dark)
c.circle(38, 52, 2, iron_mid, fill=False)
c.path("M 48 47 Q 52 52 48 57", iron_dark, fill=False)
c.set(48, 47, iron_mid)
c.set(48, 57, iron_mid)
c.set(42, 52, rust1)
c.set(45, 52, rust2)
c.set(50, 50, rust1)

# Seaweed
seaweed_d = c.color('#004D28')
seaweed_m = c.color('#00753A')
seaweed_l = c.color('#00A854')

def draw_kelp(x, y, h):
    for i in range(h):
        dx = int(1.5 * math.sin((y-i)/3.0))
        c.set(x+dx, y-i, seaweed_d)
        c.set(x+dx+1, y-i, seaweed_m)
        if i % 2 == 0:
            c.set(x+dx+2, y-i, seaweed_l)

draw_kelp(5, 55, 20)
draw_kelp(8, 58, 25)
draw_kelp(55, 52, 15)
draw_kelp(60, 55, 18)

# Corals
coral_pink1 = c.color('#FF6B81')
coral_pink2 = c.color('#FF4757')
coral_purp1 = c.color('#A55EEA')
coral_purp2 = c.color('#8854D0')
coral_y = c.color('#ECCC68')
coral_y2 = c.color('#FFA502')

c.circle(20, 45, 3, coral_pink2)
c.circle(20, 45, 2, coral_pink1)
c.circle(24, 48, 2, coral_purp2)
c.circle(24, 48, 1, coral_purp1)
c.circle(45, 42, 2, coral_pink2)
c.set(45, 42, coral_pink1)
c.ellipse(15, 52, 4, 3, coral_y2)
c.ellipse(15, 52, 3, 2, coral_y)

# School of fish
fish_base = c.color('#70A1FF')
fish_high = c.color('#1E90FF')
fish_tail = c.color('#5352ED')

def fish(x, y):
    c.set(x, y, fish_high)
    c.set(x+1, y, fish_base)
    c.set(x+2, y, fish_base)
    c.set(x+3, y-1, fish_tail)
    c.set(x+3, y+1, fish_tail)

def small_fish(x, y):
    c.set(x, y, fish_high)
    c.set(x+1, y, fish_base)
    c.set(x+2, y, fish_tail)

fish(25, 15)
fish(30, 12)
fish(28, 18)
fish(35, 14)
fish(33, 20)
fish(40, 16)
fish(20, 17)

small_fish(45, 12)
small_fish(48, 15)
small_fish(42, 18)
small_fish(50, 10)

# Bubbles
bubble = c.color('#FFFFFF60')
c.set(20, 25, bubble)
c.set(21, 22, bubble)
c.set(19, 18, bubble)
c.set(22, 14, bubble)

finish(c)
