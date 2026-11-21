result = new_canvas(16,16,background='#85502d',name='wooden_planks')
# Four narrow planks, staggered cross joints; vertical edges repeat.
bases=['#a56b39','#bd8247','#975c32','#b57840']
lights=['#bd8246','#d29755','#b7773e','#cc8e4d']
darks=['#8b512d','#a16837','#804829','#995c30']
joints=[3,11,6,14]
for b in range(4):
    x=b*4
    result.rect(x,0,1,16,'#513321')
    result.rect(x+1,0,3,16,bases[b])
    for y in range(16):
        result.set(x+1,y,lights[b])
        if (y+b*3)%9<5:
            result.set(x+3,y,darks[b])
    j=joints[b]
    result.rect(x+1,j,3,1,'#613b24')
    result.rect(x+1,(j+1)%16,3,1,lights[b])
    result.set(x+3,(j-1)%16,'#754428')
# Broken grain follows the length of the boards.
for x,y,col in [(2,0,'#b77b41'),(2,1,'#b77b41'),(2,7,'#92542c'),(2,8,'#92542c'),(2,13,'#c08647'),(2,14,'#c08647'),(6,1,'#ad6e37'),(6,2,'#ad6e37'),(6,3,'#ad6e37'),(6,13,'#c88c4b'),(10,0,'#a86b37'),(10,1,'#a86b37'),(10,10,'#874b29'),(10,11,'#874b29'),(10,12,'#874b29'),(14,0,'#c78a49'),(14,1,'#c78a49'),(14,9,'#a26633'),(14,10,'#a26633'),(14,11,'#a26633')]:
    result.set(x,y,col)
# Two pin knots with a dark heart and a curved light lip.
result.set(6,6,'#97572b')
result.set(5,7,'#ab6c35')
result.set(6,7,'#633b24')
result.set(7,7,'#d29755')
result.set(6,8,'#94542b')
result.set(6,9,'#cf9050')
result.set(14,4,'#99592d')
result.set(13,5,'#a66a35')
result.set(14,5,'#633b24')
result.set(15,5,'#cc8e4d')
result.set(14,6,'#99592d')
result.set(14,7,'#cc8e4d')
view(result,scale=24)
finish(result)
