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
"KKWKKYYKK.A.....",
# 6: Apex black border with white dot at x=1, cream spot ZZ at x=4..5, costa smooth to x=8, antenna at x=11
"KKWKKZZKK..A..ES", # Eye at x=14, Head at x=15
# 7: Costa smooth black edge to x=10, upper cell, discal cell, antenna base at x=12
"KKKKHGMLOKKK.AES", # Head/eye
# 8: Costa black edge to x=12, discal cell (G,H,L), thorax top
".KKKLGHLMORKKKTS", # Thorax top
# 9: Forewing outer margin with white dot W at x=1, cells & 1px veins, thorax white speckle at x=14
"KKWKMKHKLGHLMOKWS", # wait, let's make sure row length is exactly 16!
]

# Let's verify string lengths carefully in a script!
