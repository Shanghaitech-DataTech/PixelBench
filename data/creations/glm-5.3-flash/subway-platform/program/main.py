# ============================================================
#  subway-platform -- 64x64 pixel art
#  Side view: a train arriving behind platform screen doors,
#  a bench, station signs and three passengers.
# ============================================================

W = H = 64
c = new_canvas(W, H, background='#101319', name='subway-platform')


def stamp(cv, x, y, rows, legend):
    for j, row in enumerate(rows):
        for i, ch in enumerate(row):
            if ch != '.':
                cv.set(x + i, y + j, legend[ch])


# ============================ CEILING ============================
c.rect(0, 0, 64, 1, '#0d0f14')
c.rect(0, 1, 64, 1, '#20242e')
c.rect(2, 2, 60, 2, '#f6f1dc')          # light strip
c.rect(2, 4, 60, 1, '#3a4050')          # glow under the strip
c.rect(0, 5, 64, 1, '#151820')

# ======================= WALL / TUNNEL ===========================
c.rect(0, 6, 64, 22, '#191d26')         # back wall, rows 6-27
c.rect(41, 15, 23, 13, '#13161e')       # tunnel portal, right
c.rect(41, 15, 23, 1, '#0d0f14')

# ---- speed streaks inside the portal ----
c.rect(52, 16, 12, 1, '#5f6f84')
c.rect(52, 18, 10, 1, '#8fa0b4')
c.rect(55, 19, 8, 1, '#5f6f84')
c.rect(52, 21, 12, 1, '#8fa0b4')
c.rect(54, 23, 9, 1, '#5f6f84')
c.rect(52, 25, 11, 1, '#8fa0b4')
c.rect(56, 26, 7, 1, '#5f6f84')

# ========================== EXIT SIGN ============================
c.rect(44, 6, 20, 9, '#eef4ee')
c.rect(45, 7, 18, 7, '#1d7a44')
G = {
    'E': [(0, 0), (1, 0), (2, 0), (0, 1), (0, 2), (1, 2), (2, 2), (0, 3), (0, 4), (1, 4), (2, 4)],
    'X': [(0, 0), (2, 0), (1, 1), (0, 2), (2, 2), (0, 3), (2, 3), (0, 4), (2, 4)],
    'I': [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2), (1, 3), (0, 4), (1, 4), (2, 4)],
    'T': [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2), (1, 3), (1, 4)],
}
for k, ch in enumerate('EXIT'):
    for (px, py) in G[ch]:
        c.set(46 + k * 4 + px, 8 + py, '#f2f7f2')

# ================== ROUTE MAP (left wall) ========================
c.rect(3, 8, 14, 7, '#c9ced8')
c.rect(4, 9, 12, 5, '#17263f')
c.rect(6, 11, 9, 1, '#f0c53a')          # line
c.set(7, 11, '#eef4ee')                 # stations
c.set(13, 11, '#eef4ee')
c.set(10, 10, '#eef4ee')                # you-are-here marker
c.set(10, 11, '#eef4ee')
c.set(10, 12, '#eef4ee')

# ============================= TRAIN =============================
def tedge(y):                            # raked nose, front to the left
    return max(4, 13 - (y - 15))

for y in range(15, 28):                  # body block, x4..50
    c.rect(tedge(y), y, 51 - tedge(y), 1, '#c3c9d4')
c.rect(13, 15, 38, 1, '#6d7480')         # roof
c.rect(12, 16, 39, 1, '#5f6672')
c.rect(11, 17, 40, 1, '#dde2ea')         # highlight
c.rect(4, 26, 47, 2, '#c8452f')          # livery stripe

for y in range(16, 22):                  # raked windshield
    c.rect(tedge(y) + 1, y, 4, 1, '#1d2b45')
c.rect(13, 16, 2, 1, '#6f93bd')          # glint
c.set(10, 19, '#6f93bd')

for dx in (18, 32):                      # doors
    c.rect(dx, 18, 7, 8, '#8b93a1')
    c.rect(dx + 3, 18, 1, 8, '#6a7280')
    c.rect(dx, 18, 7, 1, '#6a7280')
    c.rect(dx, 25, 7, 1, '#6a7280')
    c.rect(dx + 1, 19, 2, 5, '#1d2b45')
    c.rect(dx + 4, 19, 2, 5, '#1d2b45')
for wx in (26, 40):                      # windows
    c.rect(wx, 18, 5, 8, '#1d2b45')
    c.rect(wx, 18, 5, 1, '#3a5a86')
    c.rect(wx, 21, 5, 1, '#6f93bd')

c.rect(48, 17, 3, 9, '#9aa1ad')          # rear end cap
c.rect(48, 20, 3, 2, '#e05a3a')          # tail light

c.rect(5, 23, 4, 2, '#ffe9a8')           # headlight
c.set(5, 23, '#fff6d0')
c.set(5, 24, '#fff6d0')
c.rect(2, 22, 3, 4, '#7d7a5e')           # glow on the wall
c.set(2, 21, '#4a4a3c')
c.set(1, 23, '#4a4a3c')
c.set(1, 25, '#4a4a3c')

# motion streaks along the body
c.rect(19, 16, 9, 1, '#e8ecf2')
c.rect(28, 22, 7, 1, '#e8ecf2')
c.rect(41, 24, 7, 1, '#e8ecf2')

# ---- the part of the train inside the portal sits in shadow ----
DIM = {
    '#c3c9d4': '#7d8492', '#dde2ea': '#8d94a2', '#e8ecf2': '#8d94a2',
    '#6d7480': '#3f4550', '#5f6672': '#363b45',
    '#8b93a1': '#565c68', '#6a7280': '#414652', '#9aa1ad': '#565c68',
    '#1d2b45': '#141d30', '#3a5a86': '#141d30', '#6f93bd': '#42586f',
    '#c8452f': '#7d2c20', '#e05a3a': '#7d2c20',
    '#ffe9a8': '#8d8054', '#fff6d0': '#8d8054',
}
pal = {}
for p in c.palette():
    r, g, b, a = p['rgba']
    pal[p['index']] = '#%02x%02x%02x' % (r, g, b)
for y in range(15, 28):
    for x in range(41, 51):
        hx = pal.get(c.get(x, y))
        if hx in DIM:
            c.set(x, y, DIM[hx])

# ========================= HANGING SIGN ==========================
c.rect(28, 5, 1, 4, '#3c414b')           # rods
c.rect(38, 5, 1, 4, '#3c414b')
c.rect(24, 9, 19, 9, '#c9ced8')          # frame
c.rect(25, 10, 17, 7, '#17263f')         # LED panel
c.text(28, 10, '2', '#f0c53a', font='5x7')
for cx0 in (35, 39):                     # chevrons
    c.set(cx0 + 2, 11, '#f0c53a')
    c.set(cx0 + 1, 12, '#f0c53a')
    c.set(cx0, 13, '#f0c53a')
    c.set(cx0 + 1, 14, '#f0c53a')
    c.set(cx0 + 2, 15, '#f0c53a')

# ====================== PLATFORM SCREEN DOORS ====================
c.rect(0, 28, 64, 1, '#a6adb8')          # top rail
c.rect(0, 29, 64, 1, '#7d848f')
c.rect(0, 30, 64, 12, '#3e4c60')         # glass
c.rect(0, 30, 4, 12, '#2a3342')          # wall behind, left of the train
c.rect(4, 30, 47, 2, '#4a5261')          # train roof, dimmed
c.rect(4, 32, 47, 9, '#8794a6')          # train body, dimmed
c.rect(4, 41, 47, 1, '#7a4247')          # stripe, dimmed
for dx in (18, 32):                      # doors behind the glass
    c.rect(dx, 32, 7, 9, '#7d8896')
    c.rect(dx + 3, 32, 1, 9, '#5d6875')
for wx in (26, 40):                      # windows behind the glass
    c.rect(wx, 33, 5, 6, '#4e5c74')
c.rect(51, 30, 13, 12, '#2c3949')        # tunnel behind the glass
c.rect(5, 31, 9, 1, '#9dc0d2')           # sheen
for i in range(5):                       # diagonal reflections
    c.set(9 + i, 40 - i, '#9dc0d2')
    c.set(31 + i, 41 - i, '#9dc0d2')
    c.set(55 + i, 39 - i, '#9dc0d2')
for x in (6, 18, 30, 42, 54):            # door split lines
    c.rect(x, 30, 1, 12, '#2c3949')
for x in (0, 12, 24, 36, 48, 60):        # mullions
    c.rect(x, 28, 2, 16, '#8b929d')
    c.rect(x + 1, 28, 1, 16, '#646a75')
c.rect(0, 42, 64, 1, '#8d939e')          # bottom rail
c.rect(0, 43, 64, 1, '#565c66')

# ========================= TACTILE STRIP =========================
c.rect(0, 44, 64, 2, '#e8bc3f')
for x in range(1, 64, 3):
    c.set(x, 45, '#a87f24')
c.rect(0, 46, 64, 1, '#565c66')

# ============================= FLOOR =============================
c.rect(0, 47, 64, 17, '#a2a7b1')
c.rect(0, 57, 64, 7, '#b2b7c1')
c.rect(0, 50, 64, 1, '#82878f')
c.rect(0, 54, 64, 1, '#82878f')
c.rect(0, 59, 64, 1, '#82878f')
for xb in (0, 11, 21, 32, 43, 53, 63):   # receding grout lines
    c.line(32, 47, xb, 63, '#82878f')

# ============================= BENCH =============================
c.rect(59, 39, 5, 5, '#7d4f2c')          # backrest
c.rect(59, 39, 5, 1, '#96613a')
c.rect(61, 40, 1, 3, '#5f3c20')
c.rect(50, 44, 14, 3, '#96613a')         # seat
c.rect(50, 46, 14, 1, '#5f3c20')
c.rect(51, 47, 2, 2, '#3c414b')          # legs
c.rect(61, 47, 2, 2, '#3c414b')

# ============================ SHADOWS ============================
c.rect(6, 59, 11, 1, '#82878f')
c.rect(26, 55, 12, 1, '#82878f')
c.rect(49, 49, 15, 1, '#82878f')

# =========================== PASSENGERS ==========================
P1 = ['....hhhhh....',
      '...hhhhhhh...',
      '.pqffhhhhh...',
      '.pqffhhhhh...',
      '.PP.fhhhh....',
      '.jj..hhh.....',
      '.jjjjjjjjj...',
      '..jjjjjjjjj..',
      '..jjjjjjjjj..',
      '..jjjjjjjjj..',
      '..jjjjjjjjj..',
      '..jjjjjjjjj..',
      '..jjjjjjjjj..',
      '..jjjjjjjjj..',
      '..jjjjjjjjj..',
      '..jjjjjjjjj..',
      '..ttttttttt..',
      '..ttttttttt..',
      '..ttt..ttt...',
      '..ttt..ttt...',
      '..ttt..ttt...',
      '..ttt..ttt...',
      '..ttt..ttt...',
      '..ttt..ttt...',
      '..ttt..ttt...',
      '..sss..sss...',
      '..sss..sss...']
L1 = {'h': '#2b1d16', 'f': '#d9a077', 'j': '#2e5f5b',
      't': '#23262f', 's': '#15171d', 'P': '#cfd6e0',
      'p': '#1b2430', 'q': '#8fd4e8'}

P2 = ['...hhhhh...',
      '..hhhhhhh..',
      '.fffhhhh...',
      '.fffhhhh...',
      '..fhhhh....',
      '..jjjjj....',
      '.jjjjjjj...',
      '.fjjjjjj...',
      'bbfjjjjj...',
      'bbfjjjjj...',
      'bbjjjjjj...',
      '..jjjjjj...',
      '..jjjjjj...',
      '..tttttt...',
      '..tttttt...',
      '..ttt.tt...',
      '.ttt..tt...',
      '.ttt..tt...',
      '.ttt...tt..',
      '.sss...sss.',
      'sss.....sss']
L2 = {'h': '#1a1410', 'f': '#d9a077', 'j': '#6b2b33',
      't': '#2a2d38', 's': '#15171d', 'b': '#7a4a2a'}

P3 = ['....hhhh....',
      '...hhhhhh...',
      '.fffhhhh....',
      '.fffhhhh....',
      '..fhhhh.....',
      '..jjjjj.....',
      '.fjjjjjj....',
      'BBfjjjjj....',
      'BBjjjjjj....',
      '..jjjjjj....',
      '..jjjjj.....',
      '.ttttttt....',
      '.tttttt.....',
      '.ttt........',
      '.ttt........',
      '.ssss.......']
L3 = {'h': '#4a3320', 'f': '#d9a077', 'j': '#cfd4dc',
      't': '#23262f', 's': '#15171d', 'B': '#e8ecf2'}

stamp(c, 5, 32, P1, L1)      # standing, reading a phone
stamp(c, 26, 34, P2, L2)     # walking with a bag
stamp(c, 52, 33, P3, L3)     # seated on the bench, reading

# ---------------- report ----------------
print('STATS:' + c.stats_text())

finish(c)

