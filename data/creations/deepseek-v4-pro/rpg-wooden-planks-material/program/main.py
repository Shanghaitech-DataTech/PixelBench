from pixelbench_api import new_canvas, finish

W = H = 16
c = new_canvas(W, H, name="planks")

palette = {
    '0': ('#241309', 'seam_dark'),
    '1': ('#5e3a1e', 'wood_dark'),
    '2': ('#8a5a2e', 'wood_med'),
    '3': ('#b07a3f', 'wood_light'),
    '4': ('#c99554', 'wood_hi'),
    '5': ('#4f2f16', 'grain_dark'),
    '6': ('#2b1a0e', 'knot_center'),
    '7': ('#7a4f28', 'knot_ring'),
    '8': ('#d3a060', 'end_light'),
    '9': ('#3d2612', 'end_dark'),
}
indices = {ch: c.color(hexv, name) for ch, (hexv, name) in palette.items()}

rows = [
    "0000000000000000",
    "0888099908880999",
    "0888099908880999",
    "0423025103420125",
    "0767025103420125",
    "0666076703420125",
    "0767066603420125",
    "0423076703420125",
    "0423025107670125",
    "0423025106660125",
    "0423025107670125",
    "0423025103420125",
    "0423025103420125",
    "0999088809990888",
    "0999088809990888",
    "0000000000000000",
]

for y, row in enumerate(rows):
    assert len(row) == W, (y, row)
    for x, ch in enumerate(row):
        c.set(x, y, indices[ch])

print(c.stats_text())
print(c.matrix_text())
finish(c)
