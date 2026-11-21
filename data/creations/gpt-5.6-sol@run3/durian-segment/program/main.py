output = input_canvas.copy(name="output")

# Remove the lower-left flesh lobe. These spans follow its stepped outer edge
# and stop at the orange diagonal that separates it from the middle lobe.
spans = {
    34:(17,20), 35:(16,21), 36:(15,21), 37:(14,22), 38:(13,22),
    39:(12,23), 40:(11,24), 41:(10,25), 42:(9,26), 43:(8,27),
    44:(7,28), 45:(6,29), 46:(5,30), 47:(5,31), 48:(5,33),
    49:(6,35), 50:(7,36), 51:(9,36), 52:(10,35), 53:(13,32),
    54:(20,29),
}
black = output.color("c1")
dark = output.color("c2")
rust = output.color("c4")
orange = output.color("c3")
ochre = output.color("c8")

for y, (x0, x1) in spans.items():
    for x in range(x0, x1 + 1):
        if output.get(x, y) != black:
            output.set(x, y, rust)

# Blocky facets and shadowed creases make the newly exposed rind consistent
# with the rind already visible along the right and lower edges.
output.poly([(17,34),(20,34),(22,39),(25,42),(24,46),(19,43),(16,39)], dark)
output.poly([(8,43),(12,39),(17,38),(18,43),(14,47),(8,47)], orange)
output.poly([(6,47),(14,47),(18,51),(13,53),(8,51)], dark)
output.poly([(18,44),(24,43),(29,47),(28,51),(22,52),(17,49)], orange)
output.poly([(27,47),(33,49),(35,51),(32,53),(27,52)], ochre)
output.rect(11, 42, 4, 3, ochre)
output.rect(13, 48, 5, 2, rust)
output.rect(21, 37, 2, 4, orange)
output.rect(23, 49, 4, 3, dark)

# Restore any black contour pixels captured by facet fills from the source.
for y, (x0, x1) in spans.items():
    for x in range(x0, x1 + 1):
        if input_canvas.get(x, y) == black:
            output.set(x, y, black)

view(output, scale=8, margin=0)
finish(output)
