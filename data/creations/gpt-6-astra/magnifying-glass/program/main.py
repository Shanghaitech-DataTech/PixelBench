result = new_canvas(16,16,name='magnifying_glass')
# Dark silhouette of a round lens and diagonal grip.
ink='#232736'
rim='#9b6944'
gold='#deb56a'
light='#ffe1a0'
result.poly([(4,1),(8,1),(10,3),(11,5),(11,8),(9,10),(6,11),(3,10),(1,8),(1,4)],ink)
# Handle behind the lens, with a metal collar.
result.poly([(10,9),(15,13),(15,15),(13,15),(9,11)],ink)
result.line(10,10,13,13,'#9b6944')
result.line(11,11,14,14,'#68483e')
result.set(13,12,'#c38b57')
result.set(14,13,'#c38b57')
result.line(10,9,11,10,gold)
# Stepped metallic bezel.
result.poly([(4,2),(8,2),(10,4),(10,8),(8,10),(4,10),(2,8),(2,4)],rim)
result.line(4,2,8,2,light)
result.line(2,4,2,7,gold)
result.set(3,3,light)
result.set(9,3,gold)
result.line(4,9,7,9,gold)
result.set(8,9,light)
# Lens: dark inner bevel and a cool translucent-looking surface.
result.poly([(4,3),(7,3),(9,5),(9,7),(7,9),(4,9),(3,7),(3,4)],ink)
result.poly([(4,4),(7,4),(8,5),(8,7),(7,8),(4,8),(3,6)],'#73a5b5')
result.line(4,4,7,4,'#c2e9ed')
result.line(4,5,7,5,'#acd9e2')
result.line(4,6,6,6,'#acd9e2')
result.set(4,4,'#f0ffff')
result.set(4,5,'#f0ffff')
result.set(3,6,'#c2e9ed')
result.set(7,7,'#d9f5ef')
view(result,scale=24,margin=0)
finish(result)
