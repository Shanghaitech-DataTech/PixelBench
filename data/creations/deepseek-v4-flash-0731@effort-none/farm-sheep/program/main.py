from pixelbench_api import *

c = new_canvas(32, 32, name="sheep")

# Palette - warm muted colors
white = c.color((245, 238, 228), name="white")          # main body
white_shadow = c.color((224, 214, 200), name="white_shadow")  # lower body shadow
white_dark = c.color((200, 188, 174), name="white_dark")      # deepest shadow
face = c.color((246, 220, 205), name="face")            # warm face tone
face_shadow = c.color((228, 198, 182), name="face_shadow")
ear = c.color((244, 205, 205), name="ear")              # pale pink
ear_inner = c.color((232, 178, 180), name="ear_inner")
leg = c.color((205, 195, 185), name="leg")
leg_shadow = c.color((178, 168, 158), name="leg_shadow")
eye = c.color((90, 80, 70), name="eye")
nose = c.color((220, 170, 160), name="nose")
cheek = c.color((224, 195, 195), name="cheek")

# --- BODY: main fluffy rounded body (right side) ---
# Body oval: x from 14 to 29, y from 12 to 26
c.ellipse(21, 18, 8, 7, white)     # main body
c.ellipse(21, 16, 7, 5, white)     # upper body rounder
c.ellipse(23, 20, 6, 5, white)     # rear body
c.ellipse(18, 20, 5, 5, white)     # front (attach to head)

# Wool bumps on top
c.ellipse(17, 13, 3, 2, white)
c.ellipse(21, 12, 3, 2, white)
c.ellipse(25, 13, 3, 2, white)
c.ellipse(28, 16, 2, 2, white)

# Tail (small ball at rear)
c.ellipse(29, 14, 2, 2, white)
c.ellipse(30, 15, 1, 1, white_shadow)

# --- HEAD (left side, facing left) ---
# Head rounded
c.ellipse(9, 17, 5, 4, face)       # head base
c.ellipse(9, 16, 4, 3, face)       # head upper
c.ellipse(6, 17, 2, 3, face)       # snout area (front/side)

# Wool on top of head
c.ellipse(11, 13, 3, 2, white)
c.ellipse(14, 13, 2, 1, white)

# --- EARS (pale pink, drooping) ---
# Front ear (near side, drooping down-left)
c.ellipse(6, 10, 2, 2, ear)
c.set(6, 11, ear_inner)
# Upper/back ear
c.ellipse(15, 11, 2, 2, ear)
c.set(15, 12, ear_inner)

# --- FACE details ---
# Eye
c.set(8, 16, eye)
c.set(7, 16, eye)
# Nose/muzzle
c.set(5, 17, nose)
# Cheek blush
c.ellipse(9, 18, 1, 1, cheek)

# --- LEGS ---
# Front legs (left)
c.rect(14, 24, 3, 5, leg)
c.rect(15, 26, 3, 3, leg_shadow)
# Back legs (right)
c.rect(25, 24, 3, 5, leg)
c.rect(26, 26, 3, 3, leg_shadow)

# --- SHADING ---
# Under-body shadow
c.ellipse(20, 24, 7, 2, white_shadow)
# Lower body shading
c.ellipse(20, 23, 7, 2, white_shadow)

# Soft wool shadow dots
for (sx, sy) in [(18,15),(22,14),(26,16),(16,17),(12,15),(24,18),(28,17),(19,20),(20,15)]:
    c.set(sx, sy, white_shadow)

# A couple deep shadow accents
c.ellipse(19, 25, 5, 1, white_dark)

# Head underside shadow
c.ellipse(8, 20, 3, 1, face_shadow)

print(c.stats_text())

finish(c)
