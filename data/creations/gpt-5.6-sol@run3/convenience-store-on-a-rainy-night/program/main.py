# 64x64 rainy-night convenience store pixel art
result = new_canvas(64, 64, background="#111827", name="rainy_convenience_store")

# Palette
sky = "#111827"
sky2 = "#17223a"
cloud = "#24304a"
far = "#1b2941"
outline = "#090f1d"
wall = "#34445a"
wall_lite = "#52647a"
trim = "#d6e0dc"
trim_shadow = "#79898f"
window = "#ffd66b"
window_hi = "#fff1a6"
window_dim = "#d9a94e"
inside = "#e47c45"
red = "#d94b4b"
cyan = "#55c9d5"
blue = "#287c9c"
road = "#18263a"
road2 = "#20344a"
puddle = "#31526b"
puddle_hi = "#7cb7bd"
rain = "#7b9fba"
coat = "#d6a62f"
coat_hi = "#f2cf58"
skin = "#d89b72"
dark = "#101722"
metal = "#8ca1a9"
green = "#5c9b70"

# Night sky, clouds, distant buildings
result.rect(0, 0, 64, 22, sky)
result.rect(0, 8, 64, 14, sky2)
result.poly([(0,10),(8,8),(16,10),(23,7),(34,9),(42,6),(53,9),(63,7),(63,15),(0,15)], cloud)
result.rect(0, 16, 9, 17, far).rect(55, 14, 9, 19, far)
result.rect(2, 20, 2, 3, "#49617a").rect(58, 18, 2, 3, "#49617a")

# Store body and roof
result.rect(6, 18, 51, 3, outline)
result.rect(5, 21, 53, 4, trim)
result.rect(7, 25, 49, 23, wall)
result.rect(5, 24, 53, 2, trim_shadow)
# Red/cyan generic fascia without lettering or logos
result.rect(9, 21, 45, 1, red)
result.rect(13, 23, 37, 1, cyan)
result.rect(6, 47, 52, 3, outline)

# Lit windows and door frames
result.rect(9, 27, 19, 18, outline)
result.rect(10, 28, 8, 16, window)
result.rect(19, 28, 8, 16, window_hi)
result.rect(29, 27, 12, 21, outline)
result.rect(30, 28, 10, 19, window)
result.rect(42, 27, 12, 18, outline)
result.rect(43, 28, 10, 16, window_hi)
# warm ceiling and shelves
result.rect(10, 28, 17, 3, window_hi)
result.rect(43, 28, 10, 3, window)
result.rect(11, 35, 15, 2, inside)
result.rect(11, 38, 15, 1, red)
result.rect(12, 39, 3, 3, green).rect(16, 39, 3, 3, blue).rect(20, 39, 2, 3, red).rect(23,39,3,3,green)
result.rect(44, 35, 8, 2, inside)
result.rect(45, 38, 2, 4, cyan).rect(48,38,3,4,red)
# window shine and mullions
result.rect(17, 28, 2, 16, trim_shadow)
result.rect(48, 28, 1, 16, "#e9d993")
result.line(11,29,11,34,"#fff8c7").line(20,29,24,29,"#fff8c7")
# glass door
result.rect(30, 29, 10, 18, "#ebb85b")
result.rect(31, 30, 8, 8, window_hi)
result.rect(31, 39, 8, 7, "#b97845")
result.rect(38, 37, 1, 2, dark)
result.line(31,31,38,38,"#f9e7a0")

# sidewalk and curb
result.rect(0, 50, 64, 4, "#4b5863")
result.rect(0, 54, 64, 2, "#92999a")
result.rect(0, 56, 64, 8, road)
result.rect(0, 58, 64, 6, road2)
result.rect(7, 51, 17, 1, "#718083").rect(44,52,13,1,"#718083")

# Umbrella rack on left, with several umbrellas
result.rect(1, 43, 8, 2, metal)
result.rect(2, 45, 6, 5, "#303c49")
result.rect(3, 46, 4, 1, wall_lite)
result.line(3,43,3,35,metal).line(5,43,5,33,metal).line(7,43,7,36,metal)
result.poly([(1,36),(3,33),(5,36)], blue)
result.poly([(3,34),(5,31),(8,34)], red)
result.poly([(5,37),(7,34),(9,37)], cyan)

# Parked bicycle on right
result.circle(48, 49, 5, dark, fill=False).circle(59,49,5,dark,fill=False)
result.circle(48,49,4,metal,fill=False).circle(59,49,4,metal,fill=False)
result.line(48,49,53,43,metal).line(53,43,57,49,metal).line(57,49,48,49,metal)
result.line(53,43,51,49,metal).line(51,49,57,49,metal)
result.line(52,42,55,42,dark).line(57,49,60,41,metal).line(59,41,62,41,metal)
result.set(53,48,window_dim).set(54,48,window_dim)
# crisp bicycle hubs and frame accents
result.set(48,49,"#d9e0d7").set(59,49,"#d9e0d7")
result.set(53,43,red).set(60,42,red)

# Person in yellow raincoat stepping into door
# back leg and boot
result.rect(34, 46, 3, 7, dark).rect(37,47,3,6,dark)
result.rect(33,52,5,2, outline).rect(37,52,5,2,outline)
# coat silhouette and hood
result.poly([(32,39),(34,35),(38,35),(41,39),(41,48),(38,49),(32,48)], outline)
result.circle(36,35,4,outline)
result.circle(36,35,3,coat)
result.rect(34,35,5,4,coat)
result.poly([(33,38),(39,38),(41,48),(32,48)], coat)
result.rect(33,39,1,7,coat_hi)
result.line(39,39,42,42,coat).line(42,42,40,45,coat)
result.set(36,34,skin).set(37,34,skin)
result.line(37,39,37,47,"#9b7425")

# Rain streaks, kept sparse over key silhouettes
for x,y in [(3,4),(12,2),(20,6),(30,3),(39,1),(50,4),(60,1),(8,14),(18,12),(28,15),(38,11),(49,14),(61,10),(2,26),(60,27),(1,38),(61,35),(13,17),(45,17)]:
    result.line(x,y,x-1,y+3,rain)
# bright rain caught by storefront light
for x,y in [(11,46),(16,48),(24,46),(45,46)]:
    result.line(x,y,x-1,y+2,"#b8d0c8")

# Wet road puddles and broken reflections
result.rect(4,58,18,2,puddle).rect(40,57,20,2,puddle)
result.rect(8,57,9,1,puddle_hi).rect(45,56,10,1,puddle_hi)
result.rect(12,60,10,1,"#546f75").rect(36,61,18,1,"#3c6370")
# warm vertical reflections
result.rect(14,56,3,2,window_dim).rect(15,59,2,3,"#8b6740")
result.rect(24,56,2,4,"#a77742").rect(25,61,1,2,"#5d5547")
result.rect(32,56,4,2,"#b78144").rect(33,59,2,3,"#72583f")
result.rect(46,59,5,1,"#6f825f")
# ripple highlights
result.line(1,62,12,62,puddle_hi).line(27,57,37,57,"#6c8f91").line(51,63,63,63,puddle_hi)
result.line(4,60,8,60,"#496f80").line(38,59,44,59,"#5b7f86")

# Pixel accents: drips, door threshold, wheel highlights
result.rect(29,47,13,2,outline).rect(31,47,9,1,trim_shadow)
result.set(46,46,"#d9e0d7").set(58,46,"#d9e0d7")

view(result, scale=8, margin=0)
finish(result)
