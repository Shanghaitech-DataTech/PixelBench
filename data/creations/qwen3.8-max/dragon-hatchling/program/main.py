# Dragon hatchling - 64x64 RPG enemy sprite
# Pose: 3/4 side view facing left, low growl with open mouth,
#       half-spread wings (far wing up-left, near wing up-right),
#       scaled green body with pale belly plate, small horns, spiked tail.

# ---------------------------------------------------------------- palette
OUT    = '#150d1a'   # outline
DARK   = '#2c4a30'   # deep scale shadow
MID    = '#4d8f4c'   # body green
LIGHT  = '#7cc45f'   # lit scales
HL     = '#a9dd80'   # brightest scale hint
PALE   = '#e8dcae'   # belly plate
PALESH = '#bda871'   # belly shadow
MEMB   = '#c4705c'   # wing membrane (near)
MEMBL  = '#e2927a'   # membrane highlight
MEMBD  = '#8b4346'   # wing membrane (far / shadowed)
MEMBDD = '#6b3238'   # far membrane deep
BONE   = '#e3d0a2'   # horns, claws, spikes
BONED  = '#a08a5c'   # bone shade
EYE    = '#ffc93c'
MOUTH  = '#3d1a24'
TONGUE = '#c2506a'
WHITE  = '#fdf6e3'

main = new_canvas(64, 64, name='dragon')


# ---------------------------------------------------------------- helpers
def P():
    """A fresh full-size part canvas (absolute coordinates)."""
    return new_canvas(64, 64)


def ring(dst, part, colour=OUT):
    """Paint an 1px 8-connected outline ring around part's opaque pixels."""
    pw, ph, data = part.to_rgba()
    n = pw * ph
    al = [1 if data[i * 4 + 3] else 0 for i in range(n)]
    for y in range(ph):
        row = y * pw
        for x in range(pw):
            if al[row + x]:
                continue
            hit = False
            for dy in (-1, 0, 1):
                ny = y + dy
                if ny < 0 or ny >= ph:
                    continue
                r2 = ny * pw
                for dx in (-1, 0, 1):
                    nx = x + dx
                    if nx < 0 or nx >= pw:
                        continue
                    if al[r2 + nx]:
                        hit = True
                        break
                if hit:
                    break
            if hit:
                dst.set(x, y, colour)


def stamp(part, colour=OUT):
    ring(main, part, colour)
    main.blit(part, 0, 0)


def blobs(c, pts, colour):
    """Tapering limb/tail: (x, y, r) samples drawn as filled discs."""
    for x, y, r in pts:
        if r <= 0:
            c.set(x, y, colour)
        else:
            c.circle(int(x), int(y), int(r), colour)


# ================================================================ FAR WING
fw = P()
# membrane: wrist W(36,3) -> finger tips -> shoulder S(36,28) -> elbow E(34,15)
fw.path("M 36 3 L 27 6 Q 31 8 27 13 Q 31 14 31 19 Q 34 20 36 24 "
        "L 36 28 L 34 15 Z", MEMBD)
for tx, ty in ((27, 6), (27, 13), (31, 19), (36, 24)):
    fw.line(36, 3, tx, ty, MEMB)
blobs(fw, [(36, 28, 2), (35, 24, 2), (34, 20, 2), (34, 15, 2),
           (35, 11, 1), (35, 7, 1), (36, 3, 1)], DARK)
blobs(fw, [(35, 23, 1), (34, 18, 1), (35, 12, 1)], MID)
fw.path("M 36 3 L 38 1 L 40 3 L 37 5 Z", BONED)          # wrist claw
stamp(fw)

# ================================================================ NEAR WING
nw = P()
# membrane: wrist W(56,8) -> tips -> shoulder S(38,33) -> elbow E(48,20)
nw.path("M 56 8 L 62 13 Q 57 17 61 22 Q 56 24 56 29 Q 51 29 48 34 "
        "L 38 33 L 48 20 Z", MEMBD)
nw.path("M 56 8 L 62 13 Q 57 17 61 22 Q 56 24 56 29 Q 51 29 48 34 "
        "L 45 32 Q 51 26 53 19 Q 54 12 56 8 Z", MEMB)
for tx, ty in ((62, 13), (61, 22), (56, 29), (48, 34)):
    nw.line(56, 8, tx, ty, MEMBL)
blobs(nw, [(38, 33, 3), (41, 29, 3), (44, 25, 2), (48, 20, 2),
           (51, 16, 2), (53, 12, 1), (56, 8, 1)], MID)
blobs(nw, [(40, 30, 1), (43, 26, 1), (47, 21, 1), (50, 17, 1),
           (52, 13, 1)], LIGHT)
nw.path("M 56 8 L 60 3 L 62 6 L 58 10 Z", BONE)          # wrist claw
stamp(nw)

# ================================================================ TAIL
tl = P()
blobs(tl, [(41, 45, 5), (45, 47, 5), (48, 49, 4), (51, 50, 4), (54, 51, 3),
           (57, 51, 3), (59, 49, 3), (60, 46, 2), (60, 43, 2), (59, 40, 2),
           (57, 38, 1), (55, 37, 1)], MID)
blobs(tl, [(45, 49, 3), (49, 51, 2), (53, 52, 2), (57, 52, 1), (59, 50, 1)], DARK)
blobs(tl, [(44, 45, 2), (48, 47, 2), (52, 48, 1), (56, 49, 1)], LIGHT)
# spikes along the outer edge
tl.path("M 46 44 L 49 37 L 52 45 Z", BONE)
tl.path("M 49 45 L 55 40 L 55 48 Z", BONE)
tl.path("M 58 44 L 63 42 L 61 49 Z", BONE)
# spade tip
tl.path("M 55 38 L 52 31 L 58 29 L 60 35 L 57 40 Z", MEMB)
tl.path("M 55 38 L 53 33 L 57 32 L 58 36 Z", MEMBD)
stamp(tl)

# ================================================================ TORSO
to = P()
# neck
to.path("M 18 26 C 22 22 27 20 31 21 C 33 28 35 34 38 41 "
        "C 33 45 26 46 22 44 C 20 38 18 32 18 26 Z", MID)
# body
to.path("M 24 30 C 32 26 42 29 46 37 C 50 44 47 52 40 54 "
        "C 32 56 25 52 23 45 C 21 39 22 33 24 30 Z", MID)
# back shading
to.path("M 26 29 C 33 26 42 29 46 37 C 48 41 48 45 47 48 "
        "C 47 42 44 36 39 33 C 34 30 29 29 26 29 Z", DARK)
to.path("M 20 30 C 22 26 26 23 30 22 C 27 25 24 28 22 32 Z", DARK)
# lit shoulder / haunch
to.path("M 30 33 C 35 31 40 33 42 37 C 39 34 34 33 30 35 Z", LIGHT)
for x, y in ((33, 32), (36, 32), (39, 34), (41, 36), (28, 34), (30, 31)):
    to.set(x, y, HL)
# pale belly: throat -> chest -> abdomen (wide band on the front/underside)
to.path("M 19 27 C 21 33 23 39 24 43 C 25 49 30 54 37 54 "
        "C 42 54 46 51 47 46 C 45 50 40 52 35 51 "
        "C 30 49 28 44 27 38 C 26 33 22 29 21 25 Z", PALE)
to.path("M 24 43 C 25 49 30 54 37 54 C 42 54 46 51 47 46 "
        "C 45 50 41 52 37 52 C 31 52 27 48 24 43 Z", PALESH)
# belly creases
for a, b in (((21, 32), (25, 33)), ((22, 37), (26, 38)), ((23, 42), (27, 43)),
             ((28, 49), (32, 51)), ((33, 51), (36, 53)), ((39, 51), (41, 53)),
             ((44, 48), (46, 50))):
    to.line(a[0], a[1], b[0], b[1], PALESH)
# scale texture on the flank
for x, y in ((30, 40), (33, 42), (36, 40), (39, 43), (34, 46), (30, 45),
             (42, 41), (44, 45), (27, 37), (37, 37), (41, 38), (26, 41)):
    to.set(x, y, DARK)
for x, y in ((31, 39), (34, 41), (37, 39), (35, 45), (31, 44), (43, 40)):
    to.set(x, y, LIGHT)
# dorsal spike on the back (the rest of the row runs along the tail)
to.path("M 40 29 L 45 24 L 46 32 Z", BONE)
stamp(to)

# ================================================================ HIND LEG
hl = P()
hl.path("M 40 39 C 47 37 52 42 52 47 C 52 52 47 55 43 53 "
        "C 39 51 38 42 40 39 Z", MID)
hl.path("M 41 41 C 46 39 50 42 50 46 C 48 42 44 41 41 43 Z", LIGHT)
hl.path("M 42 50 C 47 52 51 50 51 46 C 51 51 47 54 43 53 Z", DARK)
blobs(hl, [(45, 52, 2), (44, 55, 2), (43, 57, 2)], MID)
hl.path("M 38 56 C 43 54 48 55 50 57 L 50 59 C 45 61 39 60 37 59 Z", MID)
hl.path("M 38 58 C 42 59 47 59 50 58 L 50 59 C 45 61 39 60 38 59 Z", DARK)
hl.path("M 37 58 L 34 61 L 38 60 Z", BONE)
hl.path("M 42 59 L 40 62 L 44 60 Z", BONE)
hl.path("M 47 59 L 47 62 L 50 59 Z", BONE)
stamp(hl)

# ================================================================ FRONT LEG
fl = P()
fl.path("M 26 40 C 30 39 33 42 33 47 L 32 52 L 26 52 C 25 47 25 43 26 40 Z", MID)
fl.path("M 27 41 C 30 40 32 43 32 46 C 30 43 28 42 27 43 Z", LIGHT)
blobs(fl, [(29, 52, 2), (28, 54, 2), (27, 56, 2)], MID)
fl.path("M 22 56 C 26 54 31 55 33 57 L 33 59 C 28 61 23 60 21 59 Z", MID)
fl.path("M 22 58 C 26 59 30 59 33 58 L 33 59 C 28 61 23 60 22 59 Z", DARK)
fl.path("M 21 58 L 18 61 L 23 60 Z", BONE)
fl.path("M 26 59 L 25 62 L 29 60 Z", BONE)
fl.path("M 31 59 L 32 62 L 33 59 Z", BONE)
stamp(fl)

# ================================================================ HEAD
hd = P()
# mouth cavity (drawn first, jaws overlap it leaving an open wedge)
hd.path("M 8 21 L 24 19 L 25 31 L 9 33 Z", MOUTH)
# skull + upper jaw
hd.path("M 20 12 C 15 12 10 16 8 21 L 7 25 L 21 23 "
        "C 26 23 29 18 28 15 C 26 12 23 12 20 12 Z", MID)
hd.path("M 20 12 C 15 12 11 15 9 19 C 12 15 16 13 20 13 "
        "C 24 13 27 15 28 17 C 28 14 25 12 20 12 Z", LIGHT)
hd.path("M 8 23 L 21 22 L 21 23 L 7 25 Z", DARK)
# lower jaw
hd.path("M 22 26 C 16 27 10 29 8 30 C 8 33 10 34 13 34 "
        "L 20 34 C 24 33 27 30 26 28 Z", MID)
hd.path("M 9 32 C 12 34 18 34 22 32 C 24 31 26 29 26 28 "
        "C 26 31 22 33 18 33 C 14 33 11 33 9 32 Z", DARK)
hd.path("M 10 30 C 14 29 18 28 22 27 C 18 29 14 30 10 31 Z", LIGHT)
# tongue
hd.path("M 10 31 C 14 29 18 28 22 27 L 22 29 C 18 30 14 31 11 32 Z", TONGUE)
# teeth: upper (pointing down) then lower (pointing up)
hd.path("M 9 24 L 11 24 L 10 27 Z", WHITE)
hd.path("M 13 23 L 15 23 L 14 28 Z", WHITE)
hd.path("M 17 23 L 19 23 L 18 26 Z", WHITE)
hd.path("M 11 30 L 13 29 L 12 27 Z", WHITE)
hd.path("M 16 28 L 18 28 L 17 26 Z", WHITE)
# eye
hd.set(12, 19, EYE); hd.set(13, 19, EYE); hd.set(14, 19, EYE)
hd.set(12, 20, EYE); hd.set(13, 20, EYE); hd.set(14, 20, EYE)
hd.set(13, 21, EYE); hd.set(14, 21, EYE)
hd.set(13, 19, OUT); hd.set(13, 20, OUT); hd.set(13, 21, OUT)
hd.set(12, 19, WHITE)
hd.line(10, 17, 16, 17, DARK)
hd.set(16, 18, DARK); hd.set(11, 22, DARK); hd.set(12, 22, DARK)
# nostril
hd.set(9, 23, OUT); hd.set(10, 23, OUT)
# horns: main swept-back horn + small second horn
hd.path("M 22 13 L 30 8 L 32 11 L 26 18 Z", BONE)
hd.path("M 25 16 L 31 10 L 32 11 L 26 18 Z", BONED)
hd.path("M 24 19 L 30 16 L 31 19 L 26 23 Z", BONE)
hd.path("M 26 21 L 30 18 L 31 19 L 26 23 Z", BONED)
# crest spike on the snout bridge
hd.path("M 12 13 L 9 7 L 16 11 Z", BONE)
# cheek frill
hd.path("M 25 26 L 33 25 L 34 30 L 27 31 Z", MEMBD)
hd.path("M 27 29 L 33 28 L 34 30 L 27 31 Z", MEMBDD)
stamp(hd)

# ================================================================ GROWL
gr = P()
gr.path("M 4 23 Q 1 28 4 34", PALE, fill=False)
gr.path("M 1 25 Q 0 29 1 32", PALESH, fill=False)
main.blit(gr, 0, 0)

save('dragon_hatchling', main)
print(main.stats_text())
view(main)
view(main, scale=8, margin=0)
finish(main)
