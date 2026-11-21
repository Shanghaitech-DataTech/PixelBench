from pixelbench_api import new_canvas, view, finish

c = new_canvas(64, 64, background=None, name="cheerleader_four_views")

INK = "#241b2b"
HAIR_D = "#9b5428"
HAIR = "#e0a037"
HAIR_H = "#f4cf5a"
SKIN_D = "#c97865"
SKIN = "#f0ad88"
SKIN_H = "#ffd0a5"
RED_D = "#8f2944"
RED = "#d9405b"
RED_H = "#f05b70"
CREAM = "#fff1d2"
GOLD = "#f6c644"

# Small helpers keep the four sprites on the same pixel language.
def px(x, y, w, h, col):
    c.rect(x, y, w, h, col)

def front(ox, oy):
    # Ponytail and hair silhouette.
    px(ox+6, oy+5, 3, 9, INK); px(ox+5, oy+7, 2, 7, INK)
    px(ox+7, oy+5, 2, 8, HAIR_D); px(ox+6, oy+8, 2, 5, HAIR)
    px(ox+10, oy+2, 12, 11, INK)
    px(ox+12, oy+1, 8, 2, INK); px(ox+9, oy+4, 2, 6, INK); px(ox+21, oy+4, 2, 7, INK)
    px(ox+11, oy+3, 10, 5, HAIR); px(ox+12, oy+2, 7, 2, HAIR_H)
    px(ox+10, oy+6, 12, 6, SKIN)
    px(ox+11, oy+5, 3, 2, HAIR); px(ox+14, oy+4, 7, 2, HAIR)
    px(ox+10, oy+8, 2, 3, HAIR_D); px(ox+20, oy+8, 2, 3, HAIR_D)
    px(ox+13, oy+8, 2, 2, INK); px(ox+18, oy+8, 2, 2, INK)
    px(ox+14, oy+11, 5, 1, SKIN_H)
    # Neck, arms, torso; hands-on-hips cheer pose.
    px(ox+14, oy+12, 5, 3, INK); px(ox+15, oy+12, 3, 3, SKIN)
    px(ox+10, oy+14, 12, 9, INK)
    px(ox+8, oy+15, 3, 7, INK); px(ox+6, oy+18, 3, 5, INK)
    px(ox+21, oy+15, 3, 7, INK); px(ox+23, oy+18, 3, 5, INK)
    px(ox+8, oy+16, 2, 5, SKIN); px(ox+7, oy+19, 2, 3, SKIN_H)
    px(ox+22, oy+16, 2, 5, SKIN); px(ox+24, oy+19, 2, 3, SKIN_H)
    px(ox+11, oy+14, 10, 8, RED)
    px(ox+12, oy+14, 8, 2, CREAM); px(ox+14, oy+16, 4, 2, GOLD)
    px(ox+12, oy+18, 8, 1, RED_H); px(ox+12, oy+21, 8, 2, CREAM)
    # Pleated skirt.
    c.poly([(ox+10,oy+22),(ox+22,oy+22),(ox+25,oy+26),(ox+7,oy+26)], INK)
    c.poly([(ox+11,oy+22),(ox+21,oy+22),(ox+23,oy+25),(ox+9,oy+25)], RED)
    px(ox+11, oy+23, 2, 2, CREAM); px(ox+15, oy+23, 2, 2, RED_H); px(ox+20, oy+23, 2, 2, CREAM)
    # Legs and ankle boots.
    px(ox+10, oy+26, 5, 5, INK); px(ox+18, oy+26, 5, 5, INK)
    px(ox+11, oy+26, 3, 4, SKIN); px(ox+19, oy+26, 3, 4, SKIN)
    px(ox+9, oy+30, 6, 2, INK); px(ox+18, oy+30, 6, 2, INK)
    px(ox+10, oy+30, 4, 1, CREAM); px(ox+19, oy+30, 4, 1, CREAM)

def back(ox, oy):
    # Back hair and centered ponytail.
    px(ox+13, oy+1, 8, 2, INK); px(ox+10, oy+3, 14, 11, INK)
    px(ox+12, oy+2, 10, 9, HAIR); px(ox+11, oy+5, 12, 7, HAIR)
    px(ox+13, oy+2, 7, 2, HAIR_H); px(ox+11, oy+9, 3, 4, HAIR_D); px(ox+20, oy+8, 3, 5, HAIR_D)
    px(ox+15, oy+11, 5, 3, INK); px(ox+14, oy+12, 7, 6, INK)
    px(ox+15, oy+12, 5, 5, HAIR_D); px(ox+16, oy+13, 3, 5, HAIR); px(ox+17, oy+17, 2, 2, HAIR_D)
    # Neck and same hands-on-hips pose.
    px(ox+14, oy+12, 6, 4, INK); px(ox+15, oy+12, 4, 3, SKIN)
    px(ox+10, oy+14, 13, 9, INK)
    px(ox+8, oy+15, 3, 7, INK); px(ox+6, oy+18, 3, 5, INK)
    px(ox+22, oy+15, 3, 7, INK); px(ox+24, oy+18, 3, 5, INK)
    px(ox+8, oy+16, 2, 5, SKIN); px(ox+7, oy+19, 2, 3, SKIN)
    px(ox+23, oy+16, 2, 5, SKIN); px(ox+25, oy+19, 2, 3, SKIN)
    px(ox+11, oy+14, 11, 8, RED_D); px(ox+12, oy+15, 9, 2, RED)
    px(ox+15, oy+16, 3, 4, GOLD); px(ox+12, oy+20, 9, 2, CREAM)
    # Skirt, legs, boots.
    c.poly([(ox+10,oy+22),(ox+23,oy+22),(ox+25,oy+26),(ox+8,oy+26)], INK)
    c.poly([(ox+11,oy+22),(ox+22,oy+22),(ox+23,oy+25),(ox+10,oy+25)], RED_D)
    px(ox+12, oy+23, 2, 2, CREAM); px(ox+16, oy+23, 2, 2, RED); px(ox+21, oy+23, 2, 2, CREAM)
    px(ox+10, oy+26, 5, 5, INK); px(ox+19, oy+26, 5, 5, INK)
    px(ox+11, oy+26, 3, 4, SKIN); px(ox+20, oy+26, 3, 4, SKIN)
    px(ox+9, oy+30, 6, 2, INK); px(ox+19, oy+30, 6, 2, INK)
    px(ox+10, oy+30, 4, 1, CREAM); px(ox+20, oy+30, 4, 1, CREAM)

def side(ox, oy, facing):
    # Draw a right-facing profile, then mirror the cell externally for left.
    px(ox+7, oy+5, 4, 10, INK); px(ox+6, oy+8, 3, 7, INK)
    px(ox+8, oy+5, 3, 8, HAIR_D); px(ox+7, oy+9, 3, 5, HAIR)
    px(ox+11, oy+2, 11, 11, INK); px(ox+12, oy+1, 7, 2, INK)
    px(ox+11, oy+4, 9, 8, HAIR); px(ox+12, oy+2, 7, 3, HAIR_H)
    # Profile face and nose.
    px(ox+16, oy+5, 6, 7, SKIN); px(ox+21, oy+7, 2, 3, INK); px(ox+21, oy+7, 2, 2, SKIN_H)
    px(ox+18, oy+6, 2, 2, INK); px(ox+20, oy+10, 2, 1, SKIN_D)
    px(ox+11, oy+8, 2, 4, HAIR_D); px(ox+14, oy+11, 6, 2, INK)
    # Neck and torso.
    px(ox+14, oy+12, 5, 3, INK); px(ox+15, oy+12, 3, 3, SKIN)
    px(ox+11, oy+14, 10, 9, INK); px(ox+12, oy+14, 8, 8, RED)
    px(ox+13, oy+14, 6, 2, CREAM); px(ox+14, oy+16, 4, 2, GOLD); px(ox+13, oy+20, 7, 2, CREAM)
    # One arm bent forward, far arm visible behind.
    px(ox+10, oy+15, 3, 8, INK); px(ox+9, oy+20, 3, 4, INK)
    px(ox+11, oy+16, 2, 6, SKIN_D); px(ox+10, oy+21, 2, 2, SKIN)
    px(ox+20, oy+15, 3, 5, INK); px(ox+22, oy+18, 5, 3, INK); px(ox+25, oy+16, 3, 4, INK)
    px(ox+21, oy+16, 2, 3, SKIN); px(ox+23, oy+19, 4, 2, SKIN); px(ox+26, oy+17, 2, 3, SKIN_H)
    # Side skirt, offset legs and boots.
    c.poly([(ox+11,oy+22),(ox+21,oy+22),(ox+23,oy+26),(ox+9,oy+26)], INK)
    c.poly([(ox+12,oy+22),(ox+20,oy+22),(ox+21,oy+25),(ox+11,oy+25)], RED)
    px(ox+12, oy+23, 2, 2, CREAM); px(ox+18, oy+23, 2, 2, RED_H)
    px(ox+11, oy+26, 5, 5, INK); px(ox+18, oy+26, 5, 5, INK)
    px(ox+12, oy+26, 3, 4, SKIN); px(ox+19, oy+26, 3, 4, SKIN)
    px(ox+9, oy+30, 7, 2, INK); px(ox+18, oy+30, 7, 2, INK)
    px(ox+10, oy+30, 5, 1, CREAM); px(ox+19, oy+30, 5, 1, CREAM)

front(0, 0)
back(32, 0)
# Draw the right profile, then mirror its fixed snapshot into the left cell.
side(32, 32, "right")
c.select(32, 32, 32, 32).flip("h").copy_to(0, 32, c, mode="replace")

view(c, scale=8, margin=0)
finish(c)
