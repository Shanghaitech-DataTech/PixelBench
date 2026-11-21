# Frame 1 is an exact editable copy of the supplied image.
f1 = input_canvas.copy(name="frame1")

# Build frame 2 from the original so all character pixels remain available.
scene = input_canvas.copy(name="scene")

# Remove the old down-left blade from the action frame. These narrow erasures
# follow the existing blade and leave the character's legs and hand intact.
for a, b, c, d in [
    (0, 64, 34, 42),
    (0, 67, 34, 45),
    (2, 69, 35, 47),
]:
    scene.line(a, b, c, d, "transparent")

# The completed slash: a tapered dark-red silhouette with a solid black core.
trail = new_canvas(62, 72, name="slash_trail")
trail.poly([(7, 64), (10, 67), (61, 16), (59, 12)], "#1b0202")
trail.poly([(10, 64), (12, 66), (59, 15), (58, 13)], "#020202")
# Broken outer pixels give the trail a crisp pixel-art taper.
trail.line(3, 66, 8, 62, "#71444c")
trail.line(11, 69, 15, 65, "#71444c")
trail.line(60, 11, 61, 9, "#71444c")

# Put the trail in front of the figure so the completed motion reads clearly.
f2 = flatten([scene, trail], name="frame2")

# Sword held in the left hand, angled along the final upward-right motion.
# The blade is dark outlined with a pale steel edge and a sharp tip.
f2.poly([(35, 42), (38, 44), (61, 11), (59, 9)], "#120d1c")
f2.poly([(38, 41), (40, 42), (60, 11), (59, 10)], "#eedddd")
f2.line(40, 41, 59, 12, "#9b938d")
f2.line(59, 10, 61, 8, "#eedddd")
# Guard and a short dark grip sit at the left-side hand.
f2.poly([(32, 39), (39, 40), (41, 43), (34, 44)], "#9b938d")
f2.line(34, 43, 29, 46, "#1b0202")
f2.line(30, 45, 35, 41, "#3d2c32")

view(f1, scale=6)
view(f2, scale=6)
print(f2.stats_text())
print(input_canvas.matrix_text(region=(0,40,40,68)))
finish([f1, f2])
