c = new_canvas(64, 64, name="laundromat")
# Cool tiled room
c.rect(0, 0, 64, 50, "#b9d4dc")
c.rect(0, 0, 64, 5, "#d9edf0")
c.rect(0, 5, 64, 2, "#e9f5f4")
# Back wall tile joints
for x in range(0, 64, 16):
    c.line(x, 8, x, 49, "#a8c6ce")
for y in (13, 30, 47):
    c.line(0, y, 63, y, "#a8c6ce")
# Bright overhead light
c.rect(23, 3, 18, 3, "#fff8d8")
c.rect(25, 6, 14, 1, "#e7f4ed")
# Wall clock
c.circle(9, 10, 5, "#718c96")
c.circle(9, 10, 4, "#f4f3df")
c.line(9, 10, 9, 7, "#455e69")
c.line(9, 10, 12, 11, "#455e69")
c.set(9, 10, "#d96757")
# Washer/dryer units: dark inset outlines make every appliance distinct

def machine(x, y, accent):
    c.rect(x, y, 17, 15, "#718994")
    c.rect(x+1, y+1, 15, 13, "#e2eceb")
    c.rect(x+2, y+2, 13, 3, "#c5d6d8")
    c.rect(x+3, y+3, 4, 1, accent)
    c.rect(x+9, y+3, 2, 1, "#637d87")
    c.circle(x+9, y+9, 5, "#617984")
    c.circle(x+9, y+9, 4, "#b4d0d6")
    c.circle(x+9, y+9, 3, "#779ba5")
    c.circle(x+9, y+9, 2, "#a8c5ca")
    c.rect(x+2, y+13, 13, 1, "#c1d1d2")
    c.set(x+4, y+13, "#83ad9b")
    c.set(x+12, y+13, "#e1b85e")

for x, a in ((3, "#68a7b2"), (23, "#d7a765"), (43, "#79a991")):
    machine(x, 15, a)
for x, a in ((3, "#d7a765"), (23, "#79a991"), (43, "#68a7b2")):
    machine(x, 33, a)
# Floor and tiled perspective
c.rect(0, 50, 64, 14, "#829da5")
c.rect(0, 50, 64, 2, "#d0e0dc")
for x in range(4, 64, 16):
    c.line(x, 52, x-3, 63, "#718d96")
for y in (56, 61):
    c.line(0, y, 63, y, "#718d96")
# Folding table, clean pale top with metal legs
c.rect(7, 52, 27, 3, "#f1f1dc")
c.rect(8, 52, 25, 1, "#fff9e6")
c.line(10, 55, 9, 62, "#536f79")
c.line(30, 55, 31, 62, "#536f79")
c.line(9, 62, 31, 62, "#536f79")
# Neatly folded laundry on table
c.rect(13, 48, 9, 4, "#f4f2dc")
c.rect(14, 47, 7, 2, "#d46f70")
c.rect(15, 46, 7, 2, "#71a8b0")
c.line(16, 48, 20, 48, "#f2d9c4")
# Laundry basket foreground right
c.rect(43, 54, 15, 8, "#d3a65f")
c.rect(44, 55, 13, 6, "#e6c17b")
c.rect(46, 53, 9, 2, "#718994")
for x in (46, 50, 54):
    c.rect(x, 56, 1, 4, "#a87843")
c.rect(44, 61, 13, 1, "#9a744d")
# Clothes peeking above basket
c.rect(45, 51, 6, 3, "#e9eee1")
c.rect(49, 52, 6, 2, "#cf7c76")
print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63)))
finish(c)
