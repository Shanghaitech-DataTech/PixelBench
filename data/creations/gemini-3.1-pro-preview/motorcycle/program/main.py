from pixelbench_api import new_canvas, finish

c = new_canvas(128, 128)

# 1. Rear Wheel
c.circle(28, 100, 16, '#1a1a1a')
c.circle(28, 100, 14, '#262626')
c.circle(28, 100, 12, '#1a1a1a')
c.circle(28, 100, 10, '#00000000') # erase inner
# Spokes
c.line(28, 90, 28, 110, '#ffffff')
c.line(18, 100, 38, 100, '#ffffff')
c.line(21, 93, 35, 107, '#ffffff')
c.line(21, 107, 35, 93, '#ffffff')
# Hub
c.circle(28, 100, 4, '#555555')
c.circle(28, 100, 2, '#999999')

# 2. Rear Fender (Hugger)
c.path('M 44 100 C 44 85 34 80 24 82 L 22 85 C 32 84 40 88 40 100 Z', '#111111')

# 3. Engine Area
# Engine block background
c.poly([(52, 70), (77, 70), (82, 95), (57, 95)], '#222222')
c.poly([(54, 72), (75, 72), (79, 93), (59, 93)], '#333333')
# Round silver gray engine cover
c.circle(66, 88, 10, '#555555')
c.circle(66, 88, 8, '#999999')
c.circle(66, 88, 4, '#cccccc')
# Secondary cover
c.circle(74, 82, 6, '#333333')
c.circle(74, 82, 4, '#555555')

# 4. Swingarm (Silver)
c.poly([(28, 98), (66, 86), (66, 90), (28, 102)], '#cccccc')
c.poly([(28, 99), (64, 87), (64, 89), (28, 101)], '#999999')

# 5. Tubular Frame (Silver)
# Trellis frame structure
c.line(82, 55, 62, 75, '#cccccc')
c.line(81, 55, 61, 75, '#cccccc')
c.line(62, 75, 67, 90, '#cccccc')
c.line(61, 75, 66, 90, '#cccccc')
c.line(62, 75, 77, 70, '#cccccc')
c.line(62, 74, 77, 69, '#cccccc')
c.line(77, 70, 67, 90, '#cccccc')
c.line(78, 70, 68, 90, '#cccccc')

# 6. Exhaust
# Pipe from engine
c.path('M 66 95 C 66 105 56 105 47 100 L 27 85 L 30 80 L 50 95 C 54 98 60 98 62 90 Z', '#cccccc')
c.path('M 66 95 C 66 105 56 105 47 100 L 27 85 L 30 80 L 50 95 C 54 98 60 98 62 90 Z', '#999999', fill=False)
# Muffler tip
c.poly([(27, 85), (30, 80), (26, 78), (23, 83)], '#555555')
c.poly([(26, 84), (29, 81), (27, 79), (24, 82)], '#111111')

# 7. Upswept Tail & Tail Light
tail_path = 'M 44 65 L 22 48 L 20 53 L 42 70 Z'
c.path(tail_path, '#333333')
c.path('M 44 62 L 22 48 L 20 50 L 42 65 Z', '#111111')
c.path('M 37 62 L 22 50 L 20 52 L 35 65 Z', '#e60000') # red accent
# Tail light
c.poly([(22, 48), (18, 46), (16, 50), (20, 52)], '#990000')
c.poly([(20, 48), (18, 47), (17, 49), (19, 51)], '#ff3333')

# 8. Seat
c.path('M 57 60 L 42 65 L 44 68 L 58 64 Z', '#111111')
c.path('M 56 61 L 43 65 L 44 67 L 57 63 Z', '#222222') # slight highlight

# 9. Gas Tank
tank_path = 'M 82 50 C 77 45 62 45 57 60 L 52 65 L 67 70 Z'
c.path(tank_path, '#111111')
c.path('M 77 48 C 67 48 60 55 57 60 L 62 65 L 77 55 Z', '#333333') # highlight
c.path('M 62 65 L 67 70 L 77 60 L 72 55 Z', '#e60000') # red accent

# 10. Side Fairing
side_path = 'M 82 55 L 92 65 L 87 95 L 75 95 L 75 80 L 65 75 L 72 65 Z'
c.path(side_path, '#333333')
c.path('M 82 75 L 87 85 L 72 85 L 77 75 Z', '#e60000') # red accent on side
# Vents
c.poly([(77, 70), (82, 75), (77, 85), (72, 80)], '#111111')

# 11. Front Wheel
c.circle(104, 100, 16, '#1a1a1a')
c.circle(104, 100, 14, '#262626')
c.circle(104, 100, 12, '#1a1a1a')
c.circle(104, 100, 10, '#00000000') # erase inner
# Spokes
c.line(104, 90, 104, 110, '#ffffff')
c.line(94, 100, 114, 100, '#ffffff')
c.line(97, 93, 111, 107, '#ffffff')
c.line(97, 107, 111, 93, '#ffffff')
# Hub
c.circle(104, 100, 4, '#555555')
c.circle(104, 100, 2, '#999999')

# 12. Front Fender
c.path('M 88 100 C 88 85 98 80 108 82 L 110 85 C 100 84 92 88 92 100 Z', '#e60000')
c.path('M 90 98 C 90 86 98 82 106 83 L 108 85 C 100 84 94 88 94 98 Z', '#ff3333') # highlight

# 13. Front Fork
# Lower fork (thick silver)
c.poly([(104, 100), (100, 101), (92, 76), (96, 75)], '#cccccc')
c.poly([(100, 101), (98, 102), (90, 77), (92, 76)], '#999999')
# Upper fork (thinner silver)
c.poly([(96, 75), (94, 76), (86, 51), (88, 50)], '#cccccc')

# 14. Nose Fairing
nose_path = 'M 82 55 L 102 65 L 98 70 L 88 70 Z'
c.path(nose_path, '#333333')
c.path('M 82 55 L 102 65 L 92 65 L 82 60 Z', '#111111') # black accent on nose

# 15. Windscreen
c.path('M 85 57 L 75 45 L 82 42 L 92 52 Z', '#111111')
c.path('M 83 54 L 75 45 L 79 43 L 88 51 Z', '#333333')

# 16. Handlebars
c.line(86, 51, 80, 46, '#cccccc')
c.line(87, 52, 81, 47, '#999999')
c.circle(80, 46, 2, '#111111') # grip

finish(c)
