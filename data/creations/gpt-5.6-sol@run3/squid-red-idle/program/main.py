from pixelbench_api import *

PAD_X = 3
PAD_Y = 3
W, H = 64, 63


def is_foot(x, y):
    return y >= 45 and (x < 20 or x > 37)


def is_moving_body(x, y):
    # Three overlapping ankle rows hide the joint during the one-pixel bob.
    return not (y >= 48 and (x < 20 or x > 37))


def animated_frame(name, body_dy):
    out = new_canvas(W, H, background=None, name=name)

    # Planted feet form the lower layer.
    for y in range(57):
        for x in range(58):
            colour = input_canvas.get(x, y)
            if colour != 0 and is_foot(x, y):
                out.set(PAD_X + x, PAD_Y + y, colour)

    # The mantle, face, arms, and upper legs breathe as one soft mass.
    for y in range(57):
        for x in range(58):
            colour = input_canvas.get(x, y)
            if colour != 0 and is_moving_body(x, y):
                out.set(PAD_X + x, PAD_Y + y + body_dy, colour)
    return out


frame1 = new_canvas(W, H, background=None, name="frame_1_original")
frame1.blit(input_canvas, PAD_X, PAD_Y)
frame2 = animated_frame("frame_2_breathe_up", -1)
frame3 = animated_frame("frame_3_breathe_down", 1)

# Preview the animation frames individually at crisp integer scale.
view(frame1, scale=7, margin=1, edges="all")
view(frame2, scale=7, margin=1, edges="all")
view(frame3, scale=7, margin=1, edges="all")
finish([frame1, frame2, frame3])
