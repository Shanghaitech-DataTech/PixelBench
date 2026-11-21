out = input_canvas.copy(name="output")
W, H = out.stats()['size']
remap = {
    out.color('c2'): out.color('#f2ae00', name='bird_body_yellow'),
    out.color('c7'): out.color('#fff2b0', name='bird_light_yellow'),
    out.color('c5'): out.color('#ffe07f', name='bird_pale_yellow'),
}
for y in range(H):
    for x in range(32, W):
        cur = out.get(x, y)
        if cur in remap:
            out.set(x, y, remap[cur])

print(out.matrix_text(region=(30, 13, 63, 50)))
print(out.stats_text())
print(out.palette())
finish(out)
