# 16x16 seamless Minecraft-style dirt material.
result = new_canvas(16, 16, background="#765038", name="minecraft_dirt")

# Restrained earthy palette.
shadow = "#3f291d"
deep = "#503322"
dark = "#60402c"
base2 = "#815a3f"
midlight = "#916746"
light = "#aa7950"
highlight = "#c08b5c"

# Broad, blocky soil clumps. Several continue through opposite tile edges.
result.poly([(14,1),(15,1),(15,5),(13,5),(13,3),(12,3),(12,2)], dark)
result.poly([(0,1),(2,1),(2,2),(3,2),(3,4),(1,4),(1,5),(0,5)], dark)
result.rect(15, 3, 1, 2, deep)
result.rect(0, 3, 1, 2, deep)

result.poly([(5,0),(8,0),(8,1),(9,1),(9,3),(7,3),(7,2),(5,2)], base2)
result.poly([(5,14),(7,14),(7,13),(9,13),(9,15),(5,15)], base2)
result.set(6, 0, light)
result.set(6, 15, light)

result.poly([(4,5),(7,5),(7,6),(8,6),(8,8),(6,8),(6,9),(4,9),(4,8),(3,8),(3,6)], deep)
result.rect(5, 6, 2, 2, shadow)
result.set(7, 7, dark)
result.set(4, 8, dark)

result.poly([(10,9),(13,9),(13,10),(14,10),(14,12),(12,12),(12,13),(10,13),(10,12),(9,12),(9,10)], base2)
result.rect(11, 10, 2, 2, midlight)
result.set(13, 11, light)

# Smaller irregular grains and chips.
for x, y, colour in [
    (4,1,deep),(10,0,deep),(11,1,dark),(3,0,midlight),
    (4,3,light),(5,3,midlight),(9,4,deep),(10,4,deep),(11,4,dark),
    (1,6,midlight),(2,6,light),(10,6,base2),(12,6,midlight),(13,6,midlight),
    (15,7,shadow),(0,7,shadow),(14,8,dark),(1,9,deep),(2,9,dark),
    (7,10,midlight),(8,10,light),(4,11,base2),(5,11,base2),(15,12,midlight),(0,12,midlight),
    (2,13,light),(3,13,midlight),(8,14,deep),(11,14,dark),(12,14,deep),(14,15,base2),
    (1,15,deep),(3,15,dark)
]:
    result.set(x, y, colour)

# A few paired pixels make the texture granular without turning into noise.
result.rect(10, 2, 2, 1, light)
result.rect(14, 6, 2, 1, base2)
result.rect(0, 10, 2, 1, base2)
result.rect(6, 12, 2, 1, dark)
result.rect(12, 15, 2, 1, midlight)
result.rect(12, 0, 2, 1, midlight)
result.set(2, 11, highlight)
result.set(9, 7, highlight)
result.set(3, 4, highlight)
result.set(14, 13, highlight)

view(result, scale=24, margin=0, edges="none")
finish(result)
