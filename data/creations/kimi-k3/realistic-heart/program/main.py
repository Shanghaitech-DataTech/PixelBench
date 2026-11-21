# Realistic anatomical heart, 64x64
c = new_canvas(64, 64, background=None, name="heart")

# ---- palette ----
OUT = '#38090E'   # dark outline
R0  = '#4A0D12'   # deepest shadow
R1  = '#6B151A'   # shadow
R2  = '#8E1F22'   # dark red
R3  = '#AE2C28'   # base muscle
R4  = '#C8453A'   # mid light
R5  = '#E06450'   # light
R6  = '#F08A6C'   # highlight
R7  = '#F8B392'   # specular
B0  = '#2A3A4E'   # vein dark
B1  = '#405773'   # vein base
B2  = '#5C7796'   # vein light
B3  = '#7F99B4'   # vein highlight
F0  = '#9C7438'   # fat dark
F1  = '#D9B06A'   # fat base
F2  = '#F0D495'   # fat light

# ================= back vessels =================
# Superior vena cava (far right, behind atrium)
c.path("M44,26 L44,10 Q44,7 47,7 Q50,7 50,10 L50,26 Z", B1)
c.line(49,9, 49,24, B0)          # shadow side
c.line(45,9, 45,23, B2)          # light side
c.set(46,8, B3)

# Right pulmonary artery stub (disappears behind aorta)
c.path("M22,13 L31,12 L31,15 L23,16 Z", B1)
c.line(23,15, 30,14, B0)

# Aorta: arch rising center-left
c.path("M36,26 L36,12 Q36,6 29,6 Q22,6 22,13 L22,21 Q22,23 25,23 L36,23 Z", R4)
c.line(23,12, 23,20, R5)
c.set(24,9, R5); c.set(25,8, R6); c.set(26,7, R5)
c.path("M34,10 Q34,8 31,8 L31,10 Q32,10 32,12 L32,23 L34,23 Z", R2)
c.line(35,12, 35,22, R1)
# three arch branches
c.rect(24, 3, 3, 5, R4)
c.rect(29, 2, 3, 6, R4)
c.rect(34, 3, 3, 5, R4)
c.line(25,3, 25,7, R6); c.line(30,2, 30,7, R6); c.line(35,3, 35,7, R6)
c.line(26,3, 26,7, R2); c.line(31,2, 31,7, R2); c.line(36,3, 36,7, R2)
# vessel cut openings
c.set(25,3, R0); c.set(30,2, R0); c.set(35,3, R0)
c.set(47,7, R0)

# Pulmonary trunk (in front, left of aorta) with left branch
c.path("M20,30 C18,24 16,18 13,15 L17,11 C21,15 24,21 26,27 Z", B1)
c.path("M13,15 L9,13 L10,17 L15,19 Z", B1)
c.line(14,14, 18,12, B2)         # top light edge
c.set(15,15, B3)
c.line(24,24, 25,27, B0)         # lower shadow edge
c.line(10,14, 11,16, B0)

# ================= heart body =================
c.path("M22,22 "
       "C16,25 13,31 13,37 "
       "C13,44 14,50 17,55 "
       "C18,57 20,58 22,58 "
       "C26,58 32,55 38,51 "
       "C44,46 49,41 51,35 "
       "C53,29 51,23 46,20 "
       "C42,18 37,17 33,17 "
       "L28,17 "
       "C24,18 22,19 22,22 Z", R3)
# top-left body shading (under the pulmonary trunk)
c.path("M22,21 C18,24 15,28 14,32 L16,33 C18,29 21,25 24,23 Z", R2)
c.path("M21,23 C18,25 16,28 15,31 L17,31 C18,28 20,26 23,24 Z", R1)

# right atrium (viewer right, slightly darker base)
c.path("M41,20 C47,22 51,27 50,34 C49,37 46,39 43,39 C41,33 40,26 41,20 Z", R2)
# left ventricle (viewer left, catches light)
c.path("M16,28 C14,34 14,43 17,50 C19,55 21,57 24,56 C22,48 22,37 25,29 C21,26 17,26 16,28 Z", R4)

# ---- shadow modeling on body ----
c.path("M46,22 C50,26 52,32 50,38 C48,44 43,49 37,52 L36,50 C42,47 46,43 48,38 C50,32 48,27 44,24 Z", R1)
c.path("M44,24 C47,27 48,32 47,37 C45,42 41,46 36,49 L34,46 C39,44 43,40 44,36 C46,31 45,27 42,25 Z", R2)
c.path("M48,30 C50,33 49,38 46,42 C44,45 41,47 38,49 L37,47 C41,44 44,41 46,37 C47,34 47,32 46,30 Z", R0)
c.path("M22,30 C30,32 39,34 48,35 L48,37 C39,36 30,34 22,32 Z", R2)
c.path("M24,55 C28,54 33,52 36,50 L37,52 C33,55 27,57 23,57 Z", R1)

# ---- highlight modeling on body ----
c.path("M17,31 C16,36 16,43 18,48 C19,51 20,53 22,54 C21,47 21,38 23,31 C20,29 18,29 17,31 Z", R5)
c.path("M18,34 C17,38 17,44 19,48 C19,49 20,50 20,50 C20,45 20,39 21,34 C20,33 19,33 18,34 Z", R6)
c.set(19,37, R7); c.set(20,41, R7); c.set(19,45, R6)
c.path("M30,24 C34,23 38,24 40,27 C38,30 33,31 29,30 C28,27 28,25 30,24 Z", R4)
c.path("M31,25 C33,24 36,25 37,27 C35,28 32,28 31,28 Z", R5)

# ================= fat grooves + coronary vessels =================
c.path("M22,26 C30,28 39,30 49,31 L49,34 C39,33 29,31 21,29 Z", F1)
c.path("M22,26 C30,28 39,30 49,31 L49,32 C39,31 30,29 22,27 Z", F2)
c.path("M28,27 C27,35 25,44 22,52 L24,53 C27,45 29,36 30,28 Z", F1)
c.line(28,28, 24,50, F2)
c.path("M24,27 C32,29 40,30 48,32", R1, fill=False)
c.path("M28,29 C27,37 25,45 23,51", R1, fill=False)
c.path("M31,31 C34,35 36,40 37,45", R1, fill=False)
c.set(33,35, R2); c.set(35,40, R2)

# ================= texture speckles =================
for (x, y) in [(27,33),(33,38),(30,44),(38,30),(42,34),(35,47),(26,49),(40,41),(44,27)]:
    c.set(x, y, R2)
for (x, y) in [(28,35),(32,41),(36,33),(30,48),(38,44),(26,40)]:
    c.set(x, y, R4)
c.set(45,25, R1); c.set(47,33, R1); c.set(41,48, R1)

# ================= outline =================
c.outline(OUT)

# ---- selective inner shading (grooves, vessel rims) ----
c.path("M22,30 C30,32 39,34 48,35", F0, fill=False)   # soft shadow below coronary sulcus
c.path("M30,28 C29,36 27,45 25,53", F0, fill=False)   # soft shadow right of IV sulcus
c.line(22,21, 22,12, OUT)          # aorta left rim
c.line(21,12, 21,20, OUT)          # pulmonary trunk right rim

view(c)
print(c.stats_text())
finish(c)
