# Two animation poses packed into one 48 x 48 transparent sprite sheet.
# Each frame occupies a 24 x 48 cell, ordered left to right.
result = new_canvas(48, 48, name="slash_effect")
edge = '#b6d1de'
shade = '#e3eff5'
white = '#ffffff'

# Frame 1: a compact, sharp crescent.
result.path('M 16 15 Q 29 27 3 33 Q 20 26 16 15 Z', edge)
result.path('M 16 15 Q 27 26 4 32 Q 20 25 16 15 Z', shade)
result.path('M 16 15 Q 26 25 6 31 Q 20 24 16 15 Z', white)

# Frame 2: the arc expands, leaving a fine secondary streak behind it.
result.path('M 37 6 Q 62 28 26 41 Q 47 28 37 6 Z', edge)
result.path('M 37 6 Q 60 27 27 40 Q 46 27 37 6 Z', shade)
result.path('M 37 6 Q 58 25 29 38 Q 46 25 37 6 Z', white)
# A detached, tapered remnant on the inside of the sweep.
result.path('M 38 22 Q 38 31 27 35 Q 34 30 38 22 Z', shade)
result.path('M 37 25 Q 36 31 28 34 Q 34 30 37 25 Z', white)
result.set(26, 36, shade)

view(result, scale=8, margin=0)
save('slash_effect', result)
finish(result)
