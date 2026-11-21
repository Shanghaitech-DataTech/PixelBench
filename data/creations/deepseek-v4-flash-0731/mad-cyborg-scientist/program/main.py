import math
from pixelbench_api import new_canvas, finish, input_canvas

c = new_canvas(64, 64, background="#0a0c14", name="mad_cyborg_scientist")
C = c.color

BG=C("#0a0c14"); BGG=C("#131834"); BGD=C("#04050a")
SKL=C("#f6cba2"); SK=C("#e2a06c"); SKS=C("#bd7544"); SKD=C("#7c4a28")
ML=C("#e0e0ec"); M=C("#a8aaba"); MD=C("#6e7082"); MK=C("#3e404c"); SEAM=C("#16171f")
HW=C("#f2f2f6"); HG=C("#c6c6d2"); HD=C("#8e8e9c")
SCL=C("#f4f4e8"); IRIS=C("#3e5a4a"); BLK=C("#101016")
GL=C("#00f2ff"); GM=C("#00b4cc"); GH=C("#005a74"); GHL=C("#d6ffff")
COAT=C("#d8d4ca"); CSH=C("#a29e94"); COATD=C("#6e6a62")
STAIN=C("#9c7a4c"); STAIN2=C("#7c4a36"); STAIN3=C("#50685a")
APR=C("#8a5c32"); APRD=C("#5c3a1e"); LTH=C("#33220f")
BELT=C("#4a3016"); BUCK=C("#c8a850")
CAB=C("#26262e"); YEL=C("#e8b820"); RED=C("#c83a2a"); BLU=C("#3a6ac8")
MTH=C("#3f0c10"); TOOTH=C("#ececdd")

# ---------------- background ----------------
c.rect(0,0,64,64,BG)
c.circle(30,26,20,BGG)
c.rect(0,0,64,1,BGD); c.rect(0,63,64,1,BGD)
c.rect(0,0,1,64,BGD); c.rect(63,0,1,64,BGD)

# ---------------- torso coat ----------------
c.poly([(7,45),(14,42),(52,42),(58,45),(59,62),(5,62),(5,48)],COAT)
c.rect(6,45,3,17,CSH)
c.rect(55,45,3,17,CSH)
c.rect(10,52,3,2,STAIN); c.rect(13,55,2,3,STAIN2); c.rect(52,50,2,2,STAIN); c.rect(54,53,2,3,STAIN3)

# ---------------- ears ----------------
c.rect(15,22,3,8,SK)
c.rect(47,22,3,7,MD)
c.rect(48,23,1,4,MK)
c.rect(15,24,1,5,SKS)

# ---------------- neck ----------------
c.rect(27,40,6,7,SKS)
c.rect(33,40,6,7,MD)
c.line(38,41,38,46,MK)
c.rect(33,42,6,1,MK)
c.rect(33,44,6,1,MK)

# ---------------- head base ----------------
c.ellipse(32,25,15,17,SK)
pts=[]
for y in range(8,43):
    t=(y-25)/17
    x=32+15*math.sqrt(max(0.0,1.0-t*t))
    pts.append((round(x),y))
c.poly([(32,8)]+pts+[(32,42)],MD)
pts2=[]
for y in range(9,42):
    t=(y-25)/17
    x=32-15*math.sqrt(max(0.0,1.0-t*t))
    pts2.append((round(x),y))
c.poly([(32,9)]+pts2+[(32,41)],SKL)
pts3=[]
for y in range(9,42):
    t=(y-25)/17
    x=32-11*math.sqrt(max(0.0,1.0-t*t))
    pts3.append((round(x),y))
c.poly([(32,9)]+pts3+[(32,41)],SK)
pts4=[]
for y in range(9,42):
    t=(y-25)/17
    x=32+11*math.sqrt(max(0.0,1.0-t*t))
    pts4.append((round(x),y))
c.poly([(32,9)]+pts4+[(32,41)],M)

# ---------------- hair ----------------
for (hx,hy,hr,hcol) in [(20,13,5,HW),(28,10,5,HW),(36,10,5,HW),(43,13,5,HW),(46,18,4,HG),(16,20,4,HG),(24,15,3,HW)]:
    c.circle(hx,hy,hr,hcol)
for (sp,col) in [([(18,10),(13,2),(24,7)],HW),([(27,7),(24,1),(32,6)],HW),([(35,7),(33,1),(40,7)],HG),([(42,9),(44,3),(47,8)],HG),([(46,13),(52,6),(48,15)],HW)]:
    c.poly(sp,col)
for (a,b) in [(14,14),(15,18),(46,15),(45,20),(20,9),(38,8)]:
    c.set(a,b,HG)
c.set(44,10,HW)
# stray strand over forehead
c.set(30,15,HG); c.set(32,14,HG); c.set(34,15,HG)

# ---------------- plugs & wires ----------------
c.line(28,9,28,2,BLU); c.line(34,7,34,1,RED); c.line(40,10,40,3,YEL); c.line(40,14,47,4,YEL)
for px,py in [(27,12),(33,10),(39,13)]:
    c.circle(px,py,2,MK)
for px,py in [(28,11),(34,9),(40,12)]:
    c.set(px,py,MD)

# ---------------- face seam ----------------
c.line(31,10,31,41,SEAM)
c.set(31,14,YEL); c.set(31,18,RED); c.set(31,37,GH)

# ---------------- brows ----------------
c.rect(18,19,8,2,SKS)
c.rect(24,20,3,1,SKS)
c.rect(35,19,5,2,MK)
c.rect(35,19,4,1,ML)

# ---------------- left eye ----------------
c.rect(21,22,7,3,SCL)
c.circle(25,23,1,IRIS)
c.set(25,23,BLK)
c.set(24,22,GHL)
c.line(22,25,27,25,SKS)
c.line(21,26,28,26,SKS)

# ---------------- right eye ----------------
c.circle(39,23,4,MK)
c.circle(39,23,3,MD)
c.circle(39,23,2,GH)
c.circle(39,23,1,GM)
c.set(39,23,GL)
c.set(38,22,GHL)
c.set(43,21,GH); c.set(44,23,GH); c.set(42,26,GH); c.set(37,25,GH)

# ---------------- panel lines ----------------
for yy in (29,33,37):
    c.line(33,yy,45,yy,MK)
c.circle(44,20,1,MK); c.circle(45,28,1,MK); c.circle(44,34,1,MK)
c.line(33,38,43,38,ML)

# ---------------- nose ----------------
for (nx,ny) in [(28,25),(29,26),(29,27),(30,28),(29,29),(28,29)]:
    c.set(nx,ny,SKS)
c.set(30,30,SKD); c.set(29,30,SKD)
c.set(26,27,SKL); c.set(25,28,SKL)
c.set(31,29,SKS)

# ---------------- mouth ----------------
c.poly([(19,35),(21,32),(29,30),(37,31),(43,33),(44,35),(42,38),(34,39),(25,38),(21,37)],MTH)
c.rect(20,33,23,2,TOOTH)
for x in range(23,42,3):
    c.set(x,33,MTH)
for x in range(25,40,3):
    c.set(x,34,MTH)
c.rect(22,38,15,1,TOOTH)
for x in range(25,37,3):
    c.set(x,38,MTH)
c.set(20,34,TOOTH)
c.set(20,35,TOOTH)
c.line(25,40,35,40,SKS)
c.line(36,40,41,40,MK)
c.set(24,41,SKD)
c.set(37,39,GL)
c.line(33,41,40,41,MD)

# ---------------- collar / apron ----------------
c.line(15,42,18,46,CSH)
c.line(49,42,46,46,CSH)
c.line(20,43,19,46,LTH)
c.line(44,43,45,46,LTH)
c.poly([(19,46),(45,46),(47,60),(17,60)],APR)
c.rect(42,46,3,14,APRD)
c.rect(19,46,20,3,APRD)
c.rect(19,49,3,11,APRD)
# pocket
c.rect(31,51,9,6,APRD)
c.line(31,53,39,53,BELT)
c.rect(33,54,5,1,BELT)
c.set(23,54,STAIN2); c.set(28,57,STAIN); c.set(36,56,STAIN3)

# ---------------- belt ----------------
c.rect(10,58,40,4,BELT)
c.rect(30,58,6,4,BUCK)
c.rect(31,59,4,1,BELT)
c.rect(12,57,6,4,APRD)
c.line(12,58,17,58,BELT)
c.rect(44,57,5,3,APRD)

# ---------------- coat buttons / lapel details ----------------
c.set(12,49,COATD); c.set(12,53,COATD)
c.set(50,49,COATD)
c.set(14,48,COATD)

# ---------------- robotic arm ----------------
c.circle(51,46,2,M)
c.rect(48,45,6,8,M)
c.rect(51,47,2,5,MD)
c.rect(48,47,6,1,MK)
c.rect(48,50,6,1,MK)
c.circle(52,53,3,MD)
c.rect(49,54,9,5,MD)
c.rect(50,54,4,2,ML)
c.rect(51,56,7,1,CAB)
for x in (52,54,56):
    c.set(x,56,YEL)
c.rect(54,57,4,3,MD)
c.rect(55,57,3,1,ML)
c.rect(54,60,2,2,MD)
c.rect(56,60,2,2,MK)
c.rect(58,59,1,2,MK)
c.rect(59,58,1,1,MD)
c.line(56,60,56,62,CAB)
c.set(57,61,YEL); c.set(58,62,CAB)
c.line(41,42,49,47,CAB)
c.set(43,44,YEL); c.set(46,45,YEL)
c.set(50,57,GH)
# neck port glow
c.set(43,41,GH); c.set(41,43,GL)
c.set(32,39,GL)
print("probes", c.get(25,38), c.get(30,38), c.color_name(c.get(25,38)))

# ---------------- finish ----------------
print(c.stats_text())
print("LEGEND-EYES")
print(c.matrix_text(region=(16,18,47,30)))
print("LEGEND-MOUTH")
print(c.matrix_text(region=(15,27,47,42)))
print("LEGEND-TORSO")
print(c.matrix_text(region=(4,42,62,63)))
finish(c)
