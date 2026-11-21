from pixelbench_api import *

# Let's design the dim sum chef
c = new_canvas(32, 32)

# Palette definitions
# Hat & Coat:
HAT_WHITE = "#FFFFFF"
HAT_LIGHT = "#E8EDF2"
HAT_SHADE = "#B8C4D1"
HAT_DARK  = "#7D8C9D"
COAT_WHITE = "#FFFFFF"
COAT_SHADE = "#CBD5E1"
COAT_DARK  = "#8292A6"
COLLAR_RED = "#C53030"

# Skin:
SKIN_LIGHT = "#FFDFBD"
SKIN_MAIN  = "#F7C297"
SKIN_SHADE = "#D99368"
SKIN_DARK  = "#9C5738"
CHEEK_ROSE = "#E88282"

# Hair:
HAIR_DARK  = "#2C1E1A"
HAIR_MID   = "#4A342C"

# Eyes / Outlines:
OUTLINE_DARK = "#1E1715"
EYE_COLOR    = "#1E1715"

# Apron:
# Dark indigo blue so flour dust shows vividly!
APRON_BASE  = "#2C3E55"
APRON_DARK  = "#1C2838"
APRON_LIGHT = "#3B5270"
APRON_TIE   = "#182230"
FLOUR_DUST1 = "#E2E9F0"
FLOUR_DUST2 = "#9AAEC4"

# Bamboo Steamer:
BAMBOO_HILIGHT = "#F4D28C"
BAMBOO_LIGHT   = "#E2B666"
BAMBOO_MAIN    = "#C08B3E"
BAMBOO_SHADE   = "#8E5E23"
BAMBOO_DARK    = "#573511"
BAMBOO_BAND    = "#3D2409"

# Buns & Dim Sum:
BUN_WHITE   = "#FFFDF7"
BUN_LIGHT   = "#F5EFE1"
BUN_SHADE   = "#D8C7B0"
BUN_DOT     = "#D13434"
LEAF_GREEN  = "#6EA343"
LEAF_DARK   = "#497327"

# Steam:
STEAM_WHITE = "#F0F5FA"
STEAM_FAINT = "#D0E0F0"

# Pants & Shoes:
PANTS_MAIN  = "#333842"
PANTS_DARK  = "#21242B"
SHOES_MAIN  = "#1F2124"
SHOES_SHADE = "#121316"
SHOES_HI    = "#434852"

# Let's draft the character onto the canvas using set or coordinates
# We can define a 32x32 string grid or programmatic drawing for easy refinement.
