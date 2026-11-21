output = input_canvas.copy(name='output')
# Convert the visible blade into a three-pixel wooden staff shaft.
output.rect(42, 40, 3, 14, '#5a3a20')
output.rect(43, 40, 1, 14, '#93785a')
# Gold finial above the grip and a small matching ferrule at the base.
output.circle(43, 38, 2, '#2e1f12')
output.circle(43, 38, 1, '#c9a227')
output.set(43, 38, '#eaedf3')
output.rect(42, 53, 3, 1, '#c9a227')
output.set(43, 53, '#eaedf3')
print(output.stats_text())
print(output.matrix_text(region=(39,35,47,56), indices=True))
finish(output)
