from pixelbench_api import *

# Create 64x64 canvas
c = new_canvas(64, 64, background=None)

# Define color palette - limited to stay under 86 colors
main_color = c.color('#5B9BD5', 'main_blue')
outline_color = c.color('#1A2F4A', 'dark_outline')
highlight_color = c.color('#8BC3F0', 'light_blue')
shadow_color = c.color('#0A1525', 'shadow')
accent_color = c.color('#FFD700', 'gold')
bg_color = c.color('#2D4A6F', 'bg_accent')
inner_bg = c.color('#1F3A52', 'inner_bg')

# Letter patterns - 8px tall, 6px wide for better readability
letters = {
    'P': [
        [1,1,1,1,1,0],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,1,1,1,1,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
    ],
    'I': [
        [1,1,1,1,1,1],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        [1,1,1,1,1,1],
    ],
    'X': [
        [1,0,0,0,0,1],
        [0,1,0,0,1,0],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        [0,1,0,0,1,0],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
    ],
    'E': [
        [1,1,1,1,1,1],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,1,1,1,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,1,1,1,1,1],
    ],
    'L': [
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,1,1,1,1,1],
    ],
    'Q': [
        [0,1,1,1,1,0],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,1,0,1],
        [1,0,1,0,1,1],
        [0,1,1,0,0,1],
        [0,0,0,1,1,1],
    ],
    'U': [
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [0,1,0,0,1,0],
        [0,0,1,1,0,0],
    ],
    'S': [
        [0,1,1,1,1,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [0,1,1,1,0,0],
        [0,0,0,0,1,0],
        [0,0,0,0,1,0],
        [1,0,0,0,1,0],
        [0,1,1,1,0,0],
    ],
    'T': [
        [1,1,1,1,1,1],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
    ],
}

def draw_letter_pattern(pattern, start_x, start_y, color):
    """Draw a letter pattern at position with given color"""
    for row_idx, row in enumerate(pattern):
        for col_idx, pixel in enumerate(row):
            if pixel:
                c.set(start_x + col_idx, start_y + row_idx, color)

def draw_styled_letter(char, start_x, start_y):
    """Draw letter with shadow, outline, and fill"""
    pattern = letters.get(char.upper(), letters['E'])
    
    # Shadow (offset 1px down-right)
    draw_letter_pattern(pattern, start_x + 1, start_y + 1, shadow_color)
    # Outline
    draw_letter_pattern(pattern, start_x, start_y, outline_color)
    # Main fill
    draw_letter_pattern(pattern, start_x, start_y, main_color)
    # Highlight on top row
    for col_idx, pixel in enumerate(pattern[0]):
        if pixel:
            c.set(start_x + col_idx, start_y, highlight_color)

# Background - solid color
c.rect(0, 0, 64, 64, bg_color, fill=True)

# Inner background rectangle for title area
c.rect(2, 2, 60, 60, inner_bg, fill=True)

# Border frame
c.rect(0, 0, 64, 64, outline_color, fill=False)
c.rect(1, 1, 62, 62, highlight_color, fill=False)

# Draw "PIXEL QUEST" as one word or two lines
# Each letter 6px wide + 2px spacing = 8px per letter
# "PIXEL QUEST" = 11 letters with space = 11*8 - 1 = 87px (too wide)
# Two lines: "PIXEL" (5*8-2=38px) and "QUEST" (5*8-2=38px)
# Centered: (60-38)/2 = 11

# Draw "PIXEL" on top line
pixel_start_x = 12
pixel_y = 14
pixel_word = "PIXEL"
for i, char in enumerate(pixel_word):
    draw_styled_letter(char, pixel_start_x + i * 8, pixel_y)

# Draw "QUEST" on bottom line
quest_start_x = 12
quest_y = 28
quest_word = "QUEST"
for i, char in enumerate(quest_word):
    draw_styled_letter(char, quest_start_x + i * 8, quest_y)

# Decorative elements
# Top decorative line above title
c.rect(10, 10, 44, 2, accent_color)

# Bottom decorative line below title
c.rect(10, 42, 44, 2, accent_color)

# Corner decorations - small diamonds
corner_positions = [(5, 5), (59, 5), (5, 59), (59, 59)]
for cx, cy in corner_positions:
    c.set(cx, cy, accent_color)
    c.set(cx-1, cy, accent_color)
    c.set(cx+1, cy, accent_color)
    c.set(cx, cy-1, accent_color)
    c.set(cx, cy+1, accent_color)

# Side stars
star_positions = [(5, 32), (59, 32)]
for sx, sy in star_positions:
    c.set(sx, sy, accent_color)
    c.set(sx-1, sy, accent_color)
    c.set(sx+1, sy, accent_color)
    c.set(sx, sy-1, accent_color)
    c.set(sx, sy+1, accent_color)
    c.set(sx, sy, highlight_color)

# Small pixel sword icon at bottom center
sword_x, sword_y = 27, 50
# Blade
c.rect(sword_x+3, sword_y, 2, 6, outline_color)
c.rect(sword_x+4, sword_y+1, 1, 4, highlight_color)
# Hilt
c.rect(sword_x+1, sword_y+6, 6, 2, accent_color)
c.rect(sword_x+3, sword_y+8, 2, 2, outline_color)

print(c.stats_text())
print(c.matrix_text())

finish(c)
