# Demon King's castle beneath a hanging blood moon
out = input_canvas.copy(name='output')
W, H = 256, 128

# ---- theme remap: cool daylight blues/whites -> demon-realm reds/purples ----
MAP = {
    # sky blues (dark -> light)
    '#172a41': '#120409', '#2b476a': '#20081a', '#3e6e98': '#340d24',
    '#5a98c6': '#4a1428', '#acc8e2': '#621c30',
    '#2e4b69': '#1e0a16', '#385c82': '#280d1c', '#44719f': '#381226',
    '#476e89': '#331120', '#547eab': '#44182a', '#548ec0': '#421628',
    '#6186ac': '#4c1c2c', '#63abdc': '#4c1a2a', '#557ca4': '#3e1624',
    '#609cc7': '#461828', '#222c4c': '#180a18', '#486289': '#341220',
    '#1b2344': '#140813', '#314867': '#240d19', '#213e5d': '#1a0a15',
    '#203d5b': '#190a14', '#0c3657': '#140710', '#2b7bad': '#481626',
    '#212e41': '#150a12', '#333f50': '#221318', '#182435': '#0f060c',
    '#1c2b36': '#130a10', '#131d28': '#0d060b',
    # black space / ember stars
    '#000000': '#050107',
    '#abf7ff': '#ff5a3c', '#fff87f': '#ffb347', '#ed53fc': '#ff2a2a',
    # old moon-ring teal -> subdued blood arc
    '#56e7d5': '#5e1220', '#42dbaa': '#54101c', '#30fdf5': '#6a1420',
    '#29fdf4': '#6a1420', '#29d7e7': '#5e1220',
    # clouds (white -> blood-lit crimson)
    '#ffffff': '#9c3a40', '#c2cde7': '#7c2c38', '#909fc4': '#622230',
    '#c8cad4': '#702a36', '#b5d0f7': '#802838', '#899cd7': '#622234',
    '#86a5dd': '#6e2838', '#93c8ec': '#702736', '#90c8df': '#702736',
    '#9ed9e4': '#702836', '#72b5c6': '#541e2c', '#7dc6d9': '#5c2230',
    '#80bbd2': '#622432', '#76a5c3': '#622034', '#747a97': '#4a1a28',
    '#639aa3': '#461e2e', '#598989': '#3f1e2a', '#6ba6b4': '#512432',
    # castle stone / path tans -> obsidian + blood-light
    '#edc6a9': '#a03428', '#b99281': '#8c3a30', '#856e66': '#6e2a28',
    '#525457': '#2e1a22', '#d5b8a9': '#8c2c30', '#d5b8aa': '#8c2c30',
    '#53627e': '#3a2434',
    '#fbd982': '#ff8c3a',
    # purples / misc
    '#313774': '#2a0d2e', '#48448f': '#3a1030', '#4f5a9f': '#3c1430',
    '#1b1a20': '#120609', '#2e2a23': '#1c0d10',
    # foliage olives -> dead dark maroon
    '#9e956a': '#3f1a20', '#4a574e': '#2a1216', '#818362': '#3a1a1e',
    '#33403d': '#200e12', '#696d53': '#33161a',
}

pal = out.palette()
white_idx = None
idx_new = {}
hex_of = {}
for entry in pal:
    r, g, b, a = entry['rgba']
    h = '#%02x%02x%02x' % (r, g, b)
    hex_of[entry['index']] = h
    if h == '#ffffff':
        white_idx = entry['index']
    if h in MAP:
        idx_new[entry['index']] = MAP[h]
    else:
        t = (0.3 * r + 0.6 * g + 0.1 * b) / 255.0
        idx_new[entry['index']] = '#%02x%02x%02x' % (
            int(13 + t * (176 - 13)), int(4 + t * (68 - 4)), int(9 + t * (72 - 9)))

orig = [[out.get(x, y) for x in range(W)] for y in range(H)]
for y in range(H):
    for x in range(W):
        out.set(x, y, idx_new[orig[y][x]])

# ---- blood moon: find old moon bbox (white disc, top centre) ----
xs, ys = [], []
for y in range(0, 46):
    for x in range(100, 161):
        if orig[y][x] == white_idx:
            xs.append(x); ys.append(y)
cx = (min(xs) + max(xs)) // 2
cy = (min(ys) + max(ys)) // 2
r = max(max(xs) - min(xs), max(ys) - min(ys)) // 2 + 1
print('moon centre', cx, cy, 'r', r)

# hanging glow halo
out.circle(cx, cy, r + 8, '#20060e')
out.circle(cx, cy, r + 6, '#320a16')
out.circle(cx, cy, r + 4, '#480e1c')
out.circle(cx, cy, r + 2, '#5e1220')
# the blood moon disc
out.circle(cx, cy, r + 1, '#7a1220')
out.circle(cx, cy, r - 1, '#a01824')
out.circle(cx, cy, r - 4, '#c22430')
out.circle(cx, cy, r - 8, '#d8383c')
out.circle(cx, cy, r + 1, '#54090f', fill=False)
# craters
out.circle(cx - 4, cy - 2, 2, '#901a22')
out.circle(cx + 4, cy + 4, 1, '#901a22')
out.circle(cx + 2, cy - 5, 1, '#961c24')
out.circle(cx - 1, cy + 6, 1, '#901a22')

# ---- fiery windows on the castle ----
CASTLE = {'#b99281', '#edc6a9', '#856e66', '#525457', '#333f50',
          '#212e41', '#53627e', '#182435', '#d5b8aa'}
win = [(126, 44), (130, 48), (122, 52), (134, 54), (118, 58), (140, 60),
       (126, 62), (132, 66), (114, 66), (146, 66), (120, 72), (138, 74),
       (128, 76), (150, 72), (110, 74), (133, 42), (124, 70), (143, 68),
       (129, 32), (129, 38), (129, 26)]
placed = 0
for (x, y) in win:
    if hex_of[orig[y][x]] in CASTLE:
        out.set(x, y, '#ffb347')
        out.set(x, y + 1, '#ff6a30')
        placed += 1
print('windows placed', placed)

# ---- bats circling the moon ----
SKY = {'#172a41', '#2b476a', '#3e6e98', '#5a98c6', '#acc8e2', '#000000'}
bats = [(70, 26), (180, 20), (95, 14), (210, 34), (55, 40), (230, 48)]
for (bx, by) in bats:
    if hex_of[orig[by][bx]] in SKY:
        for (dx, dy) in [(-1, -1), (1, -1), (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)]:
            out.set(bx + dx, by + dy, '#08020a')

view(out)
save('demon_castle', out)
finish(out)
