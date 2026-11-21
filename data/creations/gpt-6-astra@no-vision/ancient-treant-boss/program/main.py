import math, random
random.seed(24)
W=H=256
c=new_canvas(256,256,background='#0c2024',name='Ancient treant')
P={'ink':'#101719','deep':'#192524','shadow':'#29312b','bark0':'#34372b','bark1':'#4c4935','bark2':'#65583c','bark3':'#817047','bark4':'#a18a58','cut':'#bfaa6e','moss0':'#233c2b','moss1':'#355737','moss2':'#537344','moss3':'#77924f','moss4':'#a4ae62','green':'#a7f66b','light':'#e1ffad'}
# Deep woodland, with stepped bands of haze.
for y,col in [(35,'#102a2d'),(75,'#153236'),(110,'#1b3b3b'),(147,'#254542'),(181,'#304b40'),(211,'#24392f')]:
 c.rect(0,y,256,256-y,col)
# distant trunks and buttresses
for x,w,top in [(5,12,0),(27,7,0),(46,9,0),(67,5,0),(191,7,0),(215,9,0),(242,15,0),(91,4,0),(177,4,0)]:
 col=random.choice(['#173135','#1b3637','#203e3c'])
 c.poly([(x,top),(x+w,top),(x+w-2,145),(x+w+9,185),(x-8,185),(x+2,137)],col)
 c.line(x+2,0,x+4,150,'#294844')
 for yy in [26,65,99]:
  s=random.choice([-1,1]);c.poly([(x+3,yy+6),(x+3+s*23,yy-17),(x+3+s*27,yy-24),(x+5,yy)],col)
# transparent geometrically stepped sun shafts through fog, composited once
rays=new_canvas(256,256,name='Sunbeams')
rays.poly([(36,0),(46,0),(163,206),(129,199)],'#d5dea220')
rays.poly([(55,0),(59,0),(183,202),(173,205)],'#d7e3ae15')
rays.poly([(177,0),(185,0),(247,155),(226,174)],'#d6e5b11b')
rays.poly([(162,0),(166,0),(222,168),(210,179)],'#d6e5b10d')
c=flatten([c,rays],name='Forest clearing')
# bordering near trees
for pts in [[(0,0),(17,0),(15,44),(20,100),(15,164),(29,204),(0,215)],[(256,0),(243,0),(235,67),(239,147),(230,195),(256,208)]]:
 c.poly(pts,'#0c2023')
c.path('M 8 0 L 6 80 L 13 144 L 9 180 M 248 0 L 244 61 L 248 142', '#203831',False)
c.poly([(0,43),(38,12),(68,0),(47,0),(20,13),(0,24)],'#0c2023')
c.poly([(256,23),(215,5),(204,0),(230,0),(256,10)],'#0c2023')
# clearing earth
c.poly([(0,212),(38,201),(75,202),(107,193),(151,192),(196,201),(231,198),(255,211),(255,255),(0,255)],'#263b31')
c.ellipse(133,220,97,25,'#354735');c.ellipse(128,214,73,17,'#43533b')
c.ellipse(130,217,59,11,'#25372c')
# Broken horizontal foliage clusters and grasses in the floor
for i in range(210):
 x=random.randrange(256);y=random.randrange(194,256)
 col=random.choice(['#1a302b','#344b35','#526044','#68734c'])
 length=random.randrange(2,8)
 c.line(x,y,min(255,x+length),y,col)
 if i%5==0:c.line(x,y,x-2,max(190,y-4),col)
# background moss ledges
for x,y in [(27,190),(225,184),(12,218),(235,224)]:
 c.poly([(x-12,y+4),(x-9,y-1),(x+4,y-4),(x+12,y),(x+14,y+7),(x-10,y+8)],'#1b302b')
 c.line(x-8,y,x+6,y-2,'#5b7049')
t=new_canvas(256,256,name='Treant')
# Gnarled, angular tapered branch: polygon around a bent centreline, with lit facet.
def branch(points,widths,col='bark1',detail=True):
 left=[];right=[]
 for i,((x,y),w) in enumerate(zip(points,widths)):
  a=points[max(0,i-1)];b=points[min(len(points)-1,i+1)];dx=b[0]-a[0];dy=b[1]-a[1];mag=math.hypot(dx,dy) or 1
  nx=-dy/mag;ny=dx/mag
  left.append((round(x+nx*w),round(y+ny*w)));right.append((round(x-nx*w),round(y-ny*w)))
 outline=left+right[::-1]
 t.poly(outline,P['ink']);t.poly(outline,P['ink'],False)
 inner=[]
 for i,((x,y),w) in enumerate(zip(points,widths)):
  a=points[max(0,i-1)];b=points[min(len(points)-1,i+1)];dx=b[0]-a[0];dy=b[1]-a[1];mag=math.hypot(dx,dy) or 1;nx=-dy/mag;ny=dx/mag
  inner.append((round(x+nx*max(0,w-2)),round(y+ny*max(0,w-2))))
 for i in range(len(points)-1,-1,-1):
  x,y=points[i];w=widths[i];a=points[max(0,i-1)];b=points[min(len(points)-1,i+1)];dx=b[0]-a[0];dy=b[1]-a[1];mag=math.hypot(dx,dy) or 1
  inner.append((round(x+dy/mag*max(0,w-2)),round(y-dx/mag*max(0,w-2))))
 t.poly(inner,P[col])
 if detail:
  for i in range(len(points)-1):
   x,y=points[i];xx,yy=points[i+1];w=widths[i]
   t.line(x-1,y-1,xx-1,yy-1,P['bark3'])
   if w>5:t.line(x+3,y+1,xx+2,yy,P['bark0'])
# tangled rear roots
for pts,ws in [([(110,177),(91,202),(65,213),(37,220)],[16,12,6,0]), ([(145,180),(174,195),(184,216),(222,222)],[18,10,5,0]), ([(104,186),(106,215),(122,237),(142,243)],[12,8,4,0]), ([(153,191),(148,216),(165,234),(183,236)],[14,8,5,0])]:branch(pts,ws,'bark0')
# Crown skeleton: scarred ancient branches reach above the trunk
for pts,ws in [([(110,78),(104,51),(88,34),(81,16),(62,9)],[15,12,8,5,0]), ([(106,53),(116,34),(110,15),(119,4)],[10,7,4,0]), ([(89,35),(69,34),(53,23),(42,24)],[7,5,3,0]), ([(83,22),(89,9),(84,3)],[4,3,0]), ([(139,77),(151,51),(167,35),(175,15),(190,7)],[18,12,7,5,0]), ([(155,49),(153,23),(160,10),(156,3)],[9,6,3,0]), ([(168,35),(189,31),(205,16),(217,17)],[7,5,3,0]), ([(188,31),(196,42),(212,42)],[4,3,0]), ([(117,64),(128,42),(128,22),(136,14)],[10,6,3,0])]:branch(pts,ws)
# limbs in imposing asymmetric pose
branch([(94,111),(72,116),(58,140),(48,160)],[19,17,13,11])
branch([(169,110),(186,119),(203,103),(213,83)],[18,16,12,9])
# projecting elbow spurs
branch([(65,132),(46,126),(39,110)],[9,6,0])
branch([(188,119),(211,126),(224,120)],[8,4,0])
# left hand and dangling twig claws
branch([(49,156),(42,172),(39,182)],[12,12,8])
for pts,ws in [([(34,171),(24,183),(24,198),(32,204)],[5,4,2,0]), ([(40,179),(34,197),(40,211),(47,210)],[5,4,2,0]), ([(47,180),(46,195),(55,204),(61,199)],[5,4,2,0]), ([(51,168),(62,175),(62,188),(57,193)],[5,4,2,0])]:branch(pts,ws)
# raised right claw, spread twig fingers
branch([(211,90),(216,77),(213,67)],[10,11,7])
for pts,ws in [([(208,76),(199,63),(199,49),(206,43)],[5,4,2,0]), ([(212,67),(210,51),(217,38),(225,36)],[5,4,2,0]), ([(220,68),(225,53),(237,48),(242,53)],[5,4,2,0]), ([(222,78),(236,68),(246,71),(246,79)],[5,4,2,0])]:branch(pts,ws)
# Main trunk silhouette: heavy shoulder shelves and rooted hips
body=[(107,59),(120,55),(131,61),(144,55),(154,65),(157,82),(170,92),(181,105),(177,124),(166,137),(165,164),(175,183),(162,200),(145,206),(124,201),(109,207),(89,194),(91,176),(85,157),(91,134),(79,119),(81,100),(96,88),(100,72)]
t.poly(body,P['ink']);t.poly(body,P['ink'],False)
t.poly([(108,63),(119,60),(130,67),(143,60),(150,67),(151,88),(165,96),(175,106),(171,122),(160,137),(160,166),(168,182),(155,196),(143,199),(124,194),(109,201),(96,192),(99,176),(92,157),(98,133),(85,118),(87,103),(101,92)],P['bark1'])
# interlocking plates following growth of the trunk
plates=[('bark0',[(145,68),(150,87),(165,98),(168,120),(153,139),(152,169),(162,184),(146,196),(134,184),(139,151),(131,129),(142,110)]),('bark2',[(106,67),(115,64),(111,86),(100,101),(96,117),(102,137),(100,161),(112,181),(109,196),(98,190),(102,173),(95,155),(101,130),(90,116),(94,102),(106,89)]),('bark3',[(116,65),(121,67),(117,86),(111,94),(108,107),(102,112),(104,98),(111,84)]),('bark2',[(128,70),(135,70),(137,85),(130,106),(135,124),(128,142),(130,166),(142,191),(128,192),(116,177),(118,155),(111,139),(119,120),(117,105),(124,89)]),('bark3',[(124,136),(129,143),(125,160),(130,176),(136,187),(127,183),(121,169)]),('bark2',[(154,94),(165,101),(170,108),(165,119),(155,129),(151,150),(145,157),(145,136),(152,117)]),('bark3',[(90,106),(98,100),(96,108),(92,117),(98,129),(92,124),(87,117)]),('bark0',[(109,148),(114,159),(110,172),(117,186),(117,197),(109,194),(112,183),(104,171)]),('bark3',[(140,69),(145,65),(146,80),(140,95),(137,95),(141,79)])]
for col,pts in plates:t.poly(pts,P[col])
# Major front buttress roots and widely flaring toes
for pts,ws in [([(111,179),(100,199),(88,219),(65,229),(42,230)],[12,12,9,4,0]), ([(103,205),(105,221),(95,239),(83,244)],[8,6,3,0]), ([(88,219),(73,216),(59,222),(50,223)],[6,4,2,0]), ([(144,180),(153,197),(164,213),(184,224),(211,231)],[14,13,10,6,0]), ([(158,209),(153,224),(163,240),(176,244)],[8,7,3,0]), ([(178,221),(195,217),(210,221),(225,219)],[5,4,2,0]), ([(118,192),(124,212),(118,224),(123,231)],[8,6,3,0])]:branch(pts,ws,'bark2')
# Deep vertical bark fissures and growth ridges
for d in ['M 106 74 L 104 90 L 98 98 L 99 104','M 115 68 L 113 82 L 109 89','M 134 66 L 132 82 L 128 88','M 149 73 L 148 88 L 143 101','M 156 100 L 162 107 L 159 119 L 150 131 L 148 145','M 104 130 L 109 142 L 105 154 L 108 162','M 135 136 L 132 149 L 136 161 L 134 174 L 144 184','M 117 141 L 121 152 L 117 164 L 120 173','M 97 147 L 96 157 L 102 170','M 149 158 L 146 171 L 153 182','M 113 186 L 110 199 L 102 212']:
 t.path(d,P['shadow'],False)
# narrow bark chips placed along the growth, confined to woody colours
wood={t.color(P[k]) for k in ['bark0','bark1','bark2','bark3']}
for i in range(490):
 x=random.randrange(28,230);y=random.randrange(20,230)
 if t.get(x,y) in wood:
  ln=random.randrange(2,7);col=random.choice([P['bark0'],P['bark2'],P['bark3']])
  for j in range(ln):
   xx=x+(j//4 if i%2 else -j//4);yy=y+j
   if yy<256 and t.get(xx,yy) in wood:t.set(xx,yy,col)
# Aged knots with angular concentric whorls
def knot(x,y,rx,ry):
 t.poly([(x,y-ry),(x+rx,y-2),(x+rx-1,y+ry-2),(x,y+ry),(x-rx,y+2),(x-rx+1,y-ry+3)],P['bark0'])
 t.path(f'M {x} {y-ry+2} L {x+rx-2} {y-1} L {x+rx-2} {y+ry-3} L {x} {y+ry-1} L {x-rx+2} {y+1}',P['bark3'],False)
 t.line(x,y-2,x-1,y+3,P['ink'])
for data in [(106,150,5,9),(147,155,5,11),(69,126,4,6),(188,114,4,6),(99,202,4,7),(159,204,4,8),(135,78,3,5)]:knot(*data)
# The face is a deep hollow in the living trunk, with overhanging angry brows.
t.poly([(98,96),(103,91),(115,93),(122,100),(118,107),(107,106),(99,102)],P['ink'])
t.poly([(134,100),(140,92),(152,90),(157,95),(153,102),(141,106),(135,105)],P['ink'])
# concentric sickly green illumination kept sharply pixelled
for pts in [[(101,97),(108,96),(118,101),(115,104),(107,102)],[(137,100),(146,95),(154,94),(150,100),(141,103)]]:t.poly(pts,'#365e36')
t.poly([(103,97),(110,98),(117,101),(110,102),(105,100)],'#76c955')
t.poly([(138,100),(146,96),(152,95),(148,99),(141,102)],'#76c955')
t.line(106,98,115,101,P['green']);t.line(140,100,150,96,P['green'])
t.line(108,98,113,100,P['light']);t.line(143,98,148,96,P['light'])
t.set(110,99,'#f1ffcf');t.set(146,97,'#f1ffcf')
# Heavy brows angled down at the centre
t.poly([(97,92),(104,87),(115,90),(124,99),(115,96),(105,93),(98,95)],P['bark2'])
t.path('M 99 91 L 105 89 L 114 92 L 122 98',P['bark4'],False)
t.poly([(132,99),(141,88),(152,86),(158,91),(148,91),(140,95)],P['bark2'])
t.path('M 135 96 L 142 90 L 151 88 L 155 90',P['bark3'],False)
# long twisted nose and gaping splinter-toothed mouth
t.poly([(124,96),(129,96),(129,106),(136,114),(130,118),(119,115),(123,108)],P['bark0'])
t.path('M 125 98 L 125 108 L 122 113 L 128 115',P['bark4'],False)
t.poly([(107,113),(117,118),(126,121),(137,116),(148,109),(146,124),(137,138),(125,143),(113,136),(108,125)],P['ink'])
t.poly([(113,126),(121,131),(128,134),(138,126),(136,135),(126,139),(117,134)],'#283b2c')
# splintered tooth edges
for pts in [[(110,116),(115,119),(116,126),(112,123)],[(119,120),(123,122),(122,129),(120,126)],[(133,120),(138,117),(134,126)],[(142,115),(147,111),(143,124)],[(116,134),(118,128),(121,138)],[(127,140),(129,132),(132,138)],[(135,135),(138,128),(138,132)]]:t.poly(pts,P['bark3'])
t.path('M 107 113 L 109 127 L 115 138 L 124 145 L 133 142 M 148 111 L 147 126 L 140 137',P['bark2'],False)
# layered moss shelves, small leaf clusters with ragged pixel edges
def moss(x,y,rx,ry,seed):
 rr=random.Random(seed)
 t.poly([(x-rx,y),(x-rx+3,y-ry),(x-3,y-ry-2),(x+3,y-ry),(x+rx-3,y-ry+1),(x+rx,y),(x+rx-4,y+3),(x-4,y+2),(x-rx+2,y+4)],P['moss0'])
 for i in range(rx*3):
  xx=x+rr.randrange(-rx+2,rx-1); yy=y+rr.randrange(-ry,2)
  if (xx-x)**2/(rx*rx)+(yy-y)**2/((ry+2)**2)<1:
   col=rr.choice(['moss1','moss1','moss2','moss3'])
   t.rect(xx,yy,rr.randrange(2,5),rr.randrange(1,3),P[col])
 for i in range(max(2,rx//4)):
  xx=x+rr.randrange(-rx+2,rx-1);yy=y-rr.randrange(1,ry+1)
  t.line(xx,yy,xx+2,yy-1,P['moss4'])
for data in [(83,33,18,5,1),(65,26,11,4,2),(113,46,9,5,3),(162,33,12,5,4),(189,29,17,5,5),(141,65,12,5,6),(104,69,13,5,7),(86,104,15,5,8),(166,101,17,6,9),(65,141,10,4,10),(192,121,11,4,11),(101,180,8,4,12),(156,187,9,5,13),(77,223,10,3,14),(177,221,9,3,15)]:moss(*data)
# Hanging vines use broken paired strands and dangling leaves
def vine(pts):
 for (x,y),(xx,yy) in zip(pts,pts[1:]):
  t.line(x+1,y,xx+1,yy,P['moss0']);t.line(x,y,xx,yy,P['moss2'])
 for i in range(1,len(pts)):
  x,y=pts[i];sgn=1 if i%2 else -1
  t.poly([(x,y-2),(x+sgn*4,y-5),(x+sgn*4,y-1),(x,y+2)],P['moss1'])
  t.set(x+sgn*2,y-2,P['moss3'])
for pts in [[(72,32),(70,46),(74,57),(73,70),(69,77)],[(88,36),(85,53),(87,66)],[(181,31),(177,46),(180,60),(176,73),(177,87)],[(194,32),(197,45),(194,58)],[(81,104),(75,120),(78,137),(74,152)],[(172,101),(179,117),(173,133),(174,150),(169,164)],[(60,143),(56,154),(59,164)],[(151,66),(156,75),(155,85)]]:vine(pts)
# Tiny shelf fungi on the oldest scars
for x,y in [(95,162),(152,145),(109,73),(160,176)]:
 t.rect(x,y,6,2,P['shadow']);t.line(x-1,y-1,x+4,y-2,'#bba46b');t.line(x,y,x+5,y,'#82734c')
# Composite the hero into the forest
result=flatten([c,t],name='Ancient Treant Boss')
# A few foreground grasses, dark stones and motes establish scale
for x,y in [(18,239),(33,248),(224,240),(238,252),(9,220),(200,247),(63,250)]:
 result.poly([(x-5,y),(x-3,y-5),(x-1,y-2),(x,y-9),(x+2,y-3),(x+5,y-6),(x+4,y)],'#122a25')
 result.line(x,y-3,x,y-7,'#547047')
for x,y in [(34,223),(219,230),(64,239),(203,209),(22,207)]:
 result.poly([(x-4,y+2),(x-3,y-1),(x+2,y-3),(x+5,y),(x+4,y+3)],'#182c29');result.line(x-2,y-1,x+2,y-2,'#637459')
for x,y in [(31,94),(58,78),(195,156),(220,96),(71,185),(184,71),(44,155),(203,182),(31,175),(231,145)]:
 result.set(x,y,'#8eac68')
 if x%2:result.set(x,y+1,'#536d48')
print(result.stats_text())
print(result.matrix_text(region=(102,94,151,103),indices=True))
# Read the complete silhouette as a compact character map.
lookup={t.color(P['ink']):'#'}
for k in ['bark0','bark1','bark2','bark3','bark4','shadow','cut']:lookup[t.color(P[k])]='B'
for k in ['moss0','moss1','moss2','moss3','moss4']:lookup[t.color(P[k])]='m'
print('TREANT SILHOUETTE (4 pixels per character):')
for y in range(0,256,4):
 row=''
 for x in range(0,256,4):
  cells=[t.get(xx,yy) for yy in range(y,y+4) for xx in range(x,x+4)]
  visible=[a for a in cells if a in lookup]
  row+=lookup[max(set(visible),key=visible.count)] if visible else ' '
 print(row)
save('ancient-treant-boss',result)
finish(result)
