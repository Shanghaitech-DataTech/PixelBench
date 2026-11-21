out = input_canvas.copy(name='output')

# Erase blade + crossguard (x 41..47, y 3..40)
out.rect(41, 3, 7, 38, None)

for nm, hx in [('p', '#6b4423'), ('q', '#5c3a21'), ('r', '#c9a227'), ('s', '#eaedf3')]:
    out.color(hx, name=nm)

# Staff shaft rising from the hand (hand/grip at x 39-40, y 43+)
out.rect(39, 8, 1, 35, 'p')   # light wood
out.rect(40, 8, 1, 35, 'q')   # shaded wood

# Orb at the top
out.circle(40, 8, 3, 'r')     # gold orb, 7px
out.set(38, 6, 's')
out.set(39, 6, 's')
out.set(38, 7, 's')

print(out.stats_text())
print(out.matrix_text(region=(34, 2, 50, 48)))
finish(out)
