# PIXEL QUEST — a compact adventure title screen.
result = new_canvas(64, 64, background='#101426', name='pixel_quest')
c = result

# Quiet, stepped midnight backdrop.
c.rect(4, 4, 56, 46, '#151c33')
c.rect(8, 7, 48, 37, '#19213c')
c.rect(13, 10, 38, 29, '#1c2542')
c.rect(2, 48, 60, 14, '#101426')

# Recessed frame, open around the corners.
c.line(6, 1, 57, 1, '#2d3b53')
c.line(6, 62, 57, 62, '#2d3b53')
c.line(1, 6, 1, 57, '#2d3b53')
c.line(62, 6, 62, 57, '#2d3b53')
for x, y, sx, sy in [(2,2,1,1),(61,2,-1,1),(2,61,1,-1),(61,61,-1,-1)]:
    c.line(x,y,x+4*sx,y,'#648084')
    c.line(x,y,x,y+4*sy,'#648084')
    c.set(x+sx,y+sy,'#c4ba8b')

# A small crest and a few deliberately sparse stars.
c.line(23,5,27,5,'#385664')
c.line(36,5,40,5,'#385664')
c.poly([(31,2),(34,5),(31,8),(28,5)],'#304c64')
c.poly([(31,3),(33,5),(31,7),(29,5)],'#5fc3bf')
c.line(30,4,31,3,'#daf4d5')
c.set(31,6,'#277f95')
for x,y in [(7,7),(55,8),(4,22),(60,22),(8,43),(56,43),(5,49),(58,49)]:
    c.set(x,y,'#48607a')
c.line(58,12,58,16,'#4e7990')
c.line(56,14,60,14,'#4e7990')
c.set(58,14,'#a3c9c5')
c.set(5,31,'#38516a')

# Faint distant terrain keeps the lower UI grounded in an adventure world.
c.poly([(3,49),(10,42),(16,47),(24,43),(33,50),(42,44),(48,47),(56,41),(61,46),(61,61),(3,61)],'#1b2940')
c.poly([(3,54),(13,48),(21,52),(31,47),(41,53),(51,48),(61,52),(61,61),(3,61)],'#152035')
# Small silhouetted pines.
for x,y in [(6,49),(57,48)]:
    c.line(x,y-5,x,y+3,'#0f192d')
    c.poly([(x,y-6),(x-2,y-2),(x-1,y-2),(x-3,y+1),(x+3,y+1),(x+1,y-2),(x+2,y-2)],'#0f192d')

# Hand-set bitmap glyphs, with independent horizontal and vertical metrics.
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
def word_pixels(word, x, y, widths, heights, gap):
    points=set()
    for char in word:
        yy=y
        for row, hh in zip(glyphs[char], heights):
            xx=x
            for v, ww in zip(row,widths):
                if v=='1':
                    for dy in range(hh):
                        for dx in range(ww):
                            points.add((xx+dx,yy+dy))
                xx+=ww
            yy+=hh
        x+=sum(widths)+gap
    return points

def embossed(points, y, height, ramps, shine, shade, side):
    # A hard pixel outline and two-pixel cast extrusion preserve each counter.
    silhouette=set()
    for dx,dy in [(0,0),(1,1),(1,2)]:
        silhouette.update((x+dx,yy+dy) for x,yy in points)
    for x,yy in silhouette:
        for dx,dy in [(0,-1),(0,1),(-1,0),(1,0)]:
            c.set(x+dx,yy+dy,'#090f20')
    for x,yy in points:
        c.set(x+1,yy+2,side)
        c.set(x,yy+1,side)
    for x,yy in points:
        k=min(len(ramps)-1,(yy-y)*len(ramps)//height)
        col=ramps[k]
        if (x,yy-1) not in points:
            col=shine if yy-y<height//2 else ramps[max(0,k-1)]
        elif (x,yy+1) not in points:
            col=shade
        c.set(x,yy,col)

# PIXEL: airy, smaller and cool. QUEST: broad, heavier and warm.
pixel=word_pixels('PIXEL',8,11,[2,1,2,1,2],[2,1,2,1,2,1,2],2)
# Optical correction gives the X the same stroke weight as its neighbours.
pixel={(x,y) for x,y in pixel if not 28 <= x < 36}
x_rows=['11000011','11000011','01100110','01100110','00111100','00011000','00111100','01100110','01100110','11000011','11000011']
for yy,row in enumerate(x_rows):
    pixel.update((28+xx,11+yy) for xx,v in enumerate(row) if v=='1')
embossed(pixel,11,11,['#d9f4e5','#a5e2d3','#6cbcbf'], '#f0f7db','#408399','#26445d')
quest=word_pixels('QUEST',3,27,[2]*5,[2]*7,2)
embossed(quest,27,14,['#ffe8a3','#ffc75c','#f2a440','#e47b36'], '#fff3cd','#c8793d','#68384b')

# A tiny horizontal sword forms the title's underline.
c.line(19,46,44,46,'#090f20')
c.line(20,45,42,45,'#627b8b')
c.line(21,46,42,46,'#aec5c1')
c.line(25,45,42,45,'#e1e9cd')
c.poly([(42,45),(46,45),(42,47)],'#aec5c1')
c.line(16,45,21,45,'#b28051')
c.line(16,46,21,46,'#664354')
c.set(15,45,'#edd18a')
c.line(22,43,22,48,'#c99959')
c.set(22,43,'#ffe6a2')
c.set(23,44,'#754954')
c.set(21,47,'#754954')

# Quiet, clean menu lettering.
c.rect(10,51,44,9,'#101426')
c.poly([(12,54),(15,56),(12,58)],'#f7c46a')
c.text(20,53,'START','#acc3c6')

view(result, scale=8, margin=0)
save('pixel_quest', result)
finish(result)
