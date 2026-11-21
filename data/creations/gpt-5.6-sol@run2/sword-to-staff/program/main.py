output = input_canvas.copy(name='output')

# Remove the sword's guard and blade, restoring the plain white background.
output.rect(41, 39, 6, 18, 1)

# Staff shaft: a slim dark outline with warm wood and a single highlight.
output.rect(46, 14, 3, 44, 2)
output.rect(47, 14, 1, 43, 16)
output.set(47, 16, 25)
output.set(47, 20, 25)
output.set(47, 24, 25)
output.set(47, 28, 25)
output.rect(45, 56, 5, 2, 2)
output.rect(46, 56, 3, 1, 16)

# Forked wooden crown holding a bright green focus.
output.rect(45, 11, 2, 5, 2)
output.rect(48, 11, 2, 5, 2)
output.circle(47, 9, 4, 2)
output.circle(47, 9, 2, 13)
output.set(46, 8, 14)
output.set(47, 8, 14)
output.set(46, 9, 14)
output.set(49, 10, 15)
output.set(47, 12, 16)

# Extend the hand around the staff, preserving the original black-brown cuff edge.
output.rect(40, 35, 5, 3, 9)
output.rect(44, 36, 2, 2, 9)
output.set(40, 38, 2)
output.rect(41, 38, 4, 1, 16)
output.set(45, 38, 2)
output.set(44, 35, 2)
output.set(46, 35, 2)

view(output, scale=8, margin=0)
finish(output)
