# Turn the water into bubbling purple magic potion
out = input_canvas.copy(name='output')

# Map of original liquid colors to purple potion colors
# e = #2f7598 (dark teal, upper liquid) -> deep purple
# f = #74b8c9 (light blue, lower liquid) -> lighter purple
# g = #77b7ce, h = #76b7d1, j = #7bb5cb (highlights) -> purple highlights
# i = #31121d (dark band) -> dark purple band

DEEP_PURPLE   = '#5b1f7a'  # replaces dark teal
LIGHT_PURPLE  = '#a355d1'  # replaces light blue
HL_PURPLE_1   = '#c98ae0'  # highlight
HL_PURPLE_2   = '#c98ae0'
HL_PURPLE_3   = '#c98ae0'
DARK_BAND     = '#3a0d4d'  # dark purple band

mapping = {
    '#2f7598': DEEP_PURPLE,
    '#74b8cf': LIGHT_PURPLE,
    '#77b7ce': HL_PURPLE_1,
    '#76b7d1': HL_PURPLE_2,
    '#7bb5cb': HL_PURPLE_3,
    '#31121d': DARK_BAND,
}

# Build reverse map from palette
pal = out.palette()
idx_to_hex = {}
for entry in pal:
    rgba = entry['rgba']
    hexc = '#%02x%02x%02x' % (rgba[0], rgba[1], rgba[2])
    idx_to_hex[entry['index']] = hexc

print("palette:", idx_to_hex)

for y in range(64):
    for x in range(64):
        idx = out.get(x, y)
        hexc = idx_to_hex.get(idx)
        if hexc in mapping:
            out.set(x, y, mapping[hexc])

# Add bubbles inside the potion (circles of highlight purple)
BUBBLE_HI = '#e3b8f5'
BUBBLE_MID = '#c77fe0'

def bubble(cx, cy, r):
    out.circle(cx, cy, r, BUBBLE_MID, fill=True)
    # small highlight
    if r >= 2:
        out.set(cx-1, cy-1, BUBBLE_HI)
        out.set(cx, cy-1, BUBBLE_HI)

# Bubbles in the lower (light) region — kept away from the outline
bubble(22, 48, 2)
bubble(29, 52, 2)
bubble(38, 49, 2)
bubble(24, 43, 1)
bubble(34, 45, 1)
bubble(19, 53, 1)
bubble(31, 55, 1)

# Bubbles in the upper (deep) region
bubble(24, 34, 1)
bubble(31, 31, 2)
bubble(40, 33, 1)
bubble(36, 29, 1)
bubble(27, 29, 1)

view(out)
print(out.matrix_text(region=(36, 40, 52, 58)))
finish(out)
