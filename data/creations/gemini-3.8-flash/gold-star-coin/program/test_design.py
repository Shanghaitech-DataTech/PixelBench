from pixelbench_api import *

# Let's define the 6-color palette
PALETTE = {
    'DARK': '#331602',     # 1. Dark outline
    'SHADOW': '#854c06',   # 2. Deep bronze shadow
    'MID': '#d48a08',      # 3. Base gold
    'LIGHT': '#f7c325',    # 4. Bright yellow gold
    'PALE': '#ffed75',     # 5. Highlight / shine
    'WHITE': '#ffffff',    # 6. Specular white
}

# Let's test a design where:
# - Outline is DARK (#331602)
# - Rim highlight (top-left) is PALE/LIGHT, rim shadow (bottom-right) is SHADOW/MID
# - Coin inner field is MID or LIGHT
# - Star in center is LIGHT / PALE with WHITE shine and SHADOW depth

# Let's write an ASCII grid parser so we can precisely paint pixel-by-pixel!
grid_str = """
..DDDDDDDD....
.D..........D.
D............D
"""
