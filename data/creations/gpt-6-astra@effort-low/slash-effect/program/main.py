result = new_canvas(48, 48, name='slash_effect_two_frames')
# Frame 1: a compact crescent, sweeping upward to the right.
result.path('M 2 30 Q 7 17 20 16 Q 13 19 10 23 Q 6 26 2 30 Z', '#bfe8f2')
result.path('M 2 30 Q 8 18 20 16 Q 12 20 9 24 Q 5 27 2 30 Z', '#ffffff')
result.set(16,18,'#ffffff')
# Frame 2: the same sweep opened into a long, bright blade.
result.path('M 26 36 Q 33 16 46 10 Q 43 24 36 29 Q 31 33 26 36 Z', '#a6d9e9')
result.path('M 26 36 Q 33 17 46 10 Q 41 23 35 28 Q 30 33 26 36 Z', '#e0f6fc')
result.path('M 26 36 Q 33 17 46 10 Q 40 22 34 27 Q 29 33 26 36 Z', '#ffffff')
# Detached trailing ribbon follows the outer curve, tapering to single pixels.
result.path('M 29 39 Q 41 32 46 22 Q 44 33 29 39 Z', '#bfe8f2')
result.path('M 32 37 Q 41 32 45 26 Q 42 33 32 37 Z', '#ffffff')
result.set(27,40,'#bfe8f2')
view(result)
finish(result)
