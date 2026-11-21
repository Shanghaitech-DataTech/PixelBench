from pixelbench_api import new_canvas, view, finish

# Two 24x48 animation cells on one transparent 48x48 sprite sheet.
c = new_canvas(48, 48, background=None, name="teleport_portal_2frame")

# Compact shared palette.
shadow = "#180b35"
deep = "#32105f"
mid = "#6819a8"
violet = "#9a32dc"
hot = "#d45cff"
lav = "#eaa0ff"
blue = "#786dff"
cyan = "#6cddff"
white = "#f6e7ff"
halo = "#bd55ff"

# FRAME 1: upright, inward-pulling purple vortex (cell x=0..23).
# Ragged outer energy silhouette.
c.poly([(11,6),(15,7),(15,9),(19,10),(18,13),(21,16),(19,19),(21,23),
        (19,27),(20,31),(17,34),(17,38),(13,38),(11,42),(9,39),(6,39),
        (6,35),(3,32),(5,28),(2,25),(4,21),(2,17),(5,14),(5,10),(9,10)], deep)
c.ellipse(11,24,9,16, mid)
c.ellipse(11,24,7,14, violet)
c.ellipse(11,24,5,11, shadow)

# Segmented outer rim gives a pulsing, pixel-stepped edge.
c.line(7,9,11,7, hot); c.line(13,8,17,11, lav)
c.line(18,14,19,20, hot); c.line(19,25,17,31, hot)
c.line(16,34,13,38, violet); c.line(8,38,5,34, hot)
c.line(4,30,3,25, violet); c.line(3,19,5,14, hot)

# Counter-clockwise energy spiral.
c.path("M 7 14 C 16 10 19 18 16 22 C 13 25 7 22 7 18 C 7 15 11 14 14 16", lav, fill=False)
c.path("M 16 18 C 19 25 14 33 8 32 C 4 31 4 26 7 24 C 10 22 15 25 14 28 C 13 31 9 31 8 28", blue, fill=False)
c.path("M 7 20 C 9 17 14 17 15 21 C 16 25 11 27 9 25", hot, fill=False)
c.set(11,21,white); c.set(12,22,cyan); c.set(10,26,lav)
# Loose energy motes.
for x,y,col in [(2,10,hot),(20,9,blue),(1,27,lav),(21,35,hot),(7,5,violet),(15,42,blue),(3,37,mid)]:
    c.set(x,y,col)
c.set(21,8,hot); c.set(20,8,hot)

# FRAME 2: the vortex phase rotated clockwise, with a luminous halo.
# Halo rays and detached sparks.
c.line(35,3,35,7, halo); c.set(36,4,lav)
c.line(28,7,30,10, violet); c.line(42,8,40,11, hot)
c.line(46,19,43,20, halo); c.line(46,30,43,29, hot)
c.line(41,38,39,36, violet); c.line(29,39,31,36, hot)
c.line(25,29,28,28, halo); c.line(25,17,28,18, hot)
c.set(45,13,lav); c.set(25,23,blue); c.set(44,35,blue); c.set(37,43,hot)

# Broad halo and core. Broken extra pixels prevent a mechanically smooth ring.
c.ellipse(35,24,10,17, halo, fill=False)
c.ellipse(35,24,9,15, violet)
c.ellipse(35,24,7,13, hot)
c.ellipse(35,24,5,11, shadow)
c.set(27,12,lav); c.set(43,14,lav); c.set(44,27,lav); c.set(27,31,lav)
c.set(31,8,hot); c.set(39,9,hot); c.set(42,36,hot); c.set(30,37,hot)

# Rotated spiral: diagonal sweep differs clearly from frame 1.
c.path("M 29 18 C 33 12 41 15 41 21 C 41 25 36 27 32 25 C 29 23 30 19 33 18 C 36 17 39 19 38 22", cyan, fill=False)
c.path("M 40 19 C 43 26 38 34 32 33 C 27 32 27 27 30 24 C 33 21 38 24 38 28 C 37 31 33 32 31 29", blue, fill=False)
c.path("M 30 16 C 37 12 43 18 41 24 C 40 28 35 29 32 27", lav, fill=False)
# Bright rotating leading edge and central flare.
c.line(29,17,32,13,white); c.line(32,13,36,12,lav)
c.line(40,25,40,29,white); c.line(39,30,36,34,lav)
c.set(34,22,white); c.set(35,22,white); c.set(36,23,cyan)
c.set(34,25,lav); c.set(37,26,hot)

view(c, scale=10, margin=0)
finish(c)
