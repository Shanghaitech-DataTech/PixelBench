result = new_canvas(16, 16, name="magnifying_glass")
# A strong stepped silhouette keeps the tool readable at inventory size.
ink = '#252333'
shadow = '#72503e'
brass = '#bd874b'
light = '#f4d58b'
glass = '#72b9c8'
deep = '#397487'
shine = '#e0f5e9'
# Handle behind the lens: angled, with a capped leather grip.
result.poly([(9,8),(14,12),(15,13),(15,14),(14,15),(13,15),(8,10)], ink)
result.line(10,10,14,14,shadow)
result.line(11,10,14,13,brass)
result.set(13,12,'#d3a16a')
result.set(14,14,'#49333a')
# Octagonal outer rim.
result.rect(4,1,5,1,ink)
result.rect(2,2,9,2,ink)
result.rect(1,4,11,5,ink)
result.rect(2,9,9,2,ink)
result.rect(4,11,5,1,ink)
# Brass inset, lit from upper left.
result.rect(4,2,5,1,light)
result.rect(3,3,7,1,brass)
result.rect(2,4,9,5,brass)
result.rect(3,9,7,1,shadow)
result.rect(4,10,5,1,shadow)
result.line(2,4,2,7,light)
result.set(3,3,light)
result.set(3,9,brass)
result.line(5,10,8,10,brass)
# Glass bounded by a dark inner bevel.
result.rect(4,3,5,1,shadow)
result.rect(3,4,7,5,shadow)
result.rect(4,9,5,1,shadow)
result.rect(4,4,5,5,glass)
result.rect(3,5,1,3,glass)
result.rect(9,5,1,3,deep)
result.line(4,8,8,8,deep)
result.line(5,9,7,9,deep)
# Crisp reflected light and a lighter lower rim.
result.line(4,4,6,4,shine)
result.line(3,5,3,6,shine)
result.set(4,5,'#b6e2df')
result.set(8,7,'#b6e2df')
result.set(8,9,brass)
view(result, scale=24)
finish(result)
