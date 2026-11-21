from pixelbench_api import *

c = input_canvas
pal = c.palette()
m = {p['index']: p for p in pal}

out = c.copy(name="output")

# Remove the sun in the sky by covering it with the adjacent sky gradient.
# Sun occupies roughly x 100..145, y 14..58. Use the sky colour from the
# same row further left (a clear-sky column) so the removal is seamless.
for y in range(12, 61):
    for x in range(98, 148):
        src = m[out.get(x - 55, y)]
        R, G, B, A = src['rgba']
        if A > 0:
            out.set(x, y, src['index'])

result = flatten([out], background=None)
finish(result)
