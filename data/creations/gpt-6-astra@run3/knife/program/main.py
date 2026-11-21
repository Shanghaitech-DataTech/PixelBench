posed=input_canvas.select(0,0,93,128).rotate(125,algorithm='rotsprite').preview()
knife=posed.select(3,58,154,30).flip('v').preview()
result=new_canvas(250,112,name='thrust')
# Two fading previous positions retain the original knife's colours.
pal={p['index']:p['rgba'] for p in knife.palette()}
def echo(dx,dy,opacity):
    ghost=new_canvas(154,30)
    for y in range(30):
        for x in range(154):
            r,g,b,a=pal[knife.get(x,y)]
            if a: ghost.set(x,y,(r,g,b,round(a*opacity)))
    result.blit(ghost,dx,dy)
echo(12,17,0.20)
echo(43,31,0.40)
# Fine, broken speed trails.
result.line(7,56,36,56,'#ccd3f83c')
result.line(25,60,67,60,'#ccd3f870')
result.line(48,77,88,77,'#e9efffa0')
result.line(15,77,35,77,'#ccd3f842')
result.line(88,16,122,16,'#e9efff48')
# Sweeping slash below the cutting edge, tapering into the thrust point.
result.path('M 28 90 Q 109 101 195 80 Q 223 72 242 57 Q 223 82 189 89 Q 102 108 28 90 Z','#dbe5ff42')
result.path('M 38 90 Q 124 96 198 76 Q 226 68 242 57 Q 225 77 197 83 Q 117 102 38 90 Z','#ffffff')
result.path('M 55 88 Q 131 89 192 72 Q 216 66 231 62', '#f4f8ffb0',fill=False)
result.blit(knife,78,44)
# A narrow extension carries the tip's momentum to the right.
result.poly([(230,57),(245,56),(235,60)],'#ffffff')
view(result)
save('knife_thrust',result)
finish(result)
