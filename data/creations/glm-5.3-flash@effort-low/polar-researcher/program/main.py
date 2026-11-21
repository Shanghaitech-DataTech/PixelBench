c = new_canvas(48, 48, name="polar-researcher")

PARKA_D = "#2b4a6f"
PARKA_M = "#3d6a99"
PARKA_L = "#5b8ab8"
FUR     = "#e8e4d8"
FUR_S   = "#c9c2b0"
SKIN    = "#e0b08a"
GOG     = "#1d2b3a"
GOG_R   = "#aee0ff"
GOG_R2  = "#d8f2ff"
PANT    = "#33404f"
PANT_D  = "#232c38"
BOOT    = "#1c222c"
CASE    = "#8a5a33"
CASE_D  = "#6b421f"
CASE_L  = "#b07a45"
METAL   = "#c8ccd4"
MITT    = "#4a5568"

def px(x,y,col): c.set(x,y,col)
def r(x,y,w,h,col): c.rect(x,y,w,h,col)

# ---- legs (leaning: front leg forward-right, back leg trailing left)
# back leg
r(16,32,5,8,PANT)
r(15,39,6,5,BOOT)
px(15,39,BOOT); px(14,40,BOOT)
# front leg
r(27,31,5,9,PANT)
r(26,39,7,5,BOOT)
r(26,42,8,2,BOOT)

# ---- torso, leaning right (shifted right toward top)
# rows from y=18 to y=33, widening
torso = [
 (20,18,14),(19,19,15),(19,20,16),(18,21,17),(18,22,17),(18,23,17),
 (18,24,17),(18,25,17),(18,26,17),(18,27,17),(18,28,16),(19,29,15),
 (19,30,14),(20,31,13),
]
for (x,y,w) in torso:
    r(x,y,w,1,PARKA_D)
# highlight on windward (right) side
r(29,19,3,10,PARKA_M)
r(30,20,2,6,PARKA_L)
# zipper line
for y in range(22,32): px(25,y,PARKA_M)
px(25,21,METAL)

# ---- head, leaning forward (right)
r(28,10,9,9,SKIN)          # face
r(27,11,1,7,SKIN)
# hood behind/left of face
r(24,8,6,12,PARKA_D)
r(24,7,10,2,PARKA_D)
r(33,9,3,9,PARKA_D)
r(23,9,1,9,PARKA_D)
# fur trim around hood
for x in range(24,36): px(x,7,FUR)
px(23,8,FUR); px(23,9,FUR); px(23,10,FUR_S)
px(36,9,FUR); px(36,10,FUR); px(36,11,FUR_S)
px(24,18,FUR); px(25,19,FUR); px(26,19,FUR_S)
# goggles: pale blue reflections
r(29,12,8,4,GOG)
r(30,13,3,2,GOG_R)
px(30,13,GOG_R2); px(31,13,GOG_R2)
px(35,13,GOG_R)
# mouth/scarf
r(30,17,6,2,FUR_S)
# wind-blown fur wisps
px(22,8,FUR); px(21,9,FUR_S); px(20,10,FUR_S)

# ---- arms: reaching forward with case
# rear arm (left, bent back)
r(18,22,4,4,PARKA_D)
r(16,25,4,4,PARKA_D)
r(15,28,5,3,MITT)
# front arm extended forward-down toward case
r(31,21,4,3,PARKA_M)
r(34,23,4,3,PARKA_M)
r(37,25,4,3,MITT)
px(40,26,MITT); px(40,27,MITT)

# ---- sample case carried in front hand
r(38,27,8,6,CASE)
r(38,27,8,1,CASE_L)
r(38,32,8,1,CASE_D)
r(41,26,2,1,METAL)   # handle
px(39,29,METAL); px(39,30,METAL)  # latches
r(43,29,2,2,CASE_D)

# ---- wind streaks (pale, sparse)
WIND="#cfe6f5"
for (x,y) in [(8,12),(6,13),(4,14),(10,20),(7,21),(12,28),(9,29),(14,36),(6,24),(11,8),(5,9)]:
    px(x,y,WIND)
for (x,y) in [(13,15),(11,16),(9,17),(15,24),(13,25)]:
    px(x,y,WIND)

print(c.stats_text())
finish(c)
