# squid-red-idle : 3 frames, gentle breathing bob
#   frame 1 = original artwork
#   frame 2 = mantle lifted 1px (inhale / body stretches, tentacle feet planted)
#   frame 3 = mantle settled 1px (exhale / body squashes, tentacle feet planted)

W, H = 58, 58      # original 58x57 plus one spare row above for the lift
OFF = 1            # sprite sits at canvas rows 1..57
SH = 57
K = 46             # rows <= K (mantle, head, crown curls, arms) bob; rows > K (tentacle feet) stay planted

# ---------------- frame 1: untouched original picture ----------------
f1 = new_canvas(W, H, name='f1')
f1.blit(input_canvas, 0, OFF)


def build(name, dy):
    """dy=-1 -> mantle lifts 1px (body 1px taller); dy=+1 -> mantle settles 1px (body 1px shorter)."""
    cv = new_canvas(W, H, name=name)
    # planted tentacle feet / arm tips: pixel-identical in every frame
    for r in range(K + 1, SH):
        for x in range(W):
            v = input_canvas.get(x, r)
            if v:
                cv.set(x, r + OFF, v)
    if dy < 0:
        # whole mantle shifted up 1px; the anchor row is repeated so the
        # trunk stretches by 1px and stays welded to the planted feet
        for r in range(0, K + 1):
            for x in range(W):
                v = input_canvas.get(x, r)
                if v:
                    cv.set(x, r + OFF + dy, v)
        for x in range(W):
            v = input_canvas.get(x, K)
            if v:
                cv.set(x, K + OFF, v)
    else:
        # whole mantle shifted down 1px; the seam row folds away so the
        # trunk squashes by 1px, everything below it untouched
        for r in range(0, K):
            for x in range(W):
                v = input_canvas.get(x, r)
                if v:
                    cv.set(x, r + OFF + dy, v)
    return cv


f2 = build('f2', -1)   # inhale: rises 1px
f3 = build('f3', 1)    # exhale: settles 1px

for n, f in (('f1', f1), ('f2', f2), ('f3', f3)):
    print(n, f.stats_text())

save('squid-red-idle_1', f1)
save('squid-red-idle_2', f2)
save('squid-red-idle_3', f3)

finish([f1, f2, f3])
