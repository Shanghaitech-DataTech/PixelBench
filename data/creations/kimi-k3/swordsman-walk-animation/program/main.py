# Swordsman walk animation: 64x32 canvas = two 32x32 frames, side view facing right.
# 16-bit RPG style: red hair, long sword, dark blue cape.
try:
    new_canvas
except NameError:
    from pixelbench_api import *

COL = dict(
    hair_hi='#e05840', hair='#c03828', hair_dk='#882018',
    skin='#f0c8a0', skin_dk='#d8a078', eye='#282028',
    tunic='#3e6b4a', tunic_dk='#2c4c38', belt='#6a4526',
    pants='#4a3a2e', pants_dk='#38291f', boot='#33241a',
    cape='#25376b', cape_dk='#18244a', cape_hi='#3a4f8c',
    blade='#cfd4de', blade_hi='#eef1f6', blade_dk='#8b93a3',
    guard='#c9a13b', grip='#4e3020',
)
SH = (14, 14, 24, 88)  # soft ground shadow


def frame(c, ox, f):
    def S(x, y, k):
        c.set(ox + x, y, COL[k])

    def R(x, y, w, h, k):
        c.rect(ox + x, y, w, h, COL[k])

    b = 0 if f == 0 else -1  # body bob: frame 2 rides 1px higher

    # ---- ground shadow
    c.ellipse(ox + 16, 29, 9, 1, SH)

    # ---- cape (behind everything)
    if f == 0:
        R(10, 11, 3, 1, 'cape'); R(9, 12, 4, 1, 'cape'); R(8, 13, 5, 2, 'cape')
        R(7, 15, 6, 1, 'cape')
        R(7, 16, 5, 1, 'cape_dk'); R(6, 17, 6, 1, 'cape_dk')
        R(6, 18, 5, 1, 'cape_dk'); R(5, 19, 5, 1, 'cape_dk'); R(5, 20, 3, 1, 'cape_dk')
        S(9, 12, 'cape_hi'); S(10, 12, 'cape_hi'); S(8, 13, 'cape_hi'); S(9, 13, 'cape_hi')
    else:
        R(10, 10, 3, 1, 'cape'); R(9, 11, 4, 1, 'cape'); R(8, 12, 5, 2, 'cape')
        R(7, 14, 6, 1, 'cape')
        R(7, 15, 5, 1, 'cape_dk'); R(6, 16, 5, 1, 'cape_dk')
        R(5, 17, 5, 1, 'cape_dk'); R(5, 18, 4, 1, 'cape_dk'); R(4, 19, 3, 1, 'cape_dk')
        S(9, 11, 'cape_hi'); S(10, 11, 'cape_hi'); S(8, 12, 'cape_hi')

    # ---- legs
    if f == 0:
        # back leg trailing left
        R(10, 19, 3, 1, 'pants_dk'); R(10, 20, 2, 3, 'pants_dk'); R(9, 23, 2, 3, 'pants_dk')
        R(7, 26, 4, 2, 'boot'); S(6, 27, 'boot')
        # front leg striding right
        R(13, 19, 3, 1, 'pants'); R(14, 20, 2, 3, 'pants'); R(15, 23, 2, 3, 'pants')
        R(15, 26, 4, 2, 'boot'); S(19, 27, 'boot')
    else:
        # support leg planted straight
        R(12, 18, 2, 8, 'pants_dk'); R(11, 26, 4, 2, 'boot')
        # passing leg bent and lifted mid-swing
        R(14, 18, 2, 2, 'pants'); R(15, 20, 2, 3, 'pants')
        R(15, 23, 3, 1, 'boot'); R(16, 24, 2, 1, 'boot')

    # ---- torso
    R(12, 11 + b, 5, 1, 'tunic')          # shoulders
    R(11, 12 + b, 6, 5, 'tunic')          # body
    R(11, 12 + b, 1, 5, 'tunic_dk')       # back shading
    S(13, 12 + b, 'belt'); S(14, 13 + b, 'belt')   # chest strap
    S(15, 14 + b, 'belt'); S(15, 15 + b, 'belt')
    R(11, 17 + b, 6, 1, 'belt')           # belt
    S(15, 17 + b, 'guard')                # buckle
    R(11, 18 + b, 5, 1, 'tunic_dk')       # tunic skirt
    S(12, 11 + b, 'guard')                # cape clasp

    # ---- head
    S(13, 10 + b, 'skin_dk'); S(14, 10 + b, 'skin_dk')   # neck
    R(14, 6 + b, 3, 4, 'skin')            # face
    S(17, 8 + b, 'skin')                  # nose
    S(16, 7 + b, 'eye')
    # hair: top, back mass, flowing ponytail
    R(12, 4 + b, 5, 1, 'hair')
    R(11, 5 + b, 6, 1, 'hair')
    S(14, 5 + b, 'hair_hi'); S(15, 5 + b, 'hair_hi'); S(13, 4 + b, 'hair_hi')
    R(11, 6 + b, 3, 2, 'hair')
    R(11, 8 + b, 2, 2, 'hair')
    R(11, 10 + b, 2, 2, 'hair_dk')
    if f == 0:
        R(9, 6, 2, 2, 'hair'); R(7, 7, 2, 2, 'hair'); R(5, 9, 3, 1, 'hair_dk')
    else:
        R(9, 4, 2, 2, 'hair'); R(7, 5, 2, 2, 'hair'); R(5, 6, 3, 1, 'hair_dk')

    # ---- front arm and long sword (held forward, horizontal)
    R(17, 12 + b, 2, 2, 'tunic')          # sleeve / arm
    R(19, 13 + b, 1, 2, 'skin')           # hand on grip
    S(18, 14 + b, 'guard')                # pommel
    R(20, 12 + b, 1, 4, 'guard')          # crossguard
    R(21, 13 + b, 9, 1, 'blade_hi')       # blade, lit edge
    R(21, 14 + b, 6, 1, 'blade')          # blade body
    R(27, 14 + b, 3, 1, 'blade_dk')       # blade shadow toward tip
    S(30, 13 + b, 'blade_hi')             # tip


c = new_canvas(64, 32, name='swordsman_walk')
frame(c, 0, 0)
frame(c, 32, 1)
print(c.stats_text())
view(c)
finish(c)
