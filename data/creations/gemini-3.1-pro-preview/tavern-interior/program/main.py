import pixelbench_api as api

# Colors
C_OUTLINE = '#1a0f0f'

C_WALL_DK = '#261410'
C_WALL_MD = '#381e17'
C_WALL_HL = '#522f22'
C_FLOOR = '#1c0f0b'

C_SHELF_DK = '#2c1812'
C_SHELF_MD = '#4a2a1f'
C_SHELF_LT = '#6b3e2e'

C_BOTTLE_1 = '#2e7d32' # Green
C_BOTTLE_2 = '#1565c0' # Blue
C_BOTTLE_3 = '#c62828' # Red
C_BOTTLE_4 = '#d84315' # Orange
C_BOTTLE_HL = '#ffffff'

C_COUNTER_DK = '#361c14'
C_COUNTER_MD = '#573224'
C_COUNTER_LT = '#7d4a35'

C_STOOL_BASE = '#24120d'
C_STOOL_SEAT = '#7a2211'
C_STOOL_SEAT_HL = '#a6331c'

C_GLASS = '#81d4fa'
C_GLASS_HL = '#e1f5fe'

C_LAMP_CAP = '#2e1812'
C_LIGHT = '#ffeb3b'
C_LIGHT_GLOW = '#ffb300'

C_SMOKE = '#4a3b32'

# Canvases
bg = api.new_canvas(64, 64, name="bg")
shelf_bg = api.new_canvas(64, 64, name="shelf_bg")
bottles = api.new_canvas(64, 64, name="bottles")
mid = api.new_canvas(64, 64, name="mid")
fx = api.new_canvas(64, 64, name="fx")
counter = api.new_canvas(64, 64, name="counter")
glasses = api.new_canvas(64, 64, name="glasses")
stools = api.new_canvas(64, 64, name="stools")
fg = api.new_canvas(64, 64, name="fg")
lamps = api.new_canvas(64, 64, name="lamps")

# 1. Background
bg.rect(0, 0, 64, 40, C_WALL_MD)
bg.circle(20, 14, 18, C_WALL_HL)
bg.circle(44, 14, 18, C_WALL_HL)

for y in range(0, 40, 8):
    bg.line(0, y, 64, y, C_WALL_DK)
for x in range(8, 64, 16):
    bg.line(x, 0, x, 40, C_WALL_DK)

bg.rect(0, 40, 64, 24, C_FLOOR)
for y in range(40, 64, 4):
    bg.line(0, y, 64, y, C_WALL_DK)

# 2. Shelf Background
shelf_bg.rect(8, 8, 48, 24, C_SHELF_DK)
shelf_bg.rect(8, 16, 48, 2, C_SHELF_MD)
shelf_bg.rect(8, 28, 48, 2, C_SHELF_MD)
shelf_bg.rect(6, 8, 2, 24, C_SHELF_LT)
shelf_bg.rect(56, 8, 2, 24, C_SHELF_LT)
shelf_bg.outline(C_OUTLINE)

# 3. Bottles
def draw_bottle(c, x, y, w, h, neck_w, neck_h, color):
    c.rect(x, y - h, w, h, color)
    c.rect(x + (w - neck_w)//2, y - h - neck_h, neck_w, neck_h, color)
    c.line(x, y - h, x, y - 1, C_BOTTLE_HL)

draw_bottle(bottles, 12, 16, 4, 5, 2, 2, C_BOTTLE_1)
draw_bottle(bottles, 18, 16, 3, 4, 1, 3, C_BOTTLE_2)
draw_bottle(bottles, 24, 16, 5, 6, 3, 2, C_BOTTLE_3)
draw_bottle(bottles, 32, 16, 4, 4, 2, 2, C_BOTTLE_4)
draw_bottle(bottles, 38, 16, 3, 5, 1, 2, C_BOTTLE_1)
draw_bottle(bottles, 46, 16, 4, 6, 2, 3, C_BOTTLE_2)

draw_bottle(bottles, 24, 28, 3, 6, 1, 2, C_BOTTLE_2)
draw_bottle(bottles, 30, 28, 4, 8, 2, 3, C_BOTTLE_3)
draw_bottle(bottles, 36, 28, 6, 4, 2, 2, C_BOTTLE_4)
draw_bottle(bottles, 44, 28, 3, 5, 1, 3, C_BOTTLE_1)
draw_bottle(bottles, 50, 28, 4, 6, 2, 2, C_BOTTLE_2)
bottles.outline(C_OUTLINE)

# 4. Mid Barrel
mid.rect(10, 18, 10, 10, C_COUNTER_DK)
mid.rect(9, 19, 12, 8, C_COUNTER_MD)
mid.rect(9, 20, 12, 2, C_OUTLINE)
mid.rect(9, 24, 12, 2, C_OUTLINE)
mid.rect(14, 22, 2, 2, C_OUTLINE)
mid.outline(C_OUTLINE)

# 5. Smoke
for i in range(5):
    fx.ellipse(8 + i*11, 4 + (i%3)*3, 12, 2, C_SMOKE)
for i in range(4):
    fx.ellipse(18 + i*13, 10 + (i%2)*3, 14, 2, C_SMOKE)
fx.outline(C_OUTLINE)

# 6. Counter
counter.rect(0, 36, 64, 6, C_COUNTER_LT)
counter.rect(0, 42, 64, 10, C_COUNTER_MD)
counter.rect(0, 42, 64, 2, C_COUNTER_DK)
counter.rect(0, 50, 64, 2, C_COUNTER_DK)
for x in range(4, 64, 12):
    counter.rect(x, 44, 8, 6, C_COUNTER_DK)
counter.outline(C_OUTLINE)

# 7. Glasses
def draw_glass(c, x, y):
    c.rect(x, y, 4, 5, C_GLASS)
    c.line(x+3, y, x+3, y+4, C_GLASS_HL)

draw_glass(glasses, 16, 31)
draw_glass(glasses, 30, 31)
draw_glass(glasses, 44, 31)
glasses.outline(C_OUTLINE)

# 8. Stools
def draw_stool(c, x, y):
    c.rect(x+3, y+4, 6, 10, C_STOOL_BASE)
    c.rect(x+2, y+12, 8, 2, C_STOOL_BASE)
    c.rect(x, y, 12, 5, C_STOOL_SEAT)
    c.rect(x+1, y, 10, 2, C_STOOL_SEAT_HL)

draw_stool(stools, 14, 46)
draw_stool(stools, 34, 46)
stools.outline(C_OUTLINE)

# 9. Foreground Barrel
fg.rect(50, 42, 14, 18, C_COUNTER_MD)
fg.rect(49, 45, 16, 12, C_COUNTER_LT)
fg.rect(49, 47, 16, 2, C_OUTLINE)
fg.rect(49, 53, 16, 2, C_OUTLINE)
fg.outline(C_OUTLINE)

# 10. Lamps
def draw_lamp(c, x, y):
    c.rect(x-2, y, 5, 2, C_LAMP_CAP)
    c.rect(x-4, y+2, 9, 4, C_LIGHT_GLOW)
    c.rect(x-3, y+6, 7, 2, C_LIGHT_GLOW)
    c.rect(x-2, y+3, 5, 2, C_LIGHT)
    c.line(x, y+2, x, y+5, C_LIGHT)

draw_lamp(lamps, 20, 10)
draw_lamp(lamps, 44, 10)
lamps.outline(C_OUTLINE)
lamps.line(20, 0, 20, 9, C_OUTLINE)
lamps.line(44, 0, 44, 9, C_OUTLINE)

# Composite
result = api.flatten([bg, shelf_bg, bottles, mid, fx, counter, glasses, stools, fg, lamps])
api.finish(result)
