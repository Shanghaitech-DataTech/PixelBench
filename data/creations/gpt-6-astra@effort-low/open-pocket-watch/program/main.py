import math
result = new_canvas(64,64, '#10151e', name='open_pocket_watch')
c=result
# restrained backdrop
c.ellipse(33,54,27,7,'#090c13')
c.ellipse(31,53,22,4,'#06090e')
# chain: overlapping polished links curling to the right
for x,y in [(43,9),(48,7),(53,8),(57,11),(59,15),(59,20),(57,24),(56,28),(58,32),(61,34)]:
 c.ellipse(x,y,3,2,'#292017',False)
 c.ellipse(x,y,2,2,'#ba8134',False)
 c.line(x-1,y-2,x+1,y-2,'#ffe5a0')
 c.set(x+2,y,'#e8b956')
# open lid above and left, oblique oval
c.ellipse(20,17,17,13,'#080b10')
c.ellipse(20,16,17,13,'#765025')
c.ellipse(19,15,16,12,'#dfaa51')
c.ellipse(19,15,14,10,'#fff0b1')
c.ellipse(19,15,13,9,'#85592d')
c.ellipse(19,15,12,8,'#b9843e')
c.ellipse(19,14,11,7,'#cca05c')
c.ellipse(19,14,9,5,'#ad7b3e',False)
c.line(9,12,17,8,'#eaca83')
c.line(7,16,10,20,'#f5d88c')
c.line(16,24,25,24,'#664225')
c.line(12,5,22,3,'#fff2bf')
c.line(4,13,4,17,'#ffdc83')
# hinge
c.poly([(19,26),(25,23),(31,28),(25,32)],'#5c3c20')
for x in range(21,29,2): c.line(x,26,x+3,29,'#d9a252')
# bow and winding crown at upper right
c.ellipse(41,19,5,6,'#bd8439',False)
c.ellipse(41,19,4,5,'#fce5a2',False)
c.ellipse(41,19,3,4,'#6e4826',False)
c.poly([(36,23),(41,24),(39,29),(34,27)],'#94622c')
for x in range(35,41):
 c.line(x,24,x-1,27,'#e8b95f' if x%2 else '#62401f')
# deep case and concentric reflective bezel
c.ellipse(31,42,23,20,'#070a10')
c.ellipse(31,41,23,20,'#6c4526')
c.ellipse(31,39,23,20,'#c18a3c')
c.ellipse(30,38,22,19,'#f9d783')
c.ellipse(31,39,21,18,'#8b5928')
c.ellipse(31,38,20,18,'#eabb63')
c.ellipse(31,38,19,17,'#38291f')
c.ellipse(31,38,18,16,'#bc8a43')
c.ellipse(31,38,16,14,'#71502c')
# hollow movement cavities
c.ellipse(26,40,10,11,'#211e1c')
c.ellipse(40,39,7,10,'#30271c')
c.ellipse(31,49,8,4,'#3d2e1d')
# dial chapter ring with dark engraved ticks
for i in range(60):
 a=2*math.pi*i/60
 x=round(31+17*math.sin(a)); y=round(38-15*math.cos(a))
 x2=round(31+(15.3 if i%5==0 else 16.4)*math.sin(a)); y2=round(38-(13.4 if i%5==0 else 14.5)*math.cos(a))
 c.line(x,y,x2,y2,'#443426')
# gear teeth, rim, spokes, annular cutouts
def gear(x,y,r,n):
 pts=[]
 for k in range(n*4):
  a=2*math.pi*k/(n*4); rr=r if k%4 in (1,2) else r-1
  pts.append((round(x+rr*math.cos(a)),round(y+rr*math.sin(a))))
 c.poly([(px+1,py+1) for px,py in pts],'#100f13')
 c.poly(pts,'#d29b42')
 c.circle(x,y,r-2,'#ffe19a')
 c.circle(x,y,r-3,'#49341e')
 for j in range(5):
  a=j*math.pi*2/5
  c.line(x,y,round(x+(r-3)*math.cos(a)),round(y+(r-3)*math.sin(a)),'#c38c3b')
 c.circle(x,y,2,'#e8b85b')
 c.set(x,y,'#29262a'); c.set(x-1,y-1,'#fff0b7')
 c.line(x-2,y-r+2,x+1,y-r+2,'#fff0ba')
gear(24,35,7,12)
gear(35,32,5,10)
gear(38,43,7,12)
gear(25,47,6,10)
# balance wheel at lower left
c.circle(21,44,4,'#b77a31',False)
c.circle(21,44,3,'#efd080',False)
c.line(18,43,24,45,'#b69b64')
c.set(21,44,'#e8e2bb')
# gilded bridge with inset screws
c.poly([(29,35),(32,34),(35,39),(34,45),(31,46),(32,39)],'#50351e')
c.line(30,35,33,39,'#ffe3a0')
c.line(33,39,32,45,'#c3954d')
for x,y in [(18,30),(41,30),(44,43),(30,51)]:
 c.circle(x,y,1,'#e7ca87');c.line(x,y,x+1,y,'#55483b');c.set(x,y-1,'#fff1c2')
# blued steel hands, contrasting face
c.line(31,39,26,29,'#0a1723')
c.line(30,38,25,28,'#345668')
c.line(31,38,39,29,'#071623')
c.line(32,38,40,29,'#9fbec0')
c.line(31,38,29,44,'#253b4c')
c.circle(31,38,2,'#18242b')
c.circle(31,38,1,'#ffe4a0')
c.set(31,37,'#fff6d5')
# bright edge glints and case facets
c.line(12,29,15,25,'#fff0b1')
c.line(10,33,9,38,'#fff3c2')
c.line(16,51,22,55,'#ffeaa5')
c.line(25,57,35,57,'#d09a4b')
c.line(38,55,43,52,'#fff2b4')
c.line(50,36,50,42,'#f8cf72')
c.set(49,33,'#fff3ca')
view(c)
finish(result)
