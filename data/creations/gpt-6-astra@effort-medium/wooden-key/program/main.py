result = new_canvas(16,16,name='wooden_key')
o='#39271f'
s='#71452d'
w='#ae743e'
h='#e0ac62'
# Stepped carved bow.
result.rect(4,0,5,1,o)
result.rect(3,1,7,1,o)
result.rect(2,2,9,5,o)
result.rect(3,7,7,1,o)
result.rect(4,8,5,1,o)
result.rect(4,1,5,1,h)
result.rect(3,2,7,4,w)
result.rect(3,3,1,3,h)
result.rect(4,6,5,1,w)
result.rect(4,7,5,1,s)
result.rect(9,3,1,3,s)
# Hollow square mortise.
result.rect(5,3,3,3,o)
result.rect(5,3,2,2,None)
result.line(4,2,7,2,h)
result.set(8,6,s)
# Straight shaft and two teeth.
result.rect(5,8,4,8,o)
result.rect(8,10,4,3,o)
result.rect(8,13,5,3,o)
result.rect(6,8,2,7,w)
result.line(6,8,6,14,h)
result.rect(8,11,3,1,w)
result.rect(8,14,4,1,w)
result.set(10,11,h)
result.set(11,14,h)
# Cut grain interrupts the long face.
result.set(7,10,s)
result.line(7,13,7,14,s)
view(result)
finish(result)
