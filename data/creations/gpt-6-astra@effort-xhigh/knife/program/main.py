# Preserve the source's shading and wrapped grip while posing it horizontally.
pose = input_canvas.select(0,0,93,128).flip('h').rotate(56,algorithm='rotsprite').preview()
knife = pose.select(3,61,154,32).preview()
W,H = 264,128
trail = new_canvas(W,H,name='afterimages')
rgba = knife.to_rgba()[2]
# Earlier positions, increasingly faint as the blade recedes to the left.
for dx,dy,opacity in [(10,34,0.22),(43,49,0.43)]:
    ghost = new_canvas(W,H)
    for y in range(32):
        for x in range(154):
            i = (y*154+x)*4
            r,g,b,a = rgba[i:i+4]
            if a:
                # A restrained cool tint keeps the dark grip visible in the trail.
                r = round(r*0.78+157*0.22)
                g = round(g*0.78+177*0.22)
                b = round(b*0.78+225*0.22)
                ghost.set(x+dx,y+dy,(r,g,b,round(a*opacity)))
    trail.blit(ghost,0,0)
# Sparse, horizontal speed accents around the older positions.
trail.line(4,71,25,71,'#cbd3fa38')
trail.line(16,75,33,75,'#cbd3fa55')
trail.line(31,85,58,85,'#dfe6ff70')
trail.line(40,89,64,89,'#dfe6ff45')
body = new_canvas(W,H,name='knife')
body.blit(knife,80,64)
# Tapered arc follows the lower cutting edge and snaps toward the thrust.
fx = new_canvas(W,H,name='slash')
fx.path('M 29 108 Q 87 118 168 108 Q 216 102 248 77 Q 223 107 172 116 Q 91 126 29 108 Z','#dbe4ff48')
fx.path('M 36 107 Q 99 115 166 105 Q 218 97 248 77 Q 220 103 169 111 Q 98 120 36 107 Z','#ffffff')
# Fine leading streak, and a pair of small detached flecks.
fx.path('M 199 85 Q 229 83 251 76', '#ffffff',fill=False)
fx.line(23,104,31,106,'#ffffffb0')
fx.line(61,117,82,119,'#edf1ff78')
composite = flatten([trail,body,fx],name='composite')
result = new_canvas(W,104,name='rightward_thrust')
composite.select(0,22,W,104).copy_to(0,0,result)
view(result,scale=3)
save('knife_rightward_thrust',result)
finish(result)
