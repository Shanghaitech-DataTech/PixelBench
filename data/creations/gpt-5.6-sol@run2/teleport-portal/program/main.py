from pixelbench_api import new_canvas, finish, view

# Two 24x48 animation cells on one transparent 48x48 sprite sheet.
c = new_canvas(48, 48, background=None, name="teleport_portal_2frame")

# Restricted luminous purple palette.
shadow = "#21103f"
deep = "#351064"
mid = "#59209a"
purple = "#7b2dc4"
bright = "#aa4df0"
light = "#d082ff"
white = "#f2d9ff"
glow1 = "#8b36d966"
glow2 = "#c266ff88"

# FRAME 1: compact purple energy vortex, centered in left cell.
# Wispy outer energy flecks.
for x, y, col in [
    (11,8,glow1),(12,8,glow1),(6,11,glow1),(18,12,glow1),
    (3,20,glow1),(20,19,glow1),(4,30,glow1),(19,32,glow1),
    (8,38,glow1),(15,37,glow1),(12,40,glow1),
    (2,24,glow2),(21,25,glow2),(12,6,glow2),(12,41,glow2)
]: c.set(x,y,col)

# Outer broken vortex ring.
c.line(8,10,14,10,mid); c.set(7,11,mid); c.set(15,11,purple)
c.line(5,13,7,11,purple); c.line(16,12,19,15,bright)
c.line(4,14,3,20,mid); c.set(3,21,purple)
c.line(20,16,21,21,mid); c.set(21,22,bright)
c.line(3,27,5,33,purple); c.line(6,34,9,37,mid)
c.line(20,27,18,33,bright); c.line(17,34,14,37,purple)
c.line(10,38,14,38,deep)

# Thick spiral bands.
c.line(7,14,14,13,bright); c.line(14,13,18,16,bright)
c.line(18,16,19,20,purple); c.line(19,20,17,23,purple)
c.line(17,23,13,24,bright)
c.line(13,24,10,22,bright); c.line(10,22,11,19,light)
c.line(11,19,14,18,light); c.line(14,18,16,20,bright)
c.set(16,21,bright); c.set(15,22,light)

c.line(16,27,13,29,purple); c.line(13,29,9,28,purple)
c.line(9,28,7,25,mid); c.line(7,25,7,21,mid)
c.line(7,21,9,17,purple)
c.line(6,31,10,34,bright); c.line(10,34,15,33,bright)
c.line(15,33,18,29,purple)

# Dark dimensional throat and hot core pixels.
c.rect(10,23,5,5,shadow)
c.set(11,23,deep); c.set(14,24,deep); c.set(10,27,deep)
c.set(12,24,white); c.set(13,25,light); c.set(11,26,bright)
c.set(9,15,white); c.set(19,24,light); c.set(7,33,light)

# FRAME 2: rotated vortex with a pronounced glowing halo, centered in right cell.
# Translucent halo corona.
for x, y in [
    (35,5),(36,5),(30,7),(41,8),(27,11),(44,13),(25,18),(46,20),
    (24,24),(47,24),(25,30),(45,33),(28,37),(42,39),(33,42),(39,42)
]: c.set(x,y,glow1)
for x, y in [
    (32,7),(39,7),(27,14),(44,16),(25,23),(46,26),(28,35),(43,35),
    (32,40),(40,40)
]: c.set(x,y,glow2)

# Halo arcs, intentionally broken for lively pixel energy.
c.line(31,8,38,7,glow2); c.line(39,8,43,11,glow2)
c.line(27,13,25,19,glow2); c.line(24,21,24,27,glow2)
c.line(45,17,47,23,glow2); c.line(46,28,43,34,glow2)
c.line(27,32,31,39,glow2); c.line(33,41,39,41,glow2)

# Bright outer portal ring.
c.line(32,10,39,10,purple); c.line(29,12,32,10,bright)
c.line(40,11,43,14,light); c.line(44,15,45,20,bright)
c.line(45,21,45,27,purple); c.line(44,28,42,33,bright)
c.line(41,34,38,37,light); c.line(37,38,32,37,purple)
c.line(31,37,27,33,bright); c.line(26,32,25,27,purple)
c.line(25,26,26,19,bright); c.line(27,18,28,14,purple)

# Rotated spiral: sweeping clockwise from upper-right to lower-left.
c.line(31,14,36,12,mid); c.line(36,12,41,14,purple)
c.line(41,14,43,18,bright); c.line(43,18,42,22,light)
c.line(42,22,39,24,light); c.line(39,24,35,23,bright)
c.line(35,23,33,20,bright); c.line(33,20,35,17,purple)
c.line(35,17,38,17,light); c.line(38,17,40,19,white)

c.line(40,27,39,31,purple); c.line(39,31,35,34,bright)
c.line(35,34,31,33,light); c.line(31,33,28,29,purple)
c.line(28,29,28,24,mid); c.line(28,24,30,19,purple)
c.set(29,18,bright); c.set(30,17,light)

# Rotated dark throat and sparkling center.
c.poly([(32,23),(36,21),(40,24),(39,29),(35,31),(31,28)], shadow)
c.set(33,23,deep); c.set(38,23,deep); c.set(39,27,deep)
c.set(34,25,bright); c.set(35,24,white); c.set(37,25,light)
c.set(36,27,white); c.set(34,28,purple); c.set(38,28,bright)

# Halo glints and orbiting energy fragments.
c.set(36,8,white); c.set(44,13,light); c.set(46,24,white)
c.set(42,35,light); c.set(36,40,white); c.set(27,34,light)
c.set(25,22,white); c.set(28,12,light)
c.line(29,9,31,8,bright); c.line(43,10,45,12,purple)
c.line(45,36,43,38,bright); c.line(26,37,28,39,purple)

view(c, scale=10, margin=0, edges="none")
finish(c)
