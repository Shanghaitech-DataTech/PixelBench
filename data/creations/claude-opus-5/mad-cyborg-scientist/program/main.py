c = new_canvas(64, 64, name="output")

# ---------------- palette ----------------
BG_D='#12161f'; BG_M='#1b2533'; BG_L='#2b3b4d'; BG_H='#41586d'
SK_H='#f2c79c'; SK_M='#cf9166'; SK_S='#a16643'; SK_D='#6e412c'; RIM='#ffe6c6'
MT_H='#dde4ef'; MT_M='#9ea9b8'; MT_S='#6b7684'; MT_D='#454e5a'; MT_K='#252b33'
HAIR_H='#ffffff'; HAIR_M='#dde3ee'; HAIR_S='#aab3c4'; HAIR_D='#7a8392'
CO_H='#eef1f7'; CO_M='#c6cdd9'; CO_S='#98a1af'; CO_D='#69727f'
DIRT='#b5a98d'; DIRT_D='#8a7e65'
AP_H='#8d5c33'; AP_M='#6a4124'; AP_D='#472a16'
BELT='#3b2a1b'; GOLD='#d8a93e'
EYE_W='#f2ead9'; IRIS='#3f6f8f'; PUP='#0e1318'
GL_C='#fff3c8'; GL_M='#ff5a2a'; GL_D='#c21f10'; GL_G='#6e1a0e'
MOU='#3a1a16'; TOOTH='#fff6e2'
CBL_A='#262c34'; CBL_B='#121519'; CBL_R='#bf3a22'; CBL_G='#2f7d4a'; CBL_Y='#c9a53a'

# ---------------- background (light from upper-left) ----------------
c.rect(0,0,64,64,BG_D)
c.rect(0,0,36,64,BG_M)
c.dither(33,0,7,64,[BG_M,BG_D],"bayer4")
c.rect(0,0,18,64,BG_L)
c.dither(16,0,5,64,[BG_L,BG_M],"bayer4")
c.rect(0,0,7,64,BG_H)
c.dither(5,0,4,64,[BG_H,BG_L],"bayer4")

# ---------------- head mask ----------------
HEAD = "M 19 25 C 19 10 43 10 43 25 L 43 30 C 43 38 37 41 31 41 C 25 41 19 38 19 30 Z"
hm = new_canvas(64,64,name="hm")
hm.path(HEAD, '#ffffff')
hidx = hm.color('#ffffff')
head_px = set()
for y in range(64):
    for x in range(64):
        if hm.get(x,y) == hidx:
            head_px.add((x,y))

rows = {}
for (x,y) in head_px:
    a,b = rows.get(y,(99,-1))
    rows[y] = (min(a,x), max(b,x))

# neck
c.rect(27,36,9,8,SK_S)
c.rect(27,36,3,8,SK_M)
c.rect(32,36,4,8,MT_D)
c.rect(34,36,2,8,MT_K)

# ---------------- face: human left / metal right ----------------
for (x,y) in head_px:
    if x <= 31:
        if x <= 22: col = SK_H
        elif x <= 27: col = SK_M
        elif x <= 29: col = SK_S
        else: col = SK_D
    else:
        if x <= 34: col = MT_M
        elif x <= 38: col = MT_S
        elif x <= 41: col = MT_D
        else: col = MT_K
    c.set(x,y,col)

# rim light on the lit edge
for y,(a,b) in rows.items():
    c.set(a,y,RIM)
    if a+1 <= 21:
        c.set(a+1,y,SK_H)
    c.set(b,y,MT_K)

# forehead / cheek modelling
c.path("M 21 16 C 25 13 29 14 29 18 C 27 16 23 17 21 20 Z", RIM)
c.path("M 20 27 C 24 26 27 29 26 33 C 23 33 21 31 20 29 Z", SK_H)
c.path("M 28 22 C 31 24 31 30 29 34 L 27 32 C 29 29 29 25 28 22 Z", SK_D)
# jaw shadow under chin
c.line(24,39,30,40,SK_D)

# chrome seam down the middle
for y in range(11,41):
    if (31,y) in head_px:
        c.set(31,y,MT_K)
        c.set(32,y,MT_H if y % 3 else MT_M)

# metal plate panels / rivets / vents
c.line(33,20,42,20,MT_K)
c.line(33,21,41,21,MT_S)
c.line(34,30,42,31,MT_K)
for (px,py) in ((36,16),(40,18),(39,27),(41,34),(35,36)):
    c.set(px,py,MT_H); c.set(px+1,py,MT_S); c.set(px,py+1,MT_S)
for vy in (34,36,38):
    c.line(33,vy,35,vy,MT_K)
c.path("M 33 12 C 37 11 41 13 42 17 L 40 17 C 39 14 36 13 33 14 Z", MT_H)

# ---------------- human eye (wide, manic) ----------------
c.rect(21,23,7,2,SK_D)
c.line(20,22,27,21,HAIR_H)
c.line(21,23,26,22,HAIR_S)
c.rect(21,25,6,4,EYE_W)
c.set(21,25,SK_S); c.set(26,28,SK_S)
c.rect(23,25,3,4,IRIS)
c.rect(24,26,2,2,PUP)
c.set(23,26,'#8fc7e6')
c.line(21,24,26,24,SK_D)
c.line(22,29,26,30,SK_S)

# ---------------- glowing cybernetic eye ----------------
c.circle(37,26,4,MT_K)
c.circle(37,26,3,GL_G)
c.circle(37,26,2,GL_D)
c.circle(37,26,1,GL_M)
c.set(37,26,GL_C)
c.set(36,25,GL_C)
c.circle(37,26,5,MT_S,fill=False)
# glow spill
for (gx,gy) in ((33,22),(34,21),(41,22),(42,25),(41,31),(34,31),(33,29),(43,27)):
    c.set(gx,gy,GL_G)
c.line(31,26,33,26,GL_D)

# nose
c.line(30,27,29,31,SK_D)
c.set(28,31,SK_D)
c.set(29,30,SK_S)

# ---------------- maniacal grin ----------------
MX0 = 21
TOP = [34,33,33,32,32,32,32,32,32,32,32,32,31,31,31,30,30,30,30]
BOT = [34,35,36,36,37,37,37,37,37,37,36,36,36,35,35,34,33,32,31]
for i,(t,b) in enumerate(zip(TOP,BOT)):
    x = MX0 + i
    c.line(x,t,x,b,MOU)
    # upper teeth
    c.set(x,t,TOOTH)
    if b > t: c.set(x,t+1,TOOTH)
    # lower teeth where the mouth is open enough
    if b - t >= 4:
        c.set(x,b,TOOTH)
        c.set(x,b-1,'#d8cbb2')
    if x % 3 == 0:
        c.set(x,t+1,MOU)
        if b - t >= 4: c.set(x,b,MOU)
# lips / corner creases
c.line(20,33,21,34,SK_D)
c.set(20,32,SK_S)
for i,(t,b) in enumerate(zip(TOP,BOT)):
    x = MX0 + i
    if b + 1 <= 40 and x <= 31:
        c.set(x,b+1,SK_D)
    elif b + 1 <= 40:
        c.set(x,b+1,MT_K)
c.set(40,30,MT_K); c.set(40,31,MT_K)

# ---------------- messy white hair ----------------
HAIR = ("M 16 30 L 13 22 L 17 21 L 14 13 L 19 16 L 18 7 L 23 13 L 25 5 "
        "L 29 12 L 32 6 L 34 13 L 38 9 L 38 15 L 41 13 L 40 18 "
        "L 36 15 L 34 19 L 30 14 L 26 18 L 22 15 L 19 22 Z")
c.path(HAIR, HAIR_M)
c.path("M 16 30 L 13 22 L 17 21 L 14 13 L 19 16 L 18 7 L 22 13 L 21 19 L 19 22 Z", HAIR_H)
c.path("M 32 6 L 34 13 L 38 9 L 38 15 L 41 13 L 40 18 L 36 15 L 34 19 L 32 14 Z", HAIR_S)
c.line(34,13,36,16,HAIR_D)
c.line(29,12,30,16,HAIR_S)
c.line(23,13,24,17,HAIR_M)
# sideburn / temple hair
c.path("M 17 22 L 20 24 L 19 31 L 16 29 Z", HAIR_M)
c.set(18,25,HAIR_H); c.set(17,27,HAIR_H)

# ---------------- brain electrode plugs ----------------
plugs = ((36,13),(40,16),(43,21))
for (px,py) in plugs:
    c.rect(px,py,3,3,MT_D)
    c.rect(px,py,3,1,MT_H)
    c.set(px+1,py+1,GOLD)
c.path("M 37 13 C 44 6 54 7 59 13", CBL_R, fill=False)
c.path("M 41 16 C 48 12 56 15 60 20", CBL_A, fill=False)
c.path("M 44 21 C 50 20 55 23 58 27", CBL_G, fill=False)
c.path("M 37 14 C 44 8 53 9 58 14", CBL_B, fill=False)

# ---------------- lab coat / shoulders ----------------
c.path("M 1 64 L 4 52 C 7 45 14 42 21 42 L 31 45 L 41 42 C 50 43 57 48 60 57 L 61 64 Z", CO_M)
c.path("M 1 64 L 4 52 C 7 45 13 42 19 42 L 20 50 L 13 56 L 12 64 Z", CO_H)
c.path("M 41 42 C 50 43 57 48 60 57 L 61 64 L 48 64 L 44 52 Z", CO_S)
# collar
c.path("M 21 42 L 31 46 L 27 50 L 20 46 Z", CO_H)
c.path("M 41 42 L 31 46 L 35 50 L 42 46 Z", CO_D)
c.line(31,46,31,52,CO_D)
# lapel + seams on the lit shoulder
c.path("M 20 46 L 13 56 L 12 63", CO_D, fill=False)
c.path("M 21 43 C 14 46 9 52 7 60", CO_S, fill=False)
c.path("M 42 46 L 46 54 L 47 63", CO_D, fill=False)
# shadow cast by the head onto the coat
c.path("M 22 45 C 27 50 36 50 41 45 L 42 48 C 36 53 27 53 21 48 Z", CO_S)
# pocket
c.rect(6,57,7,5,CO_S,fill=False)
c.line(6,57,12,57,CO_D)
# grime on the coat
c.dither(6,55,8,7,[DIRT,CO_M],"bayer4")
c.dither(46,52,7,6,[DIRT_D,CO_S],"bayer4")
c.set(14,50,DIRT_D); c.set(15,51,DIRT_D)

# ---------------- leather apron ----------------
c.path("M 22 47 L 31 51 L 40 47 L 44 64 L 18 64 Z", AP_M)
c.path("M 22 47 L 31 51 L 29 56 L 21 53 L 20 64 L 18 64 Z", AP_H)
c.path("M 40 47 L 44 64 L 36 64 L 36 52 Z", AP_D)
c.line(24,58,38,58,AP_D)
c.set(26,54,AP_H); c.set(33,60,AP_H)
# straps
c.line(23,47,27,43,AP_D)
c.line(39,47,35,43,AP_D)

# ---------------- tool belt ----------------
c.rect(17,59,28,4,BELT)
c.rect(17,59,28,1,'#54402b')
c.rect(29,59,5,4,GOLD)
c.rect(30,60,3,2,'#8a6a1f')
# tools hanging
c.rect(21,61,2,3,MT_M); c.set(21,63,MT_H)
c.rect(24,61,2,3,CBL_R)
c.rect(38,61,2,3,MT_S); c.set(39,63,MT_H)
c.rect(41,60,2,4,CBL_G)
c.set(36,61,GOLD)

# ---------------- robotic arm, raised prosthetic hand ----------------
c.circle(45,49,4,MT_S)
c.circle(45,49,2,MT_M)
c.path("M 45 45 L 57 43 L 58 49 L 46 52 Z", MT_D)
c.line(47,46,56,44,MT_S)
c.circle(55,46,3,MT_M)
c.set(54,45,MT_H)
# forearm
c.rect(51,32,7,13,MT_S)
c.rect(51,32,2,13,MT_M)
c.set(51,33,MT_H); c.set(51,38,MT_H); c.set(51,42,MT_H)
c.line(51,36,57,36,MT_K)
c.line(51,40,57,40,MT_K)
c.rect(57,32,1,13,MT_K)
# wrist joint
c.rect(50,30,9,3,MT_D)
c.line(50,30,58,30,MT_M)
# palm
c.rect(49,23,10,8,MT_S)
c.rect(49,23,2,8,MT_M)
c.set(49,24,MT_H); c.set(50,26,MT_H)
c.rect(58,23,1,8,MT_K)
c.line(50,27,57,27,MT_D)
# fingers (staggered lengths, visible knuckle gaps)
for fx,fy in ((49,19),(52,16),(55,15),(58,17)):
    c.rect(fx,fy,2,24-fy,MT_S)
    c.rect(fx,fy,1,24-fy,MT_M)
    c.set(fx,fy,MT_H)
    c.set(fx+1,fy,MT_K)
    c.set(fx+1,fy+3,MT_K)
    c.line(fx,fy+2,fx+1,fy+2,MT_D)
    c.line(fx,fy+5,fx+1,fy+5,MT_D)
    c.set(fx,fy+1,MT_H)
# thumb
c.rect(46,25,3,3,MT_S)
c.rect(45,26,2,3,MT_M)
c.set(45,26,MT_H)
c.set(47,27,MT_D)
# cables from wrist down to shoulder
c.path("M 50 31 C 46 35 46 42 48 47", CBL_R, fill=False)
c.path("M 52 31 C 48 36 47 43 50 48", CBL_A, fill=False)
c.path("M 56 31 C 59 36 60 42 58 48", CBL_B, fill=False)
c.path("M 54 31 C 57 35 58 41 56 47", CBL_Y, fill=False)
c.set(47,38,CBL_B); c.set(59,40,CBL_A)

# ---------------- final contrast touches ----------------
# chin modelling under the grin
c.line(24,39,29,40,SK_D)
c.set(23,38,SK_H); c.set(22,37,SK_H)
c.set(25,39,SK_S)
# red glow bouncing off the right-hand side of the face and teeth
for (gx,gy) in ((33,33),(34,34),(35,31),(36,32),(38,30),(37,36),(35,37)):
    c.set(gx,gy,GL_G)
c.set(34,32,GL_D)
c.set(32,27,GL_M)
# manic brow lift and eye-white glint
c.line(20,21,27,20,HAIR_H)
c.set(27,25,EYE_W); c.set(22,27,EYE_W)
c.set(26,25,SK_D)
# dark vignette bottom-right
c.dither(54,54,10,10,[BG_D,CBL_B],"bayer4")
c.outline(CBL_B)

print(c.stats_text())
save("mad_cyborg_scientist", c)
view(c)
finish(c)
