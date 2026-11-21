# Portable cassette player, 32x32 pixel-art icon.
result = new_canvas(32, 32, background=None, name="portable-cassette-player")

# Restrained hardware palette.
outline = result.color("#18202b", "outline")
outline2 = result.color("#263445", "outline-soft")
shadow = result.color("#45586a", "body-shadow")
body = result.color("#71879a", "body")
light = result.color("#a9bbc5", "body-light")
highlight = result.color("#d7e1e3", "highlight")
black = result.color("#10161e", "black")
window_edge = result.color("#344556", "window-edge")
reel = result.color("#d2dde0", "reel")
reel_shadow = result.color("#738998", "reel-shadow")
label = result.color("#efb84d", "accent")
red = result.color("#db5a55", "record")

# Headphone cable behind the player: stepped, single-pixel lead with a small plug/earbud.
result.line(24, 23, 29, 27, outline)
result.line(29, 27, 29, 30, outline)
result.set(28, 27, outline2)
result.rect(27, 29, 3, 2, outline, fill=True)
result.set(26, 30, outline)
result.set(27, 31, outline)
result.set(28, 29, light)

# Main player silhouette and offset depth.
result.rect(4, 2, 22, 25, outline, fill=True)
result.rect(3, 4, 2, 20, outline, fill=True)
result.set(5, 1, outline)
result.rect(6, 1, 17, 1, outline, fill=True)
result.set(24, 2, outline)
result.rect(5, 3, 19, 22, body, fill=True)
result.rect(5, 3, 2, 22, light, fill=True)
result.rect(7, 3, 17, 2, highlight, fill=True)
result.rect(23, 5, 1, 19, shadow, fill=True)
result.rect(7, 23, 16, 2, shadow, fill=True)
result.set(6, 24, shadow)
result.set(24, 24, outline)
result.set(5, 25, outline)
result.rect(7, 25, 16, 1, outline2, fill=True)

# Top mechanical controls and status marks.
result.rect(7, 1, 3, 2, outline, fill=True)
result.rect(8, 1, 1, 1, light, fill=True)
result.rect(12, 1, 4, 2, outline, fill=True)
result.rect(13, 1, 2, 1, light, fill=True)
result.rect(19, 1, 3, 2, outline, fill=True)
result.set(20, 1, red)
result.rect(8, 5, 8, 1, outline2, fill=True)
result.rect(8, 5, 4, 1, label, fill=True)
result.set(18, 5, red)
result.set(20, 5, outline2)

# Cassette window frame, then erase the centre for a true transparent window.
result.rect(7, 7, 16, 12, outline, fill=True)
result.rect(8, 8, 14, 10, window_edge, fill=True)
result.rect(9, 9, 12, 8, None, fill=True)
# Corner shine and base lip on the window frame.
result.rect(8, 8, 8, 1, highlight, fill=True)
result.set(8, 9, light)
result.rect(9, 17, 12, 1, shadow, fill=True)

# Two tape reels floating within the transparent aperture.
for cx in (12, 18):
    result.circle(cx, 13, 3, outline, fill=True)
    result.circle(cx, 13, 2, reel, fill=True)
    result.set(cx - 1, 12, highlight)
    result.set(cx + 1, 12, reel_shadow)
    result.set(cx - 1, 14, reel_shadow)
    result.set(cx + 1, 14, reel_shadow)
    result.set(cx, 13, None)
# Tape path and cassette hub bridge.
result.line(12, 16, 18, 16, outline2)
result.set(13, 15, outline2)
result.set(17, 15, outline2)
result.rect(14, 15, 3, 1, shadow, fill=True)

# Lower label separator and transport controls.
result.rect(8, 20, 13, 1, outline2, fill=True)
result.rect(8, 21, 3, 3, outline, fill=True)
result.poly([(9, 21), (9, 23), (11, 22)], highlight, fill=True)
result.rect(12, 21, 3, 3, outline, fill=True)
result.rect(13, 22, 1, 1, highlight, fill=True)
result.rect(16, 21, 3, 3, outline, fill=True)
result.rect(17, 22, 1, 1, red, fill=True)
result.rect(20, 21, 2, 3, outline, fill=True)
result.rect(20, 22, 1, 1, light, fill=True)

# Right-side volume wheel and tick marks.
result.rect(25, 8, 2, 8, outline, fill=True)
result.rect(25, 9, 1, 6, light, fill=True)
result.set(26, 9, shadow)
result.set(26, 11, shadow)
result.set(26, 13, shadow)
result.set(26, 15, shadow)
result.set(24, 8, highlight)
result.set(24, 15, highlight)

# Small headphone jack cue near cable exit.
result.set(23, 22, black)
result.set(24, 22, highlight)

view(result, scale=16, margin=0)
finish(result)
