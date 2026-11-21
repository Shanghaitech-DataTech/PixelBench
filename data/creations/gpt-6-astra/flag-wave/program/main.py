# Keep the original image, including every pixel, as the first keyframe.
f1 = input_canvas.copy(name='frame_1_high')

def waved(name, offsets):
    c = input_canvas.copy(name=name)
    # The staff, ties, and the fixed hoist occupy the first five grid columns.
    # Translate four-pixel-wide cloth strips to preserve the native pixel grid.
    c.clear(20, 0, 28, 56)
    for col, dy in zip(range(5, 12), offsets):
        for y in range(56):
            for x in range(col * 4, col * 4 + 4):
                idx = input_canvas.get(x, y)
                if input_canvas.palette()[idx]['rgba'][3] and 0 <= y + dy < 56:
                    c.set(x, y + dy, idx)
    return c

f2 = waved('frame_2_level', [0, 0, 4, 8, 12, 12, 12])
f3 = waved('frame_3_low', [0, 4, 12, 16, 24, 24, 24])
view(f1)
view(f2)
view(f3)
finish([f1, f2, f3])
