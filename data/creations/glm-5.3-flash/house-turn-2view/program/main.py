# ============================================================================
# house-turn-2view
#
# Two views of the same cottage, both taken by one fixed elevated camera at a
# 45-degree pitch (same height, same tilt): the roof, its chimney and the
# ground shadow are pixel-identical in the two frames, so neither view
# flattens into an eye-level elevation.
#
#   frame 1  the house standing at its 45-degree position, exactly as
#            supplied: the front door and front wall, together with the
#            window and wall on the right-hand side.
#
#   frame 2  the house turned to its 90-degree position: the right-hand wall
#            now faces the camera squarely, so only that wall and its window
#            are seen.  The front door - arched leaf, dark reveal, threshold
#            seam and lower panels - is taken out and the wall is closed with
#            the same weathered plaster as the pilasters beside it.
# ============================================================================

src = input_canvas

f1 = src.copy(name="house_45deg")
f2 = src.copy(name="house_90deg")

PLASTER = 9      # #bbae93  wall plaster (same as the pilasters)
TRIM    = 10     # #e1dca3  pale trim specks

# ---- frame 2: lift the front door out of the wall --------------------------
# arched leaf + dark reveal + threshold seam + lower panels, x33-78 y116-143
f2.rect(33, 116, 46, 28, PLASTER)

# a few pale specks so the fresh plaster reads as the same weathered plaster
for x, y in [(38, 119), (52, 121), (66, 118), (44, 126), (60, 129),
             (36, 133), (70, 133), (48, 137), (62, 140), (40, 141),
             (56, 123), (74, 124)]:
    f2.set(x, y, TRIM)

print("frame1:", f1.stats_text())
print("frame2:", f2.stats_text())
print(f2.matrix_text(region=(28, 104, 84, 146)))

finish([f1, f2])
