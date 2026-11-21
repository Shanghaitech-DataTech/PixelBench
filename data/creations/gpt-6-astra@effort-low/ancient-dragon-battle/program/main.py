import random, math
random.seed(14)
c=new_canvas(256,256,'#392c49',name='ancient-dragon-battle')
ink='#171c2b'; dark='#292638'; stone='#655663'; light='#927473'; gold='#ffcd77'
# sunset bands
for y in range(174):
 col=['#34304d','#46334f','#603b53','#834453','#ac5355','#ce6958','#e78964','#f3ac75'][min(7,y//22)]
 c.line(0,y,255,y,col)
c.circle(186,91,34,'#f9bb79'); c.circle(186,91,29,'#ffcf8b')
# streaked clouds
for i in range(60):
 x=random.randrange(256); y=random.randrange(12,115); w=random.randrange(7,40)
 c.rect(x,y,min(w,256-x),random.choice([1,2,3]),random.choice(['#633a50','#844553','#ac5355']))
# mountains
c.poly([(0,150),(0,124),(21,106),(41,131),(67,99),(85,125),(110,112),(136,144),(163,124),(181,136),(212,104),(234,128),(255,110),(255,174)],'#61475a')
c.poly([(0,157),(28,133),(49,145),(79,125),(98,146),(124,133),(155,155),(183,140),(216,147),(238,130),(255,143),(255,191),(0,191)],'#463e51')
# smoke billows behind castle
for cx,cy in [(73,133),(145,143),(206,136)]:
 for j in range(11):
  x=cx+int(math.sin(j*.7)*8)-j*2; y=cy-j*7
  c.circle(x,y,random.randrange(7,14),'#49404d' if j%3 else '#584451')
  c.circle(x-3,y-3,random.randrange(4,8),'#63505a')
# ground
c.poly([(0,187),(46,174),(95,184),(152,174),(209,187),(255,175),(255,256),(0,256)],'#343240')
for i in range(700):
 x=random.randrange(256);y=random.randrange(187,256)
 c.line(x,y,min(255,x+random.randrange(1,5)),y,random.choice(['#45404a','#514550','#292d3b']))
# flames
def fire(x,y,s):
 c.poly([(x-s,y),(x-s+2,y-10),(x-4,y-7),(x-2,y-24),(x+2,y-15),(x+5,y-30),(x+7,y-12),(x+s,y-18),(x+s+2,y)],'#c84d3d')
 c.poly([(x-s+3,y),(x-2,y-17),(x+2,y-9),(x+5,y-21),(x+8,y)],'#f38b46')
 c.poly([(x-3,y),(x+2,y-13),(x+5,y)],'#ffe39b')
# castle towers
for x,y,w,h in [(47,137,29,65),(91,125,32,77),(138,142,30,60),(185,131,32,74)]:
 c.rect(x-2,y,w+4,h,ink);c.rect(x,y,w,h,stone);c.rect(x+w-8,y,8,h,'#4e4758');c.line(x+2,y,x+2,y+h-1,light)
 for yy in range(y+8,y+h,7):
  c.line(x,yy,x+w-1,yy,'#494252')
  for xx in range(x+((yy//7)%2)*7,x+w,13):c.line(xx,yy-6,xx,yy,'#494252')
 for xx in range(x+6,x+w-3,12):
  c.rect(xx,y+13,4,12,ink);c.set(xx+1,y+14,'#e58c61')
 c.rect(x-3,y-3,w+6,7,ink);c.rect(x-2,y-2,w+4,4,light)
 for xx in range(x-2,x+w,8):c.rect(xx,y-8,5,7,ink);c.rect(xx+1,y-7,3,5,stone)
 fire(x+w//2,y-3,9)
# keep pointed roof and banner
c.poly([(85,119),(106,84),(129,119)],ink);c.poly([(89,116),(106,89),(123,116)],'#754550')
for yy in range(100,116,4):c.line(106-(yy-88)//2,yy,106+(yy-88)//2,yy,'#aa6258')
c.line(106,71,106,90,ink);c.poly([(107,72),(124,76),(117,80),(107,79)],'#c67c60')
# curtain wall
c.rect(28,168,203,44,ink);c.rect(30,172,199,38,'#5d5260');c.rect(30,173,199,3,'#a17b70')
for yy in range(181,210,7):
 c.line(30,yy,228,yy,'#403d4f')
 for xx in range(31+(yy%2)*9,229,18):c.line(xx,yy-6,xx,yy,'#403d4f')
for x in range(28,231,10):c.rect(x,162,7,10,ink);c.rect(x+1,163,5,7,'#89717a')
# gate
c.path('M 112 211 L 112 190 Q 127 168 142 190 L 142 211 Z',ink)
c.path('M 117 210 L 117 191 Q 127 177 137 191 L 137 210 Z','#7a4d43')
for x in range(119,138,4):c.line(x,187,x,209,'#2b2938')
c.line(116,198,138,198,ink)
# defenders with steel and crimson shields
def knight(x,y,scale=1):
 c.line(x-2,y+3,x-3,y+8,ink);c.line(x+1,y+3,x+3,y+8,ink)
 c.rect(x-3,y-3,6,7,ink);c.rect(x-2,y-2,4,5,'#81909a');c.line(x-2,y-2,x-2,y+2,'#bec4bc')
 c.rect(x-2,y-8,5,5,ink);c.rect(x-1,y-7,3,3,'#b0b7b3');c.set(x+1,y-5,ink)
 c.poly([(x+1,y-2),(x+6,y-2),(x+6,y+3),(x+3,y+6),(x+1,y+3)],ink)
 c.poly([(x+2,y-1),(x+5,y-1),(x+5,y+3),(x+3,y+4)],'#a94e4b');c.line(x+3,y,x+3,y+3,'#e8ab70')
 c.line(x-5,y+5,x-5,y-16,'#c09e7b');c.poly([(x-7,y-14),(x-5,y-20),(x-3,y-14)],'#b5c0bd')
for x in [36,57,81,153,175,198,221]:knight(x,160)
# siege towers on flanks
for x,y in [(4,163),(225,172)]:
 c.poly([(x,y+55),(x+5,y),(x+20,y),(x+26,y+55)],ink)
 c.poly([(x+4,y+49),(x+8,y+4),(x+18,y+4),(x+22,y+49)],'#795443')
 for yy in range(y+8,y+48,8):
  c.line(x+6,yy,x+21,yy,'#c08a5c');c.line(x+6,yy+2,x+21,yy+2,'#3c3034')
 c.line(x+7,y+3,x+20,y+49,'#bb875b');c.line(x+18,y+3,x+5,y+49,'#a07150')
 c.rect(x+1,y-3,24,8,ink);c.rect(x+3,y-2,20,4,'#a87552')
 for xx in [x+5,x+21]:c.circle(xx,y+53,5,ink);c.circle(xx,y+53,2,'#8d6b51')
 c.line(x+19,y+8,min(255,x+37),y+14,'#c09568')
# massed foreground troops
for row in range(4):
 for j in range(13):
  x=32+j*15+(row%2)*6;y=216+row*11
  if 107<x<146:continue
  knight(x,y)
# foreground pennants
for x,y in [(27,211),(201,213)]:
 c.line(x,y-23,x,y+24,'#c9a67b');c.poly([(x+1,y-23),(x+18,y-20),(x+13,y-14),(x+18,y-8),(x+1,y-11)],ink);c.poly([(x+2,y-22),(x+15,y-19),(x+10,y-14),(x+2,y-13)],'#b9544c')
# ancient dragon enormous sweeping wings
c.poly([(119,75),(101,59),(88,38),(57,19),(25,13),(44,28),(51,46),(55,69),(68,56),(83,63),(94,79),(110,86)],ink)
c.poly([(113,76),(94,49),(61,25),(33,17),(51,32),(58,59),(68,49),(86,57),(98,75)],'#704956')
c.poly([(96,63),(86,40),(58,22),(70,46),(85,53)],'#a36768')
c.poly([(122,74),(131,48),(159,22),(201,9),(231,13),(207,23),(189,41),(180,65),(163,57),(147,66),(137,85)],ink)
c.poly([(128,73),(137,49),(161,28),(207,13),(224,14),(201,25),(184,55),(163,49),(145,60),(136,78)],'#754c5a')
c.poly([(139,55),(162,29),(210,15),(180,34),(162,49)],'#b57570')
for pts in [[(119,76),(89,40),(29,15)],[(119,76),(67,50),(56,65)],[(126,77),(161,28),(226,13)],[(126,77),(179,34),(181,61)],[(127,76),(162,51),(170,56)]]:
 for a,b in zip(pts,pts[1:]):c.line(*a,*b,'#302c3d')
# curling tail and body
c.path('M 125 77 Q 111 94 88 91 Q 65 87 56 101 Q 49 111 34 105 Q 53 121 63 107 Q 72 98 91 104 Q 117 110 136 88 Z',ink)
c.path('M 125 81 Q 107 98 87 95 Q 66 92 59 105 Q 52 113 42 109 Q 56 117 65 104 Q 75 97 92 101 Q 117 106 132 86 Z','#6e6665')
c.poly([(105,83),(118,69),(136,71),(147,85),(139,97),(118,98),(107,91)],ink)
c.poly([(109,83),(119,74),(132,75),(142,85),(136,93),(120,94)],'#626a69')
c.line(114,89,132,91,'#a3a18b')
# neck and head
c.path('M 130 84 Q 145 83 147 68 L 153 57 L 166 53 L 176 60 L 181 63 L 180 71 L 166 73 L 158 68 Q 158 95 139 96 Z',ink)
c.path('M 137 86 Q 150 84 151 68 L 157 59 L 167 57 L 174 63 L 177 65 L 175 69 L 163 67 L 156 65 Q 155 89 140 92 Z','#727b73')
c.line(158,60,169,59,'#a9aa8e');c.line(161,65,173,68,'#33343e');c.set(167,62,'#ffe89d');c.set(168,62,'#ffac53')
c.poly([(154,60),(150,48),(159,55)],ink);c.line(153,51,157,57,'#d2c09a')
c.poly([(165,56),(169,46),(171,57)],ink);c.line(170,49,168,56,'#d2c09a')
# spines
for x,y in [(110,81),(118,75),(127,75),(139,79),(146,73)]:
 c.poly([(x-3,y),(x-3,y-7),(x+3,y)],ink);c.line(x-2,y-4,x,y-1,'#bcb298')
# legs claws
for pts in [[(119,92),(109,106),(116,111),(126,108)],[(136,92),(140,102),(150,103),(154,108)]]:
 c.poly(pts,ink)
 c.line(pts[0][0],pts[0][1],pts[1][0]+2,pts[1][1],'#85877a')
 for xx in range(pts[-1][0]-5,pts[-1][0]+2,3):c.line(xx,pts[-1][1]-1,xx+2,pts[-1][1]+3,'#d3bb94')
# dragon scales
for i in range(26):
 x=random.randrange(115,138);y=random.randrange(80,91)
 c.set(x,y,random.choice(['#8b9380','#434f55']))
# jet of fire down towards right castle
c.poly([(179,68),(185,71),(198,90),(209,101),(202,100),(217,119),(201,111),(203,118),(188,98),(185,84)],'#c95840')
c.poly([(179,69),(187,78),(193,91),(206,109),(196,103),(188,89)],'#ff9f4e')
c.poly([(180,70),(187,82),(191,94),(185,84)],'#ffdf8b')
# flying arrows
for x,y,dx,dy in [(33,91,10,-9),(85,122,8,-12),(122,135,7,-15),(211,92,-9,-12),(232,120,-9,-10),(24,131,10,-7),(173,119,-5,-12),(98,152,7,-11)]:
 c.line(x,y,x+dx,y+dy,ink);c.set(x+dx,y+dy,'#d9b695');c.line(x-2,y,x+1,y+3,'#a68a83')
# embers
for i in range(100):
 x=random.randrange(30,230);y=random.randrange(106,206)
 if random.random()<.6 and y<150 or y>177:
  c.set(x,y,random.choice(['#ffce79','#ed8c50','#b95c49']))
view(c)
finish(c)
