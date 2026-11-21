from pixelbench_api import *

# 32x32 transparent pixel-art chainmail armor
c = new_canvas(32, 32, background=None, name="chainmail_armor")

# Palette: deep outline, blue-steel shadows, iron mids, restrained highlights
outline = "#18232b"
deep = "#26343b"
shadow = "#3d4b52"
steel = "#68777a"
mid = "#879493"
light = "#adb6ad"
high = "#d4d4bf"
blue = "#53656d"

# Back silhouette and broad shoulder/torso contour
c.poly([(11,3),(20,3),(21,7),(24,9),(28,11),(30,15),(28,19),(26,19),(26,29),(23,31),(9,31),(6,29),(6,19),(4,19),(2,15),(5,11),(8,9),(11,7)], outline)

# Main shirt body
c.poly([(11,8),(20,8),(22,11),(25,14),(24,28),(21,29),(11,29),(8,27),(8,14)], steel)
# dark lower side folds
c.poly([(8,17),(11,18),(11,29),(9,28),(8,26)], shadow)
c.poly([(21,17),(24,16),(24,28),(21,29)], deep)
# central steel plane
c.poly([(12,11),(19,11),(21,14),(21,28),(11,28),(11,14)], mid)

# Shoulder masses, with dark segmented undersides
c.poly([(8,9),(12,9),(13,14),(10,18),(6,17),(4,15),(6,12)], blue)
c.poly([(20,9),(24,10),(28,13),(28,16),(26,18),(22,17),(19,14)], blue)
c.poly([(5,15),(9,16),(10,18),(7,18),(4,16)], deep)
c.poly([(23,16),(27,15),(28,17),(26,19),(22,18)], deep)
# shoulder edge plates
c.rect(5,12,4,2, shadow)
c.rect(6,10,4,2, steel)
c.rect(23,11,4,2, steel)
c.rect(25,13,3,2, shadow)
c.set(5,13, light); c.set(24,12, light)

# Collar / neck opening and folded collar
c.poly([(11,6),(20,6),(21,10),(19,13),(12,13),(10,10)], outline)
c.poly([(12,7),(19,7),(19,10),(17,12),(14,12),(12,10)], deep)
c.poly([(10,8),(13,10),(13,13),(10,11)], shadow)
c.poly([(19,8),(22,10),(20,13),(18,11)], shadow)
c.rect(12,6,7,1, steel)
c.set(13,6, light); c.set(18,6, light)

# Blocky hem and side trim
c.rect(10,28,12,2, deep)
c.rect(12,28,8,1, shadow)
c.set(12,28, light); c.set(19,28, mid)
c.rect(7,26,2,2, deep); c.rect(23,25,2,3, outline)

# Pixel ring motif: each ring is a dark 3x3 loop with steel body and one glint.
def ring(x, y, shade=steel, glint=True):
    c.rect(x+1,y,1,1, outline)
    c.rect(x,y+1,1,1, outline)
    c.rect(x+2,y+1,1,1, outline)
    c.rect(x+1,y+2,1,1, outline)
    c.set(x+1,y+1, shade)
    if glint:
        c.set(x,y+1, light)

# Alternating rows visually suggest interlocking links across the mail field.
for x in (10,14,18,22):
    ring(x,14, steel, x in (10,18))
for x in (8,12,16,20,24):
    ring(x,17, mid, x in (12,20))
for x in (10,14,18,22):
    ring(x,20, steel, x in (10,18))
for x in (8,12,16,20,24):
    ring(x,23, mid, x in (12,20))
for x in (10,14,18,22):
    ring(x,26, steel, x in (10,18))

# Additional rings across shoulder mail, partially tucked beneath plates
for x,y in ((6,14),(9,12),(22,13),(25,15),(7,16),(24,16)):
    ring(x,y,shadow,False)

# Small bright steel catches and dark rivet accents
c.set(11,13, high); c.set(19,13, high)
c.set(9,19, high); c.set(23,19, light)
c.set(11,25, high); c.set(19,25, light)
c.set(7,14, outline); c.set(26,15, outline)

# Crisp silhouette accents
c.line(5,18,8,19, outline)
c.line(24,18,27,18, outline)
c.set(8,28, outline); c.set(23,29, outline)

view(c, scale=16, margin=1)
finish(c)
