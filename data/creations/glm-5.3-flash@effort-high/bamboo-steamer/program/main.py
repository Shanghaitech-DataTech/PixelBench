from pixelbench_api import new_canvas, finish, view, save

c = new_canvas(32, 32, background=None, name="bamboo-steamer")

# ---- palette ----
C_OUT   = c.color('#5C3D1E', name='outline')
C_BAM   = c.color('#C89B55', name='bamboo')
C_BAM_D = c.color('#9A6F33', name='bamboo_dark')
C_BAM_L = c.color('#E8C989', name='bamboo_light')
C_DUM   = c.color('#F7F1DF', name='dumpling')
C_DUM_D = c.color('#D9CFB4', name='dumpling_shade')
C_DUM_O = c.color('#A99C7E', name='dumpling_outline')
C_STEAM = c.color('#DFF0F5', name='steam')
C_KNOB  = c.color('#7A5526', name='knob')
C_IN    = c.color('#3A2814', name='interior')

# ---- lid: drawn flat, tilted -30 deg, propped on the rim's left edge ----
lid = new_canvas(26, 16, background=None, name="lid")
lid.ellipse(13, 8, 12, 3, C_BAM_L, fill=True)
lid.ellipse(13, 8, 12, 3, C_OUT, fill=False)
lid.ellipse(13, 8, 8, 2, C_BAM_D, fill=False)   # woven ring
lid.circle(13, 4, 1, C_KNOB)
lid.set(12, 4, C_OUT); lid.set(14, 4, C_OUT)
lid.set(12, 5, C_OUT); lid.set(14, 5, C_OUT)

s = lid.select(0, 0, 26, 16)
r = s.rotate(-30)
r.copy_to(-5, -2, c, mode="over")

# ---- dumplings go in AFTER the lid, so nothing is painted over them ----
def dumpling(cx, top):
    widths = [3, 5, 5, 5, 5]
    for i, w in enumerate(widths):
        y = top + i
        x0 = cx - w // 2
        c.rect(x0, y, w, 1, C_DUM_O)
        if w >= 5:
            c.rect(x0 + 1, y, w - 2, 1, C_DUM)
    c.set(cx, top, C_DUM)
    c.set(cx, top + 1, C_DUM_D)          # centre pleat
    c.set(cx - 1, top, C_DUM_D)
    c.set(cx + 1, top, C_DUM_D)
    for dy in (2, 3, 4):                 # right-side shading
        c.set(cx + 1, top + dy, C_DUM_D)

c.rect(5, 12, 22, 5, C_IN)               # dark interior, rows 12-16
for cx in (12, 18, 24):
    dumpling(cx, 12)

# ---- basket rim ----
c.rect(4, 17, 24, 1, C_BAM_L)
c.rect(4, 18, 24, 1, C_BAM_D)
c.set(4, 17, C_OUT); c.set(27, 17, C_OUT)
c.set(4, 18, C_OUT); c.set(27, 18, C_OUT)

# ---- basket body ----
c.rect(5, 19, 22, 6, C_BAM)               # rows 19-24
for x in (5, 26):
    for y in range(19, 25):
        c.set(x, y, C_OUT)
c.rect(6, 25, 20, 1, C_BAM)
c.set(6, 25, C_OUT); c.set(25, 25, C_OUT)
c.rect(7, 26, 18, 1, C_BAM_D)
c.set(7, 26, C_OUT); c.set(24, 26, C_OUT)
c.rect(9, 27, 14, 1, C_OUT)
for x in (9, 13, 17, 22):                 # vertical slats
    c.rect(x, 20, 1, 5, C_BAM_D)

# ---- small rising steam through the open gap (drawn last) ----
for (x, y) in [(27, 13), (27, 12), (26, 11), (27, 10), (26, 9), (27, 8),
               (24, 14), (25, 13)]:
    c.set(x, y, C_STEAM)

print(c.stats_text())
print(c.matrix_text())
save("bamboo-steamer", c)
finish(c)
