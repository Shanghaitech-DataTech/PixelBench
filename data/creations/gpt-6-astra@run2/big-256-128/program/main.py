import math, random
random.seed(14)
result=input_canvas.copy(name='output')
pal=input_canvas.palette()
# Recast the existing tonal artwork into a deep wine, ash and ember palette.
for y in range(128):
 for x in range(256):
  r,g,b,a=pal[input_canvas.get(x,y)]['rgba']
  lum=(r*0.25+g*0.55+b*0.2)/255
  warm=r>b*1.12 and r>g*1.05
  if warm:
   col=(int(22+lum*162),int(13+lum*62),int(22+lum*54))
  else:
   col=(int(10+lum*147),int(8+lum*53),int(17+lum*69))
  result.set(x,y,col)
# The original moon, now a red hanging disc with an irregular dark corona.
result.circle(128,22,16,'#371321')
result.circle(128,22,14,'#7c1725')
result.circle(128,22,12,'#b82f32')
result.circle(127,21,10,'#d94b43')
result.circle(126,19,7,'#e56350')
# mottled lunar surface
for x,y,w,h,c in [(119,16,5,2,'#c83b37'),(122,13,5,2,'#d14a3e'),(130,16,5,2,'#bd3436'),(133,20,3,3,'#be3435'),(120,23,4,2,'#c03a36'),(124,27,5,2,'#c43a38'),(131,25,4,2,'#cf4139'),(116,20,3,2,'#d64a3c'),(125,18,3,1,'#f07b5a')]: result.rect(x,y,w,h,c)
# Central needle and darker crown maintain the castle's original silhouette.
result.poly([(125,48),(126,38),(127,30),(128,23),(129,30),(130,38),(131,48)],'#21131b')
result.line(128,24,128,40,'#d96c50')
result.poly([(124,54),(122,47),(121,40),(124,44),(126,48),(127,53)],'#1d1019')
result.poly([(130,53),(132,47),(134,40),(133,48),(132,55)],'#1d1019')
result.line(123,44,125,49,'#a14b43')
result.line(133,43,131,49,'#a14b43')
# Spiked rooflines and ominous banners among the original towers.
for x,y in [(104,78),(114,72),(141,70),(151,80),(95,90),(159,91)]:
 result.poly([(x-3,y+5),(x,y-4),(x+3,y+5)],'#1b101a')
 result.line(x,y-4,x,y-8,'#27111a')
 result.set(x,y-8,'#d6543b')
for x,y in [(111,69),(146,67)]:
 result.line(x,y-12,x,y+1,'#1a1019')
 result.poly([(x+1,y-11),(x+8,y-9),(x+5,y-7),(x+8,y-5),(x+1,y-6)],'#8d202c')
 result.line(x+1,y-10,x+5,y-9,'#c5473c')
# Burning windows and braziers, scattered over the fortress.
for x,y in [(111,81),(116,84),(124,71),(132,75),(138,82),(146,84),(105,88),(120,91),(129,89),(139,92),(151,92),(100,98),(156,99),(115,101),(133,102),(147,103),(92,106),(162,106)]:
 result.rect(x,y,2,3,'#e75036')
 result.set(x,y,'#ffb15e')
# Gate cut into the lower citadel.
result.rect(124,105,10,15,'#160e17')
result.poly([(124,105),(129,100),(133,105)],'#160e17')
result.line(126,105,129,102,'#aa4238')
result.line(129,102,132,105,'#aa4238')
result.line(126,107,126,117,'#69303a')
result.line(132,107,132,117,'#69303a')
# Fine red embers in the air.
for i in range(90):
 x=random.randrange(256); y=random.randrange(12,110)
 if 105<x<151 and 15<y<105: continue
 if random.random()<0.65: result.set(x,y,random.choice(['#9e3038','#c94a3c','#e7784c']))
view(result)
finish(result)
