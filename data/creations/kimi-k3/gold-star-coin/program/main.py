c = new_canvas(16, 16, background=None, name="gold_star_coin")

# Palette (6 visible colours)
O = '#6b4210'  # dark brown outline
B = '#f4c542'  # base gold
D = '#cf9526'  # dark gold shading
L = '#ffe79a'  # light gold highlight
W = '#ffffff'  # white sparkle
S = '#8a5a12'  # star amber

# Outer circle (outline) rows: (y, x, width)
outer = [(0,6,4),(1,4,8),(2,3,10),(3,2,12),(4,1,14),(5,1,14),
         (6,0,16),(7,0,16),(8,0,16),(9,0,16),(10,1,14),(11,1,14),
         (12,2,12),(13,3,10),(14,4,8),(15,6,4)]
for y, x, w in outer:
    c.rect(x, y, w, 1, O)

# Inner disc (base gold), inset by 1 px
inner = [(1,5,6),(2,4,8),(3,3,10),(4,2,12),(5,2,12),
         (6,1,14),(7,1,14),(8,1,14),(9,1,14),(10,2,12),(11,2,12),
         (12,3,10),(13,4,8),(14,5,6)]
for y, x, w in inner:
    c.rect(x, y, w, 1, B)

# Bottom-right rim shading (dark gold)
shade = [(13,5),(14,6),(14,7),(14,8),(14,9),(13,10),
         (12,11),(13,11),(11,12),(12,12),
         (9,13),(10,13),(11,13),(6,14),(7,14),(8,14),(9,14)]
for x, y in shade:
    c.set(x, y, D)

# Top-left rim highlight (light gold)
high = [(7,1),(8,1),(5,2),(6,2),(7,2),(4,3),(5,3),(3,4),(4,4),
        (2,5),(3,5),(1,6),(2,6),(1,7),(1,8)]
for x, y in high:
    c.set(x, y, L)

# White glint
for x, y in [(5,2),(4,3),(5,3)]:
    c.set(x, y, W)

# Star in the middle
star = [(7,4),
        (6,5),(7,5),(8,5),
        (6,6),(7,6),(8,6),
        (3,7),(4,7),(5,7),(6,7),(7,7),(8,7),(9,7),(10,7),(11,7),
        (4,8),(5,8),(6,8),(7,8),(8,8),(9,8),(10,8),
        (5,9),(6,9),(7,9),(8,9),(9,9),
        (5,10),(6,10),(8,10),(9,10),
        (4,11),(5,11),(9,11),(10,11)]
for x, y in star:
    c.set(x, y, S)

view(c)
finish(c)
