from pixelbench_api import *

c = new_canvas(128, 128, name="red-roofed-forge-house")

# ---------------- palette ----------------
OUT   = c.color((30,24,28), "outline")
ROOF  = c.color((188,56,44), "roof")
ROOF_D = c.color((150,44,36), "roof_dark")
ROOF_L = c.color((222,86,62), "roof_light")
ROOF_LN= c.color((128,38,32), "roof_line")
WALL_L= c.color((226,202,162), "wall_left")
WALL_R= c.color((208,178,140), "wall_right")
WALL_LN= c.color((168,138,102), "wall_line")
FND  = c.color((196,176,148), "found")
FND_S= c.color((150,126,100), "found_side")
DOOR = c.color((90,58,34), "door")
DOOR_G= c.color((70,42,26), "door_in")
GLOW = c.color((255,148,30), "glow")
GLOWC= c.color((255,212,92), "glow_core")
GLOWD= c.color((255,120,40,90), "glow_dim")
BAR  = c.color((178,118,60), "barrel")
BAR_D= c.color((134,86,42), "barrel_d")
BAND = c.color((58,50,44), "band")
BT  = c.color((206,150,84), "barrel_top")
CHIM = c.color((158,156,160), "chimney")
CHIMD= c.color((118,114,122), "chimney_d")
CHIMT= c.color((184,182,188), "chimney_t")
SMOK = c.color((238,236,240), "smoke")
SMOD = c.color((200,200,208), "smoke_d")
GR_D = c.color((90,130,60), "grass_d")
GR  = c.color((116,156,84), "grass")

# ---------------- 1. ground ----------------
c.poly([(28,84),(64,65),(100,84),(64,103)], GR_D)
c.poly([(30,84),(64,67),(98,84),(64,101)], GR)

# ---------------- 2. warm glow pool ----------------
c.ellipse(52,89,13,6, GLOWD)
c.ellipse(52,88,8,4, GLOWD)

# ---------------- 3. foundation ----------------
c.poly([(30,84),(64,66),(98,84),(64,102)], FND_S)
c.poly([(32,84),(64,68),(96,84),(64,100)], FND)
c.poly([(30,84),(64,66),(98,84),(64,102)], OUT, False)

# ---------------- 4. walls ----------------
c.poly([(34,82),(64,97),(64,77),(34,62)], WALL_L)
c.poly([(64,97),(94,82),(94,62),(64,77)], WALL_R)
c.poly([(34,82),(64,97),(64,77),(34,62)], OUT, False)
c.poly([(64,97),(94,82),(94,62),(64,77)], OUT, False)
c.line(44,67, 44,87, WALL_LN)
c.line(54,72, 54,92, WALL_LN)
c.line(84,67, 84,87, WALL_LN)

# ---------------- 5. furnace window + door ----------------
c.poly([(46,67),(58,73),(58,86),(46,80)], GLOW)
c.poly([(46,67),(58,73),(58,86),(46,80)], OUT, False)
c.poly([(48,69),(56,74),(56,84),(48,79)], GLOWC)
c.poly([(72,77),(84,70),(84,84),(72,91)], DOOR)
c.poly([(72,77),(84,70),(84,84),(72,91)], OUT, False)
c.poly([(74,78),(82,72),(82,84),(74,90)], DOOR_G)

# ---------------- 6. roof ----------------
c.poly([(50,52),(78,52),(64,46)], ROOF_D)
c.poly([(32,61),(50,52),(78,52),(96,61),(64,77)], ROOF)
c.poly([(32,61),(50,52),(64,46),(78,52),(96,61),(64,77)], OUT, False)
c.line(50,52, 78,52, ROOF_L)
c.line(42,56, 88,56, ROOF_LN)
c.line(34,62, 94,62, ROOF_LN)
c.line(44,67, 84,67, ROOF_LN)
c.line(54,72, 76,72, ROOF_LN)

# ---------------- 7. chimney ----------------
c.rect(54,26,16,4, CHIMD)
c.rect(56,30,12,18, CHIM)
c.rect(64,30,4,18, CHIMD)
c.rect(56,30,12,18, OUT, False)
c.rect(54,26,16,4, OUT, False)

# ---------------- 8. smoke ----------------
c.circle(61,23,3, SMOK)
c.circle(64,19,3, SMOD)
c.circle(59,15,3, SMOK)
c.circle(62,11,3, SMOD)
c.circle(58,7,3, SMOK)
c.circle(60,4,2, SMOK)

# ---------------- 9. barrels ----------------
def barrel(cx, gy):
    x0, y0 = cx - 9, gy - 3
    c.rect(x0, y0, 18, 13, BAR)
    c.rect(x0, y0 + 2, 18, 2, BAND)
    c.rect(x0, y0 + 8, 18, 2, BAND)
    c.ellipse(cx, gy - 5, 9, 4, BAR_D)
    c.ellipse(cx, gy - 6, 9, 4, BT)
    c.line(cx - 6, y0, cx - 6, gy + 9, BAR_D)
    c.line(cx - 3, y0, cx - 3, gy + 9, BAR_D)
    c.line(cx + 3, y0, cx + 3, gy + 9, BAR_D)
    c.line(cx + 6, y0, cx + 6, gy + 9, BAR_D)
    c.rect(x0, y0, 18, 13, OUT, False)
    c.ellipse(cx, gy - 5, 9, 4, OUT, False)

barrel(105, 117)
barrel(118, 115)
barrel(112, 98)

# ---------------- 10. wooden sign ----------------
c.rect(20, 84, 4, 26, BAR)
c.rect(20, 84, 4, 26, OUT, False)
c.rect(20, 88, 4, 2, BAND)
c.rect(20, 100, 4, 2, BAND)
c.rect(10, 71, 34, 13, BAR)
c.rect(10, 71, 34, 13, OUT, False)
c.text(12, 73, "FORGE", DOOR_G)
c.rect(13, 72, 2, 2, BAR_D)
c.rect(33, 72, 2, 2, BAR_D)

# ---------------- 11. grass tufts ----------------
c.poly([(28, 84), (36, 88), (32, 96)], GR_D)
c.poly([(92, 84), (86, 86), (90, 93)], GR)

# ---------------- finish ----------------
print(c.stats_text())
finish(c)
