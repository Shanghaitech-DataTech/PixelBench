c = new_canvas(64, 64, background='#14161f', name='subway-platform')

# ---------------- ceiling ----------------
c.rect(0, 0, 64, 6, '#1b1e29')
c.rect(0, 5, 64, 1, '#101218')
for lx in (5, 23, 41, 56):
    c.rect(lx, 2, 7, 2, '#f5ecc8')
    c.rect(lx + 1, 6, 5, 1, '#3a3f52')   # glow on wall

# ---------------- back wall ----------------
c.rect(0, 6, 64, 44, '#2a2f3e')          # y 6..49
c.rect(0, 6, 64, 2, '#222633')           # shadow under ceiling
c.rect(0, 10, 64, 4, '#3a4152')          # tile band
for x in range(2, 64, 4):
    c.set(x, 12, '#2a2f3e')
c.rect(0, 44, 64, 6, '#242833')          # darker lower wall
c.rect(58, 6, 6, 44, '#232733')          # far-end shading (depth)

# ---------------- floor ----------------
c.rect(0, 50, 64, 14, '#565d6b')
# receding tile seams, converging to the right (depth)
c.line(2, 63, 36, 50, '#48505c')
c.line(16, 63, 42, 50, '#48505c')
c.line(30, 63, 48, 50, '#48505c')
c.line(44, 63, 54, 50, '#48505c')
c.line(58, 63, 61, 50, '#48505c')
c.rect(0, 56, 64, 1, '#4c5460')

# ---------------- track pit & platform edge ----------------
c.rect(0, 52, 30, 12, '#0c0d12')
c.rect(0, 58, 30, 1, '#3f4550')          # rail
c.rect(29, 50, 2, 14, '#7d8590')         # platform edge highlight
c.rect(31, 50, 2, 14, '#c9a23f')         # tactile warning strip

# ---------------- train (arriving, moving right) ----------------
c.rect(0, 20, 25, 30, '#c3cad3')         # body
c.rect(0, 18, 24, 2, '#9aa2ad')          # roof
c.poly([(24, 20), (29, 25), (29, 45), (24, 49)], '#c3cad3')   # nose
c.poly([(25, 23), (28, 26), (28, 32), (25, 32)], '#1f2a44')   # windshield
c.rect(27, 42, 2, 3, '#ffe9a8')          # headlight
c.rect(26, 43, 1, 1, '#fff6d8')          # hot centre
c.line(29, 55, 31, 55, '#ffe9a8')        # beam on track
c.rect(0, 38, 25, 3, '#d24a3a')          # stripe
c.poly([(24, 38), (27, 39), (27, 42), (24, 41)], '#d24a3a')
c.rect(2, 25, 20, 9, '#1f2a44')          # window band
for wx in (6, 11, 16):
    c.rect(wx, 25, 1, 9, '#c3cad3')
c.rect(0, 49, 26, 3, '#3a3f4a')          # undercarriage
c.rect(3, 52, 7, 5, '#23262e')           # bogies
c.rect(15, 52, 7, 5, '#23262e')
# speed streaks trailing over the body
for (x0, x1, y) in [(0, 10, 22), (0, 14, 27), (0, 8, 33), (0, 12, 41), (0, 9, 46)]:
    c.line(x0, y, x1, y, '#e8eef4')
c.line(0, 30, 5, 30, '#9fb4c8')

# ---------------- platform screen doors ----------------
c.rect(33, 17, 15, 3, '#39404f')         # header beam
tops = {33: 20, 38: 21, 43: 22}          # receding tops (depth)
for px, ty in tops.items():
    c.rect(px, ty, 5, 50 - ty, '#39404f')
    c.rect(px + 1, ty + 2, 3, 46 - ty - 2, '#5d768c')
    c.rect(px + 1, ty + 2, 1, 46 - ty - 2, '#7e97ab')
    c.rect(px + 2, 34, 2, 1, '#39404f')  # handle
c.rect(33, 47, 15, 3, '#39404f')         # base

# ---------------- station signs (generic, no brands) ----------------
# hanging sign over the track
c.rect(10, 6, 1, 3, '#5a5f6c')
c.rect(16, 6, 1, 3, '#5a5f6c')
c.rect(8, 9, 11, 6, '#e8e4d8')
c.rect(10, 11, 5, 1, '#2a2f3e')
c.rect(10, 13, 7, 1, '#2a2f3e')
# wall sign: line number + arrow
c.rect(50, 10, 13, 9, '#1d4f9c')
c.rect(50, 10, 13, 1, '#3a6cc0')
c.rect(50, 10, 1, 9, '#3a6cc0')
c.rect(50, 18, 13, 1, '#12336a')
c.text(56, 11, '4', '#f2f4f7', font='5x7')
c.line(52, 14, 55, 14, '#f2f4f7')
c.line(54, 13, 55, 14, '#f2f4f7')
c.line(54, 15, 55, 14, '#f2f4f7')
# small route strip on wall
c.rect(50, 30, 8, 6, '#e8e4d8')
c.rect(51, 32, 6, 1, '#d24a3a')
c.set(52, 32, '#1d4f9c')
c.set(56, 32, '#1d4f9c')

# ---------------- bench ----------------
c.rect(50, 44, 12, 2, '#8a5a34')         # backrest
c.rect(50, 49, 12, 2, '#8a5a34')         # seat
c.rect(51, 46, 1, 3, '#5f3c22')
c.rect(60, 46, 1, 3, '#5f3c22')
c.rect(51, 51, 1, 4, '#5f3c22')          # legs
c.rect(60, 51, 1, 4, '#5f3c22')

# ---------------- passenger 1: standing, checking phone ----------------
c.rect(36, 41, 4, 2, '#2b2320')          # hair
c.rect(36, 43, 4, 3, '#e0b088')          # head
c.rect(35, 46, 6, 7, '#2e7d74')          # coat
c.rect(33, 44, 2, 3, '#1a1d24')          # phone
c.set(34, 45, '#bfe3ea')                 # lit screen
c.rect(34, 46, 2, 2, '#e0b088')          # hand
c.rect(35, 48, 2, 2, '#2e7d74')          # arm
c.rect(36, 53, 2, 5, '#33383f')          # legs
c.rect(39, 53, 2, 5, '#33383f')
c.rect(35, 58, 3, 1, '#1a1d24')          # shoes
c.rect(39, 58, 3, 1, '#1a1d24')

# ---------------- passenger 2: walking, mid-stride ----------------
c.rect(44, 42, 4, 2, '#4a3320')          # hair
c.rect(44, 44, 4, 3, '#c68d62')          # head
c.rect(45, 47, 6, 6, '#d9a13b')          # jacket
c.rect(43, 48, 2, 2, '#d9a13b')          # front arm swing
c.rect(50, 48, 2, 2, '#c68d3a')          # back arm swing
c.line(46, 53, 43, 60, '#33383f')        # front leg
c.line(47, 53, 50, 60, '#33383f')        # back leg
c.rect(41, 60, 3, 1, '#1a1d24')          # front shoe
c.rect(49, 60, 3, 1, '#1a1d24')          # back shoe

# ---------------- passenger 3: sitting on bench ----------------
c.rect(54, 39, 4, 2, '#1a1d24')          # hair
c.rect(54, 41, 4, 2, '#e8b48e')          # head
c.rect(53, 43, 5, 6, '#6a4a8c')          # dress / torso
c.rect(52, 46, 2, 2, '#6a4a8c')          # arm
c.rect(50, 49, 5, 2, '#6a4a8c')          # thighs
c.rect(50, 51, 2, 3, '#33383f')          # shins
c.rect(48, 54, 3, 1, '#1a1d24')          # shoes

print(c.stats_text())
finish(c)
