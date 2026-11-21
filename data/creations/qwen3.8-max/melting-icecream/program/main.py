output = input_canvas.copy(name='output')

CH = '#5e363e'   # chocolate body (same as scoop)
HL = '#95524c'   # chocolate mid-tone highlight
GL = '#c46f5b'   # wet gloss

# --- melt skirt: wavy chocolate oozing over the cone rim (y=33 down to depth per column)
skirt = {20:35, 21:36, 22:37, 23:38, 24:37, 25:36, 26:35, 27:36, 28:37,
         29:38, 30:39, 31:39, 32:38, 33:37, 34:36, 35:36, 36:37, 37:38,
         38:38, 39:37, 40:36, 41:35, 42:34}
for x, d in skirt.items():
    output.rect(x, 33, 1, d - 33 + 1, CH)

# --- teardrop drips running down the cone
def drip(x, w, ytip):
    ytop = 33
    output.rect(x, ytop, w, (ytip - 2) - ytop + 1, CH)   # stream
    output.rect(x - 1, ytip - 1, w + 2, 2, CH)           # droplet bulge
    output.rect(x, ytip + 1, w, 1, CH)                   # taper
    if w > 2:
        output.rect(x + 1, ytip + 2, w - 2, 1, CH)       # rounded end
    else:
        output.set(x, ytip + 2, CH)

drip(25, 2, 46)   # left drip
drip(30, 2, 54)   # long centre drip
drip(36, 2, 42)   # right drip

# --- detached droplets further down (melt running ahead of the drips)
output.rect(27, 50, 1, 2, CH)
output.rect(33, 48, 1, 2, CH)
output.rect(30, 58, 1, 2, CH)
output.set(39, 40, CH)

# --- highlight lines (light from the right, as on the scoop)
output.line(26, 36, 26, 44, HL)
output.line(31, 36, 31, 52, HL)
output.line(37, 36, 37, 40, HL)

# --- wet gloss pixels on the droplet bulges
output.set(26, 45, GL)
output.set(32, 53, GL)
output.set(37, 41, GL)

view(output, scale=8)
finish(output)
