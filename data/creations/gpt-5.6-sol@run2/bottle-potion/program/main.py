output = input_canvas.copy(name='output')

# Preserve the original shading structure while turning every water tone purple.
water_map = {
    5: '#682b91',   # dark surface water
    6: '#a64bd4',   # main potion
    7: '#d99cff',   # bright glint
    8: '#c675ed',   # secondary highlight
    9: '#441755',   # deep internal shadow
    10: '#be6be5',  # lower glint
}
for y in range(64):
    for x in range(64):
        idx = output.get(x, y)
        if idx in water_map:
            output.set(x, y, water_map[idx])

# Potion palette.
deep = output.color('#441755', name='potion_deep')
dark = output.color('#682b91', name='potion_dark')
mid = output.color('#a64bd4', name='potion_mid')
bright = output.color('#d99cff', name='potion_bright')
shine = output.color('#f1c6ff', name='potion_shine')

# A lively, block-aligned meniscus and foam along the liquid surface.
output.rect(12, 26, 8, 2, mid)
output.rect(20, 24, 8, 4, mid)
output.rect(28, 26, 8, 2, mid)
output.rect(36, 24, 6, 4, mid)
output.rect(42, 26, 6, 2, mid)
output.rect(14, 26, 4, 2, bright)
output.rect(24, 24, 4, 2, shine)
output.rect(36, 24, 4, 2, bright)
output.rect(44, 26, 2, 2, shine)

# Bubbles inside the potion, drawn as crisp 2px-grid rings and glints.
output.rect(12, 32, 6, 6, deep)
output.rect(14, 34, 2, 2, bright)
output.rect(24, 40, 4, 4, deep)
output.rect(26, 40, 2, 2, shine)
output.rect(38, 32, 4, 4, deep)
output.rect(38, 32, 2, 2, shine)
output.rect(32, 48, 6, 6, dark)
output.rect(34, 50, 2, 2, shine)
output.rect(16, 48, 4, 4, dark)
output.rect(16, 48, 2, 2, bright)
output.rect(42, 42, 4, 4, dark)
output.rect(42, 42, 2, 2, shine)

# Refine submerged bubbles into hollow pixel diamonds.
def potion_bubble(x, y, base):
    output.rect(x, y, 6, 6, base)
    output.rect(x + 2, y, 2, 2, deep)
    output.rect(x, y + 2, 2, 2, deep)
    output.rect(x + 4, y + 2, 2, 2, dark)
    output.rect(x + 2, y + 4, 2, 2, dark)
    output.rect(x + 2, y + 2, 2, 2, shine)

potion_bubble(12, 32, mid)
potion_bubble(32, 48, mid)
potion_bubble(40, 40, mid)

# Hollow rising bubbles in the clear upper chamber.
white = output.color('#ffffff')
def air_bubble(x, y):
    output.rect(x, y, 6, 6, white)
    output.rect(x + 2, y, 2, 2, dark)
    output.rect(x, y + 2, 2, 2, dark)
    output.rect(x + 4, y + 2, 2, 2, dark)
    output.rect(x + 2, y + 4, 2, 2, dark)
    output.set(x + 1, y + 1, shine)

# Clear the rough first-pass bubbles, then place crisp rings.
output.rect(28, 18, 4, 4, white)
output.rect(38, 14, 4, 4, white)
air_bubble(26, 18)
air_bubble(36, 12)

# Small arcane twinkles among the fizz.
output.rect(18, 18, 2, 6, bright)
output.rect(16, 20, 6, 2, bright)
output.rect(46, 18, 2, 4, shine)
output.rect(44, 20, 6, 2, shine)

view(output, scale=8, margin=0)
finish(output)
