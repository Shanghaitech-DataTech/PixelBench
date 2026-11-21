# Portable cassette player, 32x32 pixel art
result = new_canvas(32, 32, background=None, name="portable-cassette-player")

# Restricted hand-picked palette.
outline = "#18242b"
deep = "#263942"
shadow = "#3f5960"
body = "#88a6a2"
light = "#b9cbc3"
highlight = "#e4e7d7"
metal = "#6f8582"
window = "#9fbab533"
reel_dark = "#30464d"
reel = "#d9d9c5"
reel_hi = "#f3efd8"
accent = "#e15c4e"

# Headphone cable behind the player, with stepped pixel curves.
result.line(24, 23, 28, 23, outline)
result.line(28, 23, 28, 27, outline)
result.line(28, 27, 26, 29, outline)
result.line(26, 29, 21, 29, outline)
result.set(20, 28, outline)
result.set(20, 29, outline)
# Plug / earbud at cable end.
result.rect(17, 27, 3, 3, outline)
result.rect(17, 27, 2, 2, accent)
result.set(16, 27, outline)

# Main player silhouette and beveled shell.
result.rect(5, 4, 22, 23, outline)
result.rect(6, 5, 20, 21, body)
result.rect(7, 5, 18, 2, light)
result.rect(6, 7, 2, 18, metal)
result.rect(8, 24, 17, 2, shadow)
result.set(6, 5, outline)
result.set(25, 5, outline)
result.set(6, 25, outline)
result.set(25, 25, outline)

# Top ridge and playback controls.
result.rect(8, 2, 15, 2, outline)
result.rect(9, 2, 3, 2, metal)
result.rect(13, 2, 3, 2, light)
result.rect(17, 2, 3, 2, accent)
result.rect(21, 2, 2, 2, metal)
result.set(10, 1, outline)
result.set(14, 1, outline)
result.set(18, 1, outline)
result.set(22, 1, outline)

# Small status strip.
result.rect(9, 7, 13, 2, deep)
result.rect(10, 7, 7, 1, highlight)
result.set(20, 7, accent)
result.set(23, 7, outline)
result.set(24, 7, highlight)

# Cassette window: erase shell for true transparency, then frame it.
result.clear(9, 10, 14, 11)
result.rect(8, 9, 16, 13, outline, fill=False)
result.rect(9, 10, 14, 11, window)
# Window header lip and lower tape guide.
result.rect(10, 10, 12, 1, shadow)
result.rect(11, 19, 10, 1, deep)
result.rect(12, 18, 8, 1, reel)
result.set(11, 18, outline)
result.set(20, 18, outline)

# Twin tape reels.
for cx in (12, 19):
    result.circle(cx, 15, 3, reel_dark)
    result.circle(cx, 15, 2, reel)
    result.set(cx, 13, reel_hi)
    result.set(cx - 2, 15, highlight)
    result.set(cx + 2, 15, metal)
    result.set(cx, 17, metal)
    result.set(cx, 15, outline)
# Tape line linking reels.
result.line(14, 17, 17, 17, deep)

# Door corners and latch.
result.set(8, 9, highlight)
result.set(23, 9, shadow)
result.rect(22, 13, 2, 5, deep)
result.set(22, 14, accent)

# Bottom playback symbols / controls.
result.rect(9, 23, 3, 2, deep)
result.poly([(10, 23), (10, 25), (12, 24)], highlight)
result.rect(14, 23, 3, 2, deep)
result.rect(15, 23, 1, 2, highlight)
result.rect(19, 23, 3, 2, deep)
result.set(20, 24, accent)

# Side volume wheel and headphone jack.
result.rect(26, 9, 2, 7, outline)
result.set(27, 10, metal)
result.set(27, 12, light)
result.set(27, 14, metal)
result.rect(25, 19, 3, 3, outline)
result.set(26, 20, highlight)

view(result, scale=16, margin=0)
finish(result)
