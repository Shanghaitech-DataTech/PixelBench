posed=input_canvas.select(0,0,93,128).rotate(124,algorithm='rotsprite').preview()
posed.mirror('v')
knife=posed.select(3,61,154,32).preview()
result=new_canvas(248,112,name='result')
pal={p['index']:p['rgba'] for p in knife.palette()}
def ghost(dx,dy,alpha):
    g=new_canvas(154,32)
    for y in range(32):
        for x in range(154):
            rgba=pal[knife.get(x,y)]
            if rgba[3]:
                g.set(x,y,(rgba[0],rgba[1],rgba[2],alpha))
    result.blit(g,dx,dy)
ghost(10,18,48)
ghost(38,34,100)
# Fine motion trails emphasize forward travel.
result.line(6,58,40,58,'#bfc9ff45')
result.line(19,62,59,62,'#d9dfff70')
result.line(50,90,97,90,'#d9dfff65')
result.line(71,94,117,94,'#ffffff35')
# A swept, tapering slash follows the underside of the cutting edge.
result.poly([(82,85),(113,89),(158,89),(193,84),(221,72),(240,59),(228,73),(207,85),(179,94),(142,98),(111,95)],'#c7d4ff65')
result.poly([(88,86),(118,90),(154,91),(186,87),(214,77),(240,59),(229,72),(212,83),(187,92),(155,96),(122,94),(102,91)],'#ffffff')
result.poly([(150,98),(181,96),(201,90),(187,97),(169,100)],'#ffffffb0')
result.blit(knife,73,49)
# Detached slivers at the leading end.
result.line(228,52,242,50,'#ffffffb0')
result.line(232,46,238,44,'#ffffff65')
view(result)
finish(result)
