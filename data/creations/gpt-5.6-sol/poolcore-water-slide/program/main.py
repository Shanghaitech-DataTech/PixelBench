from pixelbench_api import *

# Poolcore liminal hall, built as deliberately stepped pixel art
c = new_canvas(128,128, background='#dceff1', name='poolcore_water_slide')

# palette
navy='#315b71'; deep='#214b62'; blue='#79bfd0'; water='#8ed7df'; light='#bcecef'
white='#f5fbf2'; grout='#a9d5da'; shadow='#6e9eae'; cyan='#c9f5ef'
yellow='#f2d34f'; gold='#d6a72f'; hair='#513f4a'; skin='#e7ad86'; suit='#d96a72'
lightblue='#dff8f5'; gray='#c6dfe0'; dark='#263c4c'; glow='#fffbe1'

# distant back wall and tiled floor/walls
c.rect(0,0,128,128, '#d8eef0')
# upper wall horizontal tile courses
for y in range(8,56,8):
    c.line(0,y,127,y,grout)
for x in range(0,128,16):
    c.line(x,8,x,55,grout)
# far wall blue lower band
c.rect(0,48,128,8,blue)
c.line(0,48,127,48,white)
c.line(0,55,127,55,deep)
# side perspective tile fields
c.poly([(0,56),(44,56),(20,94),(0,106)], '#c6e8ea')
c.poly([(84,56),(128,56),(128,106),(108,94)], '#c6e8ea')
# tile seams sides
for y in (64,72,80,88,96):
    c.line(0,y,37+(y-56)//2,y+0,grout)
    c.line(91-(y-56)//2,y,127,y,grout)
for x in (12,25,37): c.line(x,56,x-17,101,grout)
for x in (91,103,116): c.line(x,56,x+15,101,grout)
# far wall vertical columns/pillars
for x in (8,112):
    c.rect(x,18,9,43,white)
    c.rect(x+2,20,3,41,lightblue)
    c.rect(x-2,16,13,4,gray)
    c.rect(x-1,59,11,4,shadow)
# central back pillars
for x in (35,91):
    c.rect(x,23,7,35,white)
    c.rect(x+2,25,2,33,gray)
    c.rect(x-2,20,11,4,gray)
# ceiling bright fluorescent bars
for x in (14,43,75,104):
    c.rect(x,5,18,3,white)
    c.rect(x+2,6,14,1,glow)
    c.line(x+1,9,x+16,9,lightblue)
# pool main basin / edge
c.poly([(19,69),(42,57),(91,57),(111,69),(127,104),(127,128),(0,128),(0,104)], deep)
c.poly([(18,72),(43,60),(89,60),(110,72),(124,105),(124,128),(4,128),(4,105)], water)
# pale pool glow and horizon
c.line(21,70,107,70,white)
c.line(28,75,101,75,cyan)
# water bands and gentle ripples
for y, x0,x1 in [(82,18,108),(89,11,117),(97,7,122),(106,3,125),(115,10,119),(123,0,110)]:
    c.line(x0,y,x0+15,y,lightblue); c.line(x0+20,y,x0+36,y,white); c.line(x0+42,y,x1,y,blue)
# tile reflection grid under water
for x in (14,29,45,62,79,96,112): c.line(x,80,x+(x-62)//5,127, '#75bdc9')
for y in (86,94,103,113,124): c.line(5,y,123,y,'#79c4ce')
# central clearer water overlay patches
c.poly([(42,77),(87,77),(104,91),(110,119),(94,128),(28,128),(24,104)], '#a5e2e3')
for y in (84,91,99,108,118):
    c.line(26,y,102,y,lightblue)
# ripples reasserted
for seg in [(48,79,70),(76,83,98),(20,91,43),(86,96,115),(40,103,66),(66,111,92),(19,117,45),(93,122,119)]:
    x,y,x2=seg; c.line(x,y,x2,y,white)
    if x2-x>14: c.line(x+4,y+1,x2-5,y+1,blue)

# white curving slide: support and descending tube, stepped polygon
# supports
c.rect(73,34,4,40,shadow); c.rect(87,39,4,36,shadow)
c.rect(70,72,23,4,white)
# slide tube outer silhouette
c.path('M 70 22 L 94 22 L 94 27 L 91 27 L 91 36 C 91 46 87 52 80 57 C 73 62 68 65 70 72 L 75 79 L 67 79 C 61 70 62 62 70 56 C 78 50 82 46 82 37 L 82 30 L 70 30 Z', white, fill=True)
# slide shade edge
c.path('M 82 30 L 87 30 L 87 39 C 87 49 82 54 75 59 C 67 65 67 69 71 76 L 67 76 C 62 67 66 61 73 56 C 81 50 84 45 84 37 Z', '#c8e6e5', fill=True)
c.line(70,22,94,22,gray); c.line(70,29,82,29,shadow)
# end splash / slide reflection
c.line(62,82,82,82,white); c.line(66,84,76,84,cyan)

# girl floating in ring: yellow ring with inner water hole
c.ellipse(64,96,16,9,gold,fill=True)
c.ellipse(64,96,10,5,water,fill=True)
c.ellipse(64,97,15,8,yellow,fill=False)
# body seen from behind, shoulders and torso
c.poly([(58,88),(63,85),(70,85),(76,89),(75,101),(70,106),(59,102),(56,95)], suit, fill=True)
c.line(59,89,74,89,dark)
# arms resting on ring
c.line(58,91,52,96,skin); c.line(52,96,56,98,skin)
c.line(75,91,81,96,skin); c.line(81,96,77,98,skin)
# neck and head
c.rect(63,81,6,6,skin)
c.circle(66,77,7,skin,fill=True)
# long dark wet hair, back silhouette
c.circle(66,76,8,hair,fill=True)
c.rect(58,75,16,8,hair)
c.rect(59,81,5,11,hair)
c.rect(69,81,6,9,hair)
# face/neck glimpse
c.rect(63,79,7,6,skin)
c.rect(63,84,6,3,skin)
# hair highlights
c.line(60,73,61,82,shadow); c.line(64,70,65,80,shadow); c.line(69,71,71,80,shadow)
# ring highlight pixels
c.line(53,94,59,91,glow); c.line(71,89,77,91,glow)
# foreground glints
for x,y in [(8,110),(18,102),(32,116),(46,88),(95,105),(108,113),(119,91),(88,87),(27,124)]:
    c.line(x,y,x+4,y,white)
    c.set(x+2,y-1,white)

view(c, size=512, margin=0)
finish(c)
