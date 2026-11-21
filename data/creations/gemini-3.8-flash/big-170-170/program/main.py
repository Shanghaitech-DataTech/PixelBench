import random

# Start with a copy of input_canvas
output = input_canvas.copy(name='base')
pal = {entry['index']: entry['rgba'] for entry in input_canvas.palette()}

# Color helper
def c_rgb(spec):
    return output.color(spec)

# --- 1. REMOVE CHARACTER & RESTORE VENDING MACHINE & BACKGROUND ---

# Register key colors for vending machine & background
C_CABINET_PURPLE = output.color('#1e1a53', 'cabinet_purple')
C_CABINET_PURPLE_LIGHT = output.color('#251e5b', 'cabinet_purple_light')
C_CABINET_PURPLE_DARK = output.color('#1c184b', 'cabinet_purple_dark')
C_CABINET_PURPLE_SHADOW = output.color('#16133d', 'cabinet_purple_shadow')

C_RIM_PURPLE = output.color('#be90be', 'vm_rim')
C_RIM_PURPLE_LIGHT = output.color('#c18bbd', 'vm_rim_light')

C_INTERIOR_WHITE = output.color('#ffeae3', 'interior_white')
C_INTERIOR_CREAM = output.color('#fceadc', 'interior_cream')
C_INTERIOR_LIGHT = output.color('#fceee8', 'interior_light')

C_SHELF_GREY = output.color('#858e8f', 'shelf_grey')
C_SHELF_DARK = output.color('#6e757e', 'shelf_dark')

# Exterior background colors (sky / hills)
C_SKY_1 = output.color('#0a2e3f')
C_SKY_2 = output.color('#0b3245')
C_SKY_3 = output.color('#11465a')
C_HILL_1 = output.color('#12394d')
C_HILL_2 = output.color('#0e2a38')

# A. Restore background left of vending machine (where character arm/drink reached)
# Vending machine left edge is at x=81. Outside is x < 81.
for y in range(68, 86):
    for x in range(71, 81):
        r, g, b, _ = pal[input_canvas.get(x, y)]
        # Character fur/drink was at x in 72..80, y in 70..85
        if (r > 130 and g > 60 and b < 110) or (g > 100 and r < 130 and b < 130):
            # Sample sky/hill color from x=70
            ref_c = input_canvas.get(70, y)
            output.set(x, y, ref_c)

# B. Restore left edge of vending machine (x=81..84, y=68..86)
for y in range(68, 86):
    output.set(81, y, C_CABINET_PURPLE_SHADOW)
    output.set(82, y, C_CABINET_PURPLE)
    output.set(83, y, C_CABINET_PURPLE)
    output.set(84, y, C_RIM_PURPLE_LIGHT)

# C. Restore the lit display interior (x=85..114, y=60..107)
# First fill interior background
for y in range(60, 108):
    for x in range(85, 115):
        r, g, b, _ = pal[input_canvas.get(x, y)]
        # If character fur / coat / head
        is_coat = (70 < r < 140 and g < 65 and 45 < b < 85) or (180 < r < 210 and 95 < g < 125 and 85 < b < 125)
        is_fur = (r > 140 and 70 < g < 130 and 40 < b < 95) or (r > 210 and 150 < g < 200 and 120 < b < 170)
        is_ear_head = (y < 70 and r > 180 and g > 110)
        if is_coat or is_fur or is_ear_head or (r > 240 and g > 160 and b < 160):
            # Background tone variation
            bg_col = C_INTERIOR_WHITE if (x + y) % 3 != 0 else C_INTERIOR_CREAM
            output.set(x, y, bg_col)

# Top and bottom inner rims of display window
for x in range(85, 115):
    output.set(x, 59, C_RIM_PURPLE)
    output.set(x, 108, C_RIM_PURPLE)

# Redraw the 4 shelves dividers across the full width
for x in range(85, 115):
    output.set(x, 66, C_SHELF_GREY)
    output.set(x, 77, C_SHELF_GREY)
    output.set(x, 89, C_SHELF_GREY)
    output.set(x, 101, C_SHELF_GREY)

# Populate drinks on the shelves where the character was covering:
# Drink colors
C_RED_CAN = output.color('#c03535')
C_RED_CAN_HI = output.color('#e85555')
C_BLUE_CAN = output.color('#255fb2')
C_BLUE_CAN_HI = output.color('#5a93e8')
C_GREEN_CAN = output.color('#3ca850')
C_GREEN_CAN_HI = output.color('#6cd680')
C_ORANGE_CAN = output.color('#d87c24')
C_ORANGE_CAN_HI = output.color('#f4a456')
C_YELLOW_CAN = output.color('#e0b428')
C_PURPLE_CAN = output.color('#8c48b8')
C_PURPLE_CAN_HI = output.color('#b67ae2')
C_WHITE_CAN = output.color('#e4ecf0')
C_BLACK_CAN = output.color('#282b30')

# Shelf 1 (y=61..65): small cans
def draw_can_shelf1(x0, body_col, hi_col):
    for y in range(61, 66):
        output.set(x0, y, body_col)
        output.set(x0 + 1, y, hi_col)
        output.set(x0 + 2, y, body_col)

draw_can_shelf1(86, C_RED_CAN, C_RED_CAN_HI)
draw_can_shelf1(90, C_BLUE_CAN, C_BLUE_CAN_HI)
draw_can_shelf1(94, C_ORANGE_CAN, C_ORANGE_CAN_HI)
draw_can_shelf1(98, C_WHITE_CAN, output.color('#ffffff'))
draw_can_shelf1(102, C_PURPLE_CAN, C_PURPLE_CAN_HI)

# Shelf 2 (y=68..76): taller bottles & cans
def draw_bottle_shelf2(x0, w, body_col, hi_col, cap_col=output.color('#ffffff')):
    # cap at y=68
    output.set(x0 + w//2, 68, cap_col)
    for y in range(69, 77):
        for dx in range(w):
            col = hi_col if dx == 1 else body_col
            output.set(x0 + dx, y, col)

draw_bottle_shelf2(86, 3, C_BLUE_CAN, C_BLUE_CAN_HI)
draw_bottle_shelf2(90, 3, C_GREEN_CAN, C_GREEN_CAN_HI)
draw_bottle_shelf2(94, 3, C_RED_CAN, C_RED_CAN_HI)
draw_bottle_shelf2(98, 3, C_YELLOW_CAN, output.color('#fff070'))
draw_bottle_shelf2(102, 2, C_WHITE_CAN, output.color('#ffffff'))

# Shelf 3 (y=79..88): soda cans
def draw_can_shelf3(x0, body_col, hi_col):
    for y in range(80, 89):
        output.set(x0, y, body_col)
        output.set(x0 + 1, y, hi_col)
        output.set(x0 + 2, y, body_col)

draw_can_shelf3(86, C_PURPLE_CAN, C_PURPLE_CAN_HI)
draw_can_shelf3(90, C_BLUE_CAN, C_BLUE_CAN_HI)
draw_can_shelf3(94, C_RED_CAN, C_RED_CAN_HI)
draw_can_shelf3(98, C_ORANGE_CAN, C_ORANGE_CAN_HI)
draw_can_shelf3(102, C_BLACK_CAN, output.color('#505560'))
draw_can_shelf3(106, C_GREEN_CAN, C_GREEN_CAN_HI)

# Shelf 4 (y=92..100): warm coffee cans matching original row
C_COFFEE_1 = output.color('#c36a38')
C_COFFEE_2 = output.color('#ca6c3f')
C_COFFEE_3 = output.color('#905737')
C_COFFEE_HI = output.color('#f9b494')

def draw_coffee_shelf4(x0, c1, c2):
    for y in range(92, 101):
        output.set(x0, y, c1)
        output.set(x0 + 1, y, C_COFFEE_HI if y < 96 else c2)
        output.set(x0 + 2, y, c2)

draw_coffee_shelf4(86, C_COFFEE_1, C_COFFEE_3)
draw_coffee_shelf4(90, C_COFFEE_2, C_COFFEE_1)
draw_coffee_shelf4(94, C_COFFEE_1, C_COFFEE_2)
draw_coffee_shelf4(98, C_COFFEE_3, C_COFFEE_1)

# Push buttons / labels under Shelf 4 (y=102..105)
for x0 in [86, 90, 94, 98, 102, 106, 110]:
    output.set(x0, 103, output.color('#284580'))
    output.set(x0 + 1, 103, output.color('#5080d0'))
    output.set(x0, 104, output.color('#182540'))
    output.set(x0 + 1, 104, output.color('#182540'))

# D. Restore vending machine front body below display (y=108..145)
# Dispenser slot frame & opening colors
C_DISP_DARK = output.color('#1d3338')
C_DISP_DEEP = output.color('#06141e')
C_DISP_FRAME = output.color('#34414b')
C_DISP_RIM = output.color('#6f7a81')

# Motorcycle protection:
# Motorcycle tank is around x=55..85, y=112..128
# Motorcycle seat/tail is around x=85..118, y=114..125
# Motorcycle wheel is around x=85..122, y=128..160
for y in range(108, 146):
    for x in range(80, 119):
        r, g, b, _ = pal[input_canvas.get(x, y)]
        # Detect character coat / fur / tail pixels:
        is_coat = (70 < r < 140 and g < 65 and 45 < b < 85) or (180 < r < 210 and 95 < g < 125 and 85 < b < 125)
        is_fur = (r > 130 and 70 < g < 135 and 40 < b < 100) or (r > 200 and 140 < g < 200 and 110 < b < 170)
        # Specifically character leg/tail at x=100..112, y=124..134
        is_tail = (123 <= y <= 134 and 98 <= x <= 114 and r > 150 and g > 110)
        
        if is_coat or is_fur or is_tail:
            # Check what should be behind:
            # Dispenser slot is at x=88..112, y=134..144
            if 134 <= y <= 144 and 88 <= x <= 112:
                if y == 134:
                    output.set(x, y, C_DISP_RIM)
                elif y == 135:
                    output.set(x, y, C_DISP_FRAME)
                elif y == 144:
                    output.set(x, y, C_DISP_FRAME)
                else:
                    output.set(x, y, C_DISP_DARK if (x + y) % 2 == 0 else C_DISP_DEEP)
            else:
                # Purple cabinet front face
                if x == 80:
                    output.set(x, y, C_SKY_2)
                elif x == 81:
                    output.set(x, y, C_CABINET_PURPLE_SHADOW)
                elif x in (82, 83):
                    output.set(x, y, C_CABINET_PURPLE)
                elif x in (116, 117):
                    output.set(x, y, C_CABINET_PURPLE_LIGHT)
                elif x == 118:
                    output.set(x, y, C_CABINET_PURPLE_DARK)
                else:
                    c = C_CABINET_PURPLE if (x + y) % 2 == 0 else C_CABINET_PURPLE_LIGHT
                    output.set(x, y, c)

# --- 2. THUNDERSTORM WEATHER: LIGHTNING IN THE BACKGROUND ---

C_BOLT_CORE = output.color('#ffffff', 'bolt_core')
C_BOLT_GLOW1 = output.color('#d8f6ff', 'bolt_glow1')
C_BOLT_GLOW2 = output.color('#88d4ff', 'bolt_glow2')
C_BOLT_GLOW3 = output.color('#3888c8', 'bolt_glow3')
C_BOLT_AURA = output.color('#184878', 'bolt_aura')

# Main jagged lightning bolt from top sky (x=68, y=0) to horizon
main_bolt = [
    (68, 0), (67, 3), (69, 7), (66, 11), (68, 15), (64, 20), (66, 24),
    (63, 29), (65, 33), (62, 38), (64, 43), (60, 48), (62, 53), (58, 59),
    (60, 64), (56, 70), (58, 75), (55, 80)
]

# Branch 1 splits at (64, 20) towards left/pole
branch1 = [
    (64, 20), (61, 23), (58, 25), (59, 29), (55, 33), (53, 37), (50, 41)
]

# Branch 2 splits at (62, 38) towards middle
branch2 = [
    (62, 38), (66, 42), (69, 45), (68, 50), (72, 54), (71, 59)
]

# Smaller cloud bolt in upper-right sky
cloud_bolt = [
    (142, 6), (145, 11), (143, 16), (148, 21), (146, 26), (152, 31), (150, 36)
]
cloud_branch = [
    (146, 26), (142, 29), (139, 32)
]

def draw_lightning(path, width=1):
    # Pass 1: soft halo glow
    for i in range(len(path) - 1):
        x0, y0 = path[i]
        x1, y1 = path[i+1]
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                if dx*dx + dy*dy <= 5:
                    output.line(x0+dx, y0+dy, x1+dx, y1+dy, C_BOLT_AURA)
    # Pass 2: inner cyan glow
    for i in range(len(path) - 1):
        x0, y0 = path[i]
        x1, y1 = path[i+1]
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                output.line(x0+dx, y0+dy, x1+dx, y1+dy, C_BOLT_GLOW2)
    # Pass 3: near-white core
    for i in range(len(path) - 1):
        x0, y0 = path[i]
        x1, y1 = path[i+1]
        output.line(x0, y0, x1, y1, C_BOLT_CORE)

# Draw bolts in the background sky
draw_lightning(main_bolt)
draw_lightning(branch1)
draw_lightning(branch2)
draw_lightning(cloud_bolt)
draw_lightning(cloud_branch)

# Lightning cloud illumination (subtle rim lighting on nearby clouds)
for cx, cy, col in [
    (56, 15, C_BOLT_GLOW3), (75, 12, C_BOLT_GLOW3), (52, 35, C_BOLT_GLOW3),
    (74, 30, C_BOLT_AURA), (66, 52, C_BOLT_GLOW3), (140, 18, C_BOLT_AURA),
    (155, 25, C_BOLT_GLOW3), (135, 35, C_BOLT_AURA)
]:
    output.set(cx, cy, col)
    output.set(cx+1, cy, col)

# --- 3. WET GROUND WITH CLINGING WATER DROPLETS & SPECULAR HIGHLIGHTS ---

C_WET_DARK = output.color('#101822')
C_WET_MID = output.color('#182838')
C_PUDDLE_RIPPLE = output.color('#6090b8')
C_PUDDLE_EDGE = output.color('#88c0e0')
C_DROP_WHITE = output.color('#ffffff')
C_DROP_CYAN = output.color('#b0e8ff')
C_DROP_BLUE = output.color('#68a0d0')

# Enhance wet ground and puddle glossiness in foreground (y=140..170)
# Ripples in the existing and expanded puddles
for cx, cy, rx, ry in [
    (40, 160, 12, 2),
    (75, 164, 18, 3),
    (145, 162, 14, 2),
    (110, 158, 8, 1),
    (30, 150, 7, 1),
    (130, 152, 9, 2)
]:
    output.ellipse(cx, cy, rx, ry, C_PUDDLE_RIPPLE, fill=False)

# Clinging water droplets on the wet ground / puddle edges
rng = random.Random(42)
for _ in range(70):
    gx = rng.randint(5, 165)
    gy = rng.randint(142, 169)
    # Don't place on motorcycle wheel center
    c = C_DROP_WHITE if rng.random() < 0.3 else (C_DROP_CYAN if rng.random() < 0.7 else C_DROP_BLUE)
    output.set(gx, gy, c)

# Clinging water droplets on motorcycle surfaces (seat, tank, fairing, wheels)
moto_droplets = [
    # Fuel tank (orange surface)
    (62, 118), (66, 116), (70, 117), (74, 119), (78, 122), (64, 122), (68, 120),
    # Seat (black cushion)
    (88, 117), (92, 118), (96, 119), (100, 118), (104, 119),
    # Rear cowl / tail
    (108, 117), (112, 119), (114, 121),
    # Handlebars & mirrors
    (48, 112), (54, 110), (58, 113),
    # Rear wheel arch
    (105, 138), (115, 142), (90, 136)
]
for mx, my in moto_droplets:
    output.set(mx, my, C_DROP_WHITE)
    output.set(mx, my + 1, C_DROP_BLUE)

# Clinging water droplets on vending machine roof and side
for vx in range(82, 134, 3):
    output.set(vx, 57, C_DROP_WHITE)
    output.set(vx, 58, C_DROP_CYAN)

# Water trickles / droplets running down vending machine purple side panel
for (sx, sy) in [(122, 65), (122, 66), (128, 72), (128, 73), (125, 85), (125, 86),
                 (131, 95), (131, 96), (124, 110), (124, 111), (129, 125), (129, 126)]:
    output.set(sx, sy, C_DROP_CYAN)

# --- 4. RENDER RAIN WITH SEMI-TRANSPARENT DROPLETS (LAYERED BLENDING) ---

# Create a rain canvas for translucent droplet rendering
rain_canvas = new_canvas(170, 170, name='rain')

# Register semi-transparent rain droplet RGBA colors
C_RAIN_FAINT = rain_canvas.color((180, 215, 245, 75))   # distant thin rain
C_RAIN_MID   = rain_canvas.color((210, 235, 255, 135))  # mid-distance droplets
C_RAIN_BRIGHT= rain_canvas.color((240, 248, 255, 195))  # close rain streaks
C_RAIN_DROP  = rain_canvas.color((255, 255, 255, 220))  # glistening droplet head

rain_rng = random.Random(1337)

# Wind slant: dx = -1 for every 3 or 4 dy
# Draw background rain (faint, short droplets)
for _ in range(160):
    rx = rain_rng.randint(0, 169)
    ry = rain_rng.randint(0, 165)
    length = rain_rng.randint(2, 4)
    for l in range(length):
        rain_canvas.set(rx - l // 3, ry + l, C_RAIN_FAINT)

# Draw midground rain (semi-transparent streaks)
for _ in range(140):
    rx = rain_rng.randint(0, 169)
    ry = rain_rng.randint(0, 162)
    length = rain_rng.randint(3, 6)
    for l in range(length):
        col = C_RAIN_DROP if l == length - 1 else C_RAIN_MID
        rain_canvas.set(rx - l // 3, ry + l, col)

# Draw foreground prominent droplets & streaks
for _ in range(70):
    rx = rain_rng.randint(0, 169)
    ry = rain_rng.randint(0, 160)
    length = rain_rng.randint(4, 7)
    for l in range(length):
        col = C_RAIN_DROP if l >= length - 2 else C_RAIN_BRIGHT
        rain_canvas.set(rx - l // 3, ry + l, col)

# Rain splashes bouncing off hard surfaces (vending machine top, motorcycle, ground)
for sx, sy in [
    (85, 56), (95, 55), (105, 56), (118, 55), (128, 56), # vending machine top
    (65, 115), (75, 116), (92, 116), (110, 116),          # motorcycle top
    (35, 155), (55, 158), (80, 162), (120, 156), (145, 160) # puddle impacts
]:
    rain_canvas.set(sx - 1, sy - 1, C_RAIN_BRIGHT)
    rain_canvas.set(sx + 1, sy - 1, C_RAIN_BRIGHT)
    rain_canvas.set(sx, sy - 2, C_RAIN_DROP)

# Composite rain onto the scene using flatten()
final_result = flatten([output, rain_canvas], name='final')

# View and finish the requested single output canvas
view(final_result)
finish(final_result)
