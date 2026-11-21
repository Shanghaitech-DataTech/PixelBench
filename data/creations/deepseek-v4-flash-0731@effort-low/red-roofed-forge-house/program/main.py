from pixelbench_api import *

c = new_canvas(128, 128)

def P(*a): return a

BGD=(13,22,17)
G0=(26,44,30)
G1=(38,62,38)
G2=(54,86,48)
G3=(70,106,58)
ROOF=(206,66,46)
ROOFD=(146,44,32)
ROOFL=(234,104,62)
ROOFH=(250,150,92)
TILEL=(176,54,38)
WL=(168,120,80)
WLL=(136,98,62)
WLD=(100,72,46)
DK=(22,22,26)
DOOR=(60,36,28)
FRAME=(158,118,74)
GLOW=(255,166,90)
GLOWY=(255,222,156)
GLOWW=(255,246,224)
WIN=(40,34,30)
WINF=(150,112,70)
CHIM=(122,108,104)
CHIMT=(158,142,136)
SMK=(32,28,30)
post=(112,78,46)
BAR=(172,118,66)
BAND=(112,76,46)
BTOP=(208,152,92)
COAL=(50,46,48)
STON=(96,92,88)

# yard
c.rect(0,0,128,128,BGD)
c.poly([(66,14),(127,68),(66,122),(5,68)], G0)
c.poly([(64,24),(123,70),(64,118),(5,70)], G1)
c.poly([(64,32),(117,76),(64,110),(11,76)], G2)
# building ground shadow
c.poly([(64,62),(22,88),(64,114),(106,88)], (26,38,28))

# ---- walls ----
# front-left wall
c.poly([(64,30),(26,52),(26,88),(64,64)], WL)
# front-right wall
c.poly([(64,30),(102,52),(102,88),(64,64)], WLL)
# dark left edge of front-left wall
c.poly([(26,52),(30,54),(30,88),(26,88)], WLD)
# wall texture
c.line(34,66,62,80, (196,150,104))
c.line(40,78,62,88, (200,160,120))
c.line(66,80,98,90, (120,88,56))

# ---- hipped roof ----
# eaves under-shadow band
c.poly([(64,34),(22,56),(64,78),(106,56)], (24,20,24))
# front-left slope
c.poly([(64,14),(26,52),(64,78)], ROOF)
# front-right slope
c.poly([(64,14),(102,52),(64,78)], ROOFD)
# lit front-left
c.poly([(64,14),(32,52),(64,72)], ROOFL)
# ridge highlight
c.line(64,14,26,52, ROOFH)
c.line(64,14,102,52, ROOFH)
c.poly([(62,20),(66,26),(64,32),(60,26)], ROOFH)
# tile textures
c.line(64,14,30,60, TILEL)
c.line(64,14,40,72, TILEL)
c.line(64,14,92,66, (122,38,28))
# eave lip
c.line(26,52,64,78, (240,128,74))
c.line(102,52,64,78, (178,58,38))

# ---- chimney on front-right slope ----
c.poly([(80,44),(90,49),(90,36),(80,30)], CHIM)
c.poly([(80,30),(90,36),(86,30),(76,24)], CHIMT)
c.rect(82,38,2,4, DK)
c.line(80,22,85,15, SMK)
c.line(86,12,82,6, SMK)
c.poly([(81,19),(85,11),(80,6)], SMK)

# ---- door on front-right wall with furnace glow ----
c.poly([(70,56),(96,48),(96,68),(70,76)], DOOR)
c.poly([(70,56),(96,48),(96,50),(70,58)], FRAME)
c.poly([(73,61),(93,55),(93,59),(73,65)], GLOW)
c.poly([(74,62),(92,57),(92,60),(74,65)], GLOWY)
c.poly([(75,63),(91,59),(91,62),(75,66)], GLOWW)
# coal near furnace
c.poly([(58,76),(64,72),(70,75),(63,82)], COAL)

# ---- window on front-left wall ----
c.poly([(42,58),(58,52),(58,70),(42,76)], WINF)
c.poly([(44,60),(56,55),(56,68),(44,73)], WIN)
c.poly([(44,56),(56,51),(56,54),(44,59)], (220,200,190))

# ---- wooden sign (left) ----
c.rect(12,72,5,24, post)
c.rect(10,68,9,5, post)
c.rect(4,90,17,15, (126,88,48))
c.rect(2,88,21,3, (88,60,34))
c.rect(2,101,21,3, (88,60,34))
c.rect(2,88,3,16, (88,60,34))
c.rect(20,88,3,16, (88,60,34))
c.rect(5,92,15,11, (148,106,60))
c.text(6,94,"FORGE",(54,30,24),font="5x7")
c.circle(15,72,1, (90,62,34))

# ---- stacked barrels (right, on ground) ----
def dbarrel(x,y,w,h):
    c.rect(x,y,w,h, BAR)
    c.poly([(x,y),(x+2,y-3),(x+w-2,y-3),(x+w-1,y)], BTOP)
    c.rect(x,y+1,w,1,(150,100,56))
    c.rect(x,y+2,w,1,BTOP)
    c.rect(x,y+5,w,2,BAND)
    c.rect(x,y+h-5,w,1,BAND)
dbarrel(82,80,16,24)
dbarrel(101,86,16,19)
dbarrel(92,68,16,22)

# scattered stone
c.poly([(56,60),(63,56),(69,59),(62,65)], STON)

# grass tufts
for (tx,ty) in [(22,50),(78,120),(116,60),(58,120),(28,66),(106,100),(18,30),(72,104),(120,44)]:
    c.line(tx,ty,tx-2,ty-4,G3)
    c.line(tx,ty,tx+2,ty-3,G0)
    c.line(tx,ty,tx-4,ty-2,G2)

print(c.stats_text())
save("forge", c)
finish(c)
