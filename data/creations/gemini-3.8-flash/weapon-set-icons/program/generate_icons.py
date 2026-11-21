import sys
from pixelbench_api import *

def build_palette(c):
    # Register our rich unified palette
    palette = {
        '.': None,               # Transparent
        'k': '#14121a',          # Deepest dark outline / crevices
        'd': '#231e2b',          # Dark shadow outline
        
        # Steel / Iron
        'S': '#293242',          # Steel deep shadow
        's': '#414e66',          # Steel shadow
        'm': '#647999',          # Steel midtone
        'l': '#99b0cc',          # Steel light
        'h': '#d0e2f2',          # Steel bright highlight
        'w': '#ffffff',          # Specular glint
        
        # Gold / Brass
        'G': '#42240b',          # Gold deep shadow
        'g': '#754511',          # Gold shadow
        'y': '#b87b1c',          # Gold midtone
        'Y': '#e5ab30',          # Bright gold
        'j': '#fad45a',          # Gold highlight
        'J': '#fff5a6',          # Gold specular
        
        # Wood
        'W': '#26140b',          # Wood dark shadow
        'u': '#4d2814',          # Wood shadow
        'b': '#7a4320',          # Wood midtone
        't': '#aa6535',          # Wood light
        'T': '#d18e5c',          # Wood highlight
        
        # Leather / Straps
        'L': '#2b1b14',          # Leather shadow
        'e': '#593728',          # Leather mid
        'a': '#8a5c45',          # Leather light
        'A': '#b8866e',          # Leather highlight
        
        # Ruby Red / Velvet
        'R': '#3b0a14',          # Ruby deep shadow
        'r': '#731424',          # Ruby shadow
        'v': '#b02035',          # Ruby midtone
        'V': '#e33d52',          # Ruby bright
        'p': '#ff788a',          # Ruby highlight
        
        # Teal Feathers / Bowstring / Accents
        'f': '#3d5252',          # Feather shadow
        'c': '#648787',          # Feather midtone
        'C': '#9ec2bf',          # Feather light
        'o': '#e2f5f2',          # Feather bright / string
        'O': '#b8ccd1',          # String midtone
    }
    for char, hex_val in palette.items():
        if hex_val is not None:
            c.color(hex_val, name=char)
    return palette

def paste_ascii(c, x_offset, y_offset, lines, palette):
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in palette and palette[char] is not None:
                c.set(x_offset + x, y_offset + y, palette[char])

print("Helper ready")
