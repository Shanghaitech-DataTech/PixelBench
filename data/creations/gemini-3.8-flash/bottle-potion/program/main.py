# Purple potion palette:
DEEP_PURPLE = (45, 12, 65, 255)       # #2D0C41 - deep shadow / surface base
SURFACE_PURPLE = (75, 20, 105, 255)   # #4B1469 - surface ellipse base
SHADOW_PURPLE = (95, 25, 130, 255)    # #5F1982 - body shadow near edges/bottom
MID_PURPLE = (135, 40, 180, 255)      # #8728B4 - main liquid body
BRIGHT_PURPLE = (175, 65, 225, 255)   # #AF41E1 - inner glow
GLOW_MAGENTA = (215, 95, 245, 255)    # #D75FF5 - glowing magical aura
LIGHT_LAVENDER = (240, 185, 255, 255) # #F0B9FF - bubble body / soft highlight
BUBBLE_WHITE = (255, 255, 255, 255)   # #FFFFFF - glint / sparkle

# Reconstruct 32x32 grid from input
grid = []
for Y in range(32):
    grid.append([input_canvas.get(X*2, Y*2) for X in range(32)])

canvas32 = [[input_canvas.palette()[grid[Y][X]]['rgba'] for X in range(32)] for Y in range(32)]

# Fill base potion
for Y in range(32):
    for X in range(32):
        if grid[Y][X] == 5:
            # Surface ellipse
            canvas32[Y][X] = list(SURFACE_PURPLE)
        elif grid[Y][X] == 9:
            # Bottom rim of surface ellipse
            canvas32[Y][X] = list(DEEP_PURPLE)
        elif grid[Y][X] in (6, 7, 8, 10):
            # Smooth radial glow in liquid body
            dx = (X - 14) * 1.0
            dy = (Y - 25) * 1.3
            dist = (dx*dx + dy*dy) ** 0.5
            if dist > 8.0 or Y >= 29:
                canvas32[Y][X] = list(SHADOW_PURPLE)
            elif dist > 5.2:
                canvas32[Y][X] = list(MID_PURPLE)
            elif dist > 2.8:
                canvas32[Y][X] = list(BRIGHT_PURPLE)
            else:
                canvas32[Y][X] = list(GLOW_MAGENTA)

# Helper functions for drawing bubbles in 32x32:
def put_pixel(x, y, color):
    if 0 <= x < 32 and 0 <= y < 32:
        canvas32[y][x] = list(color)

def bubble_1px(x, y, col=BUBBLE_WHITE):
    put_pixel(x, y, col)

def bubble_2x2(x, y, shadow=DEEP_PURPLE):
    put_pixel(x, y, BUBBLE_WHITE)
    put_pixel(x+1, y, LIGHT_LAVENDER)
    put_pixel(x, y+1, LIGHT_LAVENDER)
    put_pixel(x+1, y+1, shadow)

def bubble_3x3_diamond(x, y, shadow=DEEP_PURPLE):
    # center is (x, y)
    put_pixel(x, y-1, LIGHT_LAVENDER)
    put_pixel(x-1, y, LIGHT_LAVENDER)
    put_pixel(x, y, BUBBLE_WHITE)
    put_pixel(x+1, y, GLOW_MAGENTA)
    put_pixel(x, y+1, shadow)

def air_bubble_2x2(x, y):
    # 2x2 bubble with solid colored edges so it reads against white
    put_pixel(x, y, LIGHT_LAVENDER)
    put_pixel(x+1, y, BRIGHT_PURPLE)
    put_pixel(x, y+1, BRIGHT_PURPLE)
    put_pixel(x+1, y+1, MID_PURPLE)

def air_bubble_3x3(x, y):
    # 3x3 bubble centered at (x, y)
    put_pixel(x, y-1, BRIGHT_PURPLE)
    put_pixel(x-1, y, BRIGHT_PURPLE)
    put_pixel(x, y, LIGHT_LAVENDER)
    put_pixel(x+1, y, BRIGHT_PURPLE)
    put_pixel(x, y+1, MID_PURPLE)

def magic_sparkle(x, y):
    # 4-point sparkle, center (x, y)
    put_pixel(x, y-1, GLOW_MAGENTA)
    put_pixel(x-1, y, GLOW_MAGENTA)
    put_pixel(x, y, BUBBLE_WHITE)
    put_pixel(x+1, y, GLOW_MAGENTA)
    put_pixel(x, y+1, GLOW_MAGENTA)

# 1. Rising bubbles inside liquid body (Y=22..29):
bubble_3x3_diamond(9, 24, SHADOW_PURPLE)
bubble_3x3_diamond(18, 25, SHADOW_PURPLE)

bubble_2x2(13, 23, MID_PURPLE)
bubble_2x2(14, 27, SHADOW_PURPLE)
bubble_2x2(6, 24, SHADOW_PURPLE)
bubble_2x2(21, 24, SHADOW_PURPLE)

for bx, by in [(8, 27), (11, 26), (16, 23), (19, 27)]:
    bubble_1px(bx, by, BUBBLE_WHITE)

for bx, by in [(12, 28), (10, 22), (18, 22), (7, 26), (20, 26)]:
    bubble_1px(bx, by, LIGHT_LAVENDER)

# 2. Bubbles on the surface ellipse (Y=13..21):
bubble_2x2(8, 16)
bubble_2x2(14, 15)
bubble_2x2(20, 16)
bubble_2x2(11, 18)
bubble_2x2(17, 18)

for bx, by in [(6, 17), (11, 14), (17, 14), (22, 17), (14, 20)]:
    bubble_1px(bx, by, LIGHT_LAVENDER)

for bx, by in [(9, 15), (15, 17)]:
    bubble_1px(bx, by, BUBBLE_WHITE)

# 3. Floating bubbles & sparkles in the air inside the bottle (Y=7..11):
# Floating bubble 1 at (10, 10)
air_bubble_3x3(10, 10)

# Floating bubble 2 at (18, 8)
air_bubble_2x2(18, 8)

# Magic sparkle at (14, 9)
magic_sparkle(14, 9)

# Tiny rising bubble dot at (12, 7) and (20, 10)
bubble_1px(12, 7, GLOW_MAGENTA)
bubble_1px(20, 10, GLOW_MAGENTA)

# Create 64x64 output canvas
out = new_canvas(64, 64, name="output")
for Y in range(32):
    for X in range(32):
        col = canvas32[Y][X]
        for dy in range(2):
            for dx in range(2):
                out.set(X*2 + dx, Y*2 + dy, col)

view(out)
finish(out)
