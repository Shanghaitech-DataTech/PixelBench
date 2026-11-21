result = new_canvas(48, 48, name="slash_effect_two_frames")
# Two successive motion stages in adjacent 24-pixel-wide cells.
# Frame 1: a short, clean crescent with a brilliant cutting edge.
result.path('M 9 15 Q 20 18 21 23 Q 21 29 3 34 Q 16 27 17 23 Q 18 20 9 15 Z', '#b8dbe5')
result.path('M 9 15 Q 20 18 20 23 Q 20 28 3 34 Q 17 26 18 23 Q 18 20 9 15 Z', '#ffffff')
# Frame 2: the arc expands and leaves a detached tapering wake.
result.path('M 28 5 Q 45 11 46 20 Q 47 32 25 41 Q 39 29 40 21 Q 41 14 28 5 Z', '#a8cedd')
result.path('M 28 5 Q 45 11 46 20 Q 47 30 25 41 Q 41 28 42 20 Q 42 14 28 5 Z', '#ffffff')
# A secondary streak follows the inside of the swing.
result.path('M 36 17 Q 41 26 26 36 Q 37 26 36 17 Z', '#d6eef3')
result.line(28, 34, 25, 37, '#ffffff')
view(result, scale=8, margin=0)
save('slash_effect', result)
finish(result)
