result = new_canvas(16,16)
outline='#38251f'
shadow='#70432b'
wood='#aa6b36'
light='#d49a52'
shine='#f0c47a'
# Carved bow and diagonal shaft, with two teeth at the lower end.
result.poly([(3,1),(6,1),(8,3),(8,6),(7,7),(13,13),(12,15),(10,15),(9,13),(7,13),(7,11),(5,9),(3,9),(1,7),(0,5),(1,3)],outline)
result.poly([(3,2),(6,2),(7,3),(7,6),(5,8),(3,8),(1,6),(1,4)],wood)
result.line(2,3,3,2,shine)
result.line(3,2,5,2,light)
result.line(1,4,1,5,light)
result.line(3,7,5,7,shadow)
result.line(6,6,6,4,shadow)
# Opening through the wooden bow.
result.rect(3,4,3,2,outline)
result.set(4,3,outline)
result.set(4,4,None)
result.set(4,5,None)
result.set(3,5,None)
# Shaft face and darker grain edge.
result.line(6,7,12,13,wood)
result.line(6,8,11,13,shadow)
result.line(7,8,11,12,light)
result.set(7,11,wood)
result.set(8,12,light)
result.set(10,13,wood)
result.set(11,14,light)
result.set(12,13,light)
view(result)
finish(result)
