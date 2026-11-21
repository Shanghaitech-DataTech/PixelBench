# ancient-dragon-battle : 256x256 epic fantasy battlefield (v2)
W = H = 256
c = new_canvas(W, H, name="battle")

# ---------------- palette ----------------
INK      = '#150d18'
SKY = ['#1d1033','#2a1542','#3a1c4c','#4e234d','#662b49','#7f3442',
       '#984136','#b4522f','#cd672c','#e38231','#f09c42','#fbb657',
       '#ffcd74','#ffe292']
SUN_HI   = '#fff3c8'
SUN_CORE = '#fffbe8'
MTN_FAR  = '#5c3560'
MTN_RIM  = '#cf6b45'
MTN_NEAR = '#3f2547'
GND_MID  = '#2e1c2c'
GND_DARK = '#1a101f'
ROCK     = '#3a2a33'
SMOKE_D  = '#2e2033'
SMOKE_M  = '#453053'
SMOKE_L  = '#5d4363'
FIRE_OUT = '#f4521a'
FIRE_MID = '#ff9431'
FIRE_HI  = '#ffc23e'
FIRE_CORE= '#fff0a0'
CASTLE   = '#503038'
CASTLE_D = '#331f2b'
RIM      = '#e08a3f'
WINDOW   = '#ffb347'
DRG_BODY = '#2e1b30'
DRG_BELLY= '#6b3040'
DRG_MEM  = '#a63a2a'
DRG_MEM_D= '#7e2c24'
DRG_MEM_H= '#e06430'
DRG_HORN = '#ffd08a'
DRG_EYE  = '#ffe066'
WOOD_D   = '#3e2a1c'
WOOD     = '#5c3f24'
WOOD_RIM = '#a86a3a'
ARMOR    = '#7d8794'
ARMOR_D  = '#3c4350'
SHIELD_C = '#7a2b2b'
SPEAR    = '#4a3220'
SOLDIER  = '#221826'
PLUME    = '#b03a2a'
FG_BODY  = '#1e1322'

# ---------------- sky ----------------
ys = [0,14,28,42,56,70,84,96,108,120,132,144,156,166,178]
for i in range(len(SKY)):
    y0 = ys[i]; y1 = ys[i+1] if i+1 < len(ys) else 178
    c.rect(0, y0, W, y1-y0+1, SKY[i])
for i in range(1, len(ys)):
    c.dither(0, ys[i]-1, W, 3, [SKY[i-1], SKY[min(i,len(SKY)-1)]], pattern="bayer4")

# ---------------- sun ----------------
c.circle(150,148,26, SKY[11])
c.circle(150,148,21, SKY[12])
c.circle(150,148,16, SKY[13])
c.circle(150,148,10, SUN_HI)
c.circle(150,148, 5, SUN_CORE)

for bx,by in [(120,90),(188,74),(96,70)]:
    c.line(bx-3,by,bx,by-2,INK); c.line(bx,by-2,bx+3,by,INK)

# ---------------- mountains ----------------
far_top = [(0,168),(20,152),(38,160),(60,144),(82,158),(105,148),(128,158),
           (150,150),(172,160),(196,146),(220,158),(240,150),(255,160)]
c.poly(far_top + [(255,255),(0,255)], MTN_FAR)
for i in range(len(far_top)-1):
    (x0,y0),(x1,y1) = far_top[i], far_top[i+1]
    c.line(x0,y0,x1,y1,MTN_RIM)
near_top = [(0,178),(30,166),(55,174),(85,162),(115,172),(140,164),(170,174),
            (200,164),(228,172),(255,166)]
c.poly(near_top + [(255,255),(0,255)], MTN_NEAR)

# ---------------- ground ----------------
c.rect(0,178,W,78,GND_MID)
c.rect(0,224,W,32,GND_DARK)
c.dither(0,222,W,4,[GND_MID,GND_DARK],pattern="bayer4")
c.dither(0,178,W,4,[MTN_NEAR,GND_MID],pattern="bayer4")
for rx,ry,rr in [(30,240,5),(70,246,4),(150,244,5),(168,238,3),(96,242,4),(250,244,5)]:
    c.circle(rx,ry,rr,ROCK)
    c.rect(rx-rr,ry,2*rr+1,rr+1,GND_DARK)

# ---------------- helpers ----------------
def orect(x,y,w,h,col):
    c.rect(x-1,y-1,w+2,h+2,INK)
    c.rect(x,y,w,h,col)

def flame(cx,by,h,w,lean=3):
    c.poly([(cx-w,by),(cx-w,by-h*2//5),(cx-w//2,by-3*h//5),(cx-w//4+lean,by-h),
            (cx+lean,by-h+2),(cx+w//3+lean,by-2*h//5),(cx+w,by-h//5),(cx+w,by)],FIRE_OUT)
    c.poly([(cx-w+2,by),(cx-w+2,by-h//3),(cx-1+lean,by-2*h//3),
            (cx+w//4+lean,by-h//3),(cx+w-2,by-h//6),(cx+w-2,by)],FIRE_MID)
    c.poly([(cx-2,by),(cx-1+lean//2,by-h//3),(cx+2,by-h//8),(cx+2,by)],FIRE_HI)
    c.set(cx,by-1,FIRE_CORE); c.set(cx+1,by-2,FIRE_CORE)

def crenels(x0,x1,y,col):
    x = x0
    while x <= x1-3:
        orect(x,y,4,5,col)
        x += 7

# ---------------- castle ----------------
orect(26,100,22,76,CASTLE)          # left tower
crenels(24,50,94,CASTLE)
orect(46,118,46,58,CASTLE)          # keep
crenels(44,94,112,CASTLE)
orect(92,88,26,88,CASTLE)           # tall tower
crenels(90,120,82,CASTLE)
c.rect(26,100,4,76,CASTLE_D); c.rect(46,118,4,58,CASTLE_D); c.rect(92,88,4,88,CASTLE_D)
c.rect(46,101,2,75,RIM); c.rect(90,119,2,57,RIM); c.rect(116,89,2,87,RIM)
c.rect(62,156,12,20,INK); c.rect(64,158,8,18,'#0d0710')
for wx,wy in [(32,120),(40,140),(34,158),(56,130),(76,140),(60,148),(98,110),(108,128),(100,150),(108,160)]:
    c.rect(wx,wy,3,4,WINDOW)
orect(118,150,56,26,CASTLE)         # wall to the right
crenels(118,174,144,CASTLE)
c.rect(172,151,2,25,RIM)

# castle fires
flame(37,96,26,9,lean=2)
flame(66,114,18,7,lean=2)
flame(105,84,22,8,lean=2)
flame(140,146,12,5,lean=2)

# ---------------- smoke (drifting up-LEFT, away from dragon) ----------------
for sx,sy,sr,sc in [(34,82,6,SMOKE_M),(40,72,7,SMOKE_D),(48,62,8,SMOKE_M),
                    (58,53,9,SMOKE_D),(70,45,10,SMOKE_M),(84,39,9,SMOKE_D),
                    (96,34,8,SMOKE_M),(94,68,5,SMOKE_D),(88,58,6,SMOKE_M)]:
    c.circle(sx,sy,sr,sc)
c.dither(28,88,16,3,[FIRE_MID,SMOKE_D],pattern="bayer4")
c.dither(96,72,12,3,[FIRE_MID,SMOKE_D],pattern="bayer4")
for lx,ly in [(36,77),(52,57),(66,49),(88,42)]:
    c.set(lx,ly,SMOKE_L); c.set(lx+1,ly,SMOKE_L)

# ---------------- siege towers ----------------
def siege(x0,y0,w,h):
    c.poly([(x0-1,y0-1),(x0+w,y0-1),(x0+w+3,y0+h),(x0-4,y0+h)],INK)
    c.poly([(x0,y0),(x0+w-1,y0),(x0+w+2,y0+h),(x0-3,y0+h)],WOOD_D)
    for yy in range(y0+8,y0+h-4,7):
        c.line(x0-2,yy,x0+w+1,yy,WOOD)
    c.line(x0,y0,x0-3,y0+h,WOOD_RIM)
    crenels(x0-2,x0+w+2,y0-6,WOOD_D)
    c.circle(x0+3,y0+h-1,4,INK); c.circle(x0+w-4,y0+h-1,4,INK)
    c.set(x0+3,y0+h-1,WOOD); c.set(x0+w-4,y0+h-1,WOOD)

siege(198,120,24,58)
siege(236,138,18,40)
for ax,ay in [(204,116),(212,116),(240,134)]:
    c.rect(ax,ay,2,4,SOLDIER); c.set(ax,ay-1,ARMOR_D)

# ---------------- soldiers in formation ----------------
for row,(ry,x0,x1) in enumerate([(180,118,196),(186,112,200),(192,122,190)]):
    for sx in range(x0 + (row%2)*3, x1, 6):
        c.rect(sx,ry-3,2,3,SOLDIER)
        c.set(sx,ry-4,ARMOR_D)
        c.line(sx+2,ry-1,sx+4,ry-7,SPEAR)
        c.set(sx+4,ry-8,INK)

# ---------------- knights on the ramparts ----------------
def wall_knight(x,y):
    c.set(x,y-1,INK); c.set(x+2,y-1,INK)
    c.rect(x-1,y-5,4,4,ARMOR_D)
    c.rect(x-1,y-8,4,3,ARMOR)
    c.set(x+2,y-7,RIM)
    c.line(x+4,y-1,x+4,y-12,SPEAR)
    c.set(x+4,y-13,ARMOR)
    c.rect(x-4,y-6,3,5,SHIELD_C)
    c.set(x-3,y-4,INK)
wall_knight(126,150); wall_knight(142,150); wall_knight(160,150)
wall_knight(50,112); wall_knight(84,112)

# ---------------- dragon ----------------
# far wing (behind, sweeping up-left over the smoke gap)
c.path("M168,60 L150,36 L130,24 Q136,40 138,46 Q146,52 152,58 Q160,62 168,64 Z",INK)
c.path("M166,59 L150,39 L135,29 Q140,41 142,46 Q149,52 155,57 Q161,60 166,61 Z",DRG_MEM_D)
c.line(166,60,135,29,INK); c.line(166,60,142,46,INK); c.line(166,60,155,57,INK)

# tail curl (down-right, curls up at the tip) - interpolated chain
tpts = [(192,74),(204,84),(214,96),(220,108),(216,120),(204,126),(192,122)]
trad = [5,5,4,4,3,2,2]
for si in range(len(tpts)-1):
    (ax,ay),(bx2,by2) = tpts[si], tpts[si+1]
    steps = max(1, int(((bx2-ax)**2+(by2-ay)**2)**0.5 / 3))
    for k in range(steps+1):
        t = k/steps
        tx = round(ax+(bx2-ax)*t); ty = round(ay+(by2-ay)*t)
        tr = max(2, round(trad[si]+(trad[si+1]-trad[si])*t))
        c.circle(tx,ty,tr+1,INK)
for si in range(len(tpts)-1):
    (ax,ay),(bx2,by2) = tpts[si], tpts[si+1]
    steps = max(1, int(((bx2-ax)**2+(by2-ay)**2)**0.5 / 3))
    for k in range(steps+1):
        t = k/steps
        tx = round(ax+(bx2-ax)*t); ty = round(ay+(by2-ay)*t)
        tr = max(2, round(trad[si]+(trad[si+1]-trad[si])*t))
        c.circle(tx,ty,tr,DRG_BODY)
c.poly([(192,122),(184,118),(190,128)],INK)               # tail spade

# neck + body (tapering, arched) - polygon with smooth tapered underside
c.poly([(132,49),(146,51),(158,53),(170,56),(180,61),(194,68),
        (199,73),(197,82),(186,78),(174,74),(162,71),(150,66),(138,61),(131,56)],INK)
c.poly([(134,51),(146,53),(158,55),(169,58),(179,63),(192,69),
        (196,73),(194,79),(186,75),(174,71),(163,68),(151,63),(139,58),(133,54)],DRG_BODY)
# belly plates (contained)
c.poly([(136,57),(148,61),(160,65),(172,69),(184,73),(192,77),
        (194,79),(186,75),(174,71),(163,68),(151,63),(139,58)],DRG_BELLY)
# fire rim along the underside
c.line(138,62,168,72,DRG_MEM_H); c.line(170,74,192,82,DRG_MEM_H)

# fire breath (behind the head, onto the tall tower)
c.poly([(104,52),(112,56),(116,88),(96,86),(98,62)],FIRE_OUT)
c.poly([(106,55),(110,58),(111,84),(100,83),(102,64)],FIRE_MID)
c.poly([(106,58),(108,61),(106,76),(102,75),(104,66)],FIRE_HI)
c.set(104,70,FIRE_CORE); c.set(105,80,FIRE_CORE); c.set(108,86,FIRE_CORE)

# tucked legs (clear of the tail curl)
c.poly([(168,76),(174,78),(170,86),(166,84)],INK)
c.set(171,87,INK); c.set(167,87,INK)
c.poly([(180,80),(186,82),(184,91),(179,89)],INK)
c.set(185,92,INK); c.set(181,92,INK)

# head (drawn over the flame so the silhouette reads)
c.poly([(122,44),(134,42),(141,48),(138,56),(127,58),(119,54)],INK)
c.poly([(124,46),(133,44),(138,49),(136,54),(128,55),(122,52)],DRG_BODY)
c.poly([(122,46),(104,40),(100,44),(120,50)],INK)          # upper jaw
c.poly([(120,47),(106,42),(103,45),(119,49)],DRG_BODY)
c.poly([(120,54),(108,60),(112,63),(124,58)],INK)          # lower jaw
c.poly([(120,55),(111,60),(114,61),(123,57)],DRG_BELLY)
c.set(112,53,FIRE_HI); c.set(114,54,FIRE_CORE); c.set(116,56,FIRE_HI)
c.line(134,44,144,38,DRG_HORN); c.line(136,48,147,44,DRG_HORN)
c.line(142,48,148,41,INK); c.line(152,51,159,44,INK); c.line(162,54,170,48,INK)
c.set(128,48,DRG_EYE); c.set(129,48,DRG_EYE); c.set(129,49,DRG_EYE)
c.set(102,43,INK)                                          # nostril
c.line(124,47,130,46,INK)                                  # brow
c.poly([(121,53),(128,57),(135,55),(128,50)],INK)          # throat connector
c.poly([(123,53),(128,55),(132,54),(128,51)],DRG_BODY)
# visible breath stream from the mouth to the blaze
c.line(108,55,102,87,FIRE_OUT); c.line(109,55,103,87,FIRE_OUT)
c.line(109,56,104,86,FIRE_HI)

# near wing (big, up-right)
c.path("M170,62 L186,30 L206,16 L228,8 Q218,26 214,38 Q210,50 202,58 "
       "Q196,66 188,72 Q180,78 172,78 Q166,72 162,66 Z",INK)
c.path("M173,61 L188,34 L206,22 L222,15 Q214,29 211,39 Q207,49 200,56 "
       "Q194,63 187,68 Q180,73 174,73 Q169,69 165,64 Z",DRG_MEM)
c.path("M175,58 L189,36 L205,26 L217,21 Q209,33 206,42 Q202,50 196,55 "
       "Q189,61 182,63 Q176,62 171,60 Z",DRG_MEM_H)
for fx,fy in [(228,8),(214,38),(202,58),(188,72),(172,78)]:
    c.line(170,63,fx,fy,INK)
c.line(170,62,186,30,INK); c.line(186,30,206,16,INK); c.line(206,16,228,8,INK)
c.set(186,29,DRG_HORN); c.set(185,30,DRG_HORN)             # wing claw

# flame tongue escaping the jaws + impact blaze on the tower top
flame(112,62,6,3,lean=3)
flame(104,92,16,7,lean=2)

# ---------------- foreground knight ----------------
c.ellipse(204,250,30,5,'#100a14')
c.poly([(190,230),(201,230),(199,252),(191,252)],INK)      # legs
c.poly([(209,230),(220,230),(223,252),(215,252)],INK)
c.poly([(186,204),(222,204),(226,234),(184,234)],INK)      # torso
c.poly([(189,207),(219,207),(222,232),(187,232)],FG_BODY)
c.poly([(188,208),(180,220),(186,224),(194,214)],INK)      # shield arm
c.poly([(218,206),(228,214),(224,220),(214,212)],INK)      # spear arm
# heater shield
c.poly([(172,206),(192,204),(194,220),(182,236),(170,222)],INK)
c.poly([(174,209),(190,207),(191,219),(182,232),(173,221)],SHIELD_C)
c.poly([(188,209),(190,208),(191,218),(187,220)],'#9a4545')
c.circle(182,218,2,ARMOR); c.set(182,218,INK)
# helmet + plume
c.circle(205,196,7,INK); c.circle(205,196,5,ARMOR_D)
c.rect(197,193,16,3,INK)
c.path("M205,189 Q218,178 229,184 Q219,187 209,193 Z",PLUME)
c.line(206,190,216,184,'#d05a3a')
# spear + pennant
c.line(226,216,196,152,INK); c.line(227,216,197,152,INK)
c.poly([(196,152),(202,146),(198,158)],ARMOR)
c.poly([(199,158),(208,162),(200,166)],PLUME)
# rim light
c.line(222,206,225,232,RIM); c.line(213,189,217,197,RIM)
c.line(220,234,221,244,RIM); c.line(200,234,199,244,RIM)
c.set(210,186,FIRE_HI); c.set(211,187,FIRE_MID)

# ---------------- arrows ----------------
for ax,ay,dx,dy in [(60,60,4,2),(150,44,4,2),(170,90,4,2),(90,108,4,2),(200,70,-4,2),
                    (128,118,4,2),(58,140,-4,2),(222,104,-4,2),(146,86,4,2),(108,34,4,2),
                    (186,128,-4,2),(74,42,4,2),(234,84,-4,2),(118,132,4,2)]:
    c.line(ax,ay,ax+dx,ay+dy,INK)
    c.set(ax+dx + (1 if dx>0 else -1), ay+dy, ARMOR_D)

# ---------------- embers ----------------
for i in range(80):
    px = 40 + (i*37+11) % 185
    py = 26 + (i*53+7) % 168
    if 94 <= px <= 234 and 6 <= py <= 150:   # keep the dragon clear
        continue
    col = [FIRE_HI,FIRE_MID,FIRE_OUT][i % 3]
    c.set(px,py,col)
    if i % 5 == 0: c.set(px+1,py-1,col)

# burning debris on the field
flame(64,238,9,4,lean=2)
flame(136,240,7,4,lean=2)
c.line(60,236,56,216,INK); c.line(120,240,124,222,INK); c.line(90,246,86,232,INK)
c.poly([(56,216),(59,210),(58,218)],ARMOR_D)

print(c.stats_text())
view(c)
finish(c)
