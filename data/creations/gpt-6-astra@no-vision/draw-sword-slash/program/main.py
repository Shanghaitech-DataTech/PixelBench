f1 = input_canvas.copy(name="frame1")

# Build the motion trail behind the original sprite.
trail = new_canvas(62, 72, name="slash trail")
black = "#020202"
trail.poly([(14, 62), (20, 49), (25, 38), (33, 26), (43, 14), (56, 3), (52, 18), (44, 29), (35, 40), (26, 51)], black)
# Thin branching cuts keep the trail energetic while retaining its rising direction.
trail.line(20, 52, 14, 56, black)
trail.line(39, 24, 43, 18, black)
trail.line(47, 16, 53, 11, black)

f2 = flatten([trail, input_canvas], name="frame2")
# The blade is visibly connected to the left-side hand and ends in the direction of the swing.
# Dark outline, cool steel body, and a bright edge remain distinct at this scale.
f2.line(20, 46, 38, 28, black)
f2.line(21, 45, 37, 29, "#69657d")
f2.line(22, 45, 36, 30, "#d9d7e2")
# Short guard and grip at the hand.
f2.line(18, 43, 23, 48, "#120d1c")
f2.line(18, 44, 22, 48, "#926e6b")
f2.line(19, 43, 22, 46, "#231c2c")

print("frame1:", f1.stats_text())
print("frame2:", f2.stats_text())
finish([f1, f2])
