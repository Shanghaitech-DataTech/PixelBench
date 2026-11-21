result = new_canvas(48, 48, name="slash_effect")
# Frame 1: compact crescent, moving upward and to the right.
result.path('M 3 30 Q 5 18 19 14 Q 10 20 9 25 Q 7 28 3 30 Z', '#afdeed')
result.path('M 3 29 Q 6 19 19 14 Q 11 20 9 24 Q 6 27 3 29 Z', '#ffffff')
result.set(7, 21, '#e8faff')
# Frame 2: expanded leading edge with two tapered trailing ribbons.
result.path('M 25 37 Q 23 18 44 7 Q 33 19 32 28 Q 30 34 25 37 Z', '#83bed6')
result.path('M 25 35 Q 24 18 44 7 Q 34 18 32 26 Q 29 32 25 35 Z', '#dcf7ff')
result.path('M 25 32 Q 26 17 44 7 Q 35 16 32 23 Q 29 29 25 32 Z', '#ffffff')
result.path('M 28 40 Q 36 34 38 24 Q 39 32 34 37 L 28 40 Z', '#a7d8e8')
result.path('M 29 39 Q 35 33 37 28 Q 36 35 29 39 Z', '#f3fdff')
result.path('M 38 20 Q 40 14 46 11 L 41 17 Z', '#d6f3fa')
view(result, scale=8)
finish(result)
