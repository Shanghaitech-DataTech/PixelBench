import pixelbench_api as pb

c = pb.new_canvas(32, 32)

P = {
    '.': None,
    # Outline & Creases (warm, soft, no harsh black!)
    'B': '#3E2D23',  # Deepest warm brown (eye pupil, hoof bottoms)
    'b': '#5A4334',  # Main warm outline
    'o': '#785F4D',  # Soft outline / wool fold shadow
    'i': '#9B816E',  # Inner wool fold shadow
    'j': '#BDA593',  # Very soft crease tone
    
    # Wool Shades (warm ivory/cream, fluffy, gentle flat shading)
    'W': '#FFFFFF',  # Bright pure white wool highlight
    'w': '#FCF8EE',  # Bright warm cream
    '1': '#F5ECE0',  # Main light wool body
    '2': '#E8DCCB',  # Soft cream midtone
    '3': '#D7C3AE',  # Warm tan wool shadow
    '4': '#C0AA92',  # Deep wool shadow (underbelly & recesses)
    '5': '#A48D75',  # Darkest crevice tone
    
    # Face & Skin (peachy warm skin)
    'F': '#FFF4EB',  # Snout highlight
    'f': '#FCE2CD',  # Light peach skin
    's': '#F3C9A6',  # Base peach skin
    'm': '#DAAD87',  # Shaded skin / lower snout
    't': '#BD8A65',  # Deep jaw contour
    
    # Eye & Details
    'E': '#26140D',  # Warm dark espresso eye
    'e': '#FFFFFF',  # Eye shine dot
    'k': '#4B2A1D',  # Eye contour
    'N': '#E88597',  # Pink nose tip
    'n': '#B85568',  # Mouth / nostril
    'C': '#FCAEBC',  # Blushing pink cheek
    
    # Pale Pink Ears (soft pastel pink, warm, cozy)
    'K': '#FFE9EF',  # Pale pink ear highlight
    'p': '#F9B2C2',  # Soft pale pink ear interior
    'r': '#E6899E',  # Mid pink ear shade
    'q': '#C6657A',  # Deep pink ear shadow
    'z': '#8C4656',  # Ear rim / outline
    
    # Legs & Hooves
    'L': '#F5EBDD',  # Front near leg wool/skin
    'l': '#E0D0BD',  # Front near leg shaded
    'H': '#584335',  # Near hoof light
    'h': '#3A291F',  # Near hoof dark
    'D': '#A48E7A',  # Far leg light (in shadow)
    'd': '#7E6855',  # Far leg dark
    'G': '#423126',  # Far hoof light
    'g': '#281A13',  # Far hoof dark
}

grid = [
    # 01234567890123456789012345678901
    "................................", # 0
    "................................", # 1
    "................................", # 2
    "................................", # 3
    "................................", # 4
    "...........zzb..................", # 5
    ".........zzKpzb...bbbb..........", # 6
    "........zKpprqzb.bWWwwb...bbbb..", # 7
    ".......bzzqqzzbbWwwwwwwbbWWwwwb.", # 8
    "......bWWwwbbWwwww1111ww111wwwwb", # 9
    ".....bWwwww11Www11111111111111wb", # 10
    "....bWwww11111w1111111111111111b", # 11
    "...bFFw11111111111122111111111b.", # 12
    "..bFFFfs11zzzz1111121111111111b.", # 13
    ".bNFFseEsKpprzo1111211111111bbWb", # 14
    ".bNfsEEsspprrqzo11121111111bWWwb", # 15
    "..bmmCCszpprrqqzb1112111111bWwwb", # 16
    "...bsttzqqqzzzzb111121111111bbb.", # 17
    "...bWWwbbzzzb11111111211111b....", # 18
    "..bWWwwww111111111111221111b....", # 19
    "..bWwwww1111111111111122112b....", # 20
    "...b11111111111111111112222b....", # 21
    "....bb11111111111111111122bb....", # 22
    ".....bb2222222222222222223b.....", # 23
    "......bb33333333333333334bb.....", # 24
    ".......bLLb.bDDb.bLLb.bDDb......", # 25
    ".......bLLb.bDDb.bLLb.bDDb......", # 26
    ".......bHHb.bGGb.bHHb.bGGb......", # 27
    ".......bhhb.bggb.bhhb.bggb......", # 28
    "................................", # 29
    "................................", # 30
    "................................", # 31
]

for i, r in enumerate(grid):
    assert len(r) == 32, f"Row {i} has length {len(r)}"
    for x, ch in enumerate(r):
        col = P.get(ch)
        if col:
            c.set(x, i, col)

pb.view(c)
pb.finish(c)
