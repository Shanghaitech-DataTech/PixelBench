from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32)

wool  = c.color((0xF6, 0xF2, 0xE6))
hi    = c.color((0xFC, 0xFA, 0xF1))
shade = c.color((0xE0, 0xD7, 0xC2))
deep  = c.color((0xCE, 0xC3, 0xAB))
pink  = c.color((0xF2, 0xD3, 0xCB))
pksh  = c.color((0xDE, 0xB1, 0xA9))
dark  = c.color((0x55, 0x4D, 0x44))

# legs (behind the body)
c.rect(9, 25, 3, 6, deep)
c.rect(21, 25, 3, 6, deep)
c.rect(13, 26, 3, 5, shade)
c.rect(17, 26, 3, 5, shade)

# fluffy body
c.ellipse(17, 20, 9, 7, wool)   # main lump
c.circle(10, 18, 4, wool)       # left puff
c.circle(24, 17, 4, wool)       # right puff
c.circle(17, 14, 5, wool)       # top puff
c.circle(27, 20, 2, wool)       # tail puff

# belly shading
c.ellipse(17, 24, 8, 3, shade)

# head
c.ellipse(10, 13, 5, 5, wool)
c.set(9, 8, wool)
c.set(10, 8, wool)
# ears
c.ellipse(6, 8, 2, 3, pink)
c.ellipse(13, 8, 2, 3, pink)
c.ellipse(6, 9, 1, 2, pksh)
c.ellipse(13, 9, 1, 2, pksh)
# face: gentle eyes and a small snout
c.set(7, 12, dark)
c.set(8, 12, dark)
c.rect(5, 14, 2, 2, pksh)

# soft wool highlights
c.circle(12, 11, 1, hi)
c.circle(19, 11, 1, hi)
c.circle(23, 14, 1, hi)

print(c.stats_text())
finish(c)
