import math
import numpy as np

W, H = 256, 256

# Palette definition (Hex codes)
PALETTE_MAP = {
    # Background & Architecture
    "bg_void": "#05060b",
    "bg_deep": "#0a0c16",
    "sky_dark": "#0c1222",
    "sky_mid": "#141c34",
    "sky_nebula": "#221a3a",
    "star_dim": "#526284",
    "star_bright": "#d4e6ff",
    "stone_darkest": "#0f111c",
    "stone_dark": "#181a28",
    "stone_shadow": "#222538",
    "stone_mid": "#32364e",
    "stone_light": "#494e6d",
    "stone_bright": "#686e94",
    "stone_hi": "#8e95bf",
    # Floor
    "floor_dark": "#10111d",
    "floor_mid": "#1b1d2e",
    "floor_light": "#282a40",
    "floor_joint": "#0a0b12",
    # Pedestal
    "ped_base": "#1e1b29",
    "ped_shadow": "#2c273b",
    "ped_mid": "#413b54",
    "ped_light": "#5c5474",
    "ped_hi": "#7d749a",
    "ped_gold": "#caa042",
    # Outlines & Shadows
    "outline_black": "#070608",
    "metal_shadow": "#1e1308",
    "brass_deep": "#38200a",
    # Brass / Bronze / Gold Ramps
    "brass_shadow": "#56320d",
    "brass_dark": "#784713",
    "brass_mid": "#a2651b",
    "brass_warm": "#c98524",
    "brass_light": "#e8a933",
    "brass_bright": "#f8cb4f",
    "gold_hi": "#fde877",
    "gold_shine": "#fff7b0",
    "gold_white": "#fffef0",
    # Iron / Steel / Vernier / Axles
    "iron_dark": "#1b212c",
    "iron_mid": "#2f3a4d",
    "iron_light": "#4d5f7c",
    "iron_bright": "#7b91b3",
    "iron_hi": "#b8c9e2",
    # Arcane Cyan & Glow
    "rune_dark": "#0c3042",
    "rune_mid": "#165d7a",
    "rune_bright": "#229cb5",
    "cyan_glow": "#3ae0d5",
    "cyan_bright": "#7dfbee",
    "cyan_white": "#ebffff",
    # Gem: Ruby
    "ruby_deep": "#300812",
    "ruby_dark": "#610f23",
    "ruby_mid": "#a31c3c",
    "ruby_bright": "#e63c62",
    "ruby_hi": "#ffa3b6",
    # Gem: Amethyst
    "amethyst_deep": "#210933",
    "amethyst_dark": "#4a156e",
    "amethyst_mid": "#7e28b8",
    "amethyst_bright": "#b553ee",
    "amethyst_hi": "#e6aaff",
    # Gem: Emerald
    "emerald_deep": "#082618",
    "emerald_dark": "#105234",
    "emerald_mid": "#1f8f5c",
    "emerald_bright": "#3ed48e",
    "emerald_hi": "#9effce",
    # Gem: Sapphire
    "sapphire_deep": "#081736",
    "sapphire_dark": "#123374",
    "sapphire_mid": "#245bbb",
    "sapphire_bright": "#4f92f2",
    "sapphire_hi": "#b5d7ff",
}

print(f"Total palette colors: {len(PALETTE_MAP)}")
