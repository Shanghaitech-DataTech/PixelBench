from pixelbench_api import *

# Palette for 16x16 RPG Chibi Female Lab Researcher
P = {
    '.': None,             # Transparent background
    
    # Hair (Rich layered black with dark slate-blue volume and sheen)
    '0': '#0d0e13',        # Deepest hair outline / back shadow
    '1': '#161822',        # Dark black hair base
    '2': '#242736',        # Charcoal black midtone
    '3': '#363b50',        # Hair midtone sheen
    '4': '#4e5572',        # Hair highlight sheen
    
    # Hair accessory (Cute red hairpin / barrette)
    'R': '#ef4444',        # Bright red clip
    'r': '#b91c1c',        # Dark red clip shadow
    
    # Skin
    'S': '#fcd8bd',        # Base warm skin
    's': '#ebb393',        # Skin soft shadow
    'd': '#d4916f',        # Deep neck shadow
    'b': '#f5988d',        # Soft rosy blush
    'm': '#d06868',        # Sweet mouth (natural rose)
    'n': '#e89494',        # Soft lip highlight
    
    # Eyes (Expressive brown anime chibi eyes)
    'L': '#1a100a',        # Upper eyelash
    'D': '#351608',        # Dark brown pupil / shadow
    'w': '#733512',        # Rich warm brown iris
    'a': '#b85c20',        # Glowing amber brown highlight
    'W': '#ffffff',        # Catchlight (pure white sparkle)
    
    # Lab coat (White)
    'C': '#ffffff',        # Pure white coat highlight
    'c': '#f0f4f8',        # Main lab coat white
    'g': '#cbd5e1',        # Coat soft shadow
    'G': '#90a4ae',        # Coat medium shadow / fold / pocket line
    'x': '#546e7a',        # Coat outline / seam
    
    # Inner clothes & Accessories
    't': '#1e293b',        # Dark navy inner blouse collar
    'T': '#0ea5e9',        # Cyan lanyard strap
    'I': '#ffffff',        # ID badge card
    'i': '#0284c7',        # ID badge photo
    'u': '#94a3b8',        # Silver button
    
    # Pants
    'k': '#1a1c26',        # Dark trousers base
    'K': '#2b2f3e',        # Trousers highlight
    
    # Shoes
    'B': '#261b17',        # Dark brown leather shoe
    'f': '#48342a',        # Shoe highlight
}

GRID = [
    # 0123456789012345
    "................",  # 0: transparent margin
    ".....123321.....",  # 1: hair crown top
    "...1234443210...",  # 2: hair crown with highlight sheen
    "..12Rr11123210..",  # 3: bangs + cute red hairpin at (4,3)-(5,3)
    "..12SLL1SLLS10..",  # 4: eyelashes at (5,6) and (9,10), bangs parting at 7
    "..02SWDSSWDS20..",  # 5: brown eyes top: catchlight at 5,9; dark pupil at 6,10
    "..02bawSSawb20..",  # 6: brown eyes bottom: amber/brown iris + blush on cheeks
    "...1SSSmnSSS1...",  # 7: cheeks + centered sweet soft smile at (7,8)
    "...011sSSss110..",  # 8: jawline, chin, neck shadow, hair behind
    "...xcgCtTCgcx...",  # 9: shoulders, lapels, navy collar + cyan lanyard
    "...xcIiCucGcx...",  # 10: sleeves, ID badge (I,i), button (u), breast pocket (G)
    "...ScGCCcCGcS...",  # 11: cute hands (S) at sides, coat pockets (G), buttons
    "...xgCcGCcCgx...",  # 12: coat lower body & hem
    "....xkKkkKkx....",  # 13: dark trousers emerging under coat
    ".....kK..Kk.....",  # 14: dark trousers (left 5,6; right 9,10)
    ".....Bf..fB.....",  # 15: leather shoes (left 5,6; right 9,10)
]

c = new_canvas(16, 16, name="female_lab_researcher_chibi")
for y, row in enumerate(GRID):
    for x, ch in enumerate(row):
        col = P.get(ch)
        if col:
            c.set(x, y, col)

finish(c)
