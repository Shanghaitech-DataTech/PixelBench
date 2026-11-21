posed = input_canvas.select(0,0,93,128).rotate(125,algorithm='rotsprite').preview()
posed.mirror('v')
knife = posed.select(3,62,154,30).preview()
result = new_canvas(256,100,name='rightward_thrust')
# Offset silhouettes preserve all of the original knife's pixel colours.
for dx,dy,opacity in [(8,18,0.20),(40,28,0.43)]:
    ghost = new_canvas(154,30)
    palette = {p['index']:p['rgba'] for p in knife.palette()}
    for y in range(30):
        for x in range(154):
            r,g,b,a=palette[knife.get(x,y)]
            if a:
                ghost.set(x,y,(r,g,b,round(a*opacity)))
    result.blit(ghost,dx,dy)
# Narrow, tapering white thrust arcs surround the blade.
result.path('M 52 71 Q 149 83 245 50 Q 200 77 115 78 Z','#dce8ff66')
result.path('M 67 70 Q 169 78 245 50 Q 204 71 145 74 Q 100 76 67 70 Z','#ffffff')
result.path('M 104 33 Q 189 23 245 50 Q 196 28 104 33 Z','#ffffff')
# Broken horizontal speed streaks.
result.rect(14,60,19,1,'#e5eaff55')
result.rect(39,60,24,1,'#e5eaff99')
result.rect(5,52,18,1,'#ffffff55')
result.rect(51,12,29,1,'#e5eaff55')
result.rect(85,12,12,1,'#e5eaff33')
result.blit(knife,80,38)
# Point flare and forward slash taper.
result.poly([(229,49),(249,49),(242,51),(229,52)],'#ffffff')
result.line(237,46,241,43,'#ffffff')
result.set(243,41,'#ffffff99')
view(result)
save('knife_thrust',result)
finish(result)
