from pixelbench_api import *

# Input: two mirrored parrots on a white 64x64 canvas.
#   left bird  x=3..29,  right bird x=34..60
# Palette: 1=white bg, 2=black outline, 3=blue plumage, 4=yellow (beak/eye),
#          5=darkred, 6=peach chest, 7=gray, 8=light-blue highlights
# Task: turn the RIGHT bird into a yellow parrot -> recolor its blue feathers
#       to yellow and its light-blue highlights to a pale yellow.

out = input_canvas.copy(name='output')

yellow = out.color('#ffcf1a')                 # existing yellow (index 4)
pale_yellow = out.color('#ffe97a', name='pale_yellow')

changed_blue = changed_hl = 0
for y in range(64):
    for x in range(32, 64):                   # right half only
        idx = out.get(x, y)
        if idx == 3:                          # blue -> yellow
            out.set(x, y, yellow)
            changed_blue += 1
        elif idx == 8:                        # light blue -> pale yellow
            out.set(x, y, pale_yellow)
            changed_hl += 1

print(f"recolored {changed_blue} blue pixels and {changed_hl} highlight pixels")
print(out.stats_text())

# verify: no blue/light-blue remains on the right half, left half untouched
left_before = {(x, y): input_canvas.get(x, y) for x in range(32) for y in range(64)}
left_after = {(x, y): out.get(x, y) for x in range(32) for y in range(64)}
print("left half unchanged:", left_before == left_after)
residual = [(x, y) for x in range(32, 64) for y in range(64) if out.get(x, y) in (3, 8)]
print("blue residual on right:", residual)

NM = {1:'.', 2:'K', 3:'B', 4:'Y', 5:'R', 6:'P', 7:'G', 8:'L', 9:'y'}
print("--- RIGHT BIRD after edit ---")
for y in range(15, 50):
    print(f"y={y:2d} " + ''.join(NM.get(out.get(x, y), '?') for x in range(32, 61)))

finish(out)
