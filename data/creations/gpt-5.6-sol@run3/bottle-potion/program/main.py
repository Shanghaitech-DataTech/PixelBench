output = input_canvas.copy(name="output")

# Purple potion ramp, matched to the original liquid's value structure.
dark = output.color("#54207f", "potion_shadow")
mid = output.color("#7b32ad", "potion_mid")
light = output.color("#a956d0", "potion_light")
shine = output.color("#df9cff", "potion_shine")
deep = output.color("#32104f", "bubble_deep")
glow = output.color("#f2c6ff", "bubble_glow")

# Recolour only the original water pixels; bottle, stopper, and outline stay exact.
recolour = {5: mid, 6: light, 7: shine, 8: shine, 10: light}
for y in range(64):
    for x in range(64):
        old = output.get(x, y)
        if old in recolour:
            output.set(x, y, recolour[old])

# Strengthen the upper potion layer as a darker, gently uneven magical surface.
for x0, x1, y in [(16, 39, 25), (12, 45, 27), (6, 49, 29), (4, 51, 31),
                  (4, 51, 33), (4, 49, 35)]:
    for x in range(x0, x1 + 1):
        if output.get(x, y) in (mid, light, shine):
            output.set(x, y, dark)
        if y + 1 < 64 and output.get(x, y + 1) in (mid, light, shine):
            output.set(x, y + 1, dark)

# Pixel bubbles: dark rims, bright inner liquid, and tiny specular corners.
def bubble(cx, cy, r):
    output.circle(cx, cy, r, deep, fill=True)
    if r >= 3:
        output.circle(cx, cy, r - 2, light, fill=True)
        output.set(cx - 1, cy - 1, glow)
        output.set(cx, cy - 1, glow)
    else:
        output.set(cx, cy, glow)

bubble(17, 34, 3)
bubble(39, 35, 2)
bubble(28, 42, 4)
bubble(44, 47, 3)
bubble(16, 51, 2)
bubble(34, 55, 2)

# Bubbles breaking free above the surface into the bottle's air chamber.
output.circle(30, 22, 2, deep, fill=True)
output.set(30, 22, glow)
output.set(31, 22, glow)
output.circle(36, 17, 1, mid, fill=True)
output.set(36, 17, glow)
output.circle(25, 18, 1, deep, fill=True)
output.set(25, 18, shine)
output.rect(42, 22, 2, 2, shine)

# Rising fizz and reflected magic along the body, kept on the 2px visual rhythm.
for x, y in [(23, 31), (31, 34), (47, 38), (21, 45), (39, 43),
             (12, 42), (24, 55), (42, 57), (18, 59)]:
    if output.get(x, y) in (dark, mid, light, shine):
        output.rect(x, y, 2, 2, glow)

# Foamy glints where bubbles meet the potion surface.
for x, y in [(13, 29), (20, 27), (34, 29), (43, 31)]:
    if output.get(x, y) in (dark, mid, light, shine):
        output.rect(x, y, 2, 1, shine)

# A subtle violet shadow at the bottom makes the potion read as luminous and deep.
for x, y in [(18, 58), (20, 60), (22, 62), (34, 60), (36, 58), (38, 56)]:
    if output.get(x, y) in (mid, light, shine):
        output.rect(x, y, 2, 2, mid)

view(output, scale=8, margin=0)
finish(output)
