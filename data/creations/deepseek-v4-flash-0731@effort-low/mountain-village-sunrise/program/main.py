from pixelbench_api import *

c = new_canvas(128, 128, name="mountain-village-sunrise")

# ---- Sky flat sunrise bands ----
bands = [(0,20,'#232a58'),(20,36,'#44528c'),(36,46,'#7a5a88'),
         (46,54,'#b8786c'),(54,64,'#e09562'),(64,72,'#ffc06a'),(72,82,'#ffdd8a')]
for y0,y1,hexs in bands:
    c.rect(0,y0,128,y1-y0+1, c.color(hexs), fill=True)

# ---- Sun ----
sun=c.color('#f2b060'); sun2=c.color('#ffd65c'); sun3=c.color('#ffe08c'); core=c.color('#fff8c4')
c.circle(64,46,22,sun,fill=True)
c.circle(64,46,16,sun2,fill=True)
c.circle(64,46,10,sun3,fill=True)
c.circle(64,46,5,core,fill=True)

# ---- Distant mountain (hazy) ----
far=c.color('#6a588e'); farhi=c.color('#a89abf')
c.poly([(0,90),(0,78),(14,74),(24,70),(34,76),(46,62),(56,68),(64,64),(72,72),(84,66),(98,74),(110,68),(120,76),(127,80),(127,90)],far,fill=True)
c.line(0,88,14,74,farhi); c.line(14,74,24,70,farhi); c.line(34,76,46,62,farhi)
c.line(46,62,56,68,farhi); c.line(64,64,72,72,farhi); c.line(84,66,98,74,farhi)

# ---- Near mountain ----
near=c.color('#44355c'); nearhi=c.color('#6a5a86')
c.poly([(0,96),(0,84),(16,82),(28,88),(40,80),(52,86),(64,82),(76,88),(88,82),(102,90),(114,84),(127,90),(127,96)],near,fill=True)
c.line(16,82,28,88,nearhi); c.line(40,80,52,86,nearhi); c.line(64,82,76,88,nearhi)

# ---- Middle hills ----
hill1=c.color('#3a4030'); hill2=c.color('#2e3a2a')
c.poly([(0,100),(0,92),(30,94),(64,88),(100,94),(127,92),(127,100)],hill1,fill=True)
c.poly([(0,104),(20,99),(52,104),(80,98),(110,103),(127,100),(127,106)],hill2,fill=True)

# ---- Ground ----
ground=c.color('#27351f'); ground2=c.color('#1f2a1a')
c.rect(0,100,128,28,ground,fill=True)
c.rect(0,114,128,14,ground2,fill=True)

# ---- Village plateau ----
plat=c.color('#3a4a28')
c.poly([(34,102),(52,92),(76,92),(96,102),(92,108),(36,108)],plat,fill=True)

# pine tree helper
trunk=c.color('#2a2218'); pine=c.color('#244020'); pine2=c.color('#1c3418'); pine3=c.color('#162c14')
def pine_tree(cx, groundy, h, colr):
    c.rect(cx-1, groundy-2, 2, 2, trunk, fill=True)
    i=0
    for lev in range(h, 1, -4):
        yy = groundy - lev + i*2
        c.rect(cx-(i+1), yy, 2*i+2, 3, colr, fill=True)
        i+=1

# ---- Houses ----
wall=c.color('#7c4a28'); roof=c.color('#6b2a16'); roofhi=c.color('#8a4a20')
dark=c.color('#3a201a'); win=c.color('#ffd98a'); winf=c.color('#ffb06a')
ch=c.color('#4a3624')
# central house
c.rect(56,84,20,13,wall,fill=True)
c.poly([(52,85),(66,68),(82,85)],roof,fill=True)
c.poly([(52,85),(59,76)],roofhi,fill=True)
c.line(60,85,62,79,roofhi)
c.rect(63,90,6,7,dark,fill=True)
c.rect(58,86,5,4,winf,fill=True)
c.rect(69,86,5,4,winf,fill=True)
c.rect(64,72,4,12,ch,fill=True)
# left house
c.rect(30,88,15,9,wall,fill=True)
c.poly([(27,89),(37,76),(49,89)],roof,fill=True)
c.rect(35,91,4,6,dark,fill=True)
c.rect(31,90,3,3,winf,fill=True)
# right house
c.rect(84,86,14,11,wall,fill=True)
c.poly([(81,87),(91,74),(101,87)],roof,fill=True)
c.line(81,87,83,88,roofhi)
c.rect(88,90,4,7,dark,fill=True)
c.rect(85,88,3,3,win,fill=True)
c.rect(92,76,3,10,ch,fill=True)
# shed
c.rect(102,94,8,5,wall,fill=True)
c.poly([(100,95),(106,89),(112,95)],roof,fill=True)

# ---- Smoke ----
smk=c.color('#c8c8c8'); smk2=c.color('#b8bab8'); smk3=c.color('#a2a6a8')
for (sx,sy,sr,sco) in [(66,68,3,smk),(68,64,3,smk2),(70,60,3,smk3),(71,56,3,smk3),
                      (92,72,2,smk),(94,68,2,smk2),(95,65,2,smk3)]:
    c.circle(sx,sy,sr,sco,fill=True)

# ---- Stone path ----
pathc=c.color('#9a8a70'); stone=c.color('#b8aa90'); stone2=c.color('#c8bda0'); edge=c.color('#6a5a46')
hi=c.color('#d4c8ac')
c.poly([(44,127),(86,127),(74,105),(52,105)],pathc,fill=True)
c.poly([(52,105),(74,105),(68,94),(60,94)],pathc,fill=True)
for (sx,sy,sr,sc) in [(51,125,11,stone),(64,127,10,stone2),(76,125,11,stone),(58,118,8,stone2),
                     (70,119,9,stone),(63,111,7,stone),(55,106,6,stone),(70,108,7,stone2),
                     (62,101,5,stone2),(66,96,4,stone2),(61,95,3,stone)]:
    c.circle(sx,sy,sr,sc,fill=True)

# ---- Distant pines on hills ----
for cx,gy,h,co in [(12,99,10,pine),(20,97,8,pine2),(108,98,9,pine),(120,99,11,pine),(94,97,7,pine2),(46,94,9,pine),(80,94,9,pine2)]:
    pine_tree(cx,gy,h,co)

# ---- Foreground framing pines ----
for cx,gy,h,co in [(7,116,26,pine2),(18,112,20,pine3),(110,112,22,pine2),(122,116,28,pine3),(100,108,14,pine3),(31,110,12,pine3)]:
    pine_tree(cx,gy,h,co)

# ---- foreground rocks ----
rock=c.color('#3a322a')
for (rx,ry,rr) in [(90,120,6),(100,116,4),(30,119,5),(22,114,4)]:
    c.circle(rx,ry,rr,rock,fill=True)

# ---- warm rim light on roofs ----
k=c.color('#ffc46a')
c.line(52,85,59,76,k); c.line(82,85,73,76,k)

# ---- vignette corners ----
vig=c.color('#12100e')
c.poly([(0,114),(0,127),(20,127),(6,114)],vig,fill=True)
c.poly([(127,114),(127,127),(108,127),(122,114)],vig,fill=True)

print(c.stats_text())
finish(c)
