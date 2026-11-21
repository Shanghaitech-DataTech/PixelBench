result = new_canvas(16, 16, background='#986039', name='wooden_planks')
# Four narrow boards; grooves remain continuous across repeated tile edges.
seam = '#4b3025'
dark = '#75472d'
mid = '#986039'
light = '#b57b46'
hi = '#c58c53'
# Slightly different timber values distinguish neighboring boards.
boards = [('#ad7443','#bf874e',3),('#925a35','#ab7041',11),('#b17a49','#c38b54',7),('#99613a','#b17a47',15)]
for i,(base,edge,end) in enumerate(boards):
    x=i*4
    result.rect(x,0,3,16,base)
    result.line(x,0,x,15,edge)
    result.line(x+3,0,x+3,15,seam)
    # Staggered end joints, with warm worn endgrain on one lip.
    result.line(x,end,x+2,end,'#603c29')
    result.line(x,(end+1)%16,x+2,(end+1)%16,edge)
    result.set(x+2,(end-1)%16,dark)
# Long broken grain strokes, flowing vertically.
for x,y,length,col in [(2,5,3,'#925a35'),(1,0,2,'#986039'),(2,13,3,'#925a35'),(5,2,4,'#805032'),(6,6,3,'#75472d'),(5,13,2,'#805032'),(10,0,2,'#986039'),(9,9,3,'#986039'),(10,12,3,'#986039'),(14,1,4,'#805032'),(13,5,2,'#805032'),(14,9,4,'#805032')]:
    result.line(x,y,x,y+length-1,col)
# Tiny knots: tapered grain, a dark heart and a warm lower rim.
result.set(1,8,'#925a35')
result.set(0,9,'#986039')
result.set(2,9,'#75472d')
result.set(1,10,'#603c29')
result.set(0,10,'#986039')
result.set(2,11,'#c58c53')
result.set(1,12,'#925a35')
result.set(9,2,'#986039')
result.set(8,3,'#ad7443')
result.set(10,3,'#805032')
result.set(9,4,'#603c29')
result.set(10,5,'#c58c53')
result.set(9,6,'#986039')
view(result, scale=24, margin=0)
# Independent swatch for checking seams in both directions.
swatch = new_canvas(48,48,name='tiling_preview')
for yy in range(3):
    for xx in range(3):
        swatch.blit(result,16*xx,16*yy)
view(swatch, scale=8, margin=0)
finish(result)
