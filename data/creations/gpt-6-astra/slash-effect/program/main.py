result = new_canvas(48, 48, name='slash_effect_two_frames')
# Two successive slash poses, each contained in its own 24-pixel-wide cell.
# Small opening crescent.
result.path('M 3 32 Q 22 26 18 15 Q 17 24 3 32 Z', '#bedfeb')
result.path('M 3 32 Q 21 25 18 15 Q 16 24 3 32 Z', '#ffffff')
# Expanded crescent, with a long taper toward the end of the swing.
result.path('M 26 39 Q 49 27 43 6 Q 42 25 26 39 Z', '#bedfeb')
result.path('M 26 39 Q 48 26 43 6 Q 41 25 26 39 Z', '#ffffff')
# Separated trailing streak follows the lower curve of the second slash.
result.path('M 25 43 Q 36 38 40 30 Q 34 37 25 43 Z', '#bedfeb')
result.path('M 25 43 Q 35 38 38 33 Q 32 39 25 43 Z', '#ffffff')
view(result, scale=8)
save('slash_effect', result)
finish(result)
