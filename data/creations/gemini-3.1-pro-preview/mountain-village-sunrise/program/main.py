from pixelbench_api import new_canvas, flatten, finish

w, h = 128, 128

# Colors
C_SKY = [
    '#1a1c2c', # 0
    '#29366f', # 1
    '#3b5dc9', # 2
    '#5c8b93', # 3
    '#e89c78', # 4
]
C_SUN = '#ffffff'
C_SUN_GLOW = '#ffcd75'

C_MNT_FAR = '#5d275d'
C_MNT_FAR_S = '#491e49'
C_MNT_MID = '#331e36'
C_MNT_MID_S = '#251527'

C_HILL_B = '#415243'
C_HILL_M = '#313f33'
C_HILL_F = '#222b23'
C_GRASS = '#4a5e4c'

C_PINE_D = '#151e17'
C_PINE_M = '#1b261d'
C_PINE_L = '#253327'

C_WOOD_L = '#5c4033'
C_WOOD_M = '#4a332a'
C_WOOD_D = '#38261f'

C_ROOF_L = '#3c3c3c'
C_ROOF_M = '#2c2c2c'
C_ROOF_D = '#1f1f1f'

C_WIND = '#ffcd75'
C_WIND_G = '#e89c78'

C_PATH_L = '#505759'
C_PATH_M = '#3e4547'
C_PATH_D = '#2d3335'

C_SMOKE1 = '#b0b5b588'
C_SMOKE2 = '#8a919188'

def draw_sky(c):
    bands = [
        (0, 10, C_SKY[0], C_SKY[0]),
        (10, 20, C_SKY[0], C_SKY[1]),
        (20, 30, C_SKY[1], C_SKY[1]),
        (30, 40, C_SKY[1], C_SKY[2]),
        (40, 50, C_SKY[2], C_SKY[3]),
        (50, 60, C_SKY[3], C_SKY[4]),
        (60, 128, C_SKY[4], C_SKY[4])
    ]
    for y1, y2, c1, c2 in bands:
        if c1 == c2:
            c.rect(0, y1, w, y2-y1, c1)
        else:
            c.dither(0, y1, w, y2-y1, [c1, c2])
            
    # Sun
    c.circle(64, 61, 14, C_SUN_GLOW)
    c.circle(64, 61, 9, C_SUN)

def draw_mountains(c):
    # Far mountains base
    c.poly([(0, 80), (25, 55), (50, 75), (80, 45), (110, 65), (128, 50), (128, h), (0, h)], C_MNT_FAR)
    
    # Peak at 25: sun is right. Left side shadowed.
    c.poly([(0, 80), (25, 55), (25, h), (0, h)], C_MNT_FAR_S)
    
    # Peak at 80: sun is left. Right side shadowed.
    c.poly([(80, 45), (110, 65), (110, h), (80, h)], C_MNT_FAR_S)
    
    # Snow caps for far mountains
    c.poly([(25, 55), (18, 62), (25, 60)], '#9c7a9c')
    c.poly([(25, 55), (25, 60), (32, 62)], '#c0a0c0')
    
    c.poly([(80, 45), (70, 55), (75, 52), (80, 55)], '#c0a0c0')
    c.poly([(80, 45), (80, 55), (85, 52), (90, 55)], '#9c7a9c')
    
    c.poly([(128, 50), (120, 58), (128, 56)], '#c0a0c0')
    
    # Mid mountains base
    c.poly([(0, 95), (35, 65), (65, 85), (95, 55), (128, 80), (128, h), (0, h)], C_MNT_MID)
    
    c.poly([(0, 95), (35, 65), (35, h), (0, h)], C_MNT_MID_S)
    c.poly([(95, 55), (128, 80), (128, h), (95, h)], C_MNT_MID_S)

def draw_hills(c):
    c.ellipse(30, 105, 50, 20, C_HILL_B)
    c.ellipse(100, 110, 60, 25, C_HILL_B)
    c.ellipse(64, 115, 80, 20, C_HILL_M)
    c.rect(0, 115, w, h-115, C_HILL_F)
    
    for gx, gy in [(20, 105), (40, 110), (80, 112), (110, 115), (30, 120), (90, 122), (15, 125), (105, 126)]:
        c.line(gx, gy, gx-1, gy-2, C_GRASS)
        c.line(gx, gy, gx+1, gy-2, C_GRASS)
        c.set(gx, gy-1, C_GRASS)

def draw_pine(c, x, y, size, shadow_side='left'):
    w_base = int(4 * size)
    h_base = int(6 * size)
    c.rect(x-int(size)//2, y-int(size), max(1, int(size)), int(size*2), C_WOOD_D)
    
    for i in range(4):
        yw = y - i*int(h_base*0.7)
        c.poly([(x - w_base + int(i*size), yw), (x + w_base - int(i*size), yw), (x, yw - h_base)], C_PINE_D)
        
        if shadow_side == 'left':
            c.poly([(x, yw), (x + w_base - int(i*size) - 1, yw), (x, yw - h_base + 1)], C_PINE_M)
            c.line(x, yw - h_base + 1, x + w_base - int(i*size) - 1, yw, C_PINE_L)
        else:
            c.poly([(x - w_base + int(i*size) + 1, yw), (x, yw), (x, yw - h_base + 1)], C_PINE_M)
            c.line(x, yw - h_base + 1, x - w_base + int(i*size) + 1, yw, C_PINE_L)

def draw_bush(c, x, y, size, shadow_side='left'):
    c.circle(x, y, size, C_PINE_D)
    c.circle(x-size//2, y+size//2, size, C_PINE_D)
    c.circle(x+size//2, y+size//2, size, C_PINE_D)
    
    if shadow_side == 'left':
        c.circle(x+1, y-1, size-1, C_PINE_M)
        c.circle(x-size//2+1, y+size//2-1, size-1, C_PINE_M)
        c.circle(x+size//2+1, y+size//2-1, size-1, C_PINE_M)
    else:
        c.circle(x-1, y-1, size-1, C_PINE_M)
        c.circle(x-size//2-1, y+size//2-1, size-1, C_PINE_M)
        c.circle(x+size//2-1, y+size//2-1, size-1, C_PINE_M)

def draw_house(c, x, y, width, height, shadow_side='left'):
    c.rect(x - width//2, y - height, width, height, C_WOOD_M)
    if shadow_side == 'left':
        c.rect(x - width//2, y - height, width//2, height, C_WOOD_D)
    else:
        c.rect(x, y - height, width//2, height, C_WOOD_D)
    
    for ly in range(y - height + 2, y, 4):
        c.line(x - width//2, ly, x + width//2 - 1, ly, C_WOOD_D)
        
    c.rect(x + width//4 - 2, y - height - height//2 - 8, 5, height//2 + 10, C_PATH_M)
    if shadow_side == 'left':
        c.rect(x + width//4 - 2, y - height - height//2 - 8, 2, height//2 + 10, C_PATH_D)
    else:
        c.rect(x + width//4 + 1, y - height - height//2 - 8, 2, height//2 + 10, C_PATH_D)
    
    c.poly([(x - width//2 - 6, y - height), (x + width//2 + 6, y - height), (x, y - height - height//2 - 4)], C_ROOF_M)
    if shadow_side == 'left':
        c.poly([(x - width//2 - 6, y - height), (x, y - height), (x, y - height - height//2 - 4)], C_ROOF_D)
    else:
        c.poly([(x + width//2 + 6, y - height), (x, y - height), (x, y - height - height//2 - 4)], C_ROOF_D)
    
    dw = 8
    if width <= 20: dw = 6
    c.rect(x - dw//2, y - 10, dw, 10, C_WOOD_D)
    if shadow_side == 'left':
        c.rect(x - dw//2, y - 10, dw//2, 10, '#281b15')
        c.set(x + 1, y - 5, '#111111')
    else:
        c.rect(x, y - 10, dw//2, 10, '#281b15')
        c.set(x - 2, y - 5, '#111111')
    
    ww = 4
    if width >= 28: ww = 6
    wx1 = x - width//2 + 2
    wx2 = x + width//2 - 2 - ww
    wy = y - height//2 - 2
    
    c.rect(wx1, wy, ww, ww, C_WIND_G)
    c.rect(wx1+1, wy+1, ww-2, ww-2, C_WIND)
    
    c.rect(wx2, wy, ww, ww, C_WIND_G)
    c.rect(wx2+1, wy+1, ww-2, ww-2, C_WIND)

def draw_smoke(c, x, y):
    c.circle(x, y-5, 3, C_SMOKE1)
    c.circle(x+2, y-12, 4, C_SMOKE1)
    c.circle(x-1, y-20, 5, C_SMOKE2)
    c.circle(x+3, y-28, 6, C_SMOKE2)

def draw_path(c):
    stones = [
        (64, 106, 2), (63, 108, 2), (65, 110, 3), (61, 112, 3),
        (66, 115, 4), (60, 118, 4), (67, 121, 5), (59, 124, 5),
        (66, 128, 6), (58, 131, 6)
    ]
    for sx, sy, sr in stones:
        c.ellipse(sx, sy, sr, max(1, sr-1), C_PATH_M)
        c.ellipse(sx, sy, max(1, sr-1), max(1, sr-2), C_PATH_L)

def draw_bird(c, x, y):
    c.set(x, y, '#111111')
    c.set(x-1, y-1, '#111111')
    c.set(x+1, y-1, '#111111')

bg = new_canvas(w, h)
draw_sky(bg)
draw_mountains(bg)
draw_hills(bg)

draw_bird(bg, 90, 40)
draw_bird(bg, 95, 37)
draw_bird(bg, 85, 45)

for px in range(5, 125, 12):
    side = 'left' if px < 64 else 'right'
    draw_pine(bg, px, 95 + (px%10), 1.2, side)

houses_layer = new_canvas(w, h)
draw_house(houses_layer, 35, 105, 20, 16, 'left')
draw_smoke(houses_layer, 35 + 20//4 - 2 + 2, 105 - 16 - 16//2 - 8)

draw_house(houses_layer, 93, 108, 24, 18, 'right')
draw_smoke(houses_layer, 93 + 24//4 - 2 + 2, 108 - 18 - 18//2 - 8)

draw_house(houses_layer, 64, 105, 28, 20, 'left')
draw_smoke(houses_layer, 64 + 28//4 - 2 + 2, 105 - 20 - 20//2 - 8)

draw_bush(houses_layer, 20, 105, 4, 'left')
draw_bush(houses_layer, 48, 106, 3, 'left')
draw_bush(houses_layer, 80, 108, 4, 'right')
draw_bush(houses_layer, 110, 109, 3, 'right')

draw_path(houses_layer)

for px in [10, 25, 105, 120]:
    side = 'left' if px < 64 else 'right'
    draw_pine(houses_layer, px, 120 + (px%8), 2.5, side)

final = flatten([bg, houses_layer])
finish(final)
