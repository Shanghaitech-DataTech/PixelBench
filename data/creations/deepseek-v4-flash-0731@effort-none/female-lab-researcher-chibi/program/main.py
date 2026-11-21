from pixelbench_api import *

c = new_canvas(16, 16)

# Palette
OUTLINE = c.color((15, 15, 20))        # dark outline
HAIR = c.color((25, 25, 32))           # black hair
HIGHLIGHT = c.color((80, 100, 130))    # hair highlight (blue sheen on black hair)
SKIN = c.color((242, 206, 170))        # skin
SKIN_SH = c.color((222, 184, 144))     # skin shadow
EYEB = c.color((38, 24, 14))           # eyebrow
EYE = c.color((120, 75, 40))           # brown eyes
EYED = c.color((70, 42, 22))           # eye dark
MOUTH = c.color((190, 105, 105))       # mouth
COAT = c.color((242, 242, 246))        # white lab coat
COAT_SH = c.color((205, 205, 213))     # coat shadow
COATD = c.color((155, 155, 168))       # coat dark detail
COLLAR = c.color((150, 175, 215))      # blue collar/lapel
SHIRT = c.color((220, 220, 228))       # inner shirt shadow
PANTS = c.color((70, 70, 88))          # dark pants
SHOE = c.color((55, 55, 70))           # shoes
BADGE = c.color((200, 120, 120))       # red badge/pin

# ---- HEAD (rows 0-8) ----
# Hair top outline
c.set(4, 0, OUTLINE)
c.set(5, 0, HAIR)
c.set(6, 0, HAIR)
c.set(7, 0, HAIR)
c.set(8, 0, HAIR)
c.set(9, 0, HAIR)
c.set(10, 0, HAIR)
c.set(11, 0, OUTLINE)

# Hair row 1 with highlight
c.rect(4, 1, 8, 1, HAIR)
c.set(6, 1, HIGHLIGHT)
c.set(7, 1, HIGHLIGHT)

# Hair row 2
c.set(3, 2, OUTLINE)
c.set(4, 2, HAIR)
c.set(5, 2, HAIR)
c.set(6, 2, HAIR)
c.set(7, 2, HAIR)
c.set(8, 2, HAIR)
c.set(9, 2, HAIR)
c.set(10, 2, HAIR)
c.set(11, 2, HAIR)
c.set(12, 2, OUTLINE)

# Row 3 - bangs with face starting
c.set(3, 3, HAIR)
c.set(4, 3, HAIR)
c.set(5, 3, SKIN)
c.set(6, 3, SKIN)
c.set(7, 3, SKIN)
c.set(8, 3, SKIN)
c.set(9, 3, SKIN)
c.set(10, 3, HAIR)
c.set(11, 3, HAIR)
c.set(12, 3, HAIR)

# Row 4 - eyes area
c.set(3, 4, HAIR)
c.set(4, 4, SKIN)
c.set(5, 4, EYE)
c.set(6, 4, EYE)
c.set(7, 4, SKIN)
c.set(8, 4, EYE)
c.set(9, 4, EYE)
c.set(10, 4, SKIN)
c.set(11, 4, SKIN)
c.set(12, 4, HAIR)

# Eye glints
c.set(6, 4, c.color((255, 255, 255)))
c.set(9, 4, c.color((255, 255, 255)))

# Row 5 - eyes lower / pupils
c.set(3, 5, HAIR)
c.set(4, 5, SKIN)
c.set(5, 5, EYED)
c.set(6, 5, SKIN)
c.set(7, 5, SKIN_SH)
c.set(8, 5, SKIN)
c.set(9, 5, EYED)
c.set(10, 5, SKIN)
c.set(11, 5, SKIN)
c.set(12, 5, HAIR)

# Row 6 - mouth area
c.set(3, 6, SKIN)
c.set(4, 6, SKIN)
c.set(5, 6, SKIN)
c.set(6, 6, SKIN)
c.set(7, 6, MOUTH)
c.set(8, 6, MOUTH)
c.set(9, 6, SKIN)
c.set(10, 6, SKIN)
c.set(11, 6, SKIN)
c.set(12, 6, SKIN)
c.set(13, 6, HAIR)
# Row 7 - chin + neck
c.set(3, 7, HAIR)
c.set(4, 7, SKIN)
c.set(5, 7, SKIN_SH)
c.set(6, 7, SKIN_SH)
c.set(7, 7, SKIN_SH)
c.set(8, 7, SKIN_SH)
c.set(9, 7, SKIN_SH)
c.set(10, 7, SKIN_SH)
c.set(11, 7, SKIN_SH)
c.set(12, 7, SKIN_SH)
c.set(13, 7, HAIR)

# ---- BODY (rows 8-15) ----
# Row 8 - coat collar / shoulders
c.set(1, 8, OUTLINE)
c.set(2, 8, COAT_SH)
c.set(3, 8, COLLAR)
c.set(4, 8, COLLAR)
c.set(5, 8, SHIRT)
c.set(6, 8, COAT)
c.set(7, 8, COAT)
c.set(8, 8, COAT)
c.set(9, 8, SHIRT)
c.set(10, 8, COLLAR)
c.set(11, 8, COLLAR)
c.set(12, 8, COAT_SH)
c.set(13, 8, OUTLINE)

# Row 9 - torso
c.set(1, 9, COAT_SH)
c.set(2, 9, COAT)
c.set(3, 9, COAT)
c.set(4, 9, COAT_SH)
c.set(5, 9, COAT)
c.set(6, 9, COAT)
c.set(7, 9, COAT)
c.set(8, 9, COAT)
c.set(9, 9, COAT)
c.set(10, 9, COAT_SH)
c.set(11, 9, COAT)
c.set(12, 9, COAT)
c.set(13, 9, COAT_SH)

# Row 10 - torso with pocket/buttons
c.set(1, 10, COAT_SH)
c.set(2, 10, COAT)
c.set(3, 10, COAT)
c.set(4, 10, COAT)
c.set(5, 10, COAT)
c.set(6, 10, COAT)
c.set(7, 10, COAT)
c.set(8, 10, COAT)
c.set(9, 10, COAT)
c.set(10, 10, COATD)
c.set(11, 10, COATD)
c.set(12, 10, COAT)
c.set(13, 10, COAT_SH)

# badge
c.set(7, 9, BADGE)

# Row 11 - torso continue
c.set(1, 11, COAT_SH)
c.set(2, 11, COAT)
c.set(3, 11, COAT)
c.set(4, 11, COAT)
c.set(5, 11, COAT_SH)
c.set(6, 11, COAT)
c.set(7, 11, COAT)
c.set(8, 11, COAT)
c.set(9, 11, COAT)
c.set(10, 11, COAT_SH)
c.set(11, 11, COAT)
c.set(12, 11, COAT)
c.set(13, 11, COAT_SH)

# Row 12 - coat hem
c.set(1, 12, OUTLINE)
c.set(2, 12, COAT_SH)
c.set(3, 12, COAT_SH)
c.set(4, 12, COAT)
c.set(5, 12, COAT)
c.set(6, 12, OUTLINE)
c.set(7, 12, OUTLINE)
c.set(8, 12, OUTLINE)
c.set(9, 12, OUTLINE)
c.set(10, 12, COAT)
c.set(11, 12, COAT)
c.set(12, 12, COAT_SH)
c.set(13, 12, COAT_SH)
c.set(14, 12, OUTLINE)

# Hands (skin) at bottom of sleeves
c.set(1, 13, SKIN)
c.set(2, 13, SKIN)
c.set(13, 13, SKIN)
c.set(14, 13, SKIN)

# ---- Legs (rows 13-15) ----
# Row 13 - legs
c.set(4, 13, OUTLINE)
c.set(5, 13, PANTS)
c.set(6, 13, PANTS)
c.set(7, 13, OUTLINE)
c.set(8, 13, OUTLINE)
c.set(9, 13, PANTS)
c.set(10, 13, PANTS)
c.set(11, 13, OUTLINE)

# Row 14 - shoes
c.set(4, 14, SHOE)
c.set(5, 14, SHOE)
c.set(6, 14, SHOE)
c.set(7, 14, OUTLINE)
c.set(8, 14, OUTLINE)
c.set(9, 14, SHOE)
c.set(10, 14, SHOE)
c.set(11, 14, SHOE)

# Row 15 - shoe bottoms
c.set(3, 15, OUTLINE)
c.set(4, 15, SHOE)
c.set(5, 15, SHOE)
c.set(6, 15, SHOE)
c.set(7, 15, OUTLINE)
c.set(8, 15, OUTLINE)
c.set(9, 15, SHOE)
c.set(10, 15, SHOE)
c.set(11, 15, SHOE)
c.set(12, 15, OUTLINE)

print(c.stats_text())
finish(c)
