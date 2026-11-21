result = new_canvas(16,16,background='#92532e',name='wooden_planks')
# Four narrow boards: warm alternating heartwood tones.
pal = [('#a56636','#c08749','#784227'),('#bb7b40','#d69b55','#94562e'),('#96532d','#ba7540','#713b26'),('#b1733b','#cd914d','#8b4b29')]
ends=[3,11,6,14]
for i,(base,light,shade) in enumerate(pal):
    x=i*4
    result.rect(x,0,1,16,'#4b2d23')
    result.rect(x+1,0,3,16,base)
    # Thin warm bevel and recessed right edge.
    result.line(x+1,0,x+1,15,light)
    result.line(x+3,0,x+3,15,shade)
    y=ends[i]
    result.line(x+1,y,x+3,y,'#573121')
    result.line(x+1,(y+1)%16,x+3,(y+1)%16,light)
    result.set(x+2,(y-1)%16,shade)
# Broken grain strands follow the length of each board.
for x,y,h,col in [(2,7,4,'#8a4a29'),(2,13,3,'#b87840'),(6,0,4,'#ac6835'),(6,7,3,'#9f5a2f'),(10,9,4,'#864325'),(10,0,2,'#ab6537'),(14,6,4,'#a36332'),(14,0,3,'#bd8142')]:
    result.rect(x,y,1,h,col)
# Tiny elongated knots, with dark hearts and warm lower rims.
for x,y,glow in [(2,6,'#cf8d49'),(10,3,'#c17e43'),(14,11,'#d0934c')]:
    result.set(x,y-1,'#774026')
    result.set(x-1,y,'#90502b')
    result.set(x,y,'#593123')
    result.set(x,y+1,'#784027')
    result.set(x,y+2,glow)
view(result,scale=24,margin=0)
finish(result)
