from pixelbench_api import *

W = H = 256
c = new_canvas(W, H)

# ---------------- palette ----------------
S1=(26,10,48); S2=(52,14,60); S3=(86,26,72); S4=(122,40,78)
S5=(156,56,80); S6=(196,76,78); S7=(228,104,74); S8=(246,140,78)
S9=(252,176,98); S10=(255,206,130)
SUN_GLOW=(255,150,88); SUN_DISC=(255,240,200); SUN_CORE=(255,255,248)
CLOUD=(58,20,58); CLOUD_RIM=(122,46,70)
MTN_FAR=(64,22,56); MTN_NEAR=(44,16,44)
G_DARK=(30,20,26); G_FRONT=(40,28,32); G_LIT=(120,52,44); G_PATH=(22,14,20)
STONE=(66,60,76); STONE_HI=(88,82,100); OUT=(14,10,20)
WIN_D=(34,26,34); WIN_G=(255,164,72)
F1=(255,92,32); F2=(255,150,54); F3=(255,214,110); F4=(255,252,196)
SM1=(58,56,66); SM2=(88,84,94); SM3=(124,118,128); SM4=(158,150,158)
DB=(30,22,34); DW=(48,34,50); DR=(20,14,26); DBELLY=(74,54,64); DH=(64,50,66); DEYE=(255,80,40)
K_D=(24,18,28); K_H=(148,146,158); K_S=(106,100,108)
SH_R=(150,54,48); SH_B=(60,74,120); SH_G=(188,152,84)
W1=(74,52,38); W2=(42,28,26); W3=(100,70,48); WHEEL=(34,22,26)
AR=(30,22,30); ART=(208,178,140)
EM1=(255,140,58); EM2=(255,216,128); EM3=(255,96,40)
BN_R=(168,46,42); BN_G=(200,164,96)

# ---------------- sky ----------------
bands = [(0,22,S1),(22,48,S2),(48,74,S3),(74,98,S4),(98,120,S5),
         (120,142,S6),(142,158,S7),(158,172,S8),(172,184,S9),(184,190,S10)]
for y0,y1,col in bands:
    c.rect(0,y0,W,y1-y0,col)

# sun
c.circle(72,160,30,SUN_GLOW)
c.circle(72,160,17,SUN_DISC)
c.circle(72,160,9,SUN_CORE)

# clouds
clouds = [(30,52,26,8),(74,66,34,9),(110,44,40,10),(168,56,30,8),(210,38,24,7),
          (52,96,28,7),(130,84,34,8),(236,66,18,6),(30,110,22,6),(156,104,30,7),
          (96,24,22,6),(196,14,26,6),(60,130,26,6),(120,118,22,5)]
for (cx,cy,rx,ry) in clouds:
    c.ellipse(cx,cy,rx,ry,CLOUD)
for (cx,cy,rx,ry) in clouds:
    c.ellipse(cx,cy-2,max(1,rx-4),3,CLOUD_RIM)

# mountains
far = [(0,186),(10,152),(22,158),(36,144),(50,152),(66,142),(84,150),(100,144),
       (118,152),(136,146),(154,154),(172,148),(190,156),(208,150),(226,156),
       (244,150),(256,154),(256,186)]
c.poly(far, MTN_FAR)
near = [(0,186),(16,162),(34,168),(52,160),(70,168),(90,162),(108,170),(128,164),
        (148,172),(168,166),(188,174),(208,168),(228,174),(248,170),(256,174),(256,186)]
c.poly(near, MTN_NEAR)

# ---------------- ground ----------------
c.rect(0,186,W,70,G_DARK)
c.rect(0,214,W,42,G_FRONT)
c.poly([(0,236),(130,214),(150,222),(60,246),(0,248)], G_PATH)
c.rect(140,186,116,10,G_LIT)

# ---------------- siege tower ----------------
c.rect(38,126,48,68,OUT)
c.rect(40,128,44,64,W1)
# frame
for px in (42,56,70,80):
    c.line(px,128,px,190,W2)
c.line(42,142,80,168,W2); c.line(80,142,42,168,W2)
c.line(42,176,80,188,W2); c.line(80,176,42,188,W2)
c.rect(40,128,44,8,W3)
c.circle(48,190,5,WHEEL); c.circle(78,190,5,WHEEL)
c.rect(36,128,48,4,OUT)
k_siege_x = [46, 62, 76]
for sx in k_siege_x:
    knight_y = 128
    c.set(sx, knight_y-1, K_D); c.set(sx+1, knight_y-1, K_D)
    c.set(sx, knight_y-2, K_D); c.set(sx+1, knight_y-2, K_D)
    c.set(sx, knight_y-3, K_D); c.set(sx+1, knight_y-3, K_D)
    c.set(sx, knight_y-4, K_H); c.set(sx+1, knight_y-4, K_H)
    c.rect(sx+2, knight_y-4, 2, 3, SH_R)

# ---------------- castle ----------------
def crenellate(x0, x1, top, tooth=6, gap=4, height=6, stone=STONE):
    x = x0
    while x < x1:
        w = min(tooth, x1-x)
        c.rect(x, top-height, w, height, OUT)
        c.rect(x, top-height, w, height-2, stone)
        x += tooth + gap

# keep
c.rect(150,100,94,90,OUT)
c.rect(152,102,90,86,STONE)
crenellate(152,244,100)
# left tower
c.rect(154,62,30,38,OUT)
c.rect(156,64,26,36,STONE)
crenellate(156,184,64)
# central tower
c.rect(182,48,20,52,OUT)
c.rect(184,50,16,50,STONE)
crenellate(184,202,50, tooth=5, gap=3)
# right tower
c.rect(204,70,34,30,OUT)
c.rect(206,72,30,28,STONE)
crenellate(206,238,72)
# west wall
c.rect(108,150,42,40,OUT)
c.rect(110,152,38,38,STONE)
crenellate(110,150,152)
# gate
c.rect(184,158,22,32,OUT)
c.rect(186,160,18,30,WIN_D)
c.rect(190,172,10,18,OUT)
# windows
for (wx,wy) in [(156,128),(156,162),(224,128),(224,162),(162,76),(206,84)]:
    c.rect(wx,wy,4,7,WIN_D)
c.rect(wx,wy,2,4,WIN_G)
crenellate(152,244,100)
# stone highlights
c.rect(152,102,90,2,STONE_HI)
c.rect(156,64,26,2,STONE_HI)

# banners
c.line(170,64,170,38,W2)
c.poly([(170,38),(196,42),(170,48)], BN_R)
c.set(196,42,BN_G)
c.line(192,50,192,28,W2)
c.poly([(192,28),(212,32),(192,38)], BN_R)

# flames on castle
def flame(cx, cy, sc):
    c.circle(cx,cy,int(6*sc),F1); c.circle(cx,cy-2,int(4*sc),F2)
    c.circle(cx,cy-4,int(3*sc),F3); c.set(cx,cy-6,F4)
flame(192,44,1.4); flame(178,56,1.1); flame(202,58,1.1); flame(166,72,0.9)
flame(220,88,1.0); flame(236,80,0.9); flame(158,94,0.9); flame(212,94,0.9)
flame(190,66,1.0); flame(178,88,0.8); flame(238,90,0.7); flame(154,96,0.7)
# fire glow into windows
for (wx,wy) in [(158,160),(164,160),(222,160),(230,160)]:
    c.rect(wx,wy,2,3,F2)

# ---------------- knights on ramparts ----------------
def knight(x, y, facing=1, shield=SH_R, spear_up=True, spear_h=9):
    c.set(x, y-1, K_D); c.set(x+1, y-1, K_D)
    c.set(x, y-2, K_D); c.set(x+1, y-2, K_D)
    c.set(x, y-3, K_D); c.set(x+1, y-3, K_D)
    if facing == 1:
        c.rect(x+2, y-4, 2, 3, shield)
    else:
        c.rect(x-1, y-4, 2, 3, shield)
    c.set(x, y-4, K_H); c.set(x+1, y-4, K_H)
    if spear_up:
        c.line(x+1, y-4, x+1, y-4-spear_h, K_S)

for x in range(112, 146, 7):
    knight(x, 150, facing=-1, shield=SH_B)
    knight(x+3, 150, facing=-1, shield=SH_R)
for x in range(158, 240, 8):
    knight(x, 100, facing=-1, shield=SH_G, spear_up=False)
    knight(x+4, 100, facing=-1, shield=SH_B)
knight(160, 62, facing=-1, shield=SH_R)
knight(170, 64, facing=-1, shield=SH_B)
knight(210, 72, facing=-1, shield=SH_G)
knight(222, 72, facing=-1, shield=SH_R)
knight(188, 50, facing=1, shield=SH_B)
knight(196, 50, facing=1, shield=SH_R)

# ---------------- smoke ----------------
smoke_puffs = [(152,30,11),(172,24,12),(196,18,13),(224,24,11),(186,8,12),
              (212,4,10),(160,40,9),(204,36,8),(238,12,8),(168,2,7)]
for (sx,sy,sr) in smoke_puffs:
    c.circle(sx,sy,sr,SM1)
for (sx,sy,sr) in smoke_puffs:
    c.circle(sx,sy-2,max(1,sr-3),SM2)
for (sx,sy,sr) in smoke_puffs:
    c.circle(sx,sy-4,max(1,sr-6),SM3)
c.circle(150,10,6,SM4)
c.circle(204,0,6,SM3)

# ---------------- soldiers in formation ----------------
def soldier(x, y, shield):
    c.set(x, y-1, K_D); c.set(x+1, y-1, K_D)
    c.set(x, y-2, K_D); c.set(x+1, y-2, K_D)
    c.set(x, y-3, K_D); c.set(x+1, y-3, K_D)
    c.set(x, y-4, K_D)
    c.set(x, y-5, K_H)
    c.rect(x+2, y-4, 2, 3, shield)
    c.line(x+2, y-4, x+2, y-10, K_S)

for y,sh in [(200,SH_R),(212,SH_B),(224,SH_G),(236,SH_R)]:
    for x in range(6, 100, 6):
        soldier(x, y, sh)

# ---------------- dragon ----------------
# wings (behind body)
c.poly([(98,34),(146,4),(162,14),(152,32),(108,42)], DW)
c.poly([(70,42),(36,8),(20,16),(12,30),(28,44),(58,50)], DW)
c.poly([(98,34),(146,4),(162,14),(152,32),(108,42)], DR, fill=False)
c.poly([(70,42),(36,8),(20,16),(12,30),(28,44),(58,50)], DR, fill=False)
c.line(70,42,30,12,DR); c.line(70,42,18,26,DR); c.line(70,42,44,32,DR)
c.line(98,34,120,20,DR); c.line(98,34,146,26,DR)
# body
bodypts = [(16,64,8),(30,58,8),(46,51,8),(62,45,8),(78,40,7),(92,35,6),(106,30,5)]
for (bx,by,br) in bodypts:
    c.circle(bx,by,br,DB)
for (bx,by,br) in [(30,60,4),(46,53,4),(62,47,4),(78,42,3),(92,37,2),(106,32,2)]:
    c.circle(bx,by,br,DBELLY)
c.circle(3,68,2,DB); c.circle(10,66,3,DB)
# head
c.poly([(116,26),(136,12),(146,14),(142,22),(126,28)], DB)
c.poly([(126,28),(144,28),(136,31)], DB)
c.poly([(116,26),(136,12),(146,14),(142,22),(126,28)], DR, fill=False)
c.poly([(128,14),(124,5),(135,10)], DH)
c.poly([(140,10),(142,3),(146,9)], DH)
c.set(135,16,DEYE)
# fire breath
c.circle(148,18,4,F1); c.circle(152,22,4,F2); c.circle(156,28,4,F3); c.circle(160,34,5,F1); c.set(156,30,F4)

# ---------------- arrows ----------------
arrows = [(20,118),(34,104),(48,90),(40,128),(62,80),(76,66),(88,96),(100,110),
          (56,132),(108,74),(124,58),(140,64),(30,140),(70,140),(92,120),
          (118,88),(84,120),(60,100)]
for (ax,ay) in arrows:
    c.line(ax,ay,ax+12,ay-7,AR)
    c.line(ax+10,ay-7,ax+14,ay-8,ART)
for (ax,ay) in [(162,124),(176,118),(152,132)]:
    c.line(ax,ay,ax-11,ay+5,AR)
    c.line(ax-9,ay+5,ax-13,ay+6,ART)

# ---------------- embers ----------------
embers = [(168,52),(184,40),(202,34),(224,44),(238,30),(176,24),(210,16),(240,8),
          (156,66),(190,54),(214,60),(230,52),(148,80),(200,70),(162,36),(196,26),
          (120,60),(134,52),(128,70),(146,44),(228,20),(180,12),(210,0),(152,120),
          (170,110),(192,120),(218,108),(238,100),(146,96),(186,84),(226,88),(180,150),
          (150,132),(196,140),(234,128),(120,86),(110,98),(100,60),(88,72),(78,90)]
for i,(ex,ey) in enumerate(embers):
    if i % 3 == 0:
        c.set(ex,ey,EM1)
    elif i % 3 == 1:
        c.set(ex,ey,EM2)
    else:
        c.set(ex,ey,EM3)

# ---------------- finish ----------------
print(c.stats_text())
print("palette size:", len(c.palette()))
finish(c)
