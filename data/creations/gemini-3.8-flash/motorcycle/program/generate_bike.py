import math
import numpy as np

# Let's inspect canvas and drawing tools
c = new_canvas(128, 128)

# Color Palette definition
PALETTE = {
    # Transparency
    'trans': None,
    
    # Bodywork - Dark Gray & Black
    'body_deep': '#0f1013',
    'body_black': '#16171c',
    'body_dark': '#22242c',
    'body_mid': '#323642',
    'body_slate': '#444957',
    'body_light': '#5c6375',
    'body_hi': '#7a8399',
    'body_spec': '#9da6bd',

    # Windscreen - Tinted Black Gloss
    'wind_black': '#0b0c10',
    'wind_dark': '#141720',
    'wind_mid': '#202636',
    'wind_hi': '#36435c',
    'wind_edge': '#586c8f',
    'wind_glint': '#8fa6cf',

    # Silver / Metal
    'metal_black': '#1c1f24',
    'metal_shadow': '#2b313a',
    'metal_dark': '#404752',
    'metal_mid': '#636c7a',
    'metal_light': '#8e98a8',
    'metal_bright': '#bec7d4',
    'metal_hi': '#e4ebf5',
    'metal_pure': '#ffffff',

    # Red Accents & Tail Light
    'red_shadow': '#4a080c',
    'red_dark': '#780f16',
    'red_mid': '#b81420',
    'red_bright': '#eb2332',
    'red_hi': '#ff5461',
    'red_glow': '#ff919a',

    # Tires & Rubber
    'tire_deep': '#101012',
    'tire_dark': '#1a1b20',
    'tire_mid': '#292a32',
    'tire_tread': '#383a45',
    'tire_hi': '#4d505e',

    # Accent Gold / Bronze (calipers / shock)
    'gold_dark': '#5e4317',
    'gold_mid': '#a37722',
    'gold_bright': '#dca838',
    'gold_hi': '#fce177',

    # Lights
    'light_cyan': '#c2f3ff',
    'light_white': '#f2fdff',
}

print(f"Colors planned: {len(PALETTE)}")
