import math
import numpy as np

# We will build the 256x256 image using a fast, clean pixel buffer
# and helper functions, then transfer to Canvas.

W, H = 256, 256

# Cohesive Palette (Under 80 colors)
PALETTE = {
    # Sky & Sunset Gradient
    "sky_space": "#0a0512",
    "sky_twilight": "#160b22",
    "sky_purple": "#2b0f34",
    "sky_plum": "#46133f",
    "sky_crimson": "#6b193d",
    "sky_ruby": "#992233",
    "sky_blood_orange": "#c23825",
    "sky_deep_orange": "#e35920",
    "sky_bright_orange": "#f78223",
    "sky_amber": "#fcae33",
    "sky_gold": "#fde05c",
    "sky_pale_yellow": "#fff49e",

    # Mountains & Horizon
    "mtn_shadow": "#140c1c",
    "mtn_body": "#24162e",
    "mtn_mid": "#382242",
    "mtn_light": "#54304e",
    "mtn_rim": "#9e3e44",
    "mtn_goldrim": "#c75c36",

    # Smoke & Dust
    "smoke_darkest": "#100d14",
    "smoke_deep": "#1c1720",
    "smoke_mid": "#302633",
    "smoke_light": "#4a3c4f",
    "smoke_pale": "#6e5c70",
    "smoke_warm_glow": "#8a483b",
    "smoke_fire_glow": "#bf663b",

    # Dragon
    "drg_outline": "#08060a",
    "drg_dark": "#120c14",
    "drg_scale_dark": "#240f1a",
    "drg_scale_mid": "#3d1222",
    "drg_scale_red": "#631726",
    "drg_scale_crimson": "#8c1e28",
    "drg_scale_bright": "#b82b2b",
    "drg_scale_hi": "#dc482c",
    "drg_belly_shadow": "#2e120f",
    "drg_belly_mid": "#541e15",
    "drg_belly_glow": "#87321e",
    "drg_belly_bright": "#bf4f26",
    "drg_wing_dark": "#1e0d17",
    "drg_wing_mid": "#381421",
    "drg_wing_light": "#5c1e2b",
    "drg_wing_rim": "#8f302e",
    "drg_horn_dark": "#1e222a",
    "drg_horn_light": "#4c5566",

    # Fire, Dragon Breath & Explosions
    "fire_white": "#ffffff",
    "fire_pale": "#fff7a3",
    "fire_yellow": "#fed233",
    "fire_orange": "#fa821c",
    "fire_red": "#e03b18",
    "fire_crimson": "#a61919",
    "fire_dark": "#5e0e16",
    "fire_char": "#24060b",

    # Castle Stone & Masonry
    "stone_deep": "#0c0e14",
    "stone_shadow": "#141821",
    "stone_dark": "#1e2430",
    "stone_mid": "#2e3646",
    "stone_light": "#444f66",
    "stone_pale": "#62708c",
    "stone_highlight": "#8898b8",
    "stone_fire_warm": "#783b28",
    "stone_fire_glow": "#b35932",

    # Siege Tower, Wood & Iron
    "wood_darkest": "#0e0906",
    "wood_dark": "#1a110a",
    "wood_mid": "#2d1b11",
    "wood_light": "#472c1c",
    "wood_pale": "#69422a",
    "wood_hi": "#8f5e3d",
    "wood_iron": "#292e38",

    # Soldiers, Knights, Armor & Banners
    "steel_dark": "#10141c",
    "steel_mid": "#1f2837",
    "steel_light": "#364459",
    "steel_bright": "#586c8a",
    "steel_glint": "#93a8c4",
    "steel_white": "#dbe8f7",
    "herald_red_dark": "#611017",
    "herald_red": "#a1181f",
    "herald_red_bright": "#d62828",
    "herald_gold": "#a87718",
    "herald_yellow": "#f2bc29",

    # Battlefield Ground & Earth
    "ground_deep": "#0c0806",
    "ground_shadow": "#140f0a",
    "ground_dark": "#211710",
    "ground_mid": "#332318",
    "ground_light": "#4a3424",
    "ground_rock": "#22242c",
    "ground_rockhi": "#3a3e4c",
    "ground_ember": "#4d1b12",
}

print(f"Palette size: {len(PALETTE)}")
