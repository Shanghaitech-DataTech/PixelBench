from pixelbench_api import *

c = input_canvas.copy(name='output')

# Reuse existing colours
deep = c.color('#1d8baa')    # deep blue water
cyan = c.color('#2ec7dc')    # light cyan water
white = c.color('#ffffff')  # white sparkle

# Dry basin/dish floor colours -> deep water in both pools (rows 34-49)
dry = {c.color('#b9ab90'), c.color('#e1e2ba'), c.color('#a58d8b'), c.color('#ffffff')}
for y in range(34, 50):
    for x in range(64):
        if c.get(x, y) in dry:
            c.set(x, y, deep)

# Upper dish water: cyan surface ripples
c.line(20, 35, 43, 35, cyan)
c.line(17, 37, 46, 37, cyan)
c.line(15, 39, 48, 39, cyan)
# Upper dish sparkles
for (x, y) in [(22, 34), (28, 36), (34, 36), (40, 34), (24, 38), (39, 38), (32, 39), (26, 40)]:
    c.set(x, y, white)

# Lower basin water: cyan surface ripples
c.line(16, 42, 47, 42, cyan)
c.line(14, 44, 49, 44, cyan)
c.line(13, 46, 50, 46, cyan)
c.line(14, 48, 49, 48, cyan)
# Lower basin sparkles
for (x, y) in [(19, 43), (26, 43), (37, 43), (44, 43), (17, 45), (24, 45),
               (31, 45), (38, 45), (46, 45), (15, 47), (29, 47), (35, 47), (42, 47)]:
    c.set(x, y, white)

# Falling water streams: overflowing from the upper tier down into the lower basin
for x in range(15, 50, 2):
    c.line(x, 37, x, 43, cyan)
for x in range(16, 50, 4):
    c.line(x, 38, x, 42, white)

# Splash droplets on the lower basin water
for (x, y) in [(20, 43), (26, 43), (32, 43), (38, 43), (44, 43), (17, 44),
               (23, 44), (29, 44), (35, 44), (41, 44), (47, 44)]:
    c.set(x, y, white)

finish(c)
