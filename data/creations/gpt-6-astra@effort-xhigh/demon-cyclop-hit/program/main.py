# The original remains pixel-for-pixel intact in the first frame.
f1 = new_canvas(48, 44, name='01_original')
f1.blit(input_canvas, 4, 8)

ink = '#141b1b'
horn = '#ffe18d'
skin = '#adbc3a'
shade = '#74a334'
lid = '#c8966b'
white = '#fce2ca'

# Change the expression in the original sprite's local coordinates.
pose = input_canvas.copy(name='recoil_work')
# The pupil rolls under the upper lid, leaving the lower eye exposed.
pose.rect(17, 16, 3, 3, white)
pose.rect(17, 15, 3, 3, ink)
pose.set(17, 15, lid)
pose.set(19, 15, lid)
# A wide open mouth replaces the quiet closed mouth.
pose.rect(14, 22, 9, 4, skin)
pose.line(15, 22, 21, 22, shade)
pose.line(14, 23, 14, 25, shade)
pose.line(22, 23, 22, 25, shade)
pose.line(15, 26, 21, 26, shade)
pose.rect(15, 23, 7, 3, ink)
pose.rect(16, 22, 5, 1, ink)
pose.rect(16, 26, 5, 1, ink)
pose.rect(16, 23, 2, 1, white)
pose.rect(20, 23, 1, 1, white)
pose.rect(17, 25, 4, 1, '#a84642')
pose.rect(18, 25, 2, 1, '#e57a65')

# A clockwise recoil rocks the body over its right-hand support foot.
turn = pose.select(0, 0, 37, 33).rotate(14, algorithm='rotsprite')
f2 = new_canvas(48, 44, name='02_recoil')
turn.copy_to(4, 2, f2, mode='over')

# Refine the two feet after rotation so their poses remain easy to read.
# The raised left leg bends forward and its paired claws stay off the floor.
f2.clear(9, 33, 10, 5)
f2.poly([(13, 32), (18, 33), (18, 34), (16, 35), (11, 35), (10, 34), (10, 32), (11, 31)], ink)
f2.poly([(12, 31), (15, 32), (17, 33), (16, 34), (11, 34), (11, 32)], shade)
f2.set(11, 34, horn)
f2.set(13, 34, horn)
# The supporting foot finishes on the original frame's ground line, y=40.
f2.clear(27, 36, 9, 6)
f2.poly([(28, 35), (31, 35), (32, 36), (32, 37), (33, 38), (34, 39), (34, 41), (29, 41), (28, 39), (28, 37), (27, 36)], ink)
f2.poly([(29, 35), (30, 35), (31, 37), (31, 38), (33, 39), (33, 41), (30, 41), (29, 39), (29, 37), (28, 36)], shade)
f2.set(30, 40, horn)
f2.set(33, 40, horn)

# All opaque pixels, including horns, eye, limbs and outlines, get the flash.
f3 = new_canvas(48, 44, name='03_impact')
flash = {
    ink: '#4b1724', horn: '#ff9970', skin: '#e6414b', shade: '#b52742',
    lid: '#de5956', white: '#ffc0a0', '#a84642': '#8b1d36', '#e57a65': '#ff7972'
}
for y in range(44):
    for x in range(48):
        idx = f2.get(x, y)
        rgba = f2.palette()[idx]['rgba']
        if rgba[3]:
            key = '#%02x%02x%02x' % tuple(rgba[:3])
            f3.set(x, y, flash[key])

# Check the unmodified first frame and matching dimensions before export.
for sy in range(33):
    for sx in range(37):
        assert f1.get(sx + 4, sy + 8) == input_canvas.get(sx, sy)
assert f1.stats()['size'] == f2.stats()['size'] == f3.stats()['size']
save('demon-cyclop-hit-01', f1)
save('demon-cyclop-hit-02', f2)
save('demon-cyclop-hit-03', f3)
view(f1, scale=8, margin=0)
view(f2, scale=8, margin=0)
view(f3, scale=8, margin=0)
finish([f1, f2, f3])
