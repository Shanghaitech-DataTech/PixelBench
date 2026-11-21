# Preserve the source exactly for the first, raised pose.
f1 = input_canvas.copy(name='frame_1_high')

def wave_frame(name, shifts):
    result = new_canvas(48, 56, name=name)
    # The pole, ties and hoist are fixed. Warp only the free cloth,
    # in four-pixel steps to retain the source's effective pixel grid.
    for y in range(56):
        for x in range(48):
            index = input_canvas.get(x, y)
            dy = 0 if x < 20 else shifts[(x - 20) // 4]
            if y + dy < 56:
                result.set(x, y + dy, index)
    return result

f2 = wave_frame('frame_2_middle', [0, 0, 4, 8, 12, 12, 12])
f3 = wave_frame('frame_3_low', [0, 0, 8, 16, 24, 24, 24])
view(f1, scale=6)
view(f2, scale=6)
view(f3, scale=6)
finish([f1, f2, f3])
