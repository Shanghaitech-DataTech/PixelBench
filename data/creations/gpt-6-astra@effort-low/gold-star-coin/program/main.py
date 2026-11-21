result = new_canvas(16,16)
# Stepped circular silhouette and warm metal rim.
rows = [(5,10),(3,12),(2,13),(1,14),(1,14),(0,15),(0,15),(0,15),(0,15),(0,15),(1,14),(1,14),(2,13),(3,12),(5,10)]
for y,(a,b) in enumerate(rows):
    result.line(a,y,b,y,'#77401f')
for y,(a,b) in enumerate(rows[1:-1],1):
    result.line(a+1,y,b-1,y,'#d28a24')
result.line(5,1,10,1,'#fff0a0')
result.line(3,2,5,2,'#fff0a0')
result.line(2,3,3,3,'#fff0a0')
result.line(1,5,1,9,'#ffe16a')
result.line(3,12,5,13,'#f6bb3c')
result.line(6,13,10,13,'#f6bb3c')
result.line(12,10,12,11,'#f6bb3c')
# Inset circular face.
result.ellipse(7,7,5,5,'#f6bb3c')
result.line(5,3,9,3,'#ffe16a')
result.line(3,5,3,8,'#ffe16a')
# Dark embossed star with a bright upper bevel.
star = ['...X...', '...X...', '..XXX..', 'XXXXXXX', '.XXXXX.', '..XXX..', '.XX.XX.']
for j,row in enumerate(star):
    for i,p in enumerate(row):
        if p=='X': result.set(i+4,j+4,'#77401f')
for x,y in [(7,6),(6,7),(7,7),(8,7),(7,8)]:
    result.set(x,y,'#d28a24')
view(result)
finish(result)
