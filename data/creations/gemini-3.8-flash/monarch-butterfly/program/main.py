from pixelbench_api import *

palette = {
    '.': None,
    'K': '#100f14', # Pitch black (veins, borders)
    'D': '#1e1a22', # Soft black / vein transition
    'W': '#ffffff', # Crisp pure white dots
    'Y': '#fee5b8', # Warm cream subapical spot
    'Z': '#f9d290', # Cream-gold spot shade
    'R': '#962002', # Deep burnt red-orange shadow against veins
    'O': '#d84403', # Classic monarch red-orange
    'M': '#ec6406', # Vibrant monarch orange
    'L': '#f68810', # Bright amber orange
    'H': '#fba922', # Golden highlight
    'G': '#fecf46', # Luminous honey-gold center glow
    'S': '#17161c', # Body deep charcoal
    'B': '#26252f', # Abdomen mid-tone
    'T': '#383744', # Abdomen dorsal highlight
    'E': '#505260', # Eye highlight
    'A': '#201f26', # Antenna stalk
    'C': '#141319', # Antenna club
}

# 16 columns (x=0 to 15), 32 rows (y=0 to 31)
# Center line: between x=15 and x=16
left_half = [
    # 0
    "................",
    # 1: Antenna club tip at x=7..8
    ".......CC.......",
    # 2: Antenna club & curve
    "......CCA.......",
    # 3: Forewing apex tip (x=1..3), antenna stalk at x=8
    ".KKK....A.......",
    # 4: Forewing apex black border with white dot at x=2, antenna at x=9
    "KKWKK...A.......",
    # 5: Forewing apex: white dot W at x=1, cream spot YY at x=4..5, antenna at x=10
    "KKWKKYYK..A.....",
    # 6: Apex black border with white dot at x=1, cream spot ZZ at x=4..5, costa smooth to x=8, antenna at x=11
    "KKWKKZZKK..A..ES", # Eye at x=14, Head at x=15
    # 7: Costa smooth black edge to x=10, upper cell, discal cell, antenna base at x=12
    "KKKKHGMLOKKK.AES", # Head/eye
    # 8: Costa black edge to x=13, discal cell (G,H,L), thorax top
    "KKKKLGHLMORKKKTS", # Thorax top (x=0 is K for smooth margin)
    # 9: Forewing outer margin with white dot W at x=2, cells & veins, thorax white speckle at x=14
    "KKWKLKHKLGHLOKWS",
    # 10: Outer margin, lower cell, vein K, discal cell, thorax
    "KKKMHLKKMGHLOKTS",
    # 11: Outer margin with white dot W at x=2, lower cell, submedian vein K, thorax
    "KKWKMHLKKLMROKWS",
    # 12: Outer margin, lower cell, submedian vein, thorax base
    ".KKKRMHLKKLMOKSS",
    # 13: Forewing tornus with white dot W at x=4, inner cell, abdomen top
    "..KKWKKRMHLMOKKS",
    # 14: Forewing tornus / Hindwing upper edge, abdomen
    "...KKKKKKKLMOKKB",
    # 15: Hindwing upper margin, upper radial cell, abdomen
    "....KKKKMHLMOKKT",
    # 16: Hindwing outer margin with white dot W, cell, radiating vein, abdomen
    "...KKWKKHMHLOKKB",
    # 17: Hindwing outer margin, cell, radiating vein, abdomen
    "..KKKKKLGHLMOKKT",
    # 18: Hindwing outer margin with white dot W, cell, radiating vein, abdomen
    "..KKWKKMLKKMLKKB",
    # 19: Hindwing outer margin, cells, scent patch (KK) on vein, abdomen
    ".KKKKMHLMKKMOKKT", # Male scent patch at x=9..10
    # 20: Hindwing outer margin with white dot W, cell, radiating vein, abdomen
    ".KKWKLGHLKKMLKKB",
    # 21: Hindwing outer margin, cell, radiating vein, abdomen
    ".KKKKMHLMKKMLKKT",
    # 22: Hindwing outer margin with white dot W, cell, vein, abdomen
    "..KKWKKMLKKMOKKB",
    # 23: Hindwing lower margin, lower cell, abdomen
    "..KKKKKRMHLMOKKT",
    # 24: Hindwing lower margin with white dot W, abdomen tip
    "...KKWKKKKMLOKKS",
    # 25: Hindwing curving inward to abdomen tip
    "....KKKKKKKROKKS",
    # 26: Hindwing bottom curve with white dots W
    ".....KKWKKWKKK..",
    # 27: Hindwing bottom curve
    "......KKKKKK....",
    # 28: Hindwing bottom edge
    "........KK......",
    # 29
    "................",
    # 30
    "................",
    # 31
    "................",
]

result = new_canvas(32, 32)
for y, row in enumerate(left_half):
    full_row = row + row[::-1]
    for x, ch in enumerate(full_row):
        color = palette.get(ch)
        if color:
            result.set(x, y, color)

finish(result)
