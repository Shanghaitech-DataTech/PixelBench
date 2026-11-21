# Eight-color closed leather spellbook.
result = new_canvas(32, 32, name="leather_spellbook")
c = result
ink = '#241e2b'
shadow = '#4e2c36'
leather = '#874437'
rust = '#bc7049'
metal = '#80694d'
gold = '#cda45f'
light = '#f0d9a0'
paper = '#b5ad91'

def poly(points, color):
    c.poly(points, color)
def line(a,b,color):
    c.line(*a,*b,color)

# Complete binding silhouette, including the lower cover.
body = [(8,2),(26,5),(28,7),(25,26),(23,29),(5,25),(3,23),(6,5)]
poly(body, ink)
c.poly(body, ink, fill=False)
poly([(5,21),(24,25),(25,26),(23,28),(5,24),(4,23)], shadow)
line((6,24),(22,27), leather)
line((9,25),(21,27), rust)

# Compact page block visible along the fore edge and foot of the book.
poly([(26,7),(27,8),(24,26),(22,27),(6,23),(6,21),(23,24)], paper)
line((8,22),(23,25), light)
line((11,24),(22,26), metal)
line((25,16),(24,22), light)
line((26,10),(25,15), light)

# Top cover and rounded, darker spine.
cover = [(8,3),(26,6),(27,7),(24,24),(5,20),(5,17),(7,5)]
poly(cover, ink)
c.poly(cover, ink, fill=False)
poly([(9,4),(25,7),(23,22),(7,19),(6,18),(8,5)], leather)
poly([(8,4),(11,5),(8,20),(6,19),(6,16)], shadow)
line((11,5),(24,7), rust)
line((24,8),(22,20), shadow)
line((9,20),(22,23), shadow)
line((7,7),(5,20), ink)
line((7,8),(6,15), leather)

# Spine's raised leather bands.
line((6,10),(9,11), ink)
line((6,9),(9,10), rust)
line((5,17),(8,18), ink)
line((6,16),(8,17), rust)

# Embossed panel, recessed into the leather.
poly([(12,7),(23,9),(21,20),(10,18)], shadow)
poly([(13,8),(22,10),(20,19),(11,17)], leather)
line((12,7),(22,9), rust)
line((10,18),(20,20), rust)

# Four brass corner guards, edged in old bronze.
poly([(9,3),(14,4),(13,6),(10,6),(9,9),(7,8),(8,4)], metal)
poly([(9,3),(13,4),(12,5),(9,5),(8,8),(8,5)], gold)
c.set(9,4,light)
poly([(23,5),(26,6),(27,7),(26,11),(24,10),(25,8),(22,7)], metal)
poly([(24,6),(26,6),(26,8),(25,10),(25,7),(23,7)], gold)
c.set(25,6,light)
poly([(6,16),(8,17),(8,19),(11,20),(10,22),(5,20)], metal)
poly([(6,17),(7,18),(7,20),(10,21),(6,20)], gold)
c.set(6,18,light)
poly([(22,19),(24,20),(24,24),(20,23),(19,21),(22,22)], metal)
poly([(23,20),(23,23),(20,22),(21,22),(22,22),(22,20)], gold)
c.set(23,21,light)

# A crescent seal and a tiny magical glint.
# Hand-placed clusters preserve both tips of the crescent at native size.
for y, xs in {11:[16,17,18],12:[15,16],13:[14,15],14:[14,15],15:[14,15],16:[15,16],17:[16,17,18]}.items():
    for x in xs:
        c.set(x,y,metal)
for y, xs in {10:[16,17],11:[15,16],12:[14,15],13:[14],14:[14],15:[14,15],16:[15,16,17,18]}.items():
    for x in xs:
        c.set(x,y,gold)
c.set(16,10,light)
c.set(15,11,light)
c.set(14,12,light)
c.set(19,12,gold)
line((18,13),(20,13),light)
c.set(19,14,gold)

# Small bronze latch crossing the fore edge.
poly([(23,14),(26,14),(26,17),(22,17)], ink)
c.rect(23,14,3,2,metal)
c.rect(23,14,2,1,gold)
c.set(24,15,light)
c.set(25,16,gold)

view(result, scale=12, margin=0)
save('leather-spellbook', result)
finish(result)
