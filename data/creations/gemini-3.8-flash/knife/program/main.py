import math

# 1. Transform knife: thrusting to the right with cutting edge facing downward
# In the original 93x128 image, blade points up-left, cutting edge faces down-left.
# Flipping horizontally and rotating 52 degrees clockwise poses the knife
# pointing directly to the right with cutting edge facing downward.
sel = input_canvas.select(0, 0, input_canvas.w, input_canvas.h)
knife_rotated = sel.flip("h").rotate(52, algorithm="rotsprite").preview()

# Crop tight bounding box
stats = knife_rotated.stats()
bx0, by0, bx1, by1 = stats['bbox']
kw = bx1 - bx0 + 1
kh = by1 - by0 + 1

knife = new_canvas(kw, kh, name="knife")
knife.blit(knife_rotated, -bx0, -by0)

# Function to generate semi-transparent afterimages
def make_afterimage(src, alpha_scale, tint_color=None):
    dst = new_canvas(src.w, src.h)
    pal = src.palette()
    for y in range(src.h):
        for x in range(src.w):
            idx = src.get(x, y)
            if idx != 0:
                rgba = pal[idx]['rgba']
                if rgba[3] > 0:
                    a = int(rgba[3] * alpha_scale)
                    if tint_color:
                        r = int(rgba[0] * 0.65 + tint_color[0] * 0.35)
                        g = int(rgba[1] * 0.65 + tint_color[1] * 0.35)
                        b = int(rgba[2] * 0.65 + tint_color[2] * 0.35)
                    else:
                        r, g, b = rgba[0], rgba[1], rgba[2]
                    dst.set(x, y, (r, g, b, a))
    return dst

# Generate 3 trailing afterimages with progressive fading
ai1 = make_afterimage(knife, 0.55, (200, 220, 255))
ai2 = make_afterimage(knife, 0.32, (175, 205, 255))
ai3 = make_afterimage(knife, 0.16, (150, 185, 255))

cw, ch = 320, 140
output = new_canvas(cw, ch, name="knife_thrust")

kx = 82
ky = 52

# Find exact blade tip
tip_x, tip_y = kw - 1, 0
for x in range(kw - 1, kw - 15, -1):
    for y in range(kh):
        if knife.get(x, y) != 0:
            tip_x, tip_y = x, y
            break
    if tip_x == x and knife.get(x, y) != 0:
        break

abs_tip_x = kx + tip_x
abs_tip_y = ky + tip_y

# Slash effect layers
slash_back = new_canvas(cw, ch, name="slash_back")
slash_front = new_canvas(cw, ch, name="slash_front")

# Palette for the white slash effect
C_WHITE = (255, 255, 255, 255)
C_GLOW_LIGHT = (210, 225, 255, 230)
C_GLOW_MID = (165, 185, 235, 180)
C_GLOW_EDGE = (110, 130, 180, 140)

# Helper for smooth cubic bezier curves
def bezier_cubic(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1-t)**3 * p0[0] + 3*(1-t)**2*t * p1[0] + 3*(1-t)*t**2 * p2[0] + t**3 * p3[0]
        y = (1-t)**3 * p0[1] + 3*(1-t)**2*t * p1[1] + 3*(1-t)*t**2 * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts

# Design dynamic crescent slash arc sweeping in front of the thrust and under the cutting edge
# Outer rim curve
p_out0 = (205, 18)
p_out1 = (275, 26)
p_out2 = (292, 65)
p_out3 = (150, 124)
pts_out = bezier_cubic(p_out0, p_out1, p_out2, p_out3, 60)

# Inner rim curve (creating crescent shape)
p_in3 = (150, 124)
p_in2 = (270, 68)
p_in1 = (245, 32)
p_in0 = (205, 18)
pts_in = bezier_cubic(p_in3, p_in2, p_in1, p_in0, 60)

poly_outer = [(int(round(x)), int(round(y))) for x, y in pts_out + pts_in]

# Mid glow crescent
p_m_out0 = (212, 22)
p_m_out1 = (272, 29)
p_m_out2 = (288, 64)
p_m_out3 = (165, 120)
pts_m_out = bezier_cubic(p_m_out0, p_m_out1, p_m_out2, p_m_out3, 50)

p_m_in3 = (165, 120)
p_m_in2 = (272, 66)
p_m_in1 = (250, 34)
p_m_in0 = (212, 22)
pts_m_in = bezier_cubic(p_m_in3, p_m_in2, p_m_in1, p_m_in0, 50)

poly_mid = [(int(round(x)), int(round(y))) for x, y in pts_m_out + pts_m_in]

# Core brilliant white crescent
p_c_out0 = (220, 26)
p_c_out1 = (270, 32)
p_c_out2 = (284, 63)
p_c_out3 = (180, 114)
pts_c_out = bezier_cubic(p_c_out0, p_c_out1, p_c_out2, p_c_out3, 40)

p_c_in3 = (180, 114)
p_c_in2 = (273, 64)
p_c_in1 = (256, 37)
p_c_in0 = (220, 26)
pts_c_in = bezier_cubic(p_c_in3, p_c_in2, p_c_in1, p_c_in0, 40)

poly_core = [(int(round(x)), int(round(y))) for x, y in pts_c_out + pts_c_in]

# Draw crescent layers on slash_back
slash_back.poly(poly_outer, C_GLOW_EDGE)
slash_back.poly(poly_mid, C_GLOW_LIGHT)
slash_back.poly(poly_core, C_WHITE)

# Horizontal speed and thrust lines behind/around the blade
speed_lines = [
    # (x0, y0, x1, y1)
    (140, abs_tip_y - 14, 265, abs_tip_y - 14),
    (110, abs_tip_y - 24, 240, abs_tip_y - 24),
    (75,  abs_tip_y - 9,  215, abs_tip_y - 9),
    (165, abs_tip_y + 14, 275, abs_tip_y + 14),
    (135, abs_tip_y + 24, 255, abs_tip_y + 24),
    (95,  abs_tip_y + 32, 225, abs_tip_y + 32),
    (55,  abs_tip_y + 18, 185, abs_tip_y + 18),
    (30,  abs_tip_y - 2,  160, abs_tip_y - 2),
]
for x0, y0, x1, y1 in speed_lines:
    slash_back.line(x0, y0, x1, y1, C_GLOW_LIGHT)
    # central highlight of speed line
    mx0 = x0 + (x1 - x0) // 3
    mx1 = x1 - (x1 - x0) // 4
    slash_back.line(mx0, y0, mx1, y1, C_WHITE)

# Piercing thrust diamond & beam on slash_front (in front of knife tip)
thrust_beam_core = [
    (abs_tip_x - 35, abs_tip_y),
    (abs_tip_x + 8,  abs_tip_y - 5),
    (abs_tip_x + 55, abs_tip_y),
    (abs_tip_x + 8,  abs_tip_y + 5),
]
thrust_beam_glow = [
    (abs_tip_x - 45, abs_tip_y),
    (abs_tip_x + 8,  abs_tip_y - 7),
    (abs_tip_x + 62, abs_tip_y),
    (abs_tip_x + 8,  abs_tip_y + 7),
]
slash_front.poly(thrust_beam_glow, C_GLOW_LIGHT)
slash_front.poly(thrust_beam_core, C_WHITE)
slash_front.line(abs_tip_x - 55, abs_tip_y, abs_tip_x + 65, abs_tip_y, C_WHITE)
slash_front.line(abs_tip_x - 30, abs_tip_y - 1, abs_tip_x + 35, abs_tip_y - 1, C_WHITE)
slash_front.line(abs_tip_x - 30, abs_tip_y + 1, abs_tip_x + 35, abs_tip_y + 1, C_WHITE)

# Small spark flashes near the impact / slash peak
def draw_spark(c, sx, sy, r=3):
    c.line(sx - r, sy, sx + r, sy, C_WHITE)
    c.line(sx, sy - r, sx, sy + r, C_WHITE)
    c.set(sx, sy, C_WHITE)

draw_spark(slash_front, abs_tip_x + 28, abs_tip_y - 16, 3)
draw_spark(slash_front, abs_tip_x + 34, abs_tip_y + 12, 3)
draw_spark(slash_front, abs_tip_x + 52, abs_tip_y, 2)
draw_spark(slash_back, 285, 52, 3)

# Composite all layers onto output:
# 1. Semi-transparent afterimages
output.blit(ai3, kx - 66, ky)
output.blit(ai2, kx - 44, ky)
output.blit(ai1, kx - 22, ky)

# 2. Background slash elements (crescent arc and speed lines)
output.blit(slash_back, 0, 0)

# 3. Main knife (fully opaque, posed thrusting right with cutting edge down)
output.blit(knife, kx, ky)

# 4. Foreground thrust flash and piercing slash lines
output.blit(slash_front, 0, 0)

view(output)
finish(output)
