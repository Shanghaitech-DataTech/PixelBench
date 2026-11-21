output = input_canvas.copy(name="output")

# Palette sampled and extended to match the source's nocturnal pixel-art range.
sky = "#0b3547"
sky_dark = "#082b3b"
sky_deep = "#062330"
cloud = "#145066"
cloud_hi = "#28758d"
outline = "#101a2b"
purple = "#28205d"
purple_mid = "#403079"
purple_hi = "#6750a2"
panel = "#f1ded6"
panel_hi = "#fff1e6"
panel_shadow = "#c9a9b1"
slot = "#532f39"
red = "#9d493f"
orange = "#d78145"
yellow = "#efbd6c"
metal = "#304c55"
metal_hi = "#648087"
rubber = "#111b25"
black = "#0a1721"

# Remove the person: restore open sky to the left of the machine.
output.poly([(72,69),(80,65),(82,116),(75,124),(70,111)], sky, fill=True)
output.dither(72,72,9,48,[sky,sky_dark],pattern="bayer4")
output.line(72,91,80,94,cloud)
output.line(73,106,80,105,cloud)

# Reconstruct the vending machine front and the portion hidden by the figure.
output.poly([(84,58),(91,56),(112,56),(116,60),(116,108),(110,114),(83,113),(82,65)], outline)
output.poly([(86,60),(112,59),(114,62),(114,105),(108,111),(84,110),(84,64)], panel)
output.rect(87,61,25,4,panel_hi)
output.rect(86,66,27,1,panel_shadow)
output.rect(86,68,27,18,"#ead8d2")
# Product windows, rebuilt in three crisp rows.
for y in (69,79,89):
    output.rect(88,y,22,8,"#fff0df")
    output.line(88,y+8,110,y+8,panel_shadow)
# Bottles and cans.
products = [
    (89,70,orange),(94,69,"#62a87e"),(100,70,"#d05c56"),(106,69,"#5ca7b8"),
    (89,80,"#d9914e"),(95,80,"#5d8fc2"),(101,79,"#75ad68"),(106,80,"#996bc4"),
    (89,90,"#d85f55"),(95,89,"#e9a83d"),(101,90,"#64a8a1"),(106,89,"#b76aab")]
for x,y,c in products:
    output.rect(x,y,3,6,c)
    output.set(x+1,y-1,panel_hi)
    output.set(x+2,y+1,"#ffffff")
# Lower control and dispensing area.
output.rect(86,99,26,10,"#efe0d6")
output.rect(88,100,6,5,slot)
output.rect(96,100,14,2,panel_shadow)
output.rect(97,103,12,5,"#5b3139")
output.rect(99,104,8,2,"#1d2029")
output.set(111,101,"#d87a4e")
output.set(111,104,"#62b09a")
output.line(84,109,109,109,purple_hi)

# Restore the machine's lower body behind the motorcycle.
output.poly([(83,111),(109,111),(115,106),(116,145),(108,149),(82,145)], purple)
output.dither(84,114,29,31,[purple,"#312569"],pattern="bayer4")
output.rect(87,116,23,3,"#1c1d48")
output.rect(90,121,18,2,purple_hi)
output.rect(88,126,21,2,"#171b3e")
output.rect(92,132,15,8,"#241d51")
output.line(91,135,106,135,"#564490")

# Rebuild the motorcycle where the character covered it: seat, tank, frame and engine.
output.poly([(55,117),(64,114),(75,115),(80,119),(74,123),(60,123)], outline)
output.poly([(56,117),(65,115),(74,116),(78,119),(72,121),(59,121)], "#713b3e")
output.line(60,117,73,117,"#b05b55")
output.poly([(75,119),(88,115),(98,116),(103,121),(96,127),(82,126)], black)
output.poly([(80,120),(91,117),(99,119),(95,123),(83,124)], "#183746")
output.line(81,121,96,119,metal_hi)
output.line(76,125,96,139,metal)
output.line(97,123,88,140,metal_hi)
output.line(76,125,88,141,"#1c3039")
output.circle(92,134,7,outline)
output.circle(92,134,5,"#735e59")
output.circle(92,134,3,metal_hi)
output.rect(86,128,10,5,"#8f7d72")
output.line(88,129,96,127,"#b6a08c")
# Handlebar and small front details.
output.line(86,116,100,111,metal_hi)
output.line(99,111,104,113,outline)
output.line(101,111,106,110,metal_hi)
output.set(106,110,"#d9e5d8")

# Lightning behind the foreground, as an angular high-contrast bolt in the open sky.
lightning_glow = "#53b9d1aa"
lightning = "#d9f5e8"
output.poly([(55,4),(50,18),(54,18),(46,32),(51,29),(47,42),(62,24),(56,25),(63,13),(57,15)], lightning_glow)
output.poly([(54,5),(51,19),(55,19),(48,30),(52,28),(49,38),(59,24),(54,25),(60,15),(55,17)], lightning)
output.set(55,7,"#ffffff")

# Storm layer: translucent diagonal rain, beads clinging to surfaces, and wet-road reflections.
storm = new_canvas(170,170,background=None,name="storm")
rain_far = "#72c7d35c"
rain_mid = "#a2e0df86"
rain_near = "#d5f4eab0"
# Structured rain field, varied lengths and opacity.
for i in range(54):
    x = (i * 29 + 7) % 168
    y = (i * 47 + 11) % 154
    length = 2 + (i % 4)
    col = rain_far if i % 3 else rain_mid
    storm.line(x,y,x-1,y+length,col)
for x,y in [(9,30),(24,66),(42,14),(68,48),(119,17),(146,39),(161,74),(20,104),(52,92),(132,100),(157,119),(74,6),(114,71),(35,130),(125,132)]:
    storm.line(x,y,x-2,y+6,rain_near)
    storm.set(x-2,y+7,"#e6fff0a0")

# Wet ground: dark glaze, puddles, ripples, and reflected machine/lightning colours.
storm.rect(0,151,170,19,"#061b2690")
storm.dither(0,154,170,16,["#1839477a","#24485866"],pattern="bayer4")
storm.ellipse(139,164,26,3,"#2389a07d")
storm.ellipse(139,164,17,1,"#74cbd1a2",fill=False)
storm.ellipse(31,160,23,2,"#3b6a7670",fill=False)
storm.ellipse(95,165,18,2,"#644f8670",fill=False)
storm.poly([(112,151),(119,151),(126,168),(117,168)],"#58438a70")
storm.poly([(51,153),(54,153),(47,169),(41,169)],"#bdded88a")
# Small splashes and clinging droplets along the bike, machine and ground edge.
for x,y in [(5,153),(18,155),(39,151),(58,150),(75,153),(103,150),(129,149),(148,153),(164,151),(113,119),(115,91),(84,106),(106,135),(64,123),(92,145),(49,132)]:
    storm.set(x,y,rain_near)
    storm.set(x-1,y+1,rain_mid)
for x,y in [(12,158),(27,163),(43,156),(69,160),(82,166),(110,158),(132,161),(154,166)]:
    storm.line(x-3,y,x+3,y,rain_mid)
    storm.set(x,y-1,rain_near)

result = flatten([output,storm],name="result")
view(result,scale=3,margin=0)
finish(result)
