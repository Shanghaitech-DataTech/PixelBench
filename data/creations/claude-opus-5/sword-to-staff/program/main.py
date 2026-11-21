output = input_canvas.copy(name="output")

WHITE = output.color("#ffffff")
WOOD_L = output.color("#a97c45", name="wood_light")
WOOD_D = output.color("#6b4423")          # existing c15
BIND = output.color("#4a3120")            # existing c23
GOLD = output.color("#c9a227")            # existing c17
MET = output.color("#8e96a5")             # existing c20
MET_L = output.color("#c9ced8")           # existing c19
GEM = output.color("#4ec9de", name="gem")
GEM_D = output.color("#1f6f85", name="gem_dark")
GEM_L = output.color("#cdf7ff", name="gem_light")

# ---- 1. erase the old sword (crossguard y39-40, blade y41-55) ----
output.rect(41, 39, 6, 17, WHITE)         # x41..46, y39..55
output.set(40, 39, WHITE)
output.set(40, 40, WHITE)

# ---- 2. shaft: x43 (lit) / x44 (shadow) ----
# hidden behind the hat brim (y12-13) and behind the fist (y35-37)
HIDDEN = {12, 13, 35, 36, 37}
for y in list(range(10, 56)):
    if y in HIDDEN:
        continue
    output.set(43, y, WOOD_L)
    output.set(44, y, WOOD_D)

# ---- 3. leather bindings above and below the gripping fist ----
for y in (33, 34, 38, 39, 40):
    output.set(43, y, BIND)
    output.set(44, y, BIND)
output.set(43, 39, output.color("#5f402a"))   # existing c26, slight sheen

# ---- 4. metal ferrule at the foot of the staff ----
for y in (52, 53, 54, 55):
    output.set(43, y, MET_L)
    output.set(44, y, MET)
output.set(43, 55, MET)

# ---- 5. crystal head ----
gem_rows = {2: (43, 44), 3: (42, 45), 4: (41, 46), 5: (41, 46),
            6: (41, 46), 7: (42, 45), 8: (43, 44)}
for y, (x0, x1) in gem_rows.items():
    output.rect(x0, y, x1 - x0 + 1, 1, GEM)
# shading
for y in (4, 5, 6):
    output.set(46, y, GEM_D)
output.set(45, 3, GEM_D)
output.set(45, 7, GEM_D)
output.set(44, 8, GEM_D)
output.set(42, 7, GEM_D)
# highlight
output.set(43, 3, GEM_L)
output.set(42, 4, GEM_L)
output.set(43, 4, GEM_L)

# collar holding the crystal
output.rect(42, 9, 4, 1, GOLD)

print(output.stats_text())
view(output)
finish(output)
