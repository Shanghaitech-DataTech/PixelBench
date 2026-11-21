from pixelbench_api import new_canvas, view, finish

# Sunken shipwreck, 64x64 pixel art.
c = new_canvas(64, 64, background="#082f4d", name="sunken_shipwreck")

# Palette
abyss = "#082f4d"
deep = "#0b4660"
water = "#0e6175"
midwater = "#167d86"
lightwater = "#26979a"
ray = "#43aaa3"
foam = "#87c9b4"
outline = "#172f35"
wood_dark = "#3b3430"
wood = "#64463a"
wood_light = "#8a5d45"
rust = "#a45235"
rust_light = "#cc7044"
sand_dark = "#8f7654"
sand = "#b79a66"
sand_light = "#d3b77a"
coral = "#d36c5c"
coral_light = "#ed9571"
seaweed = "#27785f"
seaweed_light = "#42a06f"
fish_dark = "#173d4b"
fish = "#7fc2ae"
fish_light = "#c3d8b2"

# Layered water depth.
c.rect(0, 0, 64, 8, water)
c.rect(0, 8, 64, 10, midwater)
c.rect(0, 18, 64, 10, water)
c.rect(0, 28, 64, 12, deep)
c.rect(0, 40, 64, 24, abyss)
# Pixel dither transitions and distant particulate.
c.dither(0, 6, 64, 4, [water, midwater], pattern="checker")
c.dither(0, 16, 64, 4, [midwater, water], pattern="checker")
c.dither(0, 26, 64, 4, [water, deep], pattern="checker")
c.dither(0, 38, 64, 4, [deep, abyss], pattern="checker")
# Broken shafts of filtered light.
c.poly([(8,0),(15,0),(26,31),(22,31)], ray)
c.poly([(35,0),(40,0),(43,24),(40,24)], lightwater)
c.dither(13, 7, 7, 18, [ray, midwater], pattern="checker")
# Sparse floating motes.
for x,y,col in [(4,11,foam),(28,8,foam),(49,13,ray),(58,7,foam),(31,22,lightwater),(5,29,midwater),(53,27,lightwater),(17,19,ray),(60,34,water),(2,39,water)]:
    c.set(x,y,col)

# Distant school of fish, each with a one-pixel eye/highlight.
def small_fish(x,y,body=fish):
    c.poly([(x,y),(x+4,y-2),(x+8,y),(x+4,y+2)], body)
    c.poly([(x,y),(x-3,y-2),(x-3,y+2)], fish_dark)
    c.set(x+6,y-1,fish_light)

small_fish(9,13)
small_fish(24,18,fish_light)
small_fish(43,11)
small_fish(51,20,fish)
# Tiny far fish silhouettes.
for x,y in [(31,12),(38,17),(56,14),(18,9)]:
    c.line(x,y,x+3,y,fish_dark)
    c.set(x-1,y-1,fish_dark)
    c.set(x-1,y+1,fish_dark)

# Broken mast and rigging behind the hull.
c.line(30,8,27,38,outline)
c.line(31,8,28,38,wood_dark)
c.rect(30,9,2,3,wood_light)
c.line(30,12,43,21,outline)
c.line(30,13,42,21,wood)
c.line(31,13,19,21,outline)
c.line(30,14,20,21,wood)
c.line(22,19,28,33,fish_dark)
c.line(41,20,34,35,fish_dark)
# Ragged remnant of sail.
c.poly([(32,14),(40,20),(34,20),(31,18)], "#31585a")
c.set(35,17,water)
c.set(37,19,deep)

# Main wreck silhouette, listing slightly into the sand.
c.poly([(5,31),(14,29),(48,31),(59,27),(57,39),(51,48),(39,53),(18,50),(9,43)], outline)
# Wood hull mass.
c.poly([(8,33),(16,31),(47,33),(56,30),(54,39),(49,46),(39,50),(19,48),(11,42)], wood_dark)
# Broad hull planks.
c.poly([(10,34),(18,32),(48,34),(54,32),(53,36),(17,36)], wood)
c.poly([(12,38),(52,38),(50,42),(15,41)], wood)
c.poly([(15,43),(49,44),(46,47),(20,47)], wood_light)
# Gunwale and broken bow.
c.line(6,31,47,31,outline)
c.line(9,32,48,33,wood_light)
c.line(48,32,59,27,outline)
c.line(50,33,57,30,wood_light)
c.poly([(56,29),(61,25),(59,34),(54,39)], outline)
c.poly([(57,30),(59,28),(58,34),(55,38)], wood)
# Jagged stern break.
c.poly([(6,31),(10,33),(8,36),(12,39),(9,43),(5,40)], outline)
c.poly([(8,33),(10,34),(9,36),(11,39),(9,40)], rust)

# Plank seams, ribs, rivets.
for x in [17,25,34,43,50]:
    c.line(x,33,x-1,47,outline)
    c.set(x+1,35,wood_light)
c.line(11,37,53,39,outline)
c.line(14,42,50,44,outline)
c.line(20,47,44,49,outline)
for x,y in [(15,34),(22,39),(30,34),(38,40),(46,35),(17,44),(34,46),(49,41)]:
    c.set(x,y,rust_light)
    c.set(x+1,y,rust)
# Dark breaches in the corroded body.
c.poly([(20,36),(25,36),(27,39),(24,42),(19,40)], outline)
c.rect(22,37,3,3,abyss)
c.set(21,37,deep)
c.poly([(39,34),(44,35),(45,38),(42,40),(38,38)], outline)
c.rect(40,36,3,2,abyss)
c.poly([(29,43),(34,43),(35,46),(32,48),(28,46)], outline)
c.rect(30,44,3,2,deep)
# Rust trails.
c.line(46,36,45,42,rust)
c.set(44,41,rust_light)
c.line(16,36,16,40,rust)
c.set(17,40,rust_light)

# Sand bed overlaps and half-buries the hull.
c.poly([(0,50),(7,48),(15,50),(22,49),(31,53),(40,51),(48,48),(57,49),(63,46),(63,63),(0,63)], sand_dark)
c.poly([(0,53),(9,50),(18,53),(28,52),(38,56),(48,52),(57,53),(63,50),(63,63),(0,63)], sand)
c.poly([(0,57),(13,54),(24,56),(33,58),(44,55),(55,56),(63,53),(63,63),(0,63)], sand_light)
# Shadow and dune pixels.
c.line(13,51,27,53,sand_dark)
c.line(38,53,51,50,sand_dark)
c.line(2,58,14,56,sand)
c.line(43,58,60,55,sand)
for x,y in [(5,54),(17,58),(27,55),(35,60),(48,55),(58,59),(11,61),(24,62),(53,62)]:
    c.set(x,y,sand_dark)
    c.set(x+1,y,sand)

# Seaweed accents, rooted in foreground.
def weed(points, col):
    c.path("M " + " Q ".join(f"{x} {y}" for x,y in points), col, fill=False)
# Use crisp segmented fronds for predictable pixel bends.
c.line(4,56,5,45,seaweed)
c.line(5,50,2,47,seaweed_light)
c.line(5,48,8,44,seaweed)
c.line(7,56,9,49,seaweed_light)
c.line(9,51,12,48,seaweed)
c.line(57,56,55,45,seaweed)
c.line(56,51,52,47,seaweed_light)
c.line(56,49,60,44,seaweed)
c.line(59,56,61,49,seaweed_light)

# Branching coral at lower left and small fan at right.
c.rect(2,55,3,5,coral)
c.line(3,56,1,52,coral)
c.line(3,55,5,50,coral_light)
c.line(4,56,8,53,coral)
c.circle(1,51,1,coral_light)
c.circle(6,49,1,coral)
c.circle(9,52,1,coral_light)
c.line(49,58,49,52,coral)
c.line(49,55,46,52,coral_light)
c.line(49,56,52,51,coral)
c.line(49,54,52,54,coral_light)
c.set(45,51,coral)
c.set(53,50,coral_light)

# Foreground shells, pebbles, and bubbles.
c.poly([(20,59),(23,57),(26,59)], sand_dark, fill=False)
c.set(22,58,foam)
c.circle(40,60,1,sand_dark)
c.set(40,59,sand)
for x,y in [(60,40),(61,36),(59,31),(12,26),(11,23)]:
    c.circle(x,y,1,foam,fill=False)

view(c, scale=8, margin=0)
finish(c)
