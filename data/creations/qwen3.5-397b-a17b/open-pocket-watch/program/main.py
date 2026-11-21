from pixelbench_api import *
import math

# Create 64x64 canvas for the pocket watch
c = new_canvas(64, 64, name="pocket_watch")

# Define color palette for realistic metallic pocket watch
# Gold tones (movement/brass gears)
gold_very_dark = c.color((100, 75, 25), "gold_very_dark")
gold_dark = c.color((139, 110, 40), "gold_dark")
gold_mid = c.color((184, 149, 56), "gold_mid")
gold_light = c.color((218, 183, 87), "gold_light")
gold_highlight = c.color((255, 235, 150), "gold_highlight")
gold_bright = c.color((255, 250, 200), "gold_bright")

# Silver/steel tones (balance wheel, some gears)
steel_very_dark = c.color((50, 55, 60), "steel_very_dark")
steel_dark = c.color((80, 85, 90), "steel_dark")
steel_mid = c.color((120, 130, 140), "steel_mid")
steel_light = c.color((170, 180, 190), "steel_light")
steel_highlight = c.color((220, 230, 240), "steel_highlight")
steel_bright = c.color((245, 250, 255), "steel_bright")

# Ruby jewel colors (for watch bearings)
ruby_dark = c.color((120, 20, 30), "ruby_dark")
ruby_mid = c.color((180, 30, 50), "ruby_mid")
ruby_light = c.color((220, 60, 80), "ruby_light")
ruby_highlight = c.color((255, 150, 160), "ruby_highlight")

# Shadow and depth colors
shadow_deep = c.color((20, 15, 10), "shadow_deep")
shadow_mid = c.color((50, 40, 30), "shadow_mid")
shadow_light = c.color((80, 65, 50), "shadow_light")

# Dial colors (watch face)
dial_bg = c.color((250, 245, 235), "dial_bg")
dial_shadow = c.color((200, 195, 185), "dial_shadow")
dial_mark = c.color((15, 15, 20), "dial_mark")
dial_mark_light = c.color((60, 60, 70), "dial_mark_light")

# Case/outer ring colors
case_gold = c.color((165, 135, 50), "case_gold")
case_shadow = c.color((90, 70, 30), "case_shadow")
case_highlight = c.color((230, 200, 100), "case_highlight")

# Chain colors
chain_dark = c.color((90, 75, 40), "chain_dark")
chain_mid = c.color((150, 125, 65), "chain_mid")
chain_light = c.color((200, 175, 95), "chain_light")

# Background
bg_dark = c.color((35, 30, 25), "bg_dark")
bg_mid = c.color((55, 48, 40), "bg_mid")

# Helper function to draw a filled circle with gradient
def draw_gradient_circle(cx, cy, r, inner_color, outer_color):
    for y in range(cy - r, cy + r + 1):
        for x in range(cx - r, cx + r + 1):
            dist = math.sqrt((x - cx)**2 + (y - cy)**2)
            if dist <= r:
                # Interpolate based on distance from center
                ratio = dist / r
                # Light from top-right
                angle_factor = math.sin(math.atan2(y - cy, x - cx) + math.pi/4) * 0.3 + 0.5
                ratio = ratio * 0.7 + angle_factor * 0.3
                if ratio < 0.3:
                    c.set(x, y, inner_color)
                elif ratio < 0.6:
                    c.set(x, y, outer_color)
                else:
                    c.set(x, y, steel_mid)

# Draw gear with teeth
def draw_gear(cx, cy, inner_r, outer_r, teeth, body_color, teeth_color, has_jewel=False):
    # Draw gear body
    c.circle(cx, cy, inner_r, body_color, fill=True)
    
    # Draw teeth
    for i in range(teeth):
        angle = (360 / teeth) * i + 15  # Offset for better meshing
        rad = math.radians(angle)
        
        # Each tooth
        tooth_angle_width = (360 / teeth) * 0.4
        for ta in range(int(-tooth_angle_width/2), int(tooth_angle_width/2), 2):
            tooth_rad = math.radians(angle + ta)
            x1 = int(cx + inner_r * math.cos(tooth_rad))
            y1 = int(cy + inner_r * math.sin(tooth_rad))
            x2 = int(cx + outer_r * math.cos(tooth_rad))
            y2 = int(cy + outer_r * math.sin(tooth_rad))
            c.line(x1, y1, x2, y2, teeth_color)
    
    # Center jewel (ruby bearing)
    if has_jewel:
        c.circle(cx, cy, 2, ruby_mid, fill=True)
        c.set(cx, cy, ruby_highlight)
    else:
        c.circle(cx, cy, 2, steel_dark, fill=True)
        c.set(cx, cy, steel_highlight)

# Draw the watch case (outer circular frame)
def draw_case():
    # Outer ring - thick golden case
    for angle in range(0, 360, 3):
        rad = math.radians(angle)
        
        # Metallic gradient based on angle (light from top-right ~45 degrees)
        light_angle = math.pi / 4
        current_angle = math.radians(angle)
        brightness = math.cos(current_angle - light_angle)
        
        if brightness > 0.5:
            color = case_highlight
        elif brightness > 0:
            color = case_gold
        elif brightness > -0.5:
            color = gold_dark
        else:
            color = case_shadow
        
        # Draw ring segment
        for r in range(26, 31):
            x = int(32 + r * math.cos(rad))
            y = int(32 + r * math.sin(rad))
            if 0 <= x < 64 and 0 <= y < 64:
                c.set(x, y, color)
    
    # Inner bevel
    for angle in range(0, 360, 5):
        rad = math.radians(angle)
        x = int(32 + 25 * math.cos(rad))
        y = int(32 + 25 * math.sin(rad))
        if 0 <= x < 64 and 0 <= y < 64:
            c.set(x, y, gold_light)

# Draw the open lid (curved, hinged on left side)
def draw_lid():
    # Lid is curved and open to the left
    for angle in range(60, 300, 4):
        rad = math.radians(angle)
        
        # Lid curves outward to the left
        lid_base_x = 32 + 8 * math.cos(rad)
        lid_base_y = 32 + 8 * math.sin(rad)
        
        # Lid thickness
        for t in range(4):
            x = int(lid_base_x - t * 1.5)
            y = int(lid_base_y)
            
            # Metallic gradient
            if t == 0:
                color = case_shadow
            elif t == 1:
                color = case_gold
            elif t == 2:
                color = gold_light
            else:
                color = case_highlight
            
            if 0 <= x < 64 and 0 <= y < 64:
                c.set(x, y, color)
    
    # Lid hinge mechanism on left
    c.rect(5, 28, 4, 8, gold_dark, fill=True)
    c.set(6, 30, gold_highlight)
    c.set(6, 34, gold_highlight)
    
    # Hinge pin
    c.set(5, 32, steel_dark)

# Draw the dial (watch face)
def draw_dial():
    # Dial background - cream colored
    c.circle(32, 32, 17, dial_bg, fill=True)
    
    # Subtle shadow on dial
    for angle in range(180, 360, 10):
        rad = math.radians(angle)
        x = int(32 + 14 * math.cos(rad))
        y = int(32 + 14 * math.sin(rad))
        c.set(x, y, dial_shadow)
    
    # Hour tick marks (12 positions - thick)
    for hour in range(12):
        angle = math.radians(hour * 30 - 90)
        for r in range(13, 17):
            x = int(32 + r * math.cos(angle))
            y = int(32 + r * math.sin(angle))
            c.set(x, y, dial_mark)
    
    # Minute tick marks (between hours - thin)
    for minute in range(60):
        if minute % 5 != 0:
            angle = math.radians(minute * 6 - 90)
            x = int(32 + 15 * math.cos(angle))
            y = int(32 + 15 * math.sin(angle))
            c.set(x, y, dial_mark_light)
    
    # Roman numerals would be nice but let's keep it simple with dots
    # Center hole for hands
    c.circle(32, 32, 2, dial_bg, fill=True)

# Draw watch hands
def draw_hands():
    # Hour hand (shorter, thicker) - pointing to ~10:10
    hour_angle = math.radians(-65 - 90)  # ~10 o'clock
    for length in range(4, 13):
        x = int(32 + length * math.cos(hour_angle))
        y = int(32 + length * math.sin(hour_angle))
        # Hand width
        for w in range(-1, 2):
            perp_x = int(-w * math.sin(hour_angle))
            perp_y = int(w * math.cos(hour_angle))
            c.set(x + perp_x, y + perp_y, steel_dark)
    
    # Minute hand (longer, thinner) - pointing to ~2
    minute_angle = math.radians(55 - 90)  # ~11 minutes (close to 2)
    for length in range(4, 17):
        x = int(32 + length * math.cos(minute_angle))
        y = int(32 + length * math.sin(minute_angle))
        c.set(x, y, steel_mid)
        if length > 8:
            c.set(x, y, steel_dark)
    
    # Second hand (thin, red or blue) - optional
    second_angle = math.radians(25 - 90)
    for length in range(6, 16):
        x = int(32 + length * math.cos(second_angle))
        y = int(32 + length * math.sin(second_angle))
        c.set(x, y, ruby_mid)
    
    # Center pivot (golden cap)
    c.circle(32, 32, 3, gold_mid, fill=True)
    c.set(32, 32, gold_highlight)

# Draw intricate gear train
def draw_gear_train():
    # Main large gear at bottom (brass)
    draw_gear(32, 48, 9, 12, 16, gold_mid, gold_light, has_jewel=True)
    
    # Medium gear meshing with large gear (top-right of large gear)
    draw_gear(44, 40, 6, 8, 12, steel_mid, steel_light, has_jewel=False)
    
    # Small gear meshing with medium gear (further right)
    draw_gear(52, 35, 4, 6, 8, gold_light, gold_highlight, has_jewel=True)
    
    # Gear on left side (balance wheel area)
    draw_gear(18, 42, 7, 9, 14, steel_light, steel_highlight, has_jewel=False)
    
    # Upper gear (escape wheel area)
    draw_gear(28, 22, 5, 7, 10, gold_dark, gold_mid, has_jewel=True)
    
    # Small pinion gear
    draw_gear(38, 28, 3, 4, 6, steel_dark, steel_mid, has_jewel=False)
    
    # Additional detail gears
    c.circle(24, 35, 3, gold_mid, fill=True)
    c.set(24, 35, gold_light)
    
    c.circle(40, 48, 2, steel_mid, fill=True)
    c.set(40, 48, steel_light)

# Draw watch chain
def draw_chain():
    # Chain links coming from top-left
    for i in range(6):
        link_x = 12 - i * 4
        link_y = 18 + i * 3
        
        if link_x < 0:
            continue
            
        # Each link is a small oval
        c.ellipse(link_x, link_y, 3, 4, chain_mid, fill=False)
        
        # Highlight on chain link
        c.set(link_x - 1, link_y - 2, chain_light)
        c.set(link_x + 1, link_y + 2, chain_dark)
    
    # Chain attachment point on watch
    c.circle(10, 15, 3, gold_mid, fill=True)
    c.set(10, 15, gold_highlight)

# Add metallic highlights and reflections
def add_metallic_effects():
    # Strong highlight on top-right of watch case (light source from top-right)
    for angle in range(-20, 70, 8):
        rad = math.radians(angle)
        x = int(32 + 28 * math.cos(rad))
        y = int(32 + 28 * math.sin(rad))
        if 0 <= x < 64 and 0 <= y < 64:
            c.set(x, y, gold_bright)
            if x + 1 < 64:
                c.set(x + 1, y, case_highlight)
    
    # Deep shadows on bottom-left of case
    for angle in range(190, 260, 10):
        rad = math.radians(angle)
        x = int(32 + 29 * math.cos(rad))
        y = int(32 + 29 * math.sin(rad))
        if 0 <= x < 64 and 0 <= y < 64:
            c.set(x, y, shadow_deep)
    
    # Reflections on gear teeth
    c.set(35, 44, gold_highlight)
    c.set(46, 38, steel_highlight)
    c.set(20, 40, steel_bright)
    c.set(30, 20, gold_bright)
    
    # Sparkle on ruby jewels
    c.set(32, 48, ruby_highlight)
    c.set(52, 35, ruby_highlight)
    c.set(28, 22, ruby_highlight)

# Draw background (dark vignette effect)
def draw_background():
    for y in range(64):
        for x in range(64):
            dist = math.sqrt((x - 32)**2 + (y - 32)**2)
            if dist > 35:
                c.set(x, y, bg_dark)
            elif dist > 32:
                c.set(x, y, bg_mid)
            elif dist > 30:
                c.set(x, y, shadow_light)

# Add fine details - screws, engravings
def add_details():
    # Screws on the case (4 cardinal points)
    screw_positions = [(32, 5), (59, 32), (32, 59), (5, 32)]
    for sx, sy in screw_positions:
        if 0 <= sx < 64 and 0 <= sy < 64:
            c.circle(sx, sy, 2, steel_mid, fill=True)
            c.set(sx, sy, steel_dark)
            c.set(sx, sy-1, steel_highlight)
    
    # Engraving lines on watch movement plate
    for i in range(5):
        y_pos = 50 + i
        if y_pos < 60:
            c.line(22, y_pos, 42, y_pos, gold_dark)
    
    # Small decorative dots
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        x = int(32 + 20 * math.cos(rad))
        y = int(32 + 20 * math.sin(rad))
        if 0 <= x < 64 and 0 <= y < 64:
            c.set(x, y, gold_mid)

# Execute all drawing functions in order
draw_background()
draw_case()
draw_lid()
draw_dial()
draw_gear_train()
draw_hands()
draw_chain()
add_metallic_effects()
add_details()

# Print stats to verify color count
print(c.stats_text())

# Submit the result
finish(c)
