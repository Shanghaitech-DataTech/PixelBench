# 32x32 forest slime RPG enemy sprite
result = new_canvas(32, 32, background=None, name="forest_slime_monster")

# Compact woodland palette
outline = result.color("#18251d", "outline")
deep = result.color("#263d2c", "deep_green")
body = result.color("#3f6541", "slime_green")
light = result.color("#638454", "slime_light")
high = result.color("#8da766", "slime_highlight")
shadow = result.color("#304c35", "slime_shadow")
moss_dark = result.color("#49612c", "moss_dark")
moss = result.color("#71863b", "moss")
moss_hi = result.color("#9aa84d", "moss_highlight")
wood = result.color("#76543a", "antler_wood")
wood_hi = result.color("#a4774b", "antler_light")
eye_glow = result.color("#d9f26a", "eye_glow")
eye_core = result.color("#f5ffb0", "eye_core")
red_dark = result.color("#7f2830", "cap_shadow")
red = result.color("#c94a3d", "mushroom_red")
red_hi = result.color("#ed7560", "cap_light")
stem = result.color("#d7c99a", "mushroom_stem")

# Tiny branching antlers, silhouetted first
# Left antler
result.line(10, 12, 8, 7, outline)
result.line(8, 8, 5, 5, outline)
result.line(6, 6, 6, 3, outline)
result.line(8, 7, 9, 3, outline)
result.line(9, 4, 11, 2, outline)
result.set(10, 2, outline)
result.line(10, 11, 9, 7, wood)
result.line(8, 7, 6, 5, wood)
result.set(6, 4, wood_hi)
result.line(9, 6, 9, 4, wood)
result.set(10, 3, wood_hi)
# Right antler
result.line(21, 12, 23, 7, outline)
result.line(23, 8, 26, 5, outline)
result.line(25, 6, 25, 3, outline)
result.line(23, 7, 22, 3, outline)
result.line(22, 4, 20, 2, outline)
result.set(21, 2, outline)
result.line(21, 11, 22, 7, wood)
result.line(23, 7, 25, 5, wood)
result.set(25, 4, wood_hi)
result.line(22, 6, 22, 4, wood)
result.set(21, 3, wood_hi)

# Mushroom behind the body on viewer's right
result.rect(23, 8, 3, 7, outline)
result.rect(24, 9, 1, 6, stem)
result.rect(21, 6, 7, 4, outline)
result.rect(22, 5, 5, 1, outline)
result.rect(23, 4, 3, 1, outline)
result.rect(22, 6, 5, 3, red)
result.rect(23, 5, 3, 1, red_hi)
result.set(22, 8, red_dark)
result.set(26, 8, red_dark)
result.set(24, 6, "#ffd0ad")

# Main slime outline: deliberately stepped pixel silhouette
outline_rows = {
    11:(12,8), 12:(9,14), 13:(7,18), 14:(6,20), 15:(5,22),
    16:(4,24), 17:(4,24), 18:(3,26), 19:(3,26), 20:(3,26),
    21:(3,26), 22:(3,26), 23:(3,26), 24:(4,24), 25:(4,24),
    26:(5,22), 27:(6,20), 28:(7,18), 29:(9,14)
}
for y, (x, w) in outline_rows.items():
    result.rect(x, y, w, 1, outline)

# Interior body bands
body_rows = {
    12:(13,6), 13:(10,12), 14:(8,16), 15:(7,18), 16:(6,20),
    17:(5,22), 18:(5,22), 19:(4,24), 20:(4,24), 21:(4,24),
    22:(4,24), 23:(4,24), 24:(5,22), 25:(5,22), 26:(6,20),
    27:(8,16), 28:(10,12)
}
for y, (x, w) in body_rows.items():
    result.rect(x, y, w, 1, body)

# Soft slime shading in chunky clusters
result.rect(6, 17, 2, 7, shadow)
result.rect(7, 15, 3, 2, light)
result.rect(8, 14, 6, 1, light)
result.rect(9, 15, 3, 1, light)
result.rect(6, 18, 2, 2, light)
result.set(8, 17, high)
result.rect(24, 18, 3, 6, deep)
result.rect(22, 24, 4, 2, deep)
result.rect(19, 27, 4, 1, deep)
result.rect(9, 27, 3, 1, shadow)

# Mossy crown and draping clumps
result.rect(10, 12, 12, 2, moss_dark)
result.rect(8, 13, 16, 2, moss)
result.rect(7, 14, 4, 2, moss)
result.rect(20, 14, 5, 2, moss)
result.rect(11, 14, 3, 3, moss)
result.rect(18, 14, 3, 4, moss_dark)
result.rect(23, 15, 2, 3, moss_dark)
result.set(9, 13, moss_hi)
result.rect(12, 13, 3, 1, moss_hi)
result.rect(21, 14, 2, 1, moss_hi)
result.set(8, 15, moss_hi)
# Side moss flecks
result.rect(5, 21, 2, 2, moss_dark)
result.set(6, 20, moss)
result.rect(25, 21, 2, 2, moss_dark)
result.set(25, 20, moss_hi)

# Dark eye sockets and luminous eyes
result.rect(8, 18, 6, 5, outline)
result.rect(18, 18, 6, 5, outline)
result.rect(9, 19, 4, 3, eye_glow)
result.rect(19, 19, 4, 3, eye_glow)
result.rect(10, 19, 2, 2, eye_core)
result.rect(20, 19, 2, 2, eye_core)
result.set(9, 22, deep)
result.set(22, 22, deep)

# Cute determined mouth and cheek marks
result.set(14, 24, outline)
result.rect(15, 25, 2, 1, outline)
result.set(17, 24, outline)
result.set(12, 24, light)
result.set(19, 24, light)

# Ground-contact lobes and wet highlights
result.rect(7, 28, 5, 1, outline)
result.rect(20, 28, 5, 1, outline)
result.rect(11, 28, 3, 1, shadow)
result.rect(18, 28, 3, 1, deep)
result.set(6, 24, high)
result.set(7, 23, light)
result.set(23, 26, moss_dark)

finish(result)
view(result, scale=16, margin=0)
