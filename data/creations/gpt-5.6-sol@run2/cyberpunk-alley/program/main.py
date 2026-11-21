# Cyberpunk alley, 128x128
# Astra Pixel Art API objects are preloaded by the environment.

W = H = 128
base = new_canvas(W, H, "#070914", name="cyberpunk_alley_base")

# Palette
sky = "#090b1b"
black = "#050711"
ink = "#0b1020"
wall_l = "#17162b"
wall_r = "#10182a"
wall_hi = "#25213b"
blue_dark = "#102c42"
blue = "#16708a"
cyan = "#27e7e1"
cyan_hi = "#b9fff4"
magenta = "#f02b9b"
pink_hi = "#ff90dd"
purple = "#702b8f"
red = "#ef315f"
yellow = "#ffd35a"
warm = "#ff8b3d"
white = "#d8f7ff"
road = "#0b1522"
road_mid = "#132738"
road_hi = "#285069"

# Distant sky and alley mouth
base.rect(0, 0, 128, 55, sky)
base.poly([(42, 0), (86, 0), (76, 58), (52, 58)], "#0c1023")
base.rect(53, 29, 23, 27, "#131a30")
base.rect(58, 38, 13, 18, "#16263a")
base.rect(61, 44, 8, 12, "#2a4051")

# Left and right building masses, perspective edges
base.poly([(0, 0), (44, 0), (49, 55), (0, 86)], wall_l)
base.poly([(128, 0), (84, 0), (78, 55), (128, 85)], wall_r)
base.poly([(0, 14), (39, 8), (44, 58), (0, 78)], "#1b1930")
base.poly([(128, 10), (91, 7), (83, 58), (128, 77)], "#121d30")
# Facade bands and brick/panel texture
for y in (8, 22, 39, 57):
    base.line(0, y, 43 + y//8, y+2, "#29233d")
for y in (16, 34, 51):
    base.line(128, y, 87-y//12, y+2, "#1d3144")
base.rect(3, 48, 31, 3, "#0a0d19")
base.rect(91, 44, 37, 3, "#080c17")
# Small windows
for x, y in [(5,9),(19,7),(32,11),(7,29),(27,27)]:
    base.rect(x, y, 7, 6, "#0b101c")
    base.rect(x+1, y+1, 5, 1, purple)
for x, y in [(101,13),(114,10),(95,30),(112,28)]:
    base.rect(x, y, 8, 7, "#09101d")
    base.rect(x+1, y+1, 6, 1, blue)

# Left neon shop sign and bracket
base.rect(3, 18, 31, 25, "#090b16")
base.rect(4, 19, 29, 23, magenta, fill=False)
base.rect(6, 21, 25, 19, "#311138")
base.text(9, 24, "NITE", pink_hi, font="5x7", spacing=1)
base.text(9, 33, "BAR", yellow, font="5x7", spacing=1)
base.line(34, 25, 44, 29, "#56304f")
base.line(34, 38, 46, 38, "#56304f")
# Neon glow pixels
base.line(2, 20, 2, 40, purple)
base.line(35, 21, 35, 40, purple)
base.set(1, 25, magenta); base.set(36, 33, magenta)

# Right vertical sign
base.rect(94, 8, 25, 35, "#070b13")
base.rect(95, 9, 23, 33, cyan, fill=False)
base.rect(98, 12, 17, 27, "#0d3543")
base.text(100, 14, "24H", cyan_hi, font="5x7", spacing=0)
base.text(100, 24, "OPEN", yellow, font="5x7", spacing=0)
base.rect(91, 15, 3, 5, "#354457")
base.rect(91, 34, 3, 5, "#354457")
# Smaller hanging magenta glyph sign
base.rect(79, 25, 13, 20, "#100916")
base.rect(80, 26, 11, 18, magenta, fill=False)
base.text(83, 30, "X", pink_hi, font="5x7")

# Shop awnings and doorways
base.poly([(0, 52), (39, 49), (44, 56), (0, 62)], "#090b15")
base.line(1, 53, 38, 51, magenta)
for x in range(3, 39, 8):
    base.line(x, 54, x+4, 59, "#5a214f")
base.rect(2, 62, 30, 26, "#080b13")
base.rect(5, 65, 22, 20, "#121929")
base.line(6, 67, 26, 65, pink_hi)
base.rect(97, 53, 31, 34, "#070b12")
base.poly([(91, 50), (128, 54), (128, 61), (88, 57)], "#0a101b")
base.line(91, 51, 127, 55, cyan)

# Vending machines on right
base.rect(101, 58, 20, 32, "#203448")
base.rect(103, 60, 16, 27, "#0b1724")
base.rect(105, 62, 12, 11, "#b8eef0")
base.rect(106, 63, 3, 3, cyan)
base.rect(110, 63, 3, 3, magenta)
base.rect(114, 63, 2, 3, yellow)
base.rect(106, 68, 3, 3, yellow)
base.rect(110, 68, 3, 3, cyan)
base.rect(114, 68, 2, 3, red)
base.rect(105, 76, 8, 2, "#37516a")
base.rect(114, 76, 3, 7, blue)
base.rect(105, 81, 7, 4, black)
base.line(101, 89, 120, 89, cyan)
# Side vending unit
base.rect(88, 63, 11, 27, "#32203b")
base.rect(90, 65, 7, 9, "#ff78bd")
base.rect(90, 77, 7, 2, purple)
base.rect(90, 82, 5, 5, "#101522")

# Pipes and utility boxes
base.line(36, 0, 39, 52, "#070912")
base.line(39, 0, 42, 51, "#3a2942")
base.rect(35, 44, 9, 11, "#323145")
base.rect(37, 46, 5, 4, "#111827")
base.line(122, 44, 122, 85, "#314052")
base.rect(121, 65, 7, 12, "#1d2937")

# Power cables overhead
base.line(0, 5, 47, 18, black)
base.line(0, 7, 47, 20, "#252035")
base.line(128, 4, 79, 19, black)
base.line(128, 6, 79, 21, "#1e2b3c")
base.path("M 17 0 Q 60 31 111 2", "#03050b", fill=False)
base.path("M 3 12 Q 55 34 125 14", "#252035", fill=False)
base.path("M 43 0 Q 64 26 90 0", "#050712", fill=False)
# Cable ties / droplets
for x,y in [(24,12),(48,20),(68,21),(91,15),(108,9)]:
    base.line(x,y,x,y+3,"#4c425a")

# Ground plane and perspective seams
base.poly([(0, 84), (50, 55), (77, 55), (128, 85), (128,128), (0,128)], road)
base.poly([(44, 66), (56, 57), (70,57), (89,128), (22,128)], "#0d1b29")
base.line(0, 96, 56, 60, road_mid)
base.line(128, 99, 71, 60, road_mid)
base.line(12, 128, 58, 58, "#182938")
base.line(111, 128, 69, 58, "#172b3a")
base.line(63, 58, 63, 127, "#07111c")
# Cobble/asphalt fragments
for x,y,w in [(3,102,18),(28,91,14),(82,92,17),(101,108,23),(6,118,25),(39,110,13),(76,117,16)]:
    base.line(x,y,x+w,y, "#1a3040")
    base.set(x+w//2,y+1,"#0a111b")

# Puddles and neon reflections
base.poly([(2,100),(26,96),(42,100),(35,106),(9,107)], "#122c3d")
base.line(5,101,33,100, magenta)
base.line(11,103,39,102, purple)
base.line(4,105,28,105, "#4b2860")
base.poly([(75,95),(102,92),(123,98),(115,104),(83,105)], "#133446")
base.line(82,96,117,97, cyan)
base.line(77,100,110,101, blue)
base.line(88,103,121,102, "#1d7181")
base.poly([(38,116),(63,111),(95,116),(85,123),(47,123)], "#17283a")
base.line(45,117,87,117, magenta)
base.line(51,120,82,120, "#6d2d74")
# Vertical broken reflections
for x,y,h,col in [(12,65,27,magenta),(18,68,20,purple),(28,61,30,red),(108,91,24,cyan),(115,91,31,blue),(96,91,18,yellow),(83,46,38,magenta)]:
    for yy in range(y, y+h, 6):
        width = 1 + ((yy + x) % 3)
        base.rect(x-width//2, yy, width, 3, col)
# Ground shine specks
for x,y,col in [(4,92,cyan),(34,99,pink_hi),(47,87,blue),(75,91,cyan),(123,94,magenta),(18,113,cyan),(102,119,pink_hi),(58,126,cyan),(72,106,white)]:
    base.line(x,y,x+3,y,col)

# Rain on background: diagonal short streaks
rain_back = [(8,3),(24,2),(53,5),(72,2),(89,7),(121,1),(14,44),(48,31),(66,12),(75,36),(87,50),(111,46),(30,58),(53,48),(98,49),(118,39),(7,73),(39,70),(77,68),(125,70),(25,84),(95,82)]
for x,y in rain_back:
    base.line(x,y,x-1,y+4, "#3b7187")

# Person and umbrella are separate so the translucent canopy composites correctly.
fg = new_canvas(W, H, None, name="umbrella_figure")
# Transparent umbrella canopy with segmented arcs
canopy = "#57dbe073"
fg.path("M 43 78 Q 64 57 87 78 Q 79 76 73 80 Q 67 75 61 80 Q 54 75 48 80 Q 46 78 43 78 Z", canopy, fill=False)
fg.path("M 43 78 Q 64 57 87 78", cyan_hi, fill=False)
fg.line(43,78,87,78, "#8ffcf0")
fg.path("M 64 62 Q 59 70 61 79", "#6ac7d0", fill=False)
fg.path("M 64 62 Q 71 70 73 79", "#6ac7d0", fill=False)
fg.set(63,61,white); fg.set(64,61,white)
# Umbrella shaft and handle
fg.line(64,78,64,110, "#a8d5da")
fg.path("M 64 108 V 112 Q 64 116 68 114", "#a8d5da", fill=False)
# Human silhouette, coat, head and legs
fg.circle(65,82,4, "#070910")
fg.rect(62,85,7,17, black)
fg.poly([(61,87),(69,87),(75,105),(70,107),(66,96),(64,108),(56,105)], "#080a12")
fg.line(59,91,63,99, "#172334")
fg.line(69,90,73,101, "#172334")
fg.poly([(60,103),(65,103),(63,119),(58,119)], "#05070c")
fg.poly([(66,103),(71,104),(75,118),(70,119)], "#05070c")
fg.line(56,120,63,120, "#172b36")
fg.line(70,120,77,120, "#172b36")
# Rim light makes silhouette readable
fg.line(60,84,60,99, magenta)
fg.set(59,87,pink_hi)
fg.line(69,85,71,99, cyan)
fg.line(58,119,63,119, magenta)
fg.line(71,119,76,119, cyan)
# Foreground rain streaks
for x,y,l in [(3,34,8),(17,55,7),(39,15,9),(49,82,8),(79,4,9),(91,65,8),(104,28,9),(124,54,8),(30,101,7),(84,102,10),(119,108,8),(9,89,6),(53,25,6)]:
    fg.line(x,y,x-2,y+l, "#8cdce5")
    fg.set(x-2,y+l+1,"#d4ffff")
# Rain splashes
for x,y in [(7,108),(31,108),(46,124),(83,110),(98,106),(118,124)]:
    fg.line(x-3,y,x+3,y,"#64aeba")
    fg.set(x,y-1,cyan_hi)

result = flatten([base, fg], name="cyberpunk_alley")
view(result, scale=4, margin=0)
finish(result)
