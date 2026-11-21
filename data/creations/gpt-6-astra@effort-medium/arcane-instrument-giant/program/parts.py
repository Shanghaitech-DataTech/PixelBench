def gear(c,x,y,r,teeth,brass,ink):
 import math
 pts=[]
 for i in range(teeth*4):
  a=i*2*math.pi/(teeth*4);rr=r if i%4 in (1,2) else r-3
  pts.append((round(x+rr*math.cos(a)),round(y+rr*math.sin(a))))
 c.poly(pts,ink);c.poly(pts,brass[2],False)
 c.circle(x,y,r-4,brass[1]);c.circle(x,y,r-6,ink)
 for a in range(0,360,60):
  t=math.radians(a);c.line(x,y,round(x+(r-6)*math.cos(t)),round(y+(r-6)*math.sin(t)),brass[3])
 c.circle(x,y,4,brass[3]);c.circle(x,y,2,ink);c.set(x-1,y-1,brass[5])
