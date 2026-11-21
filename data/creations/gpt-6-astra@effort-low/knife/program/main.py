knife=input_canvas.select(0,0,93,128).rotate(122,algorithm='rotsprite').preview()
knife.mirror('v')
sprite=knife.select(3,59,153,34).preview()
result=new_canvas(260,116,name='knife_thrust')
# Earlier positions fade away toward the upper left.
for dx,dy,alpha in [(9,18,48),(43,32,98)]:
    ghost=new_canvas(153,34)
    w,h,rgba=sprite.to_rgba()
    for y in range(h):
        for x in range(w):
            i=(y*w+x)*4
            r,g,b,a=rgba[i:i+4]
            if a:
                ghost.set(x,y,(r,g,b,alpha))
    result.blit(ghost,dx,dy)
# Tapered speed trails and a sweeping white slash under the blade.
result.poly([(7,67),(100,64),(177,64),(101,68)],'#dce5ff70')
result.poly([(29,86),(113,83),(179,77),(226,65),(248,57),(232,71),(192,86),(140,96),(85,97)],'#bdcaff65')
result.poly([(27,87),(100,88),(151,84),(197,75),(231,64),(251,55),(237,68),(203,81),(153,92),(100,95),(60,93)],'#ffffff')
result.poly([(97,99),(148,95),(194,86),(176,93),(139,100)],'#e5ecffb0')
result.blit(sprite,88,46)
# Sharp thrust streak, ending just beyond the point.
result.poly([(218,62),(255,61),(243,64),(220,64)],'#ffffff')
result.line(25,58,64,58,'#e4ebff80')
result.line(3,76,39,76,'#ffffff90')
result.line(53,104,91,104,'#c5d4ff60')
view(result)
finish(result)
