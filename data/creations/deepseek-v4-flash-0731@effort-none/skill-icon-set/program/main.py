from pixelbench_api import *

c = new_canvas(64, 64, name="skill_icons")

# Color palette
BLACK = (20, 20, 25)

# Fireball colors
FIRE_RED = (230, 60, 30)
FIRE_ORANGE = (255, 140, 20)
FIRE_YELLOW = (255, 210, 60)

# Ice colors
ICE_BLUE = (90, 170, 240)
ICE_LIGHT = (180, 220, 255)
ICE_WHITE = (240, 250, 255)

# Healing colors
HEAL_GREEN = (180, 255, 110)
HEAL_LIGHT = (230, 255, 180)
HEAL_RED = (230, 60, 80)

# Lightning colors
LIGHT_YELLOW = (255, 230, 60)
LIGHT_WHITE = (255, 255, 220)

# ============ FIREBALL (top-left, 0,0 to 31,31) ============
cx, cy = 16, 17
c.circle(cx, cy, 8, FIRE_RED)
# Inner glow
c.circle(cx, cy, 5, FIRE_ORANGE)
# Core
c.circle(cx, cy, 3, FIRE_YELLOW)

# Flame shape on top
c.poly([(8, 12), (7, 5), (10, 8), (12, 3), (15, 8), (17, 2), (19, 8), (23, 5), (22, 12)], FIRE_RED)
# Inner flame highlight
c.poly([(11, 10), (10, 7), (13, 9), (14, 6), (16, 9), (18, 5), (19, 10)], FIRE_ORANGE)
c.poly([(13, 10), (13, 8), (15, 10), (16, 7), (17, 10)], FIRE_YELLOW)

# Dark outline around the entire fireball+flame shape
outline_pts = [
    (8, 12), (7, 5), (10, 8), (12, 3), (15, 8), (17, 2), (19, 8), (23, 5), (22, 12),
]
# Top flame outline
for i in range(len(outline_pts)-1):
    c.line(outline_pts[i][0], outline_pts[i][1], outline_pts[i+1][0], outline_pts[i+1][1], BLACK)
# Connect flame to circle
c.circle(cx, cy, 8, BLACK, fill=False)
# Fill the small gap between flame bottom and circle top
c.line(8, 13, 22, 13, BLACK)
c.line(22, 12, 23, 11, BLACK)

# Sparkle highlights on the fireball
c.set(19, 14, FIRE_YELLOW)
c.set(20, 15, FIRE_YELLOW)
c.set(13, 19, FIRE_ORANGE)

# ============ ICE SHIELD (top-right, 32,0 to 63,31) ============
# A shield shape with a snowflake or ice crystal
ox, oy = 32, 0
# Shield shape: hexagonal shield
shield_pts = [
    (ox+16, oy+2),   # top
    (ox+26, oy+7),   # upper right
    (ox+26, oy+20),  # lower right
    (ox+16, oy+29),  # bottom
    (ox+6, oy+20),   # lower left
    (ox+6, oy+7),    # upper left
]
c.poly(shield_pts, ICE_BLUE)
c.poly(shield_pts, BLACK, fill=False)

# Inner shield
inner_pts = [
    (ox+16, oy+7),
    (ox+23, oy+11),
    (ox+23, oy+19),
    (ox+16, oy+25),
    (ox+9, oy+19),
    (ox+9, oy+11),
]
c.poly(inner_pts, ICE_LIGHT)
# Outline inner shield
for i in range(len(inner_pts)-1):
    c.line(inner_pts[i][0], inner_pts[i][1], inner_pts[i+1][0], inner_pts[i+1][1], BLACK)
c.line(inner_pts[-1][0], inner_pts[-1][1], inner_pts[0][0], inner_pts[0][1], BLACK)

# Ice crystal/snowflake in center
sx, sy = ox+16, oy+16
# Vertical line
c.line(sx, sy-6, sx, sy+6, ICE_WHITE)
# Horizontal line
c.line(sx-6, sy, sx+6, sy, ICE_WHITE)
# Diagonal lines
c.line(sx-4, sy-4, sx+4, sy+4, ICE_WHITE)
c.line(sx+4, sy-4, sx-4, sy+4, ICE_WHITE)
# Center dot
c.set(sx, sy, BLACK)
# Small branch marks
c.set(sx, sy-5, BLACK)
c.set(sx, sy+5, BLACK)
c.set(sx-5, sy, BLACK)
c.set(sx+5, sy, BLACK)

# Ice shine highlights on shield
c.set(ox+12, oy+10, ICE_WHITE)
c.set(ox+13, oy+9, ICE_WHITE)
c.set(ox+11, oy+11, ICE_WHITE)

# ============ HEALING (bottom-left, 0,32 to 31,63) ============
# A plus cross shape with sparkle accents (healing symbol)
hx, hy = 0, 32

# A rounded plus/cross shape (healing symbol)
# Main cross body
c.rect(hx+11, hy+5, 10, 22, HEAL_GREEN)  # vertical bar
c.rect(hx+5, hy+11, 22, 10, HEAL_GREEN)  # horizontal bar
# Inner lighter cross
c.rect(hx+13, hy+9, 6, 14, HEAL_LIGHT)
c.rect(hx+9, hy+13, 14, 6, HEAL_LIGHT)
# Center dot
c.set(hx+16, hy+16, HEAL_RED)

# Dark outline around the cross
# Vertical bar outline
c.line(hx+10, hy+5, hx+22, hy+5, BLACK)
c.line(hx+10, hy+27, hx+22, hy+27, BLACK)
c.line(hx+10, hy+5, hx+10, hy+27, BLACK)
c.line(hx+22, hy+5, hx+22, hy+27, BLACK)
# Horizontal bar extends left and right
c.line(hx+5, hy+10, hx+10, hy+10, BLACK)
c.line(hx+22, hy+10, hx+27, hy+10, BLACK)
c.line(hx+5, hy+22, hx+10, hy+22, BLACK)
c.line(hx+22, hy+22, hx+27, hy+22, BLACK)
c.line(hx+5, hy+10, hx+5, hy+22, BLACK)
c.line(hx+27, hy+10, hx+27, hy+22, BLACK)

# Small healing sparkles
c.set(hx+6, hy+18, HEAL_LIGHT)
c.set(hx+7, hy+17, HEAL_LIGHT)
c.set(hx+5, hy+18, HEAL_LIGHT)
c.set(hx+26, hy+14, HEAL_LIGHT)
c.set(hx+25, hy+13, HEAL_LIGHT)
c.set(hx+27, hy+13, HEAL_LIGHT)

# Corner sparkles
c.set(hx+8, hy+6, FIRE_RED)
c.set(hx+9, hy+5, FIRE_RED)
c.set(hx+24, hy+6, FIRE_RED)
c.set(hx+23, hy+5, FIRE_RED)
c.set(hx+8, hy+26, FIRE_RED)
c.set(hx+9, hy+27, FIRE_RED)
c.set(hx+24, hy+26, FIRE_RED)
c.set(hx+23, hy+27, FIRE_RED)

# ============ LIGHTNING (bottom-right, 32,32 to 63,63) ============
# Lightning bolt shape
lx, ly = 32, 32
bolt_pts = [
    (lx+20, ly+4),   # top right of bolt
    (lx+11, ly+24),  # bottom point going left
    (lx+16, ly+24),  # notch
    (lx+13, ly+30),  # lower point
    (lx+26, ly+15),  # upper right again
    (lx+20, ly+15),  # notch
]
# Main bolt
c.poly(bolt_pts, LIGHT_YELLOW)
# Inner bolt (darker)
inner_bolt = [
    (lx+18, ly+10),
    (lx+14, ly+21),
    (lx+17, ly+21),
    (lx+15, ly+26),
    (lx+23, ly+18),
    (lx+19, ly+18),
]
c.poly(inner_bolt, LIGHT_WHITE)

# Outline the bolt
for i in range(len(bolt_pts)-1):
    c.line(bolt_pts[i][0], bolt_pts[i][1], bolt_pts[i+1][0], bolt_pts[i+1][1], BLACK)
c.line(bolt_pts[-1][0], bolt_pts[-1][1], bolt_pts[0][0], bolt_pts[0][1], BLACK)

# Small lightning energy sparks around
c.set(lx+8, ly+8, LIGHT_YELLOW)
c.set(lx+9, ly+7, LIGHT_YELLOW)
c.set(lx+26, ly+9, LIGHT_YELLOW)
c.set(lx+27, ly+10, LIGHT_YELLOW)
c.set(lx+5, ly+8, LIGHT_YELLOW)
c.set(lx+6, ly+9, LIGHT_YELLOW)
c.set(lx+6, ly+6, LIGHT_YELLOW)
c.set(lx+7, ly+7, LIGHT_YELLOW)

# Check stats
print(c.stats_text())

# Submit
finish(c)
