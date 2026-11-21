result = new_canvas(16,16,background='#88502d',name='wooden_planks')
# Four vertical boards, with warm, varied heartwood tones.
pal=[('#a86a39','#c38a4b','#8d532d'),('#91532f','#ae7040','#764128'),('#b47a42','#cf9653','#985f32'),('#9e6033','#b87b40','#824829')]
ends=[3,11,6,14]
for b,(base,light,shade) in enumerate(pal):
    x=b*4
    result.rect(x,0,4,16,base)
    result.rect(x,0,1,16,'#573322')
    result.rect(x+1,0,1,16,light)
    result.rect(x+3,0,1,16,shade)
    y=ends[b]
    # Staggered end joints; highlight below, darker end grain above.
    result.rect(x+1,y,3,1,'#603823')
    result.rect(x+1,(y+1)%16,3,1,light)
    result.set(x+3,(y-1)%16,'#714126')
# Broken, slightly meandering grain lines within each narrow board.
for x,y,h,col in [(2,6,3,'#8d532d'),(2,12,3,'#bd8145'),(3,0,2,'#a86a39'),(6,0,4,'#764128'),(6,7,2,'#c08749'),(7,13,2,'#a86a39'),(10,0,3,'#a36937'),(11,8,3,'#b47a42'),(10,12,3,'#985f32'),(14,2,3,'#824829'),(14,8,3,'#b87b40')]:
    result.rect(x,y,1,h,col)
# Tiny elongated knots interrupt the grain without obscuring the plank rhythm.
result.set(2,9,'#714126')
result.set(1,10,'#9e6033')
result.set(2,10,'#573322')
result.set(3,10,'#ba7b40')
result.set(2,11,'#714126')
result.set(6,5,'#603823')
result.set(6,6,'#4e3022')
result.set(7,6,'#c08749')
result.set(6,7,'#824829')
result.set(14,10,'#714126')
result.set(14,11,'#573322')
result.set(15,11,'#c08749')
result.set(14,12,'#714126')
view(result,scale=20,margin=0)
# A temporary repeated preview checks the seamless material at map scale.
repeat=new_canvas(64,64,name='tiling_preview')
for y in range(0,64,16):
    for x in range(0,64,16):
        repeat.blit(result,x,y)
view(repeat,scale=6,margin=0)
finish(result)
