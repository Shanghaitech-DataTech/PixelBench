from pixelbench_api import *

c = new_canvas(32, 32, name="compass")

OUTLINE = (22, 13, 6)          # thick dark silhouette
GOLD_DEEP = (122, 86, 22)
GOLD = (198, 150, 48)          # antique gold body
GOLD_LIGHT = (238, 198, 96)    # main points
GOLD_HI = (255, 228, 140)
BLUE_DEEP = (12, 30, 92)
BLUE = (42, 88, 192)
BLUE_LIGHT = (110, 168, 255)
BLUE_HI = (190, 220, 255)

# --- gold compass body with thick dark rim ---
c.circle(15, 15, 14, OUTLINE)                 # 2px dark outline disc
c.circle(15, 15, 12, GOLD)                    # gold body
c.circle(15, 15, 9, GOLD_DEEP, fill=False)    # engraved ring

# --- 8-point compass star ---
c.poly([(15, 3), (27, 15), (15, 27), (3, 15)], GOLD_LIGHT)   # N/E/S/W
c.poly([(22, 8), (22, 22), (8, 22), (8, 8)], GOLD_DEEP)       # diagonals

# --- metallic highlights ---
c.set(14, 6, GOLD_HI)
c.set(15, 6, GOLD_HI)
c.set(16, 6, GOLD_HI)
c.set(8, 8, GOLD_HI)
c.set(9, 7, GOLD_HI)

# --- blue crystal center ---
c.poly([(11, 12), (12, 11), (18, 11), (19, 12), (19, 18), (18, 19), (12, 19), (11, 18)], BLUE_DEEP)
c.poly([(12, 13), (13, 12), (17, 12), (18, 13), (18, 17), (17, 18), (13, 18), (12, 17)], BLUE)
c.poly([(13, 12), (17, 12), (15, 15)], BLUE_LIGHT)            # top facet
c.set(14, 13, BLUE_HI)
c.set(15, 14, BLUE_HI)
c.set(16, 15, BLUE_HI)

print(c.stats_text())
finish(c)
