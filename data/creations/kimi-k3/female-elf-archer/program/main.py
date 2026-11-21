# Female elf archer - 64x64 RPG character portrait (v2)

SKIN    = '#f6cf9f'
SKIN_L  = '#ffe6c2'
SKIN_D  = '#d99f66'
HAIR_D  = '#2c7a40'
HAIR_M  = '#47ad5d'
HAIR_L  = '#7fd98c'
HAIR_H  = '#c4f4c4'
EYE     = '#157a46'
EYE_H   = '#eafff0'
OUT     = '#23311d'
CLOTH_L = '#e8f5cc'
CLOTH   = '#bce39c'
CLOTH_D = '#89bf68'
CLOTH_DD= '#5f9648'
TRIM    = '#f7fae8'
BELT    = '#7c522e'
GOLD    = '#f2cb5e'
BOOT    = '#8d5c33'
BOOT_D  = '#5f3b1d'
BOW     = '#a8723c'
BOW_D   = '#6f4620'
STRING  = '#f0e7c9'
FLETCH  = '#eaf4ee'
TEAL    = '#58c2a8'
MOUTH   = '#c96f62'
SHADOW  = (18, 30, 16, 88)

L0 = new_canvas(64, 64, name='shadow')
L1 = new_canvas(64, 64, name='gear')
C  = new_canvas(64, 64, name='elf')

L0.ellipse(31, 61, 13, 2, SHADOW)

# ---------- gear behind the body ----------
# longbow along the right side: wide D-profile, string vertical at x=46
L1.path('M46 8 Q56 30 46 52', BOW, fill=False)
L1.path('M46 8 Q55 30 46 52', BOW, fill=False)   # second pass thickens the belly
L1.line(46, 8, 46, 52, STRING)
L1.set(46, 7, BOW_D); L1.set(46, 53, BOW_D)      # tip caps
L1.rect(49, 28, 2, 3, BOW_D)                     # grip at the belly

# quiver on the back-left, mostly behind hair/torso
L1.poly([(19, 12), (25, 11), (24, 26), (18, 25)], BOOT_D)
L1.line(19, 12, 25, 11, GOLD)
# arrows above the shoulder
for ax in (20, 22, 24):
    L1.line(ax, 4, ax, 12, BOW_D)
    L1.set(ax - 1, 3, TEAL)
    L1.set(ax + 1, 3, TEAL)
    L1.set(ax, 2, FLETCH)

# ---------- back hair ----------
C.ellipse(32, 8, 8, 5, HAIR_M)          # crown mass
C.rect(23, 9, 3, 22, HAIR_M)            # left fall
C.rect(37, 9, 4, 33, HAIR_M)            # right fall
C.set(23, 31, HAIR_M); C.set(25, 31, HAIR_M)
C.set(37, 42, HAIR_M); C.set(39, 43, HAIR_M)
C.line(40, 11, 40, 40, HAIR_D)
C.line(23, 11, 23, 29, HAIR_D)
C.line(38, 12, 38, 38, HAIR_L)
C.line(24, 11, 24, 27, HAIR_L)
C.line(28, 4, 36, 4, HAIR_L)
C.set(30, 3, HAIR_H); C.set(31, 3, HAIR_H); C.set(32, 3, HAIR_H)

# ---------- body ----------
# neck
C.rect(29, 16, 4, 2, SKIN)
C.rect(29, 17, 4, 1, SKIN_D)
# head
C.rect(28, 6, 8, 1, SKIN)
C.rect(26, 7, 12, 8, SKIN)              # rows 7..14
C.rect(27, 15, 10, 1, SKIN)
C.rect(28, 16, 8, 1, SKIN)              # chin
C.line(26, 9, 26, 14, SKIN_D)           # far side shade
C.set(27, 15, SKIN_D)
C.rect(34, 9, 2, 3, SKIN_L)             # near cheek light
# pointed ears
C.poly([(36, 9), (43, 7), (37, 12)], SKIN)
C.line(38, 10, 41, 9, SKIN_D)
C.poly([(26, 9), (21, 10), (26, 12)], SKIN)
C.set(24, 10, SKIN_D)
C.set(37, 12, GOLD)                              # earring on near ear

# torso
C.rect(25, 18, 13, 8, CLOTH)            # y=18..25
C.rect(26, 26, 11, 2, CLOTH)
C.rect(25, 18, 2, 8, CLOTH_D)
C.rect(32, 19, 5, 6, CLOTH_L)
C.set(29, 18, TRIM); C.set(30, 18, TRIM)
C.set(30, 19, GOLD)
# quiver strap across the chest
C.line(25, 19, 37, 27, BOOT_D)
# belt + buckle
C.rect(26, 28, 11, 2, BELT)
C.rect(30, 28, 3, 2, GOLD)

# skirt with jagged hem
C.rect(24, 30, 15, 4, CLOTH)            # y=30..33
C.rect(23, 34, 17, 3, CLOTH)            # y=34..36
C.rect(23, 37, 17, 1, TRIM)
for px in (24, 28, 32, 36):
    C.rect(px, 38, 2, 2, CLOTH)
C.rect(23, 34, 2, 3, CLOTH_D)
C.set(33, 31, CLOTH_L); C.set(34, 32, CLOTH_L)

# far arm (image left)
C.rect(24, 19, 2, 9, CLOTH_D)
C.rect(24, 28, 2, 3, SKIN)

# near arm: bent, hand on hip
C.circle(40, 20, 2, CLOTH_L)
C.line(41, 22, 43, 27, SKIN)
C.line(40, 22, 42, 27, SKIN)
C.line(43, 27, 39, 31, SKIN)
C.line(42, 28, 39, 31, SKIN)
C.line(42, 27, 40, 29, BOOT)           # bracer
C.rect(37, 30, 3, 3, SKIN)              # hand on hip

# legs (deep green leggings), 1px gap between
C.rect(28, 40, 3, 9, CLOTH_DD)
C.rect(32, 40, 3, 9, CLOTH_DD)

# boots
C.rect(27, 49, 4, 8, BOOT)
C.rect(32, 49, 4, 8, BOOT)
C.rect(27, 49, 4, 2, BOOT_D)
C.rect(32, 49, 4, 2, BOOT_D)
C.rect(25, 57, 6, 3, BOOT)              # left foot, toe left
C.rect(32, 57, 7, 3, BOOT)              # right foot, toe right
C.rect(25, 59, 6, 1, BOOT_D)
C.rect(32, 59, 7, 1, BOOT_D)

# ---------- front hair ----------
# bangs: short jagged strands, ends above the lashes
for i, sx in enumerate(range(26, 38, 2)):
    C.rect(sx, 6, 2, 2 + (i % 2), HAIR_M)   # rows 6..8/9
C.line(27, 5, 36, 5, HAIR_L)
C.set(29, 8, HAIR_D); C.set(33, 9, HAIR_D)
# front lock over near shoulder
C.line(37, 9, 37, 25, HAIR_M)
C.line(36, 11, 36, 23, HAIR_M)
C.set(37, 26, HAIR_M)
C.line(36, 12, 36, 21, HAIR_L)
# circlet
C.line(27, 6, 36, 6, GOLD)
C.set(31, 6, TEAL)

# ---------- face ----------
C.set(27, 10, OUT)                       # far lash
C.set(27, 11, EYE); C.set(27, 12, EYE)
C.line(31, 10, 34, 10, OUT)              # near lash
C.rect(31, 11, 3, 2, EYE)
C.set(31, 11, EYE_H)
C.set(28, 13, SKIN_D)                    # nose
C.set(29, 14, MOUTH)                     # mouth
C.set(30, 14, MOUTH)

# ---------- outline ----------
C.outline(OUT)

result = flatten([L0, L1, C], name='result')
print(result.stats_text())
save('female-elf-archer', result)
view(result)
finish(result)
