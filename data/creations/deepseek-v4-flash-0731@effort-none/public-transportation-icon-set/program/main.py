from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64)

# ===== Palette =====
INK   = (32, 36, 44)      # dark outline
PAPER = (245, 245, 245)   # light body fill
BLUE  = (90, 150, 220)    # bus body
RED   = (220, 95, 90)     # subway body
GREEN = (100, 180, 100)   # bicycle frame
AMBER = (240, 205, 90)    # accents / lights
SKIN  = (243, 203, 153)   # pedestrian head
LIGHT = (176, 214, 242)   # glass window light blue

def origin(cell):
    return (cell % 2) * 32, (cell // 2) * 32

# ===== BUS (cell 0) =====
ox, oy = origin(0)
c.rect(ox+7, oy+10, 18, 13, BLUE)            # body
c.rect(ox+7, oy+10, 18, 13, INK, fill=False)  # outline
c.rect(ox+8, oy+11, 16, 2, (131,178,233))     # roof highlight
# windshield (front right)
c.poly([(ox+20, oy+11), (ox+24, oy+11), (ox+24, oy+15), (ox+20, oy+15)], LIGHT)
c.poly([(ox+20, oy+11), (ox+24, oy+11), (ox+24, oy+15), (ox+20, oy+15)], INK, fill=False)
# side windows
c.rect(ox+9, oy+12, 9, 4, LIGHT)
c.rect(ox+9, oy+12, 9, 4, INK, fill=False)
c.line(ox+13, oy+12, ox+13, oy+15, INK)
# door
c.rect(ox+11, oy+17, 4, 6, PAPER)
c.rect(ox+11, oy+17, 4, 6, INK, fill=False)
c.line(ox+13, oy+17, ox+13, oy+22, INK)
# wheels
c.rect(ox+8, oy+23, 4, 4, INK)
c.rect(ox+20, oy+23, 4, 4, INK)
c.rect(ox+9, oy+23, 2, 1, PAPER)
c.rect(ox+21, oy+23, 2, 1, PAPER)
# lights
c.set(ox+24, oy+20, AMBER)
c.set(ox+24, oy+21, PAPER)
c.set(ox+7, oy+20, RED)

# ===== SUBWAY (cell 1) =====
ox, oy = origin(1)
c.rect(ox+6, oy+10, 20, 13, RED)             # body
c.rect(ox+6, oy+10, 20, 13, INK, fill=False)
c.rect(ox+6, oy+10, 20, 2, (235,132,127))     # roof
# windshield slanted front (right)
c.poly([(ox+18, oy+11), (ox+24, oy+11), (ox+21, oy+16), (ox+18, oy+16)], (255,206,200))
c.poly([(ox+18, oy+11), (ox+24, oy+11), (ox+21, oy+16), (ox+18, oy+16)], INK, fill=False)
# windows
c.rect(ox+8, oy+13, 8, 4, (255,210,205))
c.rect(ox+8, oy+13, 8, 4, INK, fill=False)
c.line(ox+12, oy+13, ox+12, oy+16, INK)
# door
c.rect(ox+9, oy+18, 4, 6, PAPER)
c.rect(ox+9, oy+18, 4, 6, INK, fill=False)
# headlight
c.set(ox+25, oy+18, AMBER)
c.rect(ox+18, oy+18, 4, 2, (255,206,200))
# rail
c.line(ox+6, oy+24, ox+25, oy+24, INK)
c.line(ox+7, oy+25, ox+24, oy+25, INK)

# ===== BICYCLE (cell 2) =====
ox, oy = origin(2)
# wheels — proper rings with visible hubs
c.circle(ox+11, oy+17, 5, INK, fill=False)
c.circle(ox+21, oy+17, 5, INK, fill=False)
c.circle(ox+11, oy+17, 2, INK, fill=False)
c.circle(ox+21, oy+17, 2, INK, fill=False)
# frame (diamond, clean)
c.line(ox+16, oy+8,  ox+16, oy+12, INK)   # seat post
c.line(ox+14, oy+8,  ox+18, oy+8,  INK)   # seat
c.line(ox+16, oy+12, ox+20, oy+15, INK)   # top tube
c.line(ox+16, oy+12, ox+11, oy+17, INK)   # down tube (to rear hub)
c.line(ox+20, oy+15, ox+21, oy+17, INK)   # seat stay
c.line(ox+16, oy+12, ox+21, oy+17, INK)   # chain stay
c.line(ox+20, oy+15, ox+22, oy+13, INK)   # handlebar stem
c.line(ox+22, oy+12, ox+24, oy+14, INK)   # handlebar
c.line(ox+16, oy+12, ox+16, oy+15, INK)   # seat tube lower
c.line(ox+16, oy+15, ox+18, oy+15, INK)   # crank
# front fork
c.line(ox+21, oy+17, ox+23, oy+15, INK)

# ===== PEDESTRIAN (cell 3) =====
ox, oy = origin(3)
# head
c.circle(ox+16, oy+10, 3, SKIN)
c.set(ox+16, oy+10, SKIN)
# torso
c.rect(ox+14, oy+15, 4, 6, BLUE)
c.rect(ox+14, oy+15, 4, 6, INK, fill=False)
c.line(ox+14, oy+15, ox+18, oy+15, INK)
c.line(ox+14, oy+21, ox+18, oy+21, INK)
# arms
c.line(ox+14, oy+16, ox+11, oy+19, INK)
c.line(ox+18, oy+16, ox+21, oy+19, INK)
# legs
c.line(ox+15, oy+21, ox+14, oy+25, INK)
c.line(ox+17, oy+21, ox+19, oy+25, INK)
# shoes
c.set(ox+13, oy+25, INK); c.set(ox+12, oy+25, INK)
c.set(ox+19, oy+25, INK); c.set(ox+20, oy+25, INK)

print(c.stats_text())
finish(c)
