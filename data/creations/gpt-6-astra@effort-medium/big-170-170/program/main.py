import random
random.seed(23)
output=input_canvas.copy(name='output')
# Clear the projecting arm and coat with adjacent sky and skyline texture.
for y in range(69,123):
    for x in range(73,82):
        output.set(x,y,input_canvas.get(x-12,y))
# Rebuild the illuminated cabinet face, retaining its original side and perspective.
output.poly([(81,59),(112,56),(117,60),(117,146),(81,143)],'c33')
output.line(82,62,82,118,'c190')
output.poly([(84,61),(111,59),(114,61),(114,99),(105,108),(84,108)],'c244')
output.poly([(86,62),(111,60),(113,62),(113,98),(104,106),(86,106)],'c253')
# shelves and stocked drinks
for row,y in enumerate([63,75,87,99]):
    for j,x in enumerate([88,94,100,107]):
        if row==3 and j==3: continue
        colors=[('c163','c238','c117'),('c223','c236','c56'),('c156','c222','c67'),('c194','c214','c80')]
        body,hi,shadow=colors[(j+row)%4]
        output.rect(x,y+2,4,7,body)
        output.line(x+3,y+3,x+3,y+8,shadow)
        output.rect(x+1,y,2,2,'c204')
        output.line(x,y+3,x,y+6,hi)
        output.rect(x+1,y+5,2,2,'c242')
    end=113 if row<3 else 104
    output.line(86,y+10,end,y+10,'c139')
    output.line(86,y+11,end,y+11,'c207')
# lower service panel and recessed delivery slot
output.poly([(84,110),(104,110),(114,100),(114,139),(84,139)],'c34')
output.rect(87,113,16,7,'c9')
output.line(88,113,102,113,'c80')
output.line(88,119,102,119,'c43')
output.rect(108,108,5,7,'c43')
output.rect(110,109,2,2,'c223')
output.line(109,113,111,113,'c190')
# Restore the unoccluded motorcycle in front of the repaired cabinet.
for y in range(115,146):
    for x in range(79,117):
        idx=input_canvas.get(x,y)
        r,g,b,a=input_canvas.palette()[idx]['rgba']
        # lower motorcycle is entirely original; upper edge excludes the old coat and trousers
        if y>=123 or (y>=115 and (b>=r and g>=r or max(r,g,b)<42)):
            output.set(x,y,idx)
# Rebuild the motorcycle side fairing where the rider's lower leg obscured it.
output.poly([(94,128),(108,124),(108,130),(103,135),(96,133)],'c44')
output.line(95,128,107,125,'c74')
output.line(97,130,105,128,'c48')
output.line(100,133,106,130,'c13')
# blue storm ambience, keeping the luminous display warm
shade=new_canvas(170,170)
shade.rect(0,0,170,170,'#08182b32')
shade.rect(84,60,30,48,None)
output=flatten([output,shade],name='storm_scene')
# Forked lightning behind the distant skyline.
bolt=[(65,3),(61,12),(66,17),(58,28),(63,28),(53,42),(58,40),(50,56)]
branches=[[(62,18),(72,23),(69,30),(76,35)],[(57,35),(47,38),(43,46)]]
glow=new_canvas(170,170)
for pts in [bolt]+branches:
    for (x,y),(xx,yy) in zip(pts,pts[1:]):
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:glow.line(x+dx,y+dy,xx+dx,yy+dy,'#7eaedc40')
output=flatten([output,glow])
for pts in [bolt]+branches:
    for a,b in zip(pts,pts[1:]):output.line(*a,*b,'#bddfee' if pts!=bolt else '#e5f8ff')
# Shallow puddles on the pavement, with broken reflections.
for pts in [[(1,157),(21,153),(39,154),(42,158),(25,161),(3,161)],[(116,151),(142,153),(164,157),(157,164),(126,163),(114,158)],[(55,163),(73,160),(86,164),(97,167),(80,169),(48,169)]]:
    output.poly(pts,'#233e50')
for i in range(115):
    x=random.randrange(1,169); y=random.randrange(152,170)
    length=random.randrange(1,7)
    col=random.choice(['#345465','#496579','#263b4c','#688797'])
    if 85<x<134: col=random.choice(['#6c657d','#9c8494','#c1a1a8','#445575'])
    output.line(x,y,min(169,x+length),y,col)
# Small expanding rings and splash crowns.
for x,y in [(13,151),(32,161),(64,157),(141,150),(151,162),(121,165),(8,166),(75,166)]:
    output.line(x-3,y,x-1,y,'#648598');output.line(x+1,y,x+4,y,'#486779')
    output.line(x-1,y+1,x+2,y+1,'#37566b')
    output.set(x,y-2,'#adc9d4')
    output.set(x-2,y-3,'#718e9e')
# Water beads clinging to cabinet and bike edges, with little runnels.
water=new_canvas(170,170)
for x,y in [(119,67),(128,82),(132,109),(119,127),(133,141),(84,69),(116,91),(44,123),(54,119),(67,116),(93,119),(109,139),(76,144),(35,141)]:
    water.line(x,y,x,y+3,'#accfe86c')
    water.set(x,y+4,'#d2f2f8af')
    water.set(x+1,y+3,'#55869c80')
water.line(119,61,130,64,'#b5daf967')
water.line(52,119,65,117,'#d7e8ee80')
# Wind-driven rain in translucent depth layers.
for i in range(245):
    x=random.randrange(2,170); y=random.randrange(0,168)
    length=random.choice([2,3,4,5,7])
    alpha=random.choice([35,48,65,85,105])
    water.line(x,y,max(0,x-length//3),min(169,y+length),(155,198,219,alpha))
    if i%7==0:water.set(max(0,x-length//3),min(169,y+length),(208,235,246,135))
output=flatten([output,water],name='output_final')
view(output,scale=4,margin=0)
finish(output)
