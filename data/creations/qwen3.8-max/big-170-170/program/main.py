from pixelbench_api import *
import random

rnd = random.Random(7)

out = input_canvas.copy(name="output")

# ---------- reconstructed vending machine front + lower body ----------
def draw_panel(c):
    # upper lit display: frames + white panel + shelf rows
    c.rect(84, 59, 2, 53, 220)          # left frame x84-85
    c.rect(115, 59, 1, 53, 192)         # right frame
    c.rect(86, 59, 29, 53, 255)         # lit panel x86..114, y59..111
    rows = [(60, [217, 246, 215, 253]),
            (70, [214, 230, 213, 156]),
            (80, [191, 186, 182, 191]),
            (90, [123, 177, 254, 124]),
            (100, [214, 156, 160, 213])]
    for y0, cols in rows:
        x = 87
        i = 0
        while x + 4 <= 114:
            c.rect(x, y0 + 1, 4, 7, cols[i % len(cols)])
            x += 5
            i += 1
        c.rect(86, y0 + 9, 29, 1, 182)  # shelf edge
    # lower machine body
    c.rect(84, 112, 32, 37, 34)         # y112..148
    for yy in (122, 130, 138):
        c.rect(90, yy, 22, 1, 42)
    c.rect(106, 113, 10, 5, 182)        # keypad / coin panel
    c.rect(108, 114, 6, 3, 47)

draw_panel(out)

# ---------- erase person leftovers left of the machine (arm, skirt hem) ----------
CORE = {98, 99, 100, 101, 27, 26, 24, 28, 29, 30, 31, 32, 33, 51, 52,
        109, 103, 106, 107, 110,
        164, 165, 166, 167, 168, 169, 170, 147, 150, 152, 153, 128, 129,
        137, 122, 116, 143, 144, 145, 119, 121, 108, 105, 141, 111,
        249, 250, 251, 239, 238, 232, 231, 234, 235, 236, 237, 222, 223,
        224, 178, 172,
        214, 213, 212, 230, 202, 204, 207, 156, 160, 154, 159, 161, 162,
        123, 124, 125, 126, 177, 175, 176, 173, 174, 117, 102, 88, 87, 86,
        85, 81, 93, 94, 64, 68, 200, 196, 246, 217, 215}
UPPER_SET = CORE | {181, 182, 183, 184, 185, 186, 188, 189, 190, 191, 192,
                    193, 195, 253, 254, 255, 256, 248, 220, 221, 219, 216, 187}
LOWER_SET = {98, 99, 100, 101, 27,
             164, 165, 166, 167, 168, 169, 170, 147, 150, 152, 153, 128, 129,
             137, 122, 116, 143, 144, 145, 119, 121, 108, 105, 141, 111,
             249, 250, 251, 239, 238, 232, 231, 234, 235, 236, 237, 222, 223,
             224, 178, 172,
             214, 213, 212, 230, 202, 204, 207, 156, 160, 154, 159, 161, 162,
             123, 124, 125, 126, 177, 175, 176, 173, 174, 117, 102, 88, 87,
             86, 85, 81, 93, 94,
             253, 254, 255, 256}

for y in range(59, 147):
    s = UPPER_SET if y <= 109 else LOWER_SET
    for x in range(74, 84):
        if out.get(x, y) in s:
            out.set(x, y, out.get(x - 14, y))   # borrow nearby sky/scenery

# ---------- storm ambient tint (blended) ----------
tint = new_canvas(170, 170, name="tint")
tint.rect(0, 0, 170, 170, (8, 12, 26, 64))
storm = flatten([out, tint], name="storm")
draw_panel(storm)   # machine stays a bright light source in the storm

# ---------- effect layers (semi-transparent, blended at the end) ----------
wet = new_canvas(170, 170, name="wet")
glow = new_canvas(170, 170, name="glow")
rain = new_canvas(170, 170, name="rain")

# wet ground: darken + puddles + reflections
wet.rect(0, 148, 170, 22, (5, 8, 18, 80))
wet.ellipse(40, 160, 18, 3, (70, 100, 135, 110))
wet.ellipse(100, 164, 24, 3, (70, 100, 135, 100))
wet.ellipse(150, 157, 12, 2, (70, 100, 135, 90))
for x in range(88, 115, 3):                     # vending-machine reflection
    wet.line(x, 150, x, 167, (255, 240, 210, 22))
for x in range(10, 28, 3):                      # lightning reflection
    wet.line(x, 150, x, 165, (190, 210, 255, 26))

# lightning bolt in the background sky (left of the pole)
bolt = [(22, 2), (16, 18), (24, 20), (12, 40), (20, 42), (10, 56)]
glow.circle(17, 28, 42, (150, 175, 255, 10))    # flash-lit sky, soft round glow
glow.circle(17, 28, 26, (170, 190, 255, 14))
for (px, py) in bolt:
    glow.circle(px, py, 7, (170, 190, 255, 26))
    glow.circle(px, py, 3, (220, 230, 255, 45))
for i in range(len(bolt) - 1):
    x0, y0 = bolt[i]
    x1, y1 = bolt[i + 1]
    glow.line(x0, y0, x1, y1, (255, 255, 235, 255))
    glow.line(x0 + 1, y0, x1 + 1, y1, (255, 250, 200, 255))
glow.line(16, 18, 8, 26, (230, 240, 255, 255))
glow.line(12, 40, 20, 50, (230, 240, 255, 255))
# halo around the glowing machine
for (k, a) in ((4, 16), (8, 9)):
    glow.rect(84 - k, 59 - k, 32 + 2 * k, 1, (255, 240, 200, a))
    glow.rect(84 - k, 115 + k, 32 + 2 * k, 1, (255, 240, 200, a))
    glow.rect(84 - k, 59 - k, 1, 57 + 2 * k, (255, 240, 200, a))
    glow.rect(115 + k, 59 - k, 1, 57 + 2 * k, (255, 240, 200, a))

# rain: semi-transparent streaks
for _ in range(150):
    x = rnd.randint(-5, 175)
    y = rnd.randint(-10, 158)
    L = rnd.randint(6, 12)
    rain.line(x, y, x - 2, y + L, (170, 205, 235, 70))
for _ in range(45):
    x = rnd.randint(0, 172)
    y = rnd.randint(-5, 160)
    L = rnd.randint(4, 8)
    rain.line(x, y, x - 1, y + L, (210, 235, 255, 110))
# splash ticks on the wet ground
for _ in range(60):
    x = rnd.randint(0, 168)
    y = rnd.randint(150, 168)
    rain.set(x, y, (200, 225, 255, 110))
    if rnd.random() < 0.35:
        rain.set(x + 1, y, (200, 225, 255, 90))
# clinging water droplets on machine, bike and pole
def droplets(x0, x1, y0, y1, n):
    for _ in range(n):
        x = rnd.randint(x0, x1)
        y = rnd.randint(y0, y1)
        rain.set(x, y, (215, 240, 255, 150))
        if rnd.random() < 0.5:
            rain.set(x, y - 1, (255, 255, 255, 190))
droplets(86, 115, 60, 148, 26)
droplets(50, 120, 115, 158, 24)
droplets(39, 43, 10, 150, 10)
droplets(0, 169, 148, 169, 20)
# clinging droplet trails running down surfaces
for _ in range(16):
    x = rnd.choice([rnd.randint(86, 115), rnd.randint(50, 118), 41])
    y = rnd.randint(62, 140)
    L = rnd.randint(3, 7)
    rain.line(x, y, x, y + L, (190, 220, 250, 90))
    rain.set(x, y + L + 1, (235, 250, 255, 170))

final = flatten([storm, wet, glow, rain], name="thunderstorm")

view(final)
save("thunderstorm", final)
finish(final)
