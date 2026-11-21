# All three frames share a small transparent margin for the breathing motion.
f1 = new_canvas(60, 61, name='idle_1_original')
f1.blit(input_canvas, 1, 2)

def breathing_frame(name, offset):
    c = new_canvas(60, 61, name=name)
    # Translate the head rigidly, ease the motion through the lower mantle,
    # and leave the bottom tentacles anchored. Row copies preserve the palette.
    for y in range(-1, 57):
        weight = min(1.0, max(0.0, (46-y)/12.0))
        source_y = round(y - offset * weight)
        if 0 <= source_y < 57:
            input_canvas.select(0, source_y, 58, 1).copy_to(1, y+2, c)
    return c

f2 = breathing_frame('idle_2_rise', -1)
f3 = breathing_frame('idle_3_settle', 1)
view(f1, scale=6)
view(f2, scale=6)
view(f3, scale=6)
finish([f1, f2, f3])
