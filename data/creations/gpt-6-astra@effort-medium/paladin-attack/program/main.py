f1=new_canvas(80,78,name='ready')
f1.blit(input_canvas,9,6)
f2=new_canvas(80,78,name='heavy_attack')
# Broad, tapering arc following the hammer's descent.
f2.path('M 36 6 C 61 5 77 21 74 40 C 73 47 69 52 63 56 L 59 51 C 69 42 70 32 64 22 C 58 13 48 8 36 6 Z','#ffffff')
f2.path('M 48 9 C 64 15 71 27 70 39 C 69 44 67 47 64 49 L 65 44 C 70 29 62 17 48 9 Z','#ffffd5')
f2.path('M 63 12 Q 77 23 77 35', '#ffffff',fill=False)
f2.line(73,45,70,50,'#ffffff')
# Repose the original detailed armour, preserving its palette and pixel clusters.
for y in range(61):
 for x in range(43):
  idx=input_canvas.get(x,y)
  rgba=input_canvas.palette()[idx]['rgba'] if False else None
  # Remove the raised hammer and raised forearm.
  if y<8: continue
  if y<12 and x>=22: continue
  if y<23 and x>=29: continue
  if y<25 and x>=33: continue
  dx=0; dy=0
  # Head, shoulders and breastplate lean into the blow.
  if y<30 and x>=10: dx=2; dy=2
  elif y<37 and x>=17: dx=1; dy=1
  # Left leg plants forward, with its boot lowered and extended.
  if (41<=y<49 and 25<=x<=30) or (y>=49 and x>=26): dx=5; dy=4
  f2.set(x+9+dx,y+6+dy,idx)
# Lowered upper arm and elbow, in matching steel and gold.
f2.poly([(39,29),(43,30),(46,35),(45,39),(40,39),(37,35)],'#101010')
f2.poly([(40,30),(43,32),(44,35),(41,37),(38,34)],'#858086')
f2.line(40,30,43,33,'#dccaca')
f2.poly([(39,35),(42,35),(45,38),(43,41),(39,39),(37,37)],'#332d32')
f2.line(38,36,42,39,'#ffcc43')
f2.line(39,35,43,38,'#ffe38c')
# Long haft continues through the gauntlet to the lowered hammer head.
f2.line(38,31,61,53,'#101010')
f2.line(37,32,60,54,'#101010')
f2.line(39,31,62,53,'#101010')
f2.line(38,32,61,54,'#512a13')
f2.line(39,32,61,53,'#af7a18')
f2.line(45,38,61,53,'#d1b563')
# Fingers over the handle.
f2.poly([(40,33),(43,33),(46,36),(45,39),(42,39),(39,36)],'#101010')
f2.poly([(40,34),(43,34),(45,36),(44,38),(42,37)],'#a9a5ab')
f2.line(41,34,44,36,'#ffffff')
f2.line(41,36,43,38,'#5a565a')
# The original hammer head, turned across the impact direction.
head=new_canvas(12,11,name='hammer_part')
for y in range(11):
 for x in range(17,29):
  if y>=8 and x<22: continue
  head.set(x-17,y,input_canvas.get(x,y))
head.select(0,0,12,11).rotate(90).copy_to(57,48,f2,mode='over')
view(f1,scale=6)
view(f2,scale=6)
finish([f1,f2])
