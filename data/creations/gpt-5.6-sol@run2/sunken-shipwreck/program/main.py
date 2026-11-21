# Astra Pixel Art 0.6.0
# Sunken shipwreck, 64x64.

result = new_canvas(64, 64, background="#082f46", name="sunken_shipwreck")

# Palette.
deep = "#06283c"
water = "#0a4057"
midwater = "#0d5366"
blue = "#176f78"
lightwater = "#2c8d8b"
glow = "#50aaa0"
navy = "#041d2c"
ink = "#071b24"
wood_dark = "#2b2925"
wood = "#4a392a"
wood_mid = "#684a31"
wood_light = "#8a633e"
rust = "#9a5534"
rust_hi = "#c07845"
patina = "#3f8071"
patina_hi = "#65a080"
sand_dark = "#8f7451"
sand = "#b99a66"
sand_light = "#d5bb7d"
coral_red = "#bb554b"
coral_hi = "#e1785d"
coral_pink = "#c97582"
kelp_dark = "#286044"
kelp = "#3f8050"
kelp_hi = "#69a65d"
fish = "#9bc3aa"
fish_hi = "#d0d6a5"
bubble = "#83c4bd"

# Layered water with restrained pixel texture.
result.rect(0, 8, 64, 12, water)
result.rect(0, 20, 64, 13, midwater)
result.rect(0, 33, 64, 16, blue)
result.rect(0, 49, 64, 15, "#17666b")
result.dither(0, 7, 64, 4, [deep, water], pattern="bayer4")
result.dither(0, 18, 64, 5, [water, midwater], pattern="bayer4")
result.dither(0, 31, 64, 4, [midwater, blue], pattern="bayer4")

# Blocky light shafts from the surface.
result.poly([(7,0),(15,0),(29,43),(23,43)], "#176176")
result.poly([(42,0),(48,0),(42,34),(38,34)], "#1c6676")
result.dither(24, 4, 6, 28, [midwater, "#176176"], pattern="checker")
# Surface shimmer.
result.rect(3, 3, 13, 1, lightwater)
result.rect(20, 5, 9, 1, blue)
result.rect(34, 2, 14, 1, lightwater)
result.rect(51, 6, 9, 1, blue)
result.rect(0, 11, 8, 1, midwater)
result.rect(43, 10, 12, 1, midwater)

# Seafloor behind wreck.
result.poly([(0,50),(8,48),(17,50),(28,47),(38,51),(47,48),(56,50),(64,47),(64,64),(0,64)], sand_dark)
result.poly([(0,54),(12,51),(24,54),(34,51),(45,55),(55,52),(64,53),(64,64),(0,64)], sand)
result.dither(0, 57, 64, 7, [sand, sand_light], pattern="bayer4")

# Broken mast and rigging behind hull.
result.line(23, 43, 33, 10, ink)
result.line(24, 42, 34, 10, wood_dark)
result.line(25, 39, 35, 10, wood_mid)
result.rect(32, 9, 5, 3, ink)
result.rect(33, 9, 3, 2, wood_light)
result.line(34, 13, 51, 29, navy)
result.line(33, 17, 15, 29, navy)
result.line(34, 17, 43, 24, patina)
# Torn sail remnant.
result.poly([(34,15),(43,23),(36,21),(33,28)], "#58746c")
result.poly([(35,17),(40,22),(35,20)], "#789086")
result.set(35,23, None)
result.set(36,23, None)

# Main hull black silhouette: stern broken left, bow raised right.
result.poly([(7,30),(13,30),(15,33),(22,32),(27,35),(44,34),(49,30),(55,27),(58,28),(56,39),(52,47),(46,52),(25,52),(16,48),(11,42)], ink)
# Wooden hull mass.
result.poly([(10,33),(16,34),(21,34),(27,37),(43,36),(50,32),(55,29),(54,38),(50,45),(45,49),(26,49),(18,46),(13,41)], wood_dark)
result.poly([(14,36),(22,36),(28,39),(44,38),(51,34),(53,32),(52,39),(47,45),(43,47),(27,47),(19,44),(15,40)], wood)
# Raised bow cap and broken stern teeth.
result.line(44,35, 55,28, wood_light)
result.line(45,36, 56,29, rust_hi)
result.rect(6,28,8,2, ink)
result.rect(8,29,5,2, wood_mid)
result.poly([(8,29),(8,24),(10,24),(11,30)], wood_dark)
result.poly([(13,32),(12,26),(14,27),(16,34)], wood_mid)

# Hull plank bands.
result.line(14,39,51,37, wood_mid)
result.line(15,40,50,38, wood_light)
result.line(18,44,47,44, wood_mid)
result.line(20,45,44,46, rust)
result.line(27,48,42,48, wood_light)
# Vertical ribs.
for x, y0, y1 in [(18,35,44),(24,36,47),(31,38,48),(38,37,48),(45,36,45),(50,33,41)]:
    result.line(x,y0,x-1,y1,ink)
    result.set(x,y0,wood_light)
# Gaps, rot and nail pixels.
result.rect(21,39,5,2, navy)
result.rect(34,42,6,2, ink)
result.rect(42,38,4,2, navy)
result.rect(27,45,3,2, navy)
result.set(17,38,rust_hi); result.set(29,40,rust); result.set(41,45,rust_hi)
result.set(48,38,rust_hi); result.set(24,43,rust_hi); result.set(35,38,rust)

# Corroded portholes and green patina streaks.
for cx, cy in [(25,38),(33,38),(41,37),(48,35)]:
    result.circle(cx,cy,2,ink)
    result.circle(cx,cy,1,patina)
    result.set(cx,cy,navy)
result.line(47,37,46,42,patina)
result.line(48,37,47,40,patina_hi)
result.line(34,40,33,45,patina)
result.set(32,44,patina_hi)
result.rect(52,33,2,5,rust)
result.set(53,34,rust_hi)

# Sand burial over the lower hull.
result.poly([(5,51),(14,48),(22,50),(29,49),(39,52),(48,48),(57,51),(64,50),(64,64),(0,64),(0,55)], sand)
result.poly([(0,57),(10,53),(19,55),(27,53),(37,56),(48,52),(58,55),(64,54),(64,64),(0,64)], sand_light)
result.dither(0, 58, 64, 6, [sand, sand_light], pattern="checker")
# Sand shadow and grains.
result.line(12,52,25,53,sand_dark)
result.line(37,54,50,51,sand_dark)
for x,y in [(4,58),(9,55),(17,60),(24,56),(31,61),(39,57),(47,59),(55,56),(60,61),(28,52),(52,53)]:
    result.set(x,y,sand_dark)

# Coral clusters foreground left and on bow.
result.line(8,58,8,48,coral_red)
result.line(8,52,4,49,coral_red)
result.line(8,54,12,50,coral_red)
result.line(5,55,3,52,coral_hi)
result.rect(7,47,2,4,coral_hi)
result.set(4,48,coral_hi); result.set(12,49,coral_hi); result.set(2,51,coral_red)
result.line(51,55,53,46,coral_pink)
result.line(53,50,57,47,coral_pink)
result.line(52,52,49,49,coral_hi)
result.set(53,45,coral_hi); result.set(58,46,coral_pink); result.set(48,48,coral_hi)

# Seaweed accents, angular pixel fronds.
result.line(15,60,14,52,kelp_dark)
result.line(14,55,11,52,kelp)
result.line(15,57,18,53,kelp_hi)
result.line(59,61,60,50,kelp_dark)
result.line(60,55,63,51,kelp)
result.line(60,57,57,52,kelp_hi)
result.line(56,61,55,55,kelp)

# School of fish, swimming left across open water.
def draw_fish(x,y,body,shine=False):
    result.poly([(x,y),(x+4,y-2),(x+8,y),(x+4,y+2)],body)
    result.poly([(x+8,y),(x+11,y-3),(x+10,y),(x+11,y+3)],body)
    result.set(x+2,y-1,fish_hi if shine else body)
    result.set(x+1,y,ink)

draw_fish(43,14,fish,True)
draw_fish(50,20,fish_hi,False)
draw_fish(37,24,fish,False)
draw_fish(53,10,patina_hi,True)
draw_fish(27,18,fish,True)
# Tiny distant fish silhouettes.
for x,y in [(8,17),(16,13),(6,25),(20,27)]:
    result.line(x,y,x+3,y,navy)
    result.set(x+4,y-1,navy); result.set(x+4,y+1,navy)

# Bubbles around the wreck.
for x,y in [(19,29),(21,25),(20,21),(48,29),(51,25),(7,43),(9,39)]:
    result.set(x,y,bubble)
result.circle(22,19,1,bubble,fill=False)
result.circle(52,23,1,bubble,fill=False)

# A few crisp foreground pebbles and shell marks.
result.rect(34,59,4,2,sand_dark)
result.rect(35,58,2,1,"#ead39a")
result.line(22,59,25,57,"#ead39a")
result.line(25,57,27,59,sand_dark)

view(result, scale=8, margin=0)
finish(result)
