# sword-to-staff edit
output = input_canvas.copy(name="output")

# Palette colours
c_bg = output.color("#ffffff")
c_outline = output.color("#2e1f12")
c_wood = output.color("#96613a")
c_wood_dark = output.color("#7a4a26")
c_gold = output.color("#c9a227")

c_gem_sparkle = output.color("#e6ffff")
c_gem_light = output.color("#80d8ff")
c_gem_mid = output.color("#0091ea")
c_gem_dark = output.color("#01579b")

# Step 1: Clear the original sword completely
# Blade: y=41..55, x=41..45
for y in range(41, 56):
    for x in range(41, 46):
        output.set(x, y, c_bg)

# Crossguard: y=39..40, x=40..46
for y in range(39, 41):
    for x in range(40, 47):
        output.set(x, y, c_bg)

# Grip / hilt under hand: y=38, x=40..45
for x in range(40, 46):
    output.set(x, 38, c_bg)

# Step 2: Draw the staff shaft from bottom (y=54) up to headpiece (y=11)
# Bottom ferrule at y=53..54
output.set(42, 54, c_outline)
output.set(43, 54, c_outline)
output.set(44, 54, c_outline)

output.set(42, 53, c_outline)
output.set(43, 53, c_gold)
output.set(44, 53, c_outline)

output.set(42, 52, c_outline)
output.set(43, 52, c_gold)
output.set(44, 52, c_outline)

# Wooden shaft below hand: y=39..51
for y in range(39, 52):
    output.set(42, y, c_outline)
    output.set(43, y, c_wood)
    output.set(44, y, c_outline)

# At hand level:
# y=38: hand bottom outline at x=40..41, staff at x=42..44
output.set(40, 38, c_outline)
output.set(41, 38, c_outline)
output.set(42, 38, c_outline)
output.set(43, 38, c_wood)
output.set(44, 38, c_outline)

# y=35..37: hand holding the staff
# Hand skin is at x=40..43, hand right outline at x=44
c_skin = output.color("#f2c49b")
for y in range(35, 38):
    output.set(40, y, c_skin)
    output.set(41, y, c_skin)
    output.set(42, y, c_skin)
    output.set(43, y, c_skin)
    output.set(44, y, c_outline)

# Wooden shaft above hand: y=11..34
for y in range(11, 35):
    output.set(42, y, c_outline)
    output.set(43, y, c_wood)
    output.set(44, y, c_outline)

# Preserve the tip of the hat brim at (45, 12)
output.set(45, 12, c_outline)

# Step 3: Draw the staff headpiece (y=5..10)
# y=10: Gold collar
output.set(42, 10, c_outline)
output.set(43, 10, c_gold)
output.set(44, 10, c_outline)

# y=9: Gold mounting base
output.set(41, 9, c_outline)
output.set(42, 9, c_gold)
output.set(43, 9, c_gold)
output.set(44, 9, c_gold)
output.set(45, 9, c_outline)

# y=8: Prongs holding the orb base
output.set(40, 8, c_outline)
output.set(41, 8, c_gold)
output.set(42, 8, c_outline)
output.set(43, 8, c_gem_dark)
output.set(44, 8, c_outline)
output.set(45, 8, c_gold)
output.set(46, 8, c_outline)

# y=7: Gem midsection with prong tips
output.set(40, 7, c_outline)
output.set(41, 7, c_gold)
output.set(42, 7, c_gem_light)
output.set(43, 7, c_gem_mid)
output.set(44, 7, c_gem_dark)
output.set(45, 7, c_gold)
output.set(46, 7, c_outline)

# y=6: Gem upper body
output.set(41, 6, c_outline)
output.set(42, 6, c_gem_sparkle)
output.set(43, 6, c_gem_light)
output.set(44, 6, c_gem_mid)
output.set(45, 6, c_outline)

# y=5: Gem top cap
output.set(42, 5, c_outline)
output.set(43, 5, c_gem_light)
output.set(44, 5, c_outline)

# y=4: Gem top outline
output.set(43, 4, c_outline)

view(output)
finish(output)
