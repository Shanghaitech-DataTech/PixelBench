# house-turn-2view: fixed elevated isometric camera, house rotated 45 then 90 degrees
W, H = 112, 157

def base(name):
    c = new_canvas(W, H, background=None, name=name)
    # ground shadow (translucent dark, like input's k colour)
    sh = c.color('#161c2e45')
    c.ellipse(56, 128, 40, 12, sh)
    c.ellipse(56, 126, 32, 9, sh)
    return c

# ---------- Frame 1: 45 degrees - front wall+door (left face), right wall+window (right face)
f1 = base('frame45')
dark   = f1.color('#161c2e')   # outline / dark roof
wallL  = f1.color('#bda759')   # front wall (lit)
wallR  = f1.color('#97763d')   # right wall (shaded)
trim   = f1.color('#6c513a')
roofL  = f1.color('#dcaa46')
roofR  = f1.color('#98694e')
glass  = f1.color('#f9e279')
glass2 = f1.color('#e1d968')
door   = f1.color('#6c513a')
door2  = f1.color('#98694e')

# wall faces (corner at x=56)
f1.poly([(56,68),(16,88),(16,126),(56,106)], wallL)   # front wall
f1.poly([(56,68),(96,88),(96,126),(56,106)], wallR)   # right wall
# roof: pyramid, apex above corner
f1.poly([(56,30),(12,90),(56,70)], roofL)
f1.poly([(56,30),(100,90),(56,70)], roofR)
# roof ridge shading
f1.line(56,30,56,70,dark)
# outlines
f1.line(16,88,56,68,dark); f1.line(56,68,96,88,dark)
f1.line(16,88,16,126,dark); f1.line(96,88,96,126,dark)
f1.line(16,126,56,106,dark); f1.line(96,126,56,106,dark)
f1.line(12,90,56,30,dark); f1.line(56,30,100,90,dark)
f1.line(12,90,16,88,dark); f1.line(100,90,96,88,dark)
# door on front wall (parallelogram along the left face slope)
f1.poly([(38,86),(48,81),(48,111),(38,116)], door)
f1.poly([(40,88),(46,85),(46,109),(40,112)], door2)
f1.set(44,99,glass)  # knob
# window on right wall
f1.poly([(64,84),(84,93),(84,113),(64,104)], glass)
f1.poly([(64,84),(84,93),(84,113),(64,104)], dark, fill=False)
f1.line(74,89,74,109,dark)      # mullion vertical
f1.line(64,94,84,103,dark)      # mullion horizontal
# eave trim
f1.line(16,88,56,68,trim); f1.line(56,68,96,88,trim)

# ---------- Frame 2: 90 degrees - only the right wall and its window face the camera
f2 = base('frame90')
dark2  = f2.color('#161c2e')
wall   = f2.color('#97763d')   # same right-hand wall, now front-on
wallHi = f2.color('#bda759')
trim2  = f2.color('#6c513a')
roofF  = f2.color('#98694e')
roofT  = f2.color('#dcaa46')
glassF = f2.color('#f9e279')
glassF2= f2.color('#e1d968')

# right wall, flat on (rotated 90 deg: the side wall now faces the camera)
f2.rect(30, 70, 52, 44, wall)
# roof: gable runs left-right, slope falls away from viewer -> show eave strip + ridge
f2.poly([(26,70),(86,70),(90,62),(22,62)], roofF)
f2.poly([(22,62),(90,62),(88,56),(24,56)], roofT)
f2.line(24,56,88,56,dark2)
# outlines
f2.rect(30,70,52,44,dark2,fill=False)
f2.line(22,62,26,70,dark2); f2.line(90,62,86,70,dark2)
f2.line(24,56,22,62,dark2); f2.line(88,56,90,62,dark2)
# window centred on the wall
f2.rect(44,80,24,20,glassF)
f2.rect(44,80,24,20,dark2,fill=False)
f2.line(56,80,56,100,dark2)
f2.line(44,90,68,90,dark2)
f2.rect(46,82,20,16,glassF2,fill=False)
# door edge visible at side? no - only right wall at 90 deg. small vent/trim
f2.line(30,108,82,108,trim2)

finish([f1, f2])
