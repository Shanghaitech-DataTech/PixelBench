# Portable cassette player icon, 32x32, transparent background.
result = new_canvas(32, 32, background=None, name="portable-cassette-player")

# Restrained pixel-art palette.
outline = result.color("#172033", "outline")
outline2 = result.color("#28334a", "outline_soft")
body_dark = result.color("#586477", "body_dark")
body = result.color("#8c9aa8", "body")
body_light = result.color("#c4ced4", "body_light")
highlight = result.color("#eef3f2", "highlight")
shadow = result.color("#3d485c", "shadow")
teal_dark = result.color("#177f83", "teal_dark")
teal = result.color("#2db7ad", "teal")
teal_light = result.color("#77e0ce", "teal_light")
cream = result.color("#f4e6b8", "reel_cream")
tape = result.color("#4d2d37", "tape")
red = result.color("#e85d5a", "record_red")

# Headphone lead behind the player: plug at top and loose loop below.
result.line(24, 2, 28, 2, outline)
result.set(28, 3, outline)
result.line(29, 3, 29, 22, outline)
result.line(29, 22, 28, 22, outline)
result.line(28, 22, 28, 27, outline)
result.line(28, 27, 26, 29, outline)
result.line(26, 29, 22, 29, outline)
result.set(21, 28, outline)
# Small headphone plug/cable connector.
result.rect(27, 0, 3, 2, outline)
result.set(28, 2, body_light)
result.set(27, 0, highlight)

# Top controls behind the body.
result.rect(7, 2, 4, 2, outline)
result.rect(8, 1, 2, 2, body_light)
result.rect(12, 1, 3, 3, outline)
result.rect(13, 1, 1, 2, red)
result.rect(17, 1, 3, 3, outline)
result.rect(18, 1, 1, 2, teal_light)
# Ridged volume wheel.
result.rect(22, 1, 4, 3, outline)
result.line(23, 1, 23, 2, body_light)
result.line(25, 1, 25, 2, body_light)

# Main chassis and stepped corners.
result.rect(5, 4, 22, 23, outline)
result.set(5, 4, None); result.set(26, 4, None)
result.set(5, 26, None); result.set(26, 26, None)
result.rect(6, 4, 20, 1, body_light)
result.rect(6, 5, 20, 20, body)
result.rect(6, 25, 20, 1, body_dark)
result.rect(6, 6, 2, 18, body_light)
result.rect(24, 5, 2, 20, body_dark)
result.line(7, 5, 23, 5, highlight)
result.set(6, 5, highlight)
result.line(7, 24, 23, 24, shadow)
result.set(25, 24, outline2)

# Left accent stripe and tiny brand bars.
result.rect(7, 7, 2, 14, teal_dark)
result.rect(8, 7, 1, 14, teal)
result.rect(10, 7, 5, 1, outline2)
result.rect(10, 8, 3, 1, highlight)
result.set(14, 8, body_dark)

# Cassette window frame. Interior remains truly transparent.
result.rect(10, 10, 14, 11, outline)
result.rect(11, 11, 12, 9, None)
# Glass-like corner glints that do not fill the transparent window.
result.line(11, 11, 13, 11, teal_light)
result.set(11, 12, teal_light)
result.line(20, 19, 22, 19, teal_dark)
result.set(22, 18, teal_dark)

# Cassette tape and two reels, floating within the clear window.
result.line(14, 17, 19, 17, tape)
result.line(13, 16, 14, 17, tape)
result.line(20, 16, 19, 17, tape)
for cx in (14, 20):
    result.circle(cx, 15, 3, outline, fill=True)
    result.circle(cx, 15, 2, cream, fill=True)
    result.set(cx, 13, body_dark)
    result.set(cx, 17, body_dark)
    result.set(cx-2, 15, body_dark)
    result.set(cx+2, 15, body_dark)
    result.set(cx, 15, outline)
# Central cassette label bridge.
result.rect(16, 14, 3, 3, body_light)
result.set(17, 15, tape)

# Lower speaker grille and playback status details.
result.rect(10, 22, 12, 1, outline2)
for x in (11, 14, 17, 20):
    result.set(x, 23, outline2)
result.rect(22, 22, 2, 2, outline)
result.set(22, 22, red)

# Side seam, latch, and bottom shine.
result.line(25, 8, 25, 16, outline)
result.rect(25, 11, 2, 4, outline2)
result.set(25, 12, body_light)
result.line(8, 25, 18, 25, body_light)

view(result, scale=16, margin=1, edges="all")
finish(result)
