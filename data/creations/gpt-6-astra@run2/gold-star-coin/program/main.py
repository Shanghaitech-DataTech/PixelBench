result = new_canvas(16, 16, name='gold_star_coin')
# Six warm shades, from the silhouette to the glint.
edge = '#6e391c'
shade = '#ae621e'
gold = '#eaa52b'
light = '#ffcf49'
glint = '#fff19b'
star = '#8c4a1c'
# Stepped circular silhouette, with a one-pixel transparent margin.
rows = [(5,10),(3,12),(2,13),(2,13),(1,14),(1,14),(1,14),(1,14),(1,14),(1,14),(2,13),(2,13),(3,12),(5,10)]
for y,(a,b) in enumerate(rows,1):
    result.rect(a,y,b-a+1,1,edge)
# Raised outer rim.
for y,(a,b) in enumerate(rows[1:-1],2):
    result.rect(a+1,y,b-a-1,1,gold if y<10 else shade)
result.line(5,2,10,2,glint)
result.line(3,3,4,3,glint)
result.line(2,5,2,9,light)
result.set(3,4,glint)
result.line(11,3,12,4,light)
result.line(13,5,13,10,shade)
result.line(4,12,11,12,gold)
result.line(5,13,10,13,light)
# Recessed circular face.
result.poly([(5,3),(10,3),(12,5),(12,10),(10,12),(5,12),(3,10),(3,5)],shade)
result.poly([(5,4),(10,4),(11,5),(12,6),(12,9),(10,11),(5,11),(4,10),(4,6)],light)
result.line(5,11,10,11,gold)
# Crisp five-point star, picked out against the bright face.
for y,a,b in [(5,7,8),(6,7,8),(7,4,11),(8,5,10),(9,6,9),(10,5,6),(10,9,10)]:
    result.rect(a,y,b-a+1,1,star)
view(result, scale=24)
finish(result)
