from pixelbench_api import *
c = new_canvas(64,64)
CX,CY=32,34
pts=[(0,23),(-8,15),(-19,8),(-20,-4),(-21,-12),(-15,-19),(-8,-19),(-3,-19),(-1,-16),(0,-12),(1,-16),(3,-19),(8,-19),(15,-19),(21,-12),(20,-4),(19,8),(8,15),(0,23)]
def hp(s,dx=0,dy=0):
    P=[(round(CX+ox*s+dx),round(CY+oy*s+dy)) for ox,oy in pts]
    d="M %d %d"%P[0]
    for i in range(1,19,3):
        d+=" C %d %d, %d %d, %d %d"%(P[i][0],P[i][1],P[i+1][0],P[i+1][1],P[i+2][0],P[i+2][1])
    d+=" Z"; return d
c.path(hp(1.0),"#a01010")
s=c.stats(); print("after base",s["top_colors"])
c.path(hp(0.8,-2,-2),"#c41f1f")
s=c.stats(); print("after mid",s["top_colors"])
c.path(hp(0.6,-4,-3),"#e23636")
s=c.stats(); print("after light",s["top_colors"])
c.path(hp(0.4,-5,-4),"#f27878")
s=c.stats(); print("after pink",s["top_colors"])
print(c.matrix_text(region=(10,10,54,58)))
