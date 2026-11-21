# Two-frame left-fist punch animation.
# Frame 1 preserves every original pixel, with transparent room for the swing.
f1 = new_canvas(40, 44, name="frame_1_original")
f1.blit(input_canvas, 0, 0)

# Frame 2 begins from the exact same expanded pose.
f2 = f1.copy(name="frame_2_left_punch")

OUTLINE = 1   # #222034
SKIN = 3      # #eec39a
ORANGE = 5    # #df7126
SHADOW = 6    # #8f563b

# Remove the original bent image-right arm without disturbing the torso/shoulder.
f2.clear(16, 9, 7, 6)

# Straight left arm: dark lower edge, warm shadow, and skin highlight.
# Shoulder/sleeve connection.
f2.set(16, 9, OUTLINE)
f2.set(17, 9, OUTLINE)
f2.set(16, 10, ORANGE)
f2.set(17, 10, ORANGE)
f2.set(16, 11, SHADOW)
f2.set(17, 11, ORANGE)
f2.set(16, 12, OUTLINE)
f2.set(17, 12, OUTLINE)

# Extended arm, angled one pixel upward for a light jab.
f2.rect(18, 9, 12, 1, OUTLINE)
f2.rect(18, 10, 12, 2, SKIN)
f2.rect(18, 12, 12, 1, SHADOW)
f2.rect(18, 13, 12, 1, OUTLINE)
# Small elbow/underside steps keep the limb organic at pixel scale.
f2.set(18, 12, ORANGE)
f2.set(19, 12, ORANGE)
f2.set(20, 12, SHADOW)
f2.set(29, 12, SKIN)

# Closed fist with knuckle steps and a tucked thumb.
f2.rect(30, 8, 6, 1, OUTLINE)
f2.rect(29, 9, 8, 1, OUTLINE)
f2.rect(30, 10, 7, 3, SKIN)
f2.set(29, 10, SKIN)
f2.set(29, 11, SKIN)
f2.set(36, 10, OUTLINE)
f2.set(36, 11, OUTLINE)
f2.set(36, 12, OUTLINE)
f2.rect(30, 13, 6, 1, OUTLINE)
f2.set(31, 10, 6)
f2.set(35, 12, SHADOW)
# Knuckle separations and thumb definition.
f2.set(32, 9, SHADOW)
f2.set(34, 9, SHADOW)
f2.set(30, 12, SHADOW)
f2.set(31, 12, SHADOW)
f2.set(32, 13, OUTLINE)

# Two restrained speed marks behind the moving forearm.
f2.line(20, 7, 24, 7, ORANGE)
f2.line(22, 15, 26, 15, SHADOW)

view(f2, scale=10, margin=2, edges="all")
finish([f1, f2])
