from pixelbench_api import *

c = input_canvas
out = c.copy(name="output")

FLESH = {4, 7, 8, 9}   # c3,e08c37 / c6,ffc830 / c7,ffda45 / c8,ef9d0e -> flesh of the bottom segment
CREAM = 6              # c5, fbf4c9 -> the rind underneath

# Remove the bottom segment of durian flesh (the lower lobe of the fruit),
# exposing the cream rind underneath. Keep the other two pieces unchanged.
for y in range(33, 64):
    for x in range(64):
        if out.get(x, y) in FLESH:
            out.set(x, y, CREAM)

print(out.stats_text())
chars = {0:'.',1:' ',2:'#',3:'b',4:'c',5:'d',6:'E',7:'f',8:'g',9:'h'}
for y in range(28, 64):
    row = ''.join(chars[out.get(x,y)] for x in range(64))
    print(f"{y:2d} {row}")

finish([out])
