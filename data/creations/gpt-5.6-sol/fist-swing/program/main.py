# Two-frame fist swing animation. The wider canvas gives the punch room to read.
W, H = 42, 44
OX = 4

frame1 = new_canvas(W, H, background=None, name="frame_1_original")
frame1.blit(input_canvas, OX, 0)

frame2 = frame1.copy(name="frame_2_light_punch")

# Palette indices from the supplied sprite.
ink = 1
hair_shadow = 2
skin = 3
skin_shadow = 4
shirt = 5
shirt_shadow = 6

# Remove the old bent/right-reaching arm while retaining the head and torso.
frame2.clear(19, 9, 23, 10)

# Straight punching arm silhouette: sleeve, tapered forearm and compact fist.
frame2.poly([
    (17, 9), (23, 9), (23, 10),
    (33, 10), (33, 11), (37, 11),
    (37, 12), (40, 12), (40, 16),
    (38, 16), (38, 17), (33, 17),
    (33, 18), (22, 18), (22, 17),
    (17, 17)
], ink)

# Orange short sleeve, attached cleanly at the shoulder.
frame2.poly([
    (18, 10), (22, 10), (22, 11), (25, 11),
    (25, 16), (22, 16), (22, 17), (18, 17)
], shirt)
frame2.rect(18, 15, 5, 2, shirt_shadow)
frame2.set(18, 10, shirt_shadow)
frame2.set(19, 10, shirt_shadow)

# Skin forearm narrows toward the wrist; shadow stays on the lower edge.
frame2.poly([(25, 11), (33, 11), (33, 12), (35, 12),
             (35, 16), (33, 16), (33, 17), (25, 17)], skin)
frame2.rect(25, 15, 9, 2, skin_shadow)
frame2.rect(25, 11, 2, 1, '#f6d3a8')

# Closed fist: stepped knuckles, short fingers and a tucked thumb.
frame2.rect(34, 12, 5, 5, skin)
frame2.rect(35, 11, 3, 1, skin)
frame2.rect(34, 16, 4, 1, skin_shadow)
frame2.rect(38, 13, 2, 3, skin)
frame2.set(39, 15, skin_shadow)
frame2.set(37, 12, skin_shadow)
frame2.set(34, 13, skin_shadow)  # tucked thumb crease

# Restore the small shoulder/chest overlap so the arm emerges from the torso.
frame2.rect(17, 15, 3, 3, shirt)
frame2.set(17, 17, shirt_shadow)
frame2.set(19, 17, shirt_shadow)

print(frame1.stats_text())
print(frame2.stats_text())
view(frame1, scale=10, margin=2, edges="all")
view(frame2, scale=10, margin=2, edges="all")
finish([frame1, frame2])
