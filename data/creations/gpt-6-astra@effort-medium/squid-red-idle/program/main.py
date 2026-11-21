# Transparent padding preserves all of the original art and allows a gentle bob.
f1 = new_canvas(62, 61, name='idle_1_original')
f1.blit(input_canvas, 2, 2)
def breathe(name, delta):
    c = new_canvas(62, 61, name=name)
    # Translate the upper body; gradually absorb the motion through the skirt.
    # The bottom tentacle tips retain their original positions.
    for dest_y in range(-1, 57):
        if dest_y <= 30 + delta:
            source_y = dest_y - delta
        elif dest_y < 48:
            source_y = (dest_y - delta * 48 / 18) / (1 - delta / 18)
        else:
            source_y = dest_y
        source_y = int(source_y + 0.5) if source_y >= 0 else -1
        if 0 <= source_y < 57:
            for x in range(58):
                c.set(x + 2, dest_y + 2, input_canvas.get(x, source_y))
    return c
f2 = breathe('idle_2_rise', -1)
f3 = breathe('idle_3_settle', 1)
view(f1)
view(f2)
view(f3)
finish([f1, f2, f3])
