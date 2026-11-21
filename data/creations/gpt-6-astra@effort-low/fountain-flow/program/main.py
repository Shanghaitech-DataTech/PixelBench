result=input_canvas.copy(name='output')
shade='#167d9b'
water='#38bdd5'
light='#8ce7ec'
white='#d9ffff'
# Water bubbling around the central nozzle.
result.line(31,2,31,8,water)
result.line(32,1,32,7,light)
result.set(32,0,white)
result.poly([(30,3),(28,4),(27,7),(27,9),(28,9),(29,6),(31,5)],water)
result.line(28,4,29,3,light)
result.poly([(33,3),(35,4),(37,7),(37,10),(36,10),(35,7),(33,5)],water)
result.set(35,4,light)
result.set(26,6,light)
result.set(38,8,light)
# Narrow ribbons pour from each tier, keeping the carved rims visible.
def stream(x,y,end,drift=0):
    result.line(x,y,x+drift,end,shade)
    result.line(x+1,y,x+1+drift,end,water)
    result.line(x+2,y+1,x+2+drift,end-1,light)
    result.set(x+1,y,white)
    result.line(x+drift-2,end+1,x+drift+4,end+1,water)
    result.line(x+drift,end,x+drift+2,end,white)
    result.set(x+drift-2,end-1,light)
    result.set(x+drift+4,end-2,light)
stream(24,13,20,-1)
stream(38,13,20,1)
stream(19,23,29,-1)
stream(43,23,29,1)
# Longer falls arc out from the broad bowl into the reservoir.
result.poly([(15,32),(17,32),(17,37),(16,43),(15,49),(15,53),(12,53),(13,47),(14,41),(15,36)],shade)
result.path('M16 33 L16 38 L15 44 L14 49 L14 53',light,fill=False)
result.path('M15 34 L15 39 L14 45 L13 50 L13 53',water,fill=False)
result.set(16,33,white)
result.poly([(47,32),(49,32),(49,37),(50,43),(51,49),(51,53),(48,53),(48,48),(47,42)],shade)
result.path('M48 33 L48 38 L49 44 L50 50 L50 53',water,fill=False)
result.path('M49 34 L49 39 L50 45 L51 50 L51 52',light,fill=False)
result.set(48,33,white)
for x,y in [(14,54),(50,54)]:
    result.line(x-3,y,x+3,y,water)
    result.line(x-2,y+1,x+2,y+1,light)
    result.line(x-1,y-1,x+1,y-1,white)
    result.set(x-3,y-2,light)
    result.set(x+3,y-3,light)
    result.set(x-1,y-4,water)
# Ripples catch the light around the incoming water.
for x,y,w in [(26,10,3),(33,11,3),(27,20,4),(33,28,4),(23,30,3),(23,56,5),(35,57,5),(19,52,3)]:
    result.line(x,y,x+w,y,light)
view(result)
finish(result)
