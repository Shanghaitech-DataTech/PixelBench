from pixelbench_api import new_canvas, finish

W, H = 32, 32

# Character legend -> colour
cols = {
    '.': None,          # transparent
    'B': '#E8DFC4',    # bone
    'b': '#C2B494',    # bone shadow
    'K': '#2A241E',    # dark joints / spine
    'E': '#14100C',    # eye sockets
    'W': '#8A5A2E',    # shield wood
    'w': '#5C3A1C',    # shield wood dark
    'M': '#96A2AE',    # shield boss metal
    'm': '#5E6A76',    # metal dark / guard
    'S': '#C9D2DA',    # sword blade light
    's': '#7C8692',    # sword blade shade
    'G': '#6E4A28',    # sword grip
}

rows = [
    '.' * 32,
    '.' * 32,
    '.' * 14 + 'BBBBB' + '.' * 13,          # top of skull
    '.' * 13 + 'BBBBBBB' + '.' * 12,        # skull
    '.' * 13 + 'BEEBEEB' + '.' * 12,        # eye sockets
    '.' * 13 + 'BEEBEEB' + '.' * 12,
    '.' * 13 + 'BBBBBBB' + '.' * 12,
    '.' * 13 + 'BKBKBKB' + '.' * 12,        # teeth
    '.' * 14 + 'BBBBB' + '.' * 13,         # jaw
    '.' * 15 + 'BBB' + '.' * 14,           # chin
    '.' * 16 + 'B' + '.' * 15,             # neck
    '.' * 12 + 'KBBBBBBK' + '.' * 12,      # hunched shoulders rising behind jaw
    '.' * 12 + 'bBBBBBBb' + 'BBB' + '.' * 9,   # shoulders + hanging upper arm
    '.' * 5 + 'WWWWWWW' + 'BBBKKBBB' + 'BBB' + '.' * 9,   # shield top + ribs + upper arm
    '.' * 5 + 'WWMMMWW' + 'bBBKKBBb' + 'BBB' + '.' * 9,
    '.' * 5 + 'WwMMMwW' + 'BBBKKBBB' + 'KKb' + '.' * 9,  # elbow
    '.' * 5 + 'wwMMMww' + 'bBBKKBBb' + 'BBB' + '.' * 9,
    '.' * 5 + 'wwwwwww' + 'bBBKKBBb' + 'BBB' + '.' * 9,
    '.' * 6 + 'wwwww' + '.' + 'bBBKKBBb' + 'K' + 'GG' + '.' * 9,  # hand + grip
    '.' * 12 + 'bBKKBb' + '..' + 'KGG' + '.' * 9,
    '.' * 12 + 'KKK..KKK' + 'mmmmm' + '.' * 7,   # hips + crossguard
    '.' * 13 + 'BBB..BBB' + 'sSs' + '.' * 8,     # thighs + blade
    '.' * 13 + 'BBB..BBB' + 'sSs' + '.' * 8,
    '.' * 13 + 'bBb..bBb' + 'sSs' + '.' * 8,
    '.' * 13 + 'KKK..KKK' + 'sSs' + '.' * 8,     # knees (dark joints)
    '.' * 13 + 'BBB..BBB' + 'sSs' + '.' * 8,
    '.' * 13 + 'bbb..bbb' + 'sSs' + '.' * 8,
    '.' * 13 + 'bbb..bbb' + 'SSS' + '.' * 8,     # blade tip
    '.' * 12 + 'BBB..BBB' + '.' * 12,    # insteps
    '.' * 11 + 'bbbb..bbbb' + '.' * 11,  # feet
    '.' * 32,
    '.' * 32,
]

assert len(rows) == 32
for i, r in enumerate(rows):
    assert len(r) == 32, (i, len(r))

c = new_canvas(W, H)
for y, r in enumerate(rows):
    for x, ch in enumerate(r):
        col = cols[ch]
        if col is not None:
            c.set(x, y, col)

# Ink-style dark outline around the whole figure for RPG readability
ink = c.color('#151210')
c.outline(ink)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31), indices=True))

finish(c)
