import random
from pixelbench_api import new_canvas, finish

c = new_canvas(16, 16, background=None, name="dirt")

# base browns
dark   = c.color("#5a3d23", "dark")
mid    = c.color("#795533", "mid")
light  = c.color("#8f6a42", "light")
pebble = c.color("#9c7a52", "pebble")
shadow = c.color("#4a3120", "shadow")
speck  = c.color("#6b4a2c", "speck")

rnd = random.Random(7)
# fill base with mid, sprinkle variation
for y in range(16):
    for x in range(16):
        r = rnd.random()
        if r < 0.18:
            c.set(x, y, dark)
        elif r < 0.40:
            c.set(x, y, speck)
        elif r < 0.72:
            c.set(x, y, mid)
        elif r < 0.92:
            c.set(x, y, light)
        else:
            c.set(x, y, pebble)

# wrap-friendly clumps: small 2x2 blobs of dark and light
for _ in range(6):
    x, y = rnd.randrange(16), rnd.randrange(16)
    for dx in range(2):
        for dy in range(2):
            c.set((x + dx) % 16, (y + dy) % 16, dark if rnd.random() < 0.6 else shadow)
for _ in range(5):
    x, y = rnd.randrange(16), rnd.randrange(16)
    for dx in range(2):
        for dy in range(2):
            c.set((x + dx) % 16, (y + dy) % 16, light if rnd.random() < 0.6 else pebble)

# scattered single-pixel pebbles
for _ in range(8):
    x, y = rnd.randrange(16), rnd.randrange(16)
    c.set(x, y, pebble)
for _ in range(6):
    x, y = rnd.randrange(16), rnd.randrange(16)
    c.set(x, y, shadow)

print(c.stats_text())
finish(c)
