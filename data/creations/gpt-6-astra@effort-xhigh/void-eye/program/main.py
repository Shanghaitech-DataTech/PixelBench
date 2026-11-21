# Void-eye — 64px RPG boss sprite
result = new_canvas(64, 64, name='void_eye')
c = result
# Cool shadow, with stepped alpha falloff; the rest of the field stays empty.
c.ellipse(32, 57, 20, 4, '#1513290a')
c.ellipse(32, 57, 17, 3, '#15132913')
c.ellipse(32, 57, 13, 2, '#15132922')
c.ellipse(32, 57, 8, 1, '#1513292d')

ink = '#100e1e'
dark = '#1b182d'
shade = '#292039'
plum = '#3e294e'
mid = '#513660'
light = '#76517e'
rim = '#a37d9f'
# Back tentacles. Their hooked ends keep the entire silhouette compact.
c.path('M 13 26 Q 6 27 6 34 Q 5 39 9 41 Q 13 42 14 37 L 11 36 Q 10 39 9 36 Q 9 32 16 32 Z', ink)
c.path('M 12 28 Q 8 29 8 34 Q 7 38 10 39 L 11 37 L 10 35 Q 11 32 16 31 Z', plum)
c.line(8,32,8,35,light)
c.path('M 51 27 Q 58 26 59 33 Q 60 38 55 41 L 52 38 Q 57 36 56 33 Q 55 32 51 34 Z', ink)
c.path('M 52 29 Q 56 29 57 33 Q 58 36 54 38 L 53 36 Q 55 34 53 32 Z', plum)
c.set(57,33,light)
# Rear lower feelers.
c.path('M 18 37 Q 10 41 13 47 Q 15 51 20 47 L 21 44 Q 16 47 16 44 L 22 41 Z', ink)
c.path('M 18 39 Q 14 42 14 46 Q 15 49 18 46 L 17 46 Q 15 44 21 41 Z', mid)
c.path('M 45 37 Q 53 39 54 44 Q 55 49 49 48 L 46 44 Q 51 46 51 43 L 44 41 Z', ink)
c.path('M 47 39 Q 52 41 52 44 Q 53 47 49 46 L 50 44 Q 50 42 45 41 Z', plum)
c.set(51,42,light)
# Orb casing, with a deliberately irregular, heavy brow.
c.path('M 10 23 L 11 17 L 15 12 L 21 8 L 27 7 L 37 7 L 46 10 L 52 16 L 55 23 L 55 30 L 52 37 L 47 42 L 40 45 L 29 46 L 21 43 L 15 39 L 11 32 Z', ink)
c.path('M 12 23 L 13 18 L 17 13 L 23 10 L 30 8 L 38 9 L 45 12 L 50 17 L 53 24 L 53 30 L 50 36 L 46 40 L 39 43 L 30 44 L 22 41 L 17 37 L 13 31 Z', shade)
# Large material planes: desaturated cool light above, wine in the folds.
c.path('M 13 24 L 14 18 L 18 14 L 24 11 L 31 9 L 37 10 L 44 13 L 49 18 L 47 22 L 35 18 L 23 20 Z', mid)
c.path('M 15 20 L 18 15 L 25 12 L 31 10 L 37 11 L 42 13 L 31 12 L 25 14 L 21 17 Z', light)
c.path('M 19 15 L 25 12 L 30 11 L 34 11 L 28 13 L 23 15 Z', rim)
c.line(18,16,16,19,light)
c.path('M 48 18 L 51 23 L 52 30 L 49 35 L 44 39 L 37 41 L 25 40 L 17 34 L 15 28 L 25 32 L 43 31 Z', dark)
c.path('M 17 31 Q 20 39 30 42 L 38 42 L 43 40 Q 32 40 27 36 Z', plum)
# Aperture outline and shadowed sclera.
c.path('M 12 24 Q 18 16 31 15 Q 45 14 53 23 Q 51 32 44 36 Q 32 43 21 36 Q 15 33 12 24 Z', ink)
c.path('M 15 24 Q 20 18 31 17 Q 43 16 50 23 Q 49 30 42 34 Q 32 39 23 34 Q 17 31 15 24 Z', '#776682')
c.path('M 16 24 Q 23 19 32 19 Q 44 18 49 24 Q 46 32 39 35 Q 30 38 23 33 Q 18 29 16 24 Z', '#aca0b2')
c.path('M 17 24 Q 22 20 29 20 L 27 33 L 24 32 Q 19 29 17 24 Z', '#e0d6d4')
c.path('M 18 24 L 22 22 L 25 22 L 24 29 L 21 28 Z', '#f2e9dc')
c.path('M 41 20 Q 46 21 49 24 Q 47 30 42 32 L 39 34 Z', '#c9bfca')
c.path('M 45 23 L 48 24 L 46 27 L 44 28 Z', '#e0d6d4')
# Sparse organic veins avoid noise while grounding the enormous eyeball.
c.line(18,25,21,26,'#a58caa')
c.line(21,26,23,29,'#a58caa')
c.set(21,27,'#bba6bf')
c.line(47,27,44,28,'#a58caa')
c.line(44,28,43,30,'#a58caa')
# Iris: deep violet rim, dark top, rich amethyst lower crescent.
c.ellipse(33,26,11,11,'#25132f')
c.ellipse(33,26,10,10,'#422050')
c.ellipse(33,26,9,10,'#542668')
c.path('M 24 27 Q 25 35 32 36 Q 40 36 42 29 L 39 29 L 36 33 L 30 33 L 27 28 Z', '#71358e')
c.path('M 25 23 Q 27 17 33 17 Q 39 17 42 23 L 39 25 L 35 22 L 29 24 Z', '#36183f')
c.path('M 25 26 L 26 30 L 29 33 L 28 29 L 28 26 Z', '#8546a5')
c.path('M 39 26 L 40 28 L 38 32 L 37 30 Z', '#8546a5')
c.line(30,33,31,35,'#aa60bd')
c.line(34,33,34,35,'#9550b0')
c.line(37,32,36,34,'#aa60bd')
c.line(24,24,27,25,'#6a327f')
c.line(26,21,28,23,'#673078')
c.line(39,22,37,24,'#673078')
c.set(41,27,'#9a54b0')
c.set(28,32,'#b073c3')
# Faint inner light around a vertical void pupil.
c.path('M 32 19 L 35 19 L 37 25 L 36 30 L 34 34 L 31 32 L 29 26 Z', '#3b1a50')
c.path('M 33 19 L 35 22 L 36 26 L 35 30 L 33 33 L 31 29 L 31 24 Z', '#190e2b')
c.path('M 33 22 L 34 24 L 34 29 L 33 31 L 32 28 L 32 25 Z', '#9760b5')
c.line(33,24,33,28,'#c698d9')
c.set(33,25,'#e2c3e9')
# One reflected highlight, separate from the dim pupil emission.
c.rect(27,20,2,2,'#c0a3ce')
c.set(29,22,'#9666ad')
# Upper lid overlaps the iris and creates the threatening gaze.
c.path('M 12 23 Q 17 16 30 15 Q 43 13 53 23 L 50 22 Q 42 17 31 18 Q 21 18 15 25 Z', ink)
c.path('M 14 21 Q 20 15 30 14 Q 41 13 49 19 L 51 22 Q 42 16 31 17 Q 21 17 15 23 Z', plum)
c.path('M 16 20 Q 22 15 30 15 L 38 15 L 42 16 L 30 16 Q 22 17 17 21 Z', light)
c.line(19,19,23,17,rim)
# Lower lid: bright broken edge over a heavy black socket.
c.path('M 16 30 Q 21 38 31 39 Q 43 40 50 30 L 47 36 L 41 40 L 32 41 L 24 39 L 19 35 Z', ink)
c.path('M 18 32 Q 23 38 32 38 Q 42 38 47 33 L 44 37 L 38 40 L 30 40 L 23 37 Z', mid)
c.line(22,35,26,37,'#8c638e')
c.line(27,38,32,39,'#a37d9f')
c.line(34,39,39,38,'#76517e')
c.line(41,37,44,35,'#76517e')
# Foreground short tentacles, emerging from the lower flesh.
c.path('M 22 39 Q 22 43 20 46 Q 17 51 22 52 Q 27 53 29 47 L 28 43 L 25 41 L 25 46 Q 24 50 22 49 Q 23 46 25 43 Z', ink)
c.path('M 23 41 L 24 43 Q 23 47 21 49 Q 24 52 27 47 L 27 44 L 26 44 L 25 48 Q 23 51 21 49 Q 21 46 23 43 Z', plum)
c.path('M 23 42 L 24 43 L 22 47 L 21 48 L 21 46 Z', light)
c.set(22,50,mid)
c.set(25,49,light)
c.path('M 36 41 L 42 40 Q 43 44 45 46 Q 47 50 43 51 Q 38 52 36 47 L 34 44 Z', ink)
c.path('M 37 42 L 40 41 Q 40 45 43 47 L 44 49 Q 40 51 38 47 L 36 44 Z', plum)
c.path('M 37 42 L 39 42 Q 39 46 42 48 L 41 49 Q 38 47 37 44 Z', light)
c.line(37,42,38,44,rim)
c.set(43,48,mid)
# Tiny material accents on the outer shell, kept clustered.
c.line(13,24,14,27,light)
c.set(15,30,mid)
c.line(47,14,49,16,mid)
c.line(51,25,52,27,mid)
c.set(50,32,plum)

# Final broken highlights on the little hooked appendages.
c.line(7,33,7,35,mid)
c.set(8,31,light)
c.line(15,43,15,45,light)
c.set(16,46,mid)
c.line(55,30,56,31,mid)
c.set(51,44,mid)
c.set(23,49,light)

assert result.stats()['colors_used'] <= 86
view(result, scale=8, margin=0)
save('void-eye', result)
finish(result)
