# squid-red-idle: preserve the original artwork and animate a subtle two-pose breath.
# A 64x64 stage gives the one-pixel bob room while keeping every frame aligned.
STAGE_W = 64
STAGE_H = 64
OX = 3
OY = 4
SPLIT_Y = 42
OVERLAP_Y = 45

# Capture independently editable sprite parts from the supplied image.
upper = input_canvas.select(0, 0, 58, OVERLAP_Y).preview()
lower = input_canvas.select(0, SPLIT_Y, 58, 57 - SPLIT_Y).preview()


def make_frame(name, upper_dy):
    frame = new_canvas(STAGE_W, STAGE_H, name=name)
    # Feet and lower tentacles stay planted. The overlapping waist hides the joint.
    frame.blit(lower, OX, OY + SPLIT_Y)
    frame.blit(upper, OX, OY + upper_dy)
    return frame


# Neutral original, inhale (body rises), exhale (body settles).
f1 = new_canvas(STAGE_W, STAGE_H, name="frame_1_original")
f1.blit(input_canvas, OX, OY)
f2 = make_frame("frame_2_inhale", -1)
f3 = make_frame("frame_3_exhale", 1)

print(f1.stats_text())
print(f2.stats_text())
print(f3.stats_text())
view(f1, scale=8, margin=0)
view(f2, scale=8, margin=0)
view(f3, scale=8, margin=0)
finish([f1, f2, f3])
