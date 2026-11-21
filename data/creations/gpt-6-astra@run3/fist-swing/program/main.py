# Preserve the original artwork on a shared, slightly wider canvas.
f1 = new_canvas(36, 46, name='frame_1_original')
f1.blit(input_canvas, 1, 1)
pose = input_canvas.copy(name='punch_work')
# Remove the bent left forearm and fist; the head, torso and other arm stay intact.
pose.clear(13, 8, 9, 7)
# Work on the wider canvas in original sprite coordinates.
arm = new_canvas(34, 44, name='extended_pose')
arm.blit(pose, 0, 0)
# Shoulder, extended forearm, and compact clenched fist, using original colours.
rows = {
 9: [(27,'1111')],
10: [(12,'11111'), (26,'133331')],
11: [(12,'53333111111111'), (26,'5333311')],
12: [(12,'333333333333333335331')],
13: [(12,'533555555555555553551')],
14: [(13,'55666666666666666111')],
15: [(15,'1111111111111111')],
}
for y, runs in rows.items():
    for x, values in runs:
        for dx, value in enumerate(values):
            arm.set(x+dx, y, int(value))
# Round the shoulder into the chest, retaining the existing torso contour.
arm.set(12, 10, 5)
arm.set(13, 10, 3)
arm.set(14, 10, 3)
arm.set(15, 10, 5)
# Small contour and finger details keep the extended hand readable as a fist.
arm.line(13, 9, 15, 9, 1)
arm.set(30, 11, 5)
arm.set(28, 12, 6)
arm.set(28, 13, 3)
arm.set(29, 13, 5)
f2 = new_canvas(36, 46, name='frame_2_left_jab')
f2.blit(arm, 1, 1)
view(f1, scale=10)
view(f2, scale=10)
finish([f1, f2])
