# Preserve the original sprite exactly, with room for its breathing motion.
f1 = new_canvas(62, 61, name='idle_1_original')
f1.blit(input_canvas, 2, 2)

def breathing_frame(name, bob):
    c = new_canvas(62, 61, name=name)
    # The upper body translates intact. The short lower-body transition
    # stretches/compresses by one row while the tentacle tips stay anchored.
    for y in range(bob, 57):
        if y <= 32 + bob:
            sy = y - bob
        elif y < 47:
            sy = round(32 + (y - 32 - bob) * 15 / (15 - bob))
        else:
            sy = y
        for x in range(58):
            c.set(x + 2, y + 2, input_canvas.get(x, sy))
    return c

f2 = breathing_frame('idle_2_rise', -1)
f3 = breathing_frame('idle_3_settle', 1)
view(f1, scale=6)
view(f2, scale=6)
view(f3, scale=6)
finish([f1, f2, f3])
