output = input_canvas.copy(name='output')

# Recolor only the two blue plumage tones on the right-hand parrot.
yellow = output.color('#f2c230', name='right_parrot_yellow')
yellow_highlight = output.color('#fff176', name='right_parrot_yellow_highlight')
for y in range(64):
    for x in range(34, 64):
        source = input_canvas.get(x, y)
        if source == 3:       # blue body plumage
            output.set(x, y, yellow)
        elif source == 8:     # cyan feather highlights
            output.set(x, y, yellow_highlight)

print(output.stats_text())
view(output, scale=8, margin=0)
finish(output)
