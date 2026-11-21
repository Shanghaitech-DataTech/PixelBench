# Preserve the original sprite, with room above and below for breathing.
f1 = new_canvas(62, 61, name='idle_1_original')
f1.blit(input_canvas, 2, 2)

# Move the upper body as a unit, easing back into the fixed lower
# tentacles through the broad underside of the mantle.
def breathing_frame(name, offset):
    frame = new_canvas(62, 61, name=name)
    for y in range(-1, 57):
        if offset == -1:
            sy = y + 1 if y <= 37 else y
        else:
            sy = y - 1 if y <= 38 else y
        if 0 <= sy < 57:
            for x in range(58):
                frame.set(x + 2, y + 2, input_canvas.get(x, sy))
    return frame

f2 = breathing_frame('idle_2_inhale', -1)
f3 = breathing_frame('idle_3_exhale', 1)
view(f1, scale=6)
view(f2, scale=6)
view(f3, scale=6)
finish([f1, f2, f3])
