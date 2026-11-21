# Two-frame draw-sword slash animation on a roomier shared stage.
W, H = 96, 80
OX, OY = 18, 4

# Source palette sampled from the original sprite.
pal = input_canvas.palette()
for p in pal:
    print(p)

f1 = new_canvas(W, H, name="frame_1_original")
f1.blit(input_canvas, OX, OY)

f2 = new_canvas(W, H, name="frame_2_completed_slash")

# Completed lower-left to upper-right black slash trail, behind the character.
# A stepped outer wake makes the direction legible in pixel art.
black = "#050509"
black2 = "#101018"
edge = "#29283a"
f2.poly([(3,68),(8,61),(16,55),(27,49),(39,42),(53,33),(66,23),(79,12),(91,3),
         (86,13),(76,23),(64,34),(51,44),(38,53),(25,61),(13,68)], black)
f2.poly([(7,69),(17,62),(29,55),(42,47),(57,37),(70,27),(84,13),(91,7),
         (84,18),(72,30),(59,41),(45,51),(31,59),(18,66)], black2)
# Broken rims frame the black core so it remains readable on transparency.
f2.line(5,68,20,60,edge)
f2.line(24,57,39,49,edge)
f2.line(44,46,58,37,edge)
f2.line(62,34,74,24,edge)
f2.line(78,20,88,9,edge)
f2.line(9,70,24,62,"#171722")
f2.line(29,59,42,52,"#171722")
f2.set(3,70,edge).set(5,69,edge).set(12,66,edge).set(27,57,edge)

# Character over the wake.
f2.blit(input_canvas, OX, OY)

# Remove only the old blade and its stray dark outline; retain the left gripping hand.
f2.clear(OX, OY+39, 28, 13)

# Rebuild a few back-edge pixels where the old blade crossed the coat.
coat_dark = pal[7]["rgba"] if False else "#29283f"
f2.rect(OX+27, OY+40, 3, 6, coat_dark)
f2.rect(OX+29, OY+38, 3, 7, coat_dark)

# Left-hand grip remains at the original lower hand, around (48,48) on this stage.
# Dark pommel and wrapped hilt point into the completed diagonal.
hilt_dark = "#17131b"
hilt_mid = "#443342"
wrap = "#9b6f6d"
steel_dark = "#77768a"
steel = "#b9b9c5"
shine = "#e5e1df"
skin = "#f39a69"

# Reinforce the visible left hand around the grip, separate from the free right hand.
f2.rect(45,46,7,6,skin)
f2.rect(48,44,5,7,skin)
f2.set(45,45,skin).set(44,48,skin).set(46,52,skin)
# Pommel behind the fist and a short wrapped hilt under the palm.
f2.line(43,53,49,47,hilt_dark)
f2.line(44,52,50,46,hilt_mid)
f2.line(48,45,55,51,hilt_dark)
f2.line(49,45,54,50,wrap)
# Compact guard centered just beyond the gripping left fist.
f2.line(51,43,58,50,hilt_dark)
f2.line(52,42,59,49,steel_dark)
f2.rect(54,43,2,2,shine)

# Raised sword from lower-left grip to upper-right endpoint.
# Black outline first, then steel body and a bright edge.
f2.poly([(52,44),(55,47),(89,10),(91,5),(86,9)], hilt_dark)
f2.poly([(54,44),(56,46),(88,11),(90,7),(86,11)], steel_dark)
f2.poly([(56,43),(57,44),(89,8),(90,6),(87,9)], steel)
f2.line(58,42,89,7,shine)
# Pixel tip and tiny motion sparks at the terminal upper-right.
f2.set(91,5,shine).set(92,4,steel).set(89,3,edge)
f2.set(93,8,edge).set(88,1,black2)

finish([f1, f2])
view(f1, scale=5, margin=1, edges="all")
view(f2, scale=5, margin=1, edges="all")
