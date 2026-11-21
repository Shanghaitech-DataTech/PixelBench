# Stardew-style cozy farm sheep, 32x32, side view, transparent background.
W = H = 32
c = new_canvas(W, H, name="sheep")

# ---------------------------------------------------------------- palette ---
wool_hi = c.color('#fdfaf2', 'wool_hi')   # fleece highlight
wool    = c.color('#f3ebda', 'wool')      # fleece base
wool_sh = c.color('#e2d5bf', 'wool_sh')   # fleece soft shade
wool_dp = c.color('#cfc0a6', 'wool_dp')   # fleece deep shade

face    = c.color('#f8efe4', 'face')      # muzzle / head base
face_sh = c.color('#e3d0bd', 'face_sh')   # head shade

ear     = c.color('#eec7c1', 'ear')       # pale pink ear
ear_sh  = c.color('#d7a49f', 'ear_sh')    # inner ear

leg     = c.color('#f1e5d5', 'leg')       # near leg
leg_sh  = c.color('#dbc9b3', 'leg_sh')    # near leg shade
leg_far = c.color('#cdb9a2', 'leg_far')   # far leg
hoof    = c.color('#a3836d', 'hoof')
hoof_fr = c.color('#8b7059', 'hoof_fr')

eye     = c.color('#5d483c', 'eye')
nose    = c.color('#c99a8d', 'nose')
blush   = c.color('#f0cbc2', 'blush')


# ----------------------------------------------------------------- helper ---
def masked(target, draw_fn, allowed):
    """Draw draw_fn on a scratch layer, keep only pixels landing on `allowed`."""
    tmp = new_canvas(W, H)
    draw_fn(tmp)
    tw, th, buf = tmp.to_rgba()
    for y in range(th):
        for x in range(tw):
            o = (y * tw + x) * 4
            if buf[o + 3] == 0:
                continue
            if target.get(x, y) in allowed:
                target.set(x, y, tmp.get(x, y))


# ------------------------------------------------------------------- legs ---
# far legs (behind the fleece)
c.rect(15, 16, 3, 8, leg_far)
c.rect(15, 23, 3, 2, hoof_fr)
c.rect(23, 16, 3, 8, leg_far)
c.rect(23, 23, 3, 2, hoof_fr)

# near legs
c.rect(12, 17, 3, 9, leg)
c.rect(14, 17, 1, 9, leg_sh)
c.rect(12, 25, 3, 2, hoof)
c.rect(20, 17, 3, 9, leg)
c.rect(22, 17, 1, 9, leg_sh)
c.rect(20, 25, 3, 2, hoof)

# ------------------------------------------------------------- fleece body ---
def body_base(t):
    t.ellipse(18, 13, 7, 5, wool)
    # top bumps
    t.circle(13, 8, 2, wool)
    t.circle(17, 7, 2, wool)
    t.circle(21, 8, 2, wool)
    t.circle(24, 9, 2, wool)
    # right bumps
    t.circle(25, 11, 2, wool)
    t.circle(25, 13, 2, wool)
    t.circle(25, 15, 2, wool)
    t.circle(27, 10, 1, wool)   # little tail tuft
    # bottom bumps
    t.circle(13, 18, 2, wool)
    t.circle(17, 19, 2, wool)
    t.circle(21, 18, 2, wool)
    t.circle(24, 17, 2, wool)

body_base(c)


def body_shade(t):
    t.ellipse(18, 20, 8, 5, wool_sh)
    t.circle(13, 16, 2, wool_sh)
    t.circle(17, 15, 2, wool_sh)
    t.circle(21, 16, 2, wool_sh)
    t.circle(24, 17, 2, wool_sh)

masked(c, body_shade, {wool})


def body_light(t):
    t.ellipse(15, 9, 5, 3, wool_hi)
    t.circle(20, 8, 2, wool_hi)
    t.circle(24, 11, 1, wool_hi)

masked(c, body_light, {wool, wool_sh})


def body_deep(t):
    t.ellipse(18, 24, 7, 3, wool_dp)
    t.ellipse(13, 13, 2, 3, wool_dp)    # shadow the head casts on the fleece
    t.circle(25, 17, 1, wool_dp)

masked(c, body_deep, {wool, wool_sh, wool_hi})


def curls(t):
    for (x, y) in [(14, 13), (18, 14), (22, 13), (16, 17), (20, 18), (24, 15), (13, 16)]:
        t.path('M%d %d q1 2 2 0' % (x, y), wool_sh, fill=False)
    for (x, y) in [(15, 9), (19, 10), (23, 10), (12, 11)]:
        t.path('M%d %d q1 2 2 0' % (x, y), wool_hi, fill=False)

masked(c, curls, {wool, wool_sh, wool_hi, wool_dp})

# ------------------------------------------------------------------- head ---
def head_base(t):
    t.ellipse(8, 11, 4, 4, face)      # skull
    t.ellipse(6, 14, 3, 2, face)      # muzzle
    t.rect(5, 12, 6, 3, face)

head_base(c)


def head_shade(t):
    t.rect(11, 10, 1, 5, face_sh)     # back of the jaw
    t.rect(10, 13, 1, 2, face_sh)
    t.rect(6, 15, 4, 1, face_sh)      # under-chin shade

masked(c, head_shade, {face})

# ear: narrow band drooping back from under the wool cap
for (x, y) in [(11, 9), (12, 9), (13, 10), (14, 11), (14, 12)]:
    c.set(x, y, ear)
for (x, y) in [(12, 10), (13, 11), (13, 12)]:
    c.set(x, y, ear_sh)

# fluffy forelock over the forehead, scalloped fringe
def cap(t):
    t.circle(6, 7, 2, wool)
    t.circle(9, 7, 2, wool)
    t.circle(4, 8, 1, wool)
    t.circle(11, 8, 1, wool)

cap(c)

# face features
c.set(6, 11, eye)
c.set(7, 11, eye)
c.set(6, 12, eye)
c.set(3, 13, nose)
c.set(4, 13, nose)
c.set(4, 15, nose)
c.set(8, 13, blush)
c.set(9, 13, blush)
c.set(8, 14, blush)

print(c.matrix_text(region=(0, 4, 18, 20)))
view(c)
save('sheep_v3', c)
finish(c)
