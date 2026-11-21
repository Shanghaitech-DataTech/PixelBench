# Detective game magnifying glass icon, 16x16.
c = new_canvas(16, 16, background=(0, 0, 0, 0))

dark   = (40, 42, 54, 255)      # outline
rim    = (96, 106, 130, 255)    # metal rim
glass  = (150, 205, 235, 255)   # lens
glass2 = (115, 178, 214, 255)   # lens shade
shine  = (225, 244, 252, 255)   # highlight
wood   = (176, 118, 62, 255)    # handle
wood2  = (122, 78, 40, 255)     # handle shadow

# Handle band first (drawn beneath the lens)
c.poly([(9, 8), (12, 8), (15, 11), (15, 15), (12, 15), (9, 12)], wood)
# outline the handle edges
c.line(9, 8, 15, 14, dark)
c.line(9, 12, 15, 14, dark)

# Lens (covers any overlap with the handle)
c.circle(7, 6, 5, dark)
c.circle(7, 6, 4, rim)
c.circle(7, 6, 3, glass)
c.circle(8, 7, 2, glass2)
c.circle(5, 3, 1, shine)
c.set(4, 2, shine)

print(c.matrix_text())
finish(c)
