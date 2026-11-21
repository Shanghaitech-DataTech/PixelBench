from pixelbench_api import *

c = new_canvas(64, 64, background=None, name="weapon_set")

OUT = "#14141f"      # dark outline
STEEL = "#c9d2dc"
STEEL_D = "#8a95a3"
STEEL_L = "#eef3f8"
WOOD = "#8b5a2b"
WOOD_D = "#5c3a1a"
GOLD = "#e0b040"
GOLD_D = "#9a7220"
RED = "#b03030"
LEATHER = "#6b3f22"

# ---------------- SWORD (top-left, 0..31) ----------------
# blade
c.rect(15, 3, 3, 20, STEEL)
c.set(15, 3, STEEL_L); c.set(16, 3, STEEL_L); c.set(17, 4, STEEL_L)
c.set(17, 21, STEEL_D); c.set(17, 20, STEEL_D); c.set(17, 19, STEEL_D)
c.set(16, 6, STEEL_L); c.set(16, 9, STEEL_L); c.set(16, 12, STEEL_L)
# crossguard
c.rect(11, 23, 11, 2, GOLD)
c.set(11, 23, GOLD_D); c.set(21, 24, GOLD_D)
# grip
c.rect(15, 25, 3, 5, LEATHER)
c.set(15, 26, WOOD_D); c.set(15, 28, WOOD_D)
# pommel
c.rect(14, 30, 5, 2, GOLD)
c.set(14, 31, GOLD_D); c.set(18, 31, GOLD_D)

# ---------------- BOW (top-right, 32..63) ----------------
ox = 32
# bow body: arc bulging left
c.path(f"M {ox+11} 3 Q {ox-1} 16 {ox+11} 29", WOOD, fill=False)
c.path(f"M {ox+12} 3 Q {ox} 16 {ox+12} 29", WOOD, fill=False)
c.path(f"M {ox+13} 3 Q {ox+1} 16 {ox+13} 29", WOOD_D, fill=False)
# string
c.line(ox+12, 3, ox+12, 29, "#d8d8d8")
# grip wrap
c.rect(ox+7, 14, 3, 5, LEATHER)
c.set(ox+7, 15, WOOD_D); c.set(ox+7, 17, WOOD_D)
# arrow nocked, pointing right
c.line(ox+8, 16, ox+26, 16, WOOD)
c.poly([(ox+26, 14), (ox+30, 16), (ox+26, 18)], STEEL)
c.set(ox+7, 15, RED); c.set(ox+7, 16, RED); c.set(ox+7, 17, RED)
c.set(ox+8, 15, RED); c.set(ox+8, 17, RED)
# fletching
c.line(ox+10, 14, ox+13, 12, RED)
c.line(ox+11, 14, ox+14, 12, RED)
c.line(ox+10, 18, ox+13, 20, RED)
c.line(ox+11, 18, ox+14, 20, RED)

# ---------------- SHIELD (bottom-left, 0..31 x 32..63) ----------------
oy = 32
c.poly([(10, oy+4), (22, oy+4), (22, oy+16), (16, oy+26), (10, oy+16)], STEEL)
# inner shading
c.poly([(12, oy+6), (20, oy+6), (20, oy+15), (16, oy+22), (12, oy+15)], STEEL_D)
# gold trim on top edge
c.rect(10, oy+4, 13, 2, GOLD)
c.set(22, oy+5, GOLD_D); c.set(10, oy+5, GOLD_D)
# boss
c.circle(16, oy+11, 2, GOLD)
c.set(15, oy+10, GOLD_D); c.set(16, oy+10, GOLD_D)
c.set(16, oy+11, GOLD_D)
# highlight
c.set(12, oy+7, STEEL_L); c.set(13, oy+7, STEEL_L)
# rivets
c.set(11, oy+8, GOLD_D); c.set(21, oy+8, GOLD_D)
c.set(13, oy+14, GOLD_D); c.set(19, oy+14, GOLD_D)

# ---------------- BATTLE AXE (bottom-right, 32..63 x 32..63) ----------------
ox, oy = 32, 32
# handle diagonal
c.line(ox+7, oy+27, ox+20, oy+8, WOOD)
c.line(ox+8, oy+27, ox+21, oy+8, WOOD_D)
# blade: crescent on upper right of handle
c.poly([(ox+16, oy+2), (ox+27, oy+5), (ox+28, oy+13), (ox+20, oy+10),
        (ox+15, oy+7)], STEEL)
c.poly([(ox+17, oy+4), (ox+25, oy+6), (ox+25, oy+11), (ox+19, oy+9),
        (ox+16, oy+7)], STEEL_D)
c.set(ox+17, oy+3, STEEL_L); c.set(ox+18, oy+3, STEEL_L)
c.set(ox+26, oy+7, STEEL_L)
# binding on handle
c.rect(ox+10, oy+21, 3, 2, LEATHER)
c.set(ox+10, oy+21, WOOD_D)
# pommel
c.rect(ox+5, oy+27, 4, 3, GOLD)
c.set(ox+5, oy+29, GOLD_D); c.set(ox+8, oy+29, GOLD_D)

# unified dark outline around all icons
c.outline(OUT)

print(c.stats_text())
save("weapon_set", c)
finish(c)
