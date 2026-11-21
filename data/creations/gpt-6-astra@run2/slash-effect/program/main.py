# Two sequential slash poses on a single transparent 48 x 48 sprite sheet.
result = new_canvas(48, 48, name='slash_effect')
edge = '#b9d8e9'
light = '#e6f5ff'
white = '#ffffff'
# Frame 1: compact crescent, with needle-thin tips and a bright cutting edge.
result.path('M 6 16 C 14 17 21 20 20 24 C 19 28 12 31 4 32 C 11 29 15 26 15 23 C 15 20 11 18 6 16 Z', edge)
result.path('M 6 16 C 14 17 20 20 19 24 C 18 27 12 30 5 32 C 12 28 16 25 16 23 C 16 20 11 18 6 16 Z', white)
# Frame 2: expanded sweep, with the belly of the arc carrying the weight.
result.path('M 27 7 C 39 10 47 16 46 23 C 45 31 35 37 25 40 C 34 34 40 28 40 22 C 41 15 34 10 27 7 Z', edge)
result.path('M 27 7 C 38 10 46 16 45 23 C 44 30 35 36 26 39 C 35 33 41 28 41 22 C 42 15 34 10 27 7 Z', white)
# A second taper follows the main arc, separated by transparent negative space.
result.path('M 46 29 C 43 36 34 40 26 42 C 33 38 39 36 46 29 Z', light)
result.path('M 43 34 C 38 39 31 41 26 42 L 36 38 Z', white)
view(result, scale=8, margin=0)
save('slash_effect', result)
finish(result)
