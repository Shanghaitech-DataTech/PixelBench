result = new_canvas(64, 64, background='#11152d', name='pixel_quest')
c = result
# A quiet, framed night-sky backdrop.
c.rect(0, 0, 64, 28, '#171b38')
c.rect(0, 28, 64, 22, '#14182f')
c.rect(0, 50, 64, 14, '#10152a')
for x,y,dx,dy in [(1,1,1,1),(62,1,-1,1),(1,62,1,-1),(62,62,-1,-1)]:
    c.line(x,y,x+11*dx,y,'#33445b')
    c.line(x,y,x,y+11*dy,'#33445b')
    c.set(x+2*dx,y+2*dy,'#66a2a4')
for x,y in [(7,9),(55,10),(4,25),(59,24),(8,48),(56,48),(17,5),(46,5)]:
    c.set(x,y,'#41546a')
# Tiny gem and rules crown the title.
c.line(23,7,27,7,'#355465')
c.line(36,7,40,7,'#355465')
c.poly([(31,3),(35,7),(31,11),(28,7)], '#223d53')
c.poly([(31,4),(34,7),(31,10),(29,7)], '#4ba7b0')
c.line(31,5,31,8,'#bcf2d7')
c.set(30,6,'#bcf2d7')
# Custom bitmap lettering, rendered as solid pixel clusters.
glyphs = {
'P':['11110','10001','10001','11110','10000','10000','10000'],
'I':['11111','00100','00100','00100','00100','00100','11111'],
'X':['10001','10001','01010','00100','01010','10001','10001'],
'E':['11111','10000','10000','11110','10000','10000','11111'],
'L':['10000','10000','10000','10000','10000','10000','11111'],
'Q':['01110','10001','10001','10001','10101','10010','01101'],
'U':['10001','10001','10001','10001','10001','10001','01110'],
'S':['01111','10000','10000','01110','00001','00001','11110'],
'T':['11111','00100','00100','00100','00100','00100','00100'],
}
def title(word, x, y, w, h, gap, colors, edge, shade):
    points=set()
    for i,letter in enumerate(word):
        for yy in range(h):
            for xx in range(w):
                if glyphs[letter][yy*7//h][xx*5//w]=='1':
                    points.add((x+i*(w+gap)+xx,y+yy))
    for px,py in points:
        for ox,oy in [(0,0),(-1,0),(1,0),(0,-1),(0,1)]:
            c.set(px+ox+1,py+oy+2,shade)
    for px,py in points:
        for ox,oy in [(-1,0),(1,0),(0,-1),(0,1)]:
            c.set(px+ox,py+oy,edge)
    for px,py in points:
        col=colors[min(len(colors)-1,(py-y)*len(colors)//h)]
        c.set(px,py,col)
    # Fine top-facing highlights give each stroke a cut-stone edge.
    for px,py in points:
        if (px,py-1) not in points:
            c.set(px,py,colors[0])

title('PIXEL',10,15,7,10,2,
      ['#e6f6d4','#b7e0c4','#7db9b3'], '#274557','#080e22')
title('QUEST',3,30,10,14,2,
      ['#fff1b0','#ffd577','#f4ad56','#da7844'], '#713c3c','#080d20')
# A small divider and a readable menu prompt.
c.line(21,49,28,49,'#33445b')
c.line(35,49,42,49,'#33445b')
c.set(31,48,'#6d8790')
c.set(30,49,'#6d8790')
c.set(32,49,'#6d8790')
c.set(31,50,'#6d8790')
c.poly([(11,54),(14,56),(11,59)], '#f4ad56')
c.text(18,54,'START','#b7cbd0')
view(result)
save('pixel_quest', result)
finish(result)
