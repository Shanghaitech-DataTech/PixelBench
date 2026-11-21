# Final Submission: 32x32 RPG Closed Leather Spellbook

PALETTE = {
    '.': None,       # Transparent
    'O': '#140c13',  # 1. Dark outline (black-brown)
    'D': '#3c1a15',  # 2. Deep leather shadow
    'M': '#79361c',  # 3. Mid leather body
    'L': '#b85e28',  # 4. Light leather highlight
    'G': '#e29d23',  # 5. Bright gold / brass
    'H': '#fff375',  # 6. Pale gold / Specular shine
    'S': '#967f5c',  # 7. Parchment shadow / Antique brass shadow
    'P': '#ded0a2',  # 8. Parchment pages
}

# 32x32 grid
rows = [
    #  01234567890123456789012345678901
    r"................................", # 0
    r"................................", # 1
    r".........OOOOOOOOOOOOOOOOOOO....", # 2
    r"....OOOOODDDDDDDDDDDDDDDDDDDO...", # 3
    r"...OGHHGOSPPSPSPSPSPSPSPSPPSDO..", # 4
    r"..OGHHGGOOOOOOOOOOOOOOOOSPPSDO..", # 5
    r"..OGHLGGOOGHHGLLLLLGHHGOOSPSDO..", # 6
    r"..OGLLMMOODHHGDDDDDGHHDOOSPSDO..", # 7
    r"..OMLLMMOODGHOLMMMDOHGDOOSPSDO..", # 8
    r"..OMMMMMOODGOOLMMMLOOGDOOSPSDO..", # 9
    r"..OMLHLMOODDLLMMMMMLLDDOOSPSDO..", # 10 Spine rib 1
    r"..OMDDDMOPDDLMMOGOMMDDDOOSPSDO..", # 11 Arcane eye top
    r"..OMLLMMODDDLMOGHHGMDDDOOSPSDO..", # 12 Arcane eye brow
    r"..OLLMMMODDDLMGHHHGMDDDODDDDDO..", # 13 Clasp strap top
    r"..OMMMMMODDDLGHHHHHGDDOGHGHGDO..", # 14 Clasp plate top
    r"..OMLHLMODDDLGHHOHHGDDOGHHHGDO..", # 15 Eye pupil & Clasp center
    r"..OMDDDMODDDLGHHHHHGDDOGHOGGDO..", # 16 Clasp keyhole
    r"..OMLLMMODDDLMGHHHGMDDDODDDDDO..", # 17 Clasp strap bottom
    r"..OLLMMMODDDLMOGHHGMDDDOOSPSDO..", # 18 Arcane eye bottom
    r"..OMMMMMODDDLMMOGOMMDDDOOSPSDO..", # 19 Arcane eye bottom point
    r"..OMLHLMOODDLLMMMMMLLDDOOSPSDO..", # 20 Spine rib 3
    r"..OMDDDMOODGOOLMMMLOOGDOOSPSDO..", # 21
    r"..OMLLMMOODGHOLMMMDOHGDOOSPSDO..", # 22
    r"..OGHLGMOODHHGDDDDDGHHDOOSPSDO..", # 23
    r"..OGHHGGOOGHHGLLLLLGHHGOOSPSDO..", # 24
    r"..OGHHGGOOOOOOOOOOOOOOOOSPPSDO..", # 25
    r"...OGHHGODDDDDDDDDDDDDDDDDDDO...", # 26
    "....OOOOOOOOOOOOOOOOOOOOOOOO....", # 27
    r"................................", # 28
    r"................................", # 29
    r"................................", # 30
    r"................................", # 31
]

# Fix row 11 stray character:
# In row 11: "..OMDDDMOPDDLMM..." -> replace the stray P at col 9 with O
rows[11] = r"..OMDDDM ODDLMMOGOMMDDDOOSPSDO..".replace(' ', 'O')

for idx, r in enumerate(rows):
    assert len(r) == 32, f"Row {idx:2d} length {len(r)} != 32: {r}"

c = new_canvas(32, 32, name="leather_spellbook")
for y, row in enumerate(rows):
    for x, ch in enumerate(row):
        col = PALETTE[ch]
        if col:
            c.set(x, y, col)

print(c.stats_text())
finish(c)
