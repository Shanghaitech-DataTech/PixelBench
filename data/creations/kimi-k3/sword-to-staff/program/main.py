# sword-to-staff edit
out = input_canvas.copy(name='output')

W    = '#ffffffff'   # background white (opaque)
B    = '#2e1f12'     # dark outline
ZL   = '#93785a'     # wood light
PD   = '#6b4423'     # wood dark
GOLD = '#c9a227'     # gold
BR   = '#ffd94d'     # bright gold
PAL  = '#fff3b0'     # pale highlight
SKIN = '#f2c49b'
Q    = '#5c3a21'

# 1) Erase the sword: crossguard (y39-40, x40-46) and blade (y41-55, x42-44)
out.rect(40, 39, 7, 2, W)
out.rect(42, 41, 3, 15, W)

# 2) Draw the wooden shaft: outline x41/x44, wood x42/x43, from y11 down to ground y54
for y in range(11, 54):
    out.set(41, y, B)
    out.set(42, y, ZL)
    out.set(43, y, PD)
    out.set(44, y, B)
# bottom cap (planted on the ground, same level as boots)
out.rect(41, 54, 4, 1, B)

# 3) Redraw the fist on top of the shaft so the hand grips it
for y in (35, 36, 37):
    out.set(38, y, B)
    out.rect(39, y, 4, 1, SKIN)
    out.set(43, y, B)
out.set(38, 38, B)
out.set(39, 38, W)
out.set(40, 38, B)
out.set(41, 38, B)
out.set(42, 38, B)
out.set(43, 38, Q)

# 4) Golden orb on top of the staff
out.circle(42, 7, 3, B, fill=True)
out.circle(42, 7, 2, GOLD, fill=True)
out.circle(42, 7, 1, BR, fill=True)
out.set(41, 6, PAL)

print(out.matrix_text(region=(36, 2, 50, 56)))
view(out)
finish(out)
