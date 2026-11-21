# Isometric forge house - RTS strategy tileset style, 128x128
# Red tiled roof, furnace glow, wooden sign, stacked barrels, small chimney.

c = new_canvas(128, 128, name="forge")

# ---------------- palette ----------------
GRASS      = "#6f9c46"
GRASS_DK   = "#59823a"
GRASS_LT   = "#82b155"
DIRT       = "#8a6238"
DIRT_DK    = "#6d4c2b"
DIRT_LT    = "#9c7446"

STONE_SE   = "#c9b99c"   # lit wall (front-right)
STONE_SE_D = "#b3a285"
STONE_SE_L = "#d8c9ae"
STONE_SW   = "#a08e73"   # shaded wall (front-left)
STONE_SW_D = "#8b7a60"
STONE_SW_L = "#b09e82"
GABLE      = "#d3c3a5"
GABLE_D    = "#b8a687"

ROOF_SW    = "#b53a2c"   # lit slope
ROOF_SW_L  = "#cf5540"
ROOF_SW_D  = "#8e2a20"
ROOF_NE    = "#8e2c22"   # shaded slope
ROOF_NE_D  = "#74211a"
RIDGE      = "#d4634c"
RIDGE_D    = "#7c231a"
FASCIA     = "#54331e"

CH_ST      = "#8f8f98"   # chimney stone
CH_ST_D    = "#71717a"
CH_ST_L    = "#a9a9b2"
CH_TOP     = "#33333c"
SMOKE      = "#cfd2da"
SMOKE_D    = "#aeb2bc"

FURN_DK    = "#241418"
FURN_OR    = "#e86a1e"
FURN_YL    = "#ffc22e"
FURN_HOT   = "#ffe98a"

WOOD       = "#8a5a30"   # door / sign
WOOD_DK    = "#5f3d1e"
WOOD_LT    = "#a06f3e"
WOOD_PALE  = "#c79a5e"
ICON       = "#e8c368"
METAL      = "#8b93a1"

BARREL     = "#9c6b3c"
BARREL_DK  = "#6f4a26"
BARREL_LT  = "#b5814c"
BAND       = "#4a3a2c"

OUTLINE    = "#2e2420"
SHADOW     = "#4e7036"

# ---------------- key geometry ----------------
# wall-top diamond:  N(64,26) E(108,48) S(64,70) W(20,48)
# wall-base diamond: N(64,56) E(108,78) S(64,100) W(20,78)
# eaves diamond:     N(64,24) E(112,48) S(64,72) W(16,48)
# ridge:             (40,14) -> (88,38)

# ---------------- grass terrain tile ----------------
c.poly([(64,40),(124,72),(64,104),(4,72)], GRASS)
# dirt thickness (front-left and front-right faces)
c.poly([(4,72),(64,104),(64,110),(4,78)], DIRT)
c.poly([(64,104),(124,72),(124,78),(64,110)], DIRT_DK)
c.line(4,72,4,78, DIRT_DK)
c.line(124,72,124,78, DIRT_DK)
c.line(4,78,64,110, DIRT_DK)
c.line(64,110,124,78, "#5a3d21")
# dirt speckle
for (x,y) in [(20,84),(34,92),(50,101),(78,101),(94,92),(110,83),(30,88),(60,105),(88,96),(104,87)]:
    c.set(x,y,DIRT_LT)
for (x,y) in [(26,88),(44,97),(70,104),(86,98),(100,89),(116,80)]:
    c.set(x,y,"#5a3d21")
# grass texture tufts
tufts = [(30,60),(46,52),(80,50),(96,58),(110,66),(18,70),(40,86),(56,94),
         (74,90),(90,80),(104,72),(60,62),(86,64),(52,74),(68,80),(24,76),
         (112,70),(8,73),(120,74),(64,98),(38,64),(92,54)]
for (x,y) in tufts:
    c.set(x,y,GRASS_DK)
    c.set(x+1,y,GRASS_LT)
    c.set(x-1,y+1,GRASS_DK)
# small stones on grass
c.set(36,80,GRASS_DK); c.set(37,80,"#9aa0a8"); c.set(37,81,"#7d838c")
c.set(100,64,"#9aa0a8"); c.set(101,64,"#7d838c"); c.set(100,65,"#7d838c")

# building shadow on grass (cast to the front-left)
c.poly([(20,78),(64,100),(64,104),(52,104),(14,85),(14,81)], SHADOW)

# ---------------- walls ----------------
# SW wall (shaded, front-left)
c.poly([(20,48),(64,70),(64,100),(20,78)], STONE_SW)
# SE wall (lit, front-right)
c.poly([(64,70),(108,48),(108,78),(64,100)], STONE_SE)
# SE gable triangle
c.poly([(64,70),(108,48),(86,37)], GABLE)

# stone coursing - SW wall (lines slope +0.5)
for y0 in (54,60,66,72,78,84,90):
    c.line(20,y0,64,y0+22, STONE_SW_D)
# vertical joints SW
joints_sw = [(28,54,28,58),(44,60,44,64),(34,65,34,69),(52,72,52,76),
             (24,58,24,62),(40,74,40,78),(30,81,30,85),(48,88,48,92),
             (58,84,58,88),(22,68,22,72),(36,90,36,94),(60,92,60,96)]
for (x,ya,x2,yb) in joints_sw:
    c.line(x,ya,x2,yb, STONE_SW_D)
# a few lighter/darker stones SW
for (x,y) in [(32,60),(50,80),(26,72),(42,86),(56,78)]:
    c.set(x,y,STONE_SW_L); c.set(x+1,y,STONE_SW_L); c.set(x,y+1,STONE_SW_L); c.set(x+1,y+1,STONE_SW_L)

# stone coursing - SE wall (lines slope -0.5)
for y0 in (76,82,88,94):
    c.line(64,y0,108,y0-22, STONE_SE_D)
for y0 in (56,62,68):
    c.line(96,y0,108,y0-6, STONE_SE_D)
joints_se = [(70,74,70,78),(84,60,84,64),(98,58,98,62),(76,84,76,88),
             (92,72,92,76),(104,66,104,70),(68,88,68,92),(88,82,88,86),
             (102,76,102,80),(80,66,80,70),(94,52,94,56),(106,50,106,54)]
for (x,ya,x2,yb) in joints_se:
    c.line(x,ya,x2,yb, STONE_SE_D)
for (x,y) in [(90,66),(72,82),(100,70),(80,90)]:
    c.set(x,y,STONE_SE_L); c.set(x+1,y,STONE_SE_L); c.set(x,y+1,STONE_SE_L); c.set(x+1,y+1,STONE_SE_L)

# gable texture
c.line(72,62,96,50, GABLE_D)
c.line(78,55,92,48, GABLE_D)
c.line(84,47,90,44, GABLE_D)
c.line(86,66,86,60, GABLE_D)
c.line(78,62,78,58, GABLE_D)
c.line(94,58,94,54, GABLE_D)
# round vent window in the gable
c.circle(86,52,3, WOOD_DK)
c.circle(86,52,2, "#3c4a5c")
c.set(85,51,"#5c6e82"); c.set(86,51,"#5c6e82"); c.set(85,52,"#5c6e82")
c.line(86,49,86,55, WOOD_DK)
c.line(83,52,89,52, WOOD_DK)

# corner quoins at the front corner (x=64)
for y in range(72,100,4):
    c.set(64,y,STONE_SE_L); c.set(63,y,STONE_SW_L)
for y in range(50,76,4):
    c.set(20,y,STONE_SW_L)
for y in range(50,70,4):
    c.set(108,y,STONE_SE_L)

# shadow under eaves on walls
c.line(20,50,64,72, "#7c6b52")
c.line(20,49,64,71, "#7c6b52")
c.line(65,71,108,49, "#a8977a")
c.line(66,70,108,49, "#a8977a")

# ---------------- door (SE wall) ----------------
c.poly([(82,91),(96,84),(96,60),(82,67)], WOOD_DK)          # frame
c.poly([(84,89),(94,84),(94,63),(84,68)], WOOD)              # leaf
for xx in (87,90):
    ya = 67 + (84-xx)*0.5 + 1
    yb = 88 - (xx-84)*0.5 - 1
    c.line(xx,int(ya),xx,int(yb), WOOD_DK)
c.set(92,76,ICON); c.set(92,77,ICON)                        # handle
c.line(82,91,96,84, WOOD_DK)

# ---------------- hanging wooden sign (SE wall) ----------------
c.set(70,70,METAL); c.set(78,66,METAL)                      # hooks
c.line(68,72,78,67, WOOD_DK)                                # top rail
c.poly([(68,74),(80,68),(80,82),(68,88)], WOOD)             # board
c.poly([(69,75),(79,70),(79,81),(69,86)], WOOD_LT)
# horseshoe icon (forge mark)
c.line(72,76,77,74, METAL)          # arch
c.line(72,77,72,82, METAL)          # left leg
c.line(77,75,77,80, METAL)          # right leg
c.set(72,83,"#3a3a42"); c.set(77,81,"#3a3a42")   # shoe tips
c.set(74,74,SMOKE); c.set(75,74,SMOKE)           # top glint

# ---------------- window (SW wall) ----------------
c.poly([(26,57),(36,62),(36,72),(26,67)], WOOD_DK)
c.poly([(27,59),(35,63),(35,70),(27,66)], "#3c4a5c")
c.line(31,61,31,68, WOOD_DK)
c.line(27,63,35,67, WOOD_DK)
c.set(28,61,"#5c6e82"); c.set(29,61,"#5c6e82"); c.set(28,62,"#5c6e82")

# ---------------- furnace opening (SW wall) ----------------
c.path("M40 88 L56 96 L56 80 Q48 69 40 72 Z", STONE_SW_D)   # stone surround
c.path("M42 89 L54 95 L54 81 Q48 72 42 74 Z", FURN_DK)      # opening
c.path("M44 89 L52 93 L52 83 Q48 76 44 78 Z", FURN_OR)      # glow
c.path("M46 89 L50 91 L50 85 Q48 80 46 82 Z", FURN_YL)      # hot core
c.set(48,88,FURN_HOT); c.set(48,87,FURN_HOT); c.set(49,89,FURN_HOT)
c.set(47,86,FURN_HOT); c.set(49,84,FURN_YL)
# embers / coals at mouth
c.set(43,90,FURN_OR); c.set(45,91,FURN_YL); c.set(51,94,FURN_OR); c.set(53,95,FURN_YL)
# glow spill on grass below
for (x,y) in [(43,93),(46,94),(49,95),(52,96),(45,95),(50,97),(41,92),(54,97),(47,96),(52,94)]:
    c.set(x,y,FURN_OR)
for (x,y) in [(44,94),(48,95),(51,95),(47,93),(53,96)]:
    c.set(x,y,FURN_YL)
# faint glow tint on wall stones around opening
for (x,y) in [(39,74),(38,80),(39,85),(57,84),(57,90),(56,76),(46,71),(50,72)]:
    c.set(x,y,"#b07a52")

# ---------------- roof ----------------
# NE slope (shaded, drawn first)
c.poly([(40,14),(88,38),(112,48),(64,24)], ROOF_NE)
# SW slope (lit)
c.poly([(40,14),(88,38),(64,72),(16,48)], ROOF_SW)

# tile courses - SW slope
for t in (0.2,0.4,0.6,0.8):
    px, py = 16+24*t, 48-34*t
    qx, qy = 64+24*t, 72-34*t
    c.line(int(px),int(py),int(qx),int(qy), ROOF_SW_D)
    c.line(int(px),int(py)+1,int(qx),int(qy)+1, ROOF_SW_L)
# tile courses - NE slope
for t in (0.25,0.5,0.75):
    px, py = 64+24*t, 24+34*t
    qx, qy = 40+48*t, 14+24*t
    c.line(int(qx),int(qy),int(px),int(py), ROOF_NE_D)
# staggered vertical seams - SW slope
seams = [(0.15,0.25),(0.4,0.5),(0.65,0.75),(0.25,0.35),(0.5,0.6),(0.75,0.85),(0.3,0.4),(0.6,0.7)]
for (t1,t2) in seams:
    ax, ay = 16+48*t1, 48+24*t1
    bx, by = 40+48*t2, 14+24*t2
    c.line(int(ax),int(ay),int(bx),int(by), ROOF_SW_D)
# a couple of highlight tiles
for (x,y) in [(36,44),(52,52),(60,38),(44,56),(68,46),(30,40)]:
    c.set(x,y,ROOF_SW_L); c.set(x+1,y+1,ROOF_SW_L)

# ridge cap
c.line(40,14,88,38, RIDGE_D)
c.line(40,13,88,37, RIDGE)
c.line(41,12,88,36, ROOF_SW_L)

# fascia boards along eaves
c.line(16,48,64,72, FASCIA)
c.line(16,49,64,73, FASCIA)
c.line(64,72,112,48, FASCIA)
c.line(64,73,112,49, FASCIA)
# (far eaves are hidden behind the roof from this view - not drawn)
# eave corners
c.set(16,48,OUTLINE); c.set(16,49,OUTLINE)
c.set(64,72,OUTLINE); c.set(64,73,OUTLINE)
c.set(112,48,OUTLINE); c.set(112,49,OUTLINE)

# ---------------- chimney (on SW slope) ----------------
c.poly([(66,22),(72,25),(72,51),(66,48)], CH_ST_D)          # left face
c.poly([(72,25),(78,22),(78,48),(72,51)], CH_ST)            # right face
for y in (30,36,42):
    c.line(66,y+3,72,y+6, "#5d5d66")
    c.line(72,y+6,78,y+3, "#5d5d66")
c.set(68,34,CH_ST_L); c.set(69,34,CH_ST_L); c.set(74,40,CH_ST_L); c.set(75,40,CH_ST_L)
c.poly([(72,19),(78,22),(72,25),(66,22)], CH_ST_L)          # cap rim
c.poly([(72,20),(76,22),(72,24),(68,22)], CH_TOP)           # sooty mouth
# smoke puffs
c.circle(74,12,2, SMOKE)
c.circle(78,6,2, SMOKE_D)
c.circle(83,2,1, SMOKE)
c.set(76,9,SMOKE); c.set(80,4,SMOKE)

# ---------------- stacked barrels (right of door) ----------------
def barrel(cx, cy):
    # cy = bottom centre of barrel; 12 wide, 15 tall, upright cylinder
    c.ellipse(cx,cy-8,6,7, BARREL)                    # body
    c.ellipse(cx,cy-8,6,7, BARREL_DK, fill=False)     # body outline
    c.line(cx-6,cy-8,cx-6,cy-2, BARREL_DK)            # left edge shade
    c.line(cx-5,cy-11,cx-5,cy-2, BARREL_DK)
    c.line(cx+5,cy-11,cx+5,cy-2, BARREL_LT)           # right highlight
    c.line(cx+4,cy-12,cx+4,cy-2, BARREL_LT)
    c.line(cx-2,cy-11,cx-2,cy-1, BARREL_DK)
    c.line(cx+2,cy-11,cx+2,cy-1, BARREL_DK)
    c.path("M%d %d A6 2 0 0 0 %d %d" % (cx-6,cy-10,cx+6,cy-10), BAND, fill=False)
    c.path("M%d %d A6 2 0 0 0 %d %d" % (cx-6,cy-4,cx+6,cy-4), BAND, fill=False)
    c.line(cx-5,cy-1, cx+5,cy-1, BARREL_DK)           # base shade
    c.line(cx-4,cy,   cx+4,cy,   BARREL_DK)
    c.ellipse(cx,cy-14,6,3, WOOD_DK)                  # top rim
    c.ellipse(cx,cy-14,4,2, BARREL_LT)                # lid
    c.ellipse(cx,cy-14,2,1, BARREL)                   # lid centre

c.ellipse(104,81,7,2, SHADOW)
c.ellipse(114,75,7,2, SHADOW)
barrel(114,76)     # ground, right (farther)
barrel(104,82)     # ground, front of wall corner
barrel(104,66)     # stacked on the first

# ---------------- final crisp-up ----------------
# dark contact line where walls meet grass
c.line(20,78,64,100, "#3f5a2c")
c.line(64,100,108,78, "#3f5a2c")

print(c.matrix_text(region=(0,20,26,46)))
print(c.stats())
view(c, scale=4, margin=0)
save("forge_house", c)
finish(c)
