# Two-frame elf archer attack animation.
W, H = 52, 47
f1 = new_canvas(W, H, name="frame_1_original")
f2 = new_canvas(W, H, name="frame_2_full_draw")

# Preserve the source exactly in frame 1, with equal-height transparent staging room.
f1.blit(input_canvas, 8, 0)

# Frame 2 starts from the source, shifted left to make room for the fully drawn bow.
f2.blit(input_canvas, 1, 0)

# Palette aliases from the original sprite.
outline = 20       # #121311
outline2 = 25      # #14110e
brown = 2          # #7b4231
wood_dark = 1      # #422110
wood_light = 9     # #df9859
skin = 12          # #f6d39b
skin_light = 14    # #faf3c9
skin_shadow = 16   # #a9794f
green = 26         # #9cde5a
green_dark = 24    # #304915
metal = 33         # #a4b496
string = 35        # #ffffce

# Remove the old close bow, extended arm, and their shadowed overlap.
f2.clear(20, 16, 32, 16)
f2.clear(28, 0, 24, 40)

# Open the stance by shifting the feet farther apart while retaining original detail.
left_foot = input_canvas.select(0, 38, 12, 9).preview()
right_foot = input_canvas.select(18, 38, 12, 9).preview()
f2.clear(0, 38, 31, 9)
f2.blit(left_foot, 0, 38)
f2.blit(right_foot, 24, 38)
# Reconnect the planted ankles.
f2.poly([(8,35),(13,35),(14,41),(11,43),(7,40)], outline2)
f2.poly([(9,35),(12,35),(12,40),(9,40)], 38)
f2.poly([(19,35),(23,35),(27,41),(25,43),(21,40)], outline2)
f2.poly([(20,35),(22,35),(25,40),(22,40)], 39)

# Fully flexed bow: string first so the hand and grip sit in front of it.
f2.line(44, 3, 19, 16, outline2)
f2.line(19, 16, 44, 43, outline2)
f2.line(44, 4, 20, 16, string)
f2.line(20, 16, 44, 42, string)

# Tall recurved bow, strongly opened around the grip.
f2.path("M44 3 C47 8 49 13 46 18 C44 21 42 22 40 22 C43 23 45 26 47 30 C49 35 47 40 44 43", outline2, fill=False)
f2.path("M43 4 C46 9 47 14 45 18 C43 21 41 21 39 22 C42 23 44 27 46 31 C47 35 46 39 43 42", wood_dark, fill=False)
f2.path("M44 5 C46 10 46 14 44 18 M44 26 C47 32 46 37 44 41", wood_light, fill=False)
# Reinforced tips and central leather grip.
f2.rect(42, 2, 3, 3, outline2)
f2.set(43, 3, wood_light)
f2.rect(42, 42, 3, 3, outline2)
f2.set(43, 42, wood_light)
f2.rect(38, 19, 4, 7, outline2)
f2.rect(39, 20, 2, 5, brown)
f2.set(40, 22, wood_light)

# Drawing arm: elbow driven behind the torso, forearm folded sharply to the cheek.
# Short upper arm and green sleeve run back from the shoulder to the elbow.
f2.poly([(18,21),(15,20),(10,20),(7,22),(7,25),(10,26),(15,24),(19,24)], outline2)
f2.poly([(17,22),(14,21),(10,21),(8,23),(10,25),(15,23),(18,23)], green_dark)
f2.poly([(16,22),(13,22),(10,23),(12,24),(16,23)], green)
# Narrow bare forearm rises diagonally from the rear elbow to the jaw.
f2.poly([(7,21),(9,19),(17,15),(21,15),(22,18),(19,20),(11,25),(7,25),(5,23)], outline2)
f2.poly([(8,21),(10,20),(18,16),(20,16),(20,18),(18,19),(10,24),(7,24),(7,22)], skin)
f2.line(10,21,18,17,skin_light)
f2.set(9,23,skin_shadow)
f2.set(10,23,skin_shadow)
# Rear hand anchors at the jaw and visibly pinches only the string: no arrow.
f2.rect(17, 14, 5, 5, outline2)
f2.rect(18, 15, 3, 3, skin)
f2.set(19,15,skin_light)
f2.set(21,16,skin_shadow)

# Bow arm: shoulder rolls forward and the arm locks nearly straight toward the grip.
f2.poly([(16,22),(19,19),(25,19),(31,20),(38,19),(41,21),(41,25),(38,27),(31,24),(25,24),(20,26),(16,25)], outline2)
# Green sleeve emerging from the torso.
f2.poly([(16,22),(19,20),(23,20),(25,24),(20,26),(16,25)], green_dark)
f2.poly([(18,22),(20,21),(23,21),(24,23),(20,24),(18,24)], green)
# Long straight forearm and highlights.
f2.poly([(24,20),(31,21),(37,20),(39,21),(39,24),(37,25),(31,23),(24,24)], skin)
f2.line(26,21,36,22,skin_light)
f2.line(27,24,36,24,skin_shadow)
# Closed bow hand around the grip.
f2.rect(37, 20, 4, 6, outline2)
f2.rect(38, 21, 3, 4, skin)
f2.set(39,21,skin_light)
f2.set(40,24,skin_shadow)

# Restore a crisp shoulder edge and a slight forward torso lean.
f2.line(16, 25, 18, 30, outline2)
f2.line(17, 25, 19, 30, green_dark)
f2.set(18,26,green)

view(f2, scale=10, margin=1, edges="all")
finish([f1, f2])
