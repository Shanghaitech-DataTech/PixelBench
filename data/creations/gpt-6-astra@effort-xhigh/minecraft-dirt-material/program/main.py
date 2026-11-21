# Seamless, full-face dirt material. All marks wrap across the tile edges.
import random

result = new_canvas(16, 16, '#855b3e', name='dirt')
palette = {
    'deep': '#593d2c',
    'shade': '#704c34',
    'earth': '#855b3e',
    'light': '#996d49',
    'ochre': '#aa7c53',
    'stone_shadow': '#777265',
    'stone': '#928b79',
}

def mark(x, y, pixels, color):
    for dx, dy in pixels:
        result.set((x + dx) % 16, (y + dy) % 16, palette[color])

# Irregular, interlocking soil grains; no outline or border around the tile.
shadows = [
    (0,0,[(0,0),(1,0),(0,1),(-1,1)]),
    (5,0,[(0,0),(1,0),(1,1),(2,1),(2,2)]),
    (11,1,[(0,0),(1,0),(0,1),(-1,1)]),
    (3,3,[(0,0),(1,0),(0,1),(0,2),(-1,2)]),
    (8,3,[(0,0),(1,0),(1,1),(2,1)]),
    (14,4,[(0,0),(1,0),(0,1),(-1,1),(-1,2)]),
    (6,6,[(0,0),(1,0),(0,1),(-1,1)]),
    (0,7,[(0,0),(1,0),(1,1),(2,1)]),
    (10,7,[(0,0),(1,0),(0,1),(0,2),(-1,2)]),
    (4,10,[(0,0),(1,0),(2,0),(1,1),(2,1)]),
    (14,9,[(0,0),(1,0),(0,1),(1,1),(1,2)]),
    (0,12,[(0,0),(1,0),(0,1),(-1,1)]),
    (8,12,[(0,0),(1,0),(2,0),(2,1)]),
    (4,14,[(0,0),(1,0),(0,1),(-1,1)]),
    (12,14,[(0,0),(1,0),(0,1),(1,1)]),
]
for x,y,p in shadows:
    mark(x,y,p,'shade')

lights = [
    (2,0,[(0,0),(1,0),(1,-1)]),
    (8,0,[(0,0),(1,0),(0,1),(-1,1)]),
    (14,1,[(0,0),(1,0),(0,1)]),
    (1,3,[(0,0),(0,1),(-1,1)]),
    (5,3,[(0,0),(1,0),(1,1)]),
    (11,4,[(0,0),(1,0),(0,1)]),
    (3,6,[(0,0),(1,0),(0,1)]),
    (8,6,[(0,0),(0,1),(-1,0)]),
    (15,7,[(0,0),(0,-1),(-1,0)]),
    (6,9,[(0,0),(1,0),(1,-1),(2,0)]),
    (12,9,[(0,0),(0,1),(-1,1)]),
    (2,11,[(0,0),(0,-1),(1,0)]),
    (6,12,[(0,0),(0,1),(-1,1)]),
    (11,12,[(0,0),(1,0),(1,1)]),
    (2,14,[(0,0),(0,1),(-1,1)]),
    (8,15,[(0,0),(1,0),(1,-1)]),
    (15,14,[(0,0),(0,1),(-1,1)]),
]
for x,y,p in lights:
    mark(x,y,p,'light')

# Sparse deeper crevices and warm mineral grains.
for x,y in [(0,1),(6,1),(3,4),(9,4),(13,6),(6,7),(1,8),(10,8),(5,11),(15,10),(0,13),(9,12),(4,15),(13,15)]:
    mark(x,y,[(0,0)],'deep')
for x,y in [(3,0),(8,0),(14,1),(5,3),(11,4),(3,6),(15,6),(7,8),(2,10),(6,12),(12,12),(2,14),(9,14)]:
    mark(x,y,[(0,0)],'ochre')

# Small embedded stone fragments, muted enough to sit within the soil.
mark(11,0,[(0,0),(1,0),(1,-1)],'stone_shadow')
mark(11,0,[(0,0)],'stone')
mark(5,5,[(0,0),(1,0),(1,1)],'stone_shadow')
mark(5,5,[(0,0)],'stone')
mark(12,7,[(0,0),(1,0),(0,1)],'stone_shadow')
mark(12,7,[(0,0)],'stone')
mark(8,11,[(0,0),(0,1)],'stone_shadow')
mark(8,11,[(0,0)],'stone')
mark(2,13,[(0,0)],'stone_shadow')

view(result, scale=24, margin=0)
# A temporary repeat preview tests the joins; only the 16x16 tile is delivered.
repeat = new_canvas(48, 48, name='repeat_check')
for yy in range(3):
    for xx in range(3):
        repeat.blit(result,16*xx,16*yy)
view(repeat, scale=8, margin=0)
print(result.stats_text())
save('dirt', result)
finish(result)
