# Red squid: original pose, inhale, exhale.
# Padding preserves every original pixel and provides room for the head bob.
W, H = 64, 63
OX, OY = 3, 3
f1 = new_canvas(W, H, name='01_original')
f1.blit(input_canvas, OX, OY)

# The head, face and mouth move together as one rigid shape. The eight-row
# belly below them stretches or compresses to meet the stationary feet.
# Inverse row sampling keeps every pose connected without transparent seams.
def breathing_pose(name, bob):
    result = new_canvas(W, H, name=name)
    source_joint = 38
    source_anchor = 47
    moved_joint = source_joint + bob
    for y in range(bob, 57):
        if y <= moved_joint:
            sy = y - bob
        elif y < source_anchor:
            sy = source_joint + (y - moved_joint) * (source_anchor - source_joint) / (source_anchor - moved_joint)
            sy = int(sy + 0.5)
        else:
            sy = y
        for x in range(58):
            result.set(x + OX, y + OY, input_canvas.get(x, sy))
    return result

f2 = breathing_pose('02_inhale', -1)
f3 = breathing_pose('03_exhale', 1)

# Preview only: this strip is not an output frame.
strip = new_canvas(W * 3, H, name='comparison')
for i, frame in enumerate([f1, f2, f3]):
    strip.blit(frame, i * W, 0)
view(strip, scale=5, margin=0)
view(f2, scale=8, margin=0)
finish([f1, f2, f3])
