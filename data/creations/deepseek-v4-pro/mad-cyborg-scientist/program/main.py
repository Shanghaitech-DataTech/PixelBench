c = new_canvas(64, 64, background=None, name="mad-cyborg")

# ---------- palette ----------
bg       = c.color('#0d0e14', 'bg')
bg2      = c.color('#1a1b26', 'bg2')
glow     = c.color('#0f3a44', 'glow')
skin     = c.color('#e3ac7f', 'skin')
skin_hi  = c.color('#f2cba4', 'skin_hi')
skin_sh  = c.color('#b07f5c', 'skin_sh')
metal    = c.color('#9fb0c0', 'metal')
metal_hi = c.color('#c8d6e2', 'metal_hi')
metal_sh = c.color('#5b6a7a', 'metal_sh')
metal_dk = c.color('#37424f', 'metal_dk')
eye      = c.color('#3cf0ff', 'eye')
eye_core = c.color('#d0fbff', 'eye_core')
hair     = c.color('#eef1f5', 'hair')
hair_sh  = c.color('#c3cad4', 'hair_sh')
hair_dk  = c.color('#96a0ad', 'hair_dk')
coat     = c.color('#d9d2c0', 'coat')
coat_sh  = c.color('#a89e89', 'coat_sh')
coat_dk  = c.color('#7d745f', 'coat_dk')
apron    = c.color('#6e4c33', 'apron')
apron_sh = c.color('#4c3322', 'apron_sh')
apron_hi = c.color('#8d6744', 'apron_hi')
belt     = c.color('#2c2830', 'belt')
buckle   = c.color('#c2a04a', 'buckle')
mouth    = c.color('#5e2a2e', 'mouth')
teeth    = c.color('#efe6d4', 'teeth')
eye_white= c.color('#f2ece0', 'eye_white')
pupil    = c.color('#241f26', 'pupil')
cable    = c.color('#3a4a5c', 'cable')
cable_red= c.color('#b0463e', 'cable_red')
cable_ylw= c.color('#c8a24a', 'cable_ylw')
coat_hi  = c.color('#efe8d6', 'coat_hi')
hair_hi  = c.color('#ffffff', 'hair_hi')

# ---------- background ----------
c.rect(0, 0, 64, 64, bg)
c.dither(0, 0, 32, 64, [bg2, bg], 'bayer4')       # key light side, subtle
c.ellipse(32, 27, 21, 24, glow)                 # halo behind head

# ---------- hair (behind head) ----------
c.ellipse(32, 14, 21, 12, hair)

spikes = [
    [(15, 8), (12, 2), (19, 7)],
    [(21, 6), (22, 1), (26, 6)],
    [(28, 5), (31, 0), (34, 5)],
    [(36, 5), (39, 1), (42, 6)],
    [(44, 6), (48, 2), (49, 8)],
    [(13, 16), (9, 22), (14, 20)],
    [(14, 22), (10, 28), (16, 24)],
    [(50, 16), (55, 22), (50, 20)],
    [(49, 22), (54, 28), (48, 24)],
]
for s in spikes:
    c.poly(s, hair)

# ---------- head silhouette ----------
head_pts = [(19, 8), (24, 5), (31, 4), (38, 5), (44, 8), (48, 14),
            (49, 22), (48, 30), (45, 38), (40, 44), (35, 46),
            (29, 46), (24, 44), (19, 38), (16, 30), (15, 22), (16, 14)]
c.poly(head_pts, skin)

# metal half of head
metal_pts = [(32, 5), (38, 5), (44, 8), (48, 14), (49, 22), (48, 30),
             (45, 38), (40, 44), (35, 46), (32, 44)]
c.poly(metal_pts, metal)

# split seam + rivets
c.line(32, 5, 32, 44, metal_dk)
for y in (10, 16, 22, 28, 34, 40):
    c.set(32, y, metal_hi)

# ---------- mechanical details on metal half ----------
c.line(32, 10, 48, 13, metal_sh)       # forehead plate
c.line(34, 26, 48, 24, metal_sh)       # cheek plate
c.line(34, 34, 47, 36, metal_sh)       # jaw plate
c.line(38, 38, 44, 42, metal_sh)       # jaw hinge
c.set(35, 14, metal_hi); c.set(44, 11, metal_hi)
c.set(37, 27, metal_hi); c.set(45, 25, metal_hi)
c.set(39, 35, metal_hi); c.set(43, 40, metal_hi)
c.line(48, 16, 49, 24, metal_dk)       # right edge shadow
c.line(47, 28, 48, 36, metal_dk)
# cheek vents + glowing circuit trace
c.line(36, 29, 46, 29, metal_dk)
c.line(37, 31, 45, 31, metal_dk)
c.set(35, 30, metal_hi)
c.line(42, 27, 42, 33, eye)

# ---------- human eye (left) ----------
c.rect(20, 21, 9, 5, skin_sh)
c.rect(21, 22, 7, 3, eye_white)
c.rect(23, 22, 3, 3, pupil)
c.set(21, 22, skin_hi)                 # glint

# brow
c.line(19, 18, 28, 17, hair)
c.line(19, 19, 28, 18, hair_sh)

# ---------- cybernetic eye (right) ----------
c.ellipse(42, 23, 3, 3, metal_dk)
c.ellipse(42, 23, 2, 2, eye)
c.ellipse(42, 23, 1, 1, eye_core)
# glow spill on metal
c.set(37, 22, eye); c.set(38, 24, eye); c.set(40, 20, eye)
c.set(45, 21, eye); c.set(46, 24, eye)

# metal brow
c.line(37, 18, 46, 16, metal_hi)
c.line(37, 19, 46, 17, metal_sh)

# ---------- nose (split down the middle) ----------
c.rect(30, 25, 2, 8, skin)
c.rect(32, 25, 2, 8, metal)
c.rect(29, 33, 3, 2, skin_sh)
c.rect(32, 33, 3, 2, metal_sh)
c.set(34, 24, eye)                     # tiny glow reflection on bridge

# ---------- maniacal grin ----------
mouth_pts = [(21, 37), (27, 35), (33, 36), (39, 36), (43, 34),
             (44, 36), (42, 40), (36, 42), (30, 42), (24, 41)]
c.poly(mouth_pts, mouth)
c.line(23, 36, 42, 35, teeth)          # upper teeth
for x in (26, 29, 32, 35, 38):
    c.line(x, 35, x, 36, mouth)
c.line(44, 36, 47, 38, metal_dk)       # metal jaw seam

# ---------- brain electrode plugs (temple / forehead) ----------
c.ellipse(17, 12, 1, 1, metal_hi)
c.ellipse(21, 9, 1, 1, metal_hi)
c.ellipse(15, 16, 1, 1, metal_hi)
c.line(17, 12, 12, 6, cable)
c.line(21, 9, 17, 4, cable_red)
c.line(15, 16, 10, 13, cable_ylw)
c.ellipse(45, 9, 1, 1, metal_hi)
c.line(45, 9, 49, 5, cable)

# top-of-skull plug
c.rect(30, 1, 5, 4, metal_sh)
c.rect(31, 2, 3, 2, metal_hi)
c.line(32, 5, 32, 9, cable)

# ---------- neck ----------
c.rect(29, 45, 3, 4, skin)
c.rect(32, 45, 3, 4, metal)

# ---------- lab coat ----------
coat_pts = [(10, 50), (14, 46), (26, 45), (30, 48), (34, 48), (38, 45),
            (50, 46), (54, 50), (57, 60), (56, 63), (8, 63), (6, 58)]
c.poly(coat_pts, coat)

# collar
c.line(29, 48, 27, 52, coat_sh)
c.line(35, 48, 37, 52, coat_sh)
c.line(30, 49, 34, 49, coat_dk)

# stains / shadows on coat
c.rect(10, 53, 4, 3, coat_dk)
c.rect(17, 56, 3, 2, coat_sh)
c.rect(44, 55, 4, 3, coat_dk)
c.rect(52, 52, 3, 3, coat_sh)
c.line(7, 58, 10, 55, coat_sh)
c.line(55, 55, 57, 60, coat_sh)

# ---------- leather apron ----------
apron_pts = [(21, 51), (28, 49), (36, 49), (43, 51), (45, 58), (42, 63),
             (22, 63), (19, 58)]
c.poly(apron_pts, apron)
c.line(21, 51, 19, 58, apron_sh)
c.line(43, 51, 45, 58, apron_sh)
c.line(23, 53, 41, 53, apron_sh)       # stitch line
c.line(24, 54, 40, 54, apron_hi)

# straps
c.line(22, 51, 15, 47, apron_sh)
c.line(42, 51, 49, 47, apron_sh)

# ---------- tool belt ----------
c.rect(8, 59, 48, 5, belt)
c.rect(29, 59, 6, 4, buckle)
c.rect(12, 59, 5, 4, apron_sh)         # pouch
c.rect(47, 59, 5, 4, apron_sh)         # pouch
c.set(14, 61, buckle)
c.set(49, 61, buckle)
# wrench tucked in the belt (left)
c.rect(13, 55, 2, 5, metal)
c.rect(12, 54, 4, 1, metal_hi)
c.set(14, 56, metal_dk)

# ---------- exposed metal robotic arm + prosthetic hand ----------
c.ellipse(50, 45, 6, 4, metal)         # shoulder pauldron
c.set(52, 44, eye)                     # glowing indicator light
c.rect(47, 46, 9, 8, metal_sh)         # upper arm
c.line(47, 46, 55, 46, metal_hi)       # highlight
c.rect(46, 54, 8, 6, metal)            # forearm
c.line(46, 54, 53, 54, metal_hi)
c.set(52, 56, metal_dk)                # elbow joint
c.rect(43, 55, 12, 4, metal_sh)        # wrist block

# prosthetic fingers (three, with dark gaps between them)
c.rect(44, 58, 2, 4, metal_hi)
c.rect(47, 58, 2, 4, metal_hi)
c.rect(50, 58, 2, 4, metal_hi)
c.line(43, 57, 53, 57, metal_hi)       # knuckle plate
c.set(42, 58, metal)                   # thumb stub
c.set(42, 59, metal)

# cables from wrist, curling left across the belt
c.line(43, 58, 37, 55, cable)
c.line(43, 60, 35, 60, cable_red)
c.line(44, 61, 39, 63, cable_ylw)
c.line(45, 59, 41, 57, cable)

# ---------- lighting accents ----------
c.line(17, 10, 20, 8, skin_hi)
c.line(16, 14, 20, 12, skin_hi)
c.line(16, 20, 20, 18, skin_hi)
c.line(17, 26, 20, 24, skin_hi)
c.line(19, 32, 22, 30, skin_hi)
# bright rim light on lit (left) side
c.set(16, 12, hair_hi)
c.set(15, 16, hair_hi)
c.set(15, 22, skin_hi)
c.set(16, 28, skin_hi)
c.line(12, 8, 14, 4, hair_hi)
c.line(10, 50, 14, 46, coat_hi)
c.line(11, 53, 15, 49, coat_hi)
c.line(13, 57, 16, 54, coat_hi)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63)))
finish(c)
