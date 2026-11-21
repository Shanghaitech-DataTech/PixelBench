# 16x16 glowing deep-water jellyfish enemy
result = new_canvas(16, 16, background=None, name="glow-jellyfish")

# Palette: dark ocean outline, saturated cyan glow, pale core.
outline = result.color("#102747", "deep outline")
rim = result.color("#1688a8", "blue rim")
glow = result.color("#31d6d2", "cyan glow")
light = result.color("#a8fff0", "bell light")
hot = result.color("#e4fff2", "hot highlight")
shade = result.color("#176582", "cool shade")
soft = result.color("#48e7dbb8", "translucent glow")

# Bell outline: broad dome with a slightly scalloped lower edge.
result.poly([(3,7),(3,5),(4,3),(6,2),(9,2),(11,3),(12,5),(12,8),
             (10,9),(9,8),(8,9),(7,8),(6,9),(4,8)], outline)

# Luminous translucent bell interior.
result.poly([(4,7),(4,5),(5,4),(6,3),(9,3),(11,5),(11,7),
             (10,8),(9,7),(8,8),(7,7),(6,8),(5,7)], soft)
result.set(5,5,rim).set(5,6,glow)
result.set(6,4,glow).set(6,5,light).set(6,6,glow)
result.set(7,3,light).set(7,4,hot).set(7,5,light).set(7,6,glow)
result.set(8,3,light).set(8,4,light).set(8,5,glow).set(8,6,glow)
result.set(9,4,glow).set(9,5,glow).set(9,6,rim)
result.set(10,5,rim).set(10,6,shade)

# Reassert crisp lower rim and scallops.
result.set(4,7,rim).set(5,7,glow).set(6,8,outline)
result.set(7,7,light).set(8,8,outline).set(9,7,glow)
result.set(10,8,outline).set(11,7,rim)

# Four short, curling tentacles with bright inner strands.
result.set(5,9,outline).set(5,10,outline).set(4,11,outline).set(4,12,outline).set(5,13,outline)
result.set(6,9,glow).set(6,10,glow).set(6,11,outline).set(6,12,outline)
result.set(8,9,outline).set(8,10,glow).set(8,11,glow).set(9,12,outline).set(9,13,outline).set(8,14,outline)
result.set(10,9,outline).set(10,10,glow).set(11,11,outline).set(11,12,outline).set(10,13,outline)

# Tiny emissive tips and detached glow motes.
result.set(5,12,glow).set(8,13,glow).set(10,12,glow)
result.set(2,6,"#31d6d288").set(13,4,"#48e7db88").set(13,9,"#31d6d266")

finish(result)
view(result, scale=24, margin=1, edges="all")
