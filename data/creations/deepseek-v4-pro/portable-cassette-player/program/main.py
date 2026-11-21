c = new_canvas(32, 32, name="portable-cassette-player")

# palette
cable = c.color("#1a1d20", "cable")
plug_silver = c.color("#c6cbd0", "plug_silver")
plug_dark = c.color("#2a2e33", "plug_dark")
body = c.color("#aeb6be", "body")
body_outline = c.color("#3d434a", "body_outline")
body_highlight = c.color("#d4d9dd", "body_highlight")
window_frame = c.color("#2e3338", "window_frame")
reel = c.color("#24282c", "reel")
hub = c.color("#cfd4d8", "hub")
tape = c.color("#4a3a30", "tape")
btn = c.color("#4a5056", "btn")
glyph = c.color("#eef0f2", "glyph")
play_green = c.color("#43b87a", "play_green")
vol = c.color("#6e767e", "vol")
vol_ridge = c.color("#3a4046", "vol_ridge")

# headphone cable + jack plug at top
c.rect(15, 0, 2, 3, cable)          # cable
c.rect(13, 2, 5, 4, plug_silver)    # plug body
c.rect(13, 3, 5, 1, plug_dark)      # ring
c.rect(13, 5, 5, 1, plug_dark)      # tip/base

# body: rounded rectangle x4..27, y6..30
body_path = "M 7 6 L 24 6 Q 27 6 27 9 L 27 27 Q 27 30 24 30 L 7 30 Q 4 30 4 27 L 4 9 Q 4 6 7 6 Z"
c.path(body_path, body, fill=True)
c.path(body_path, body_outline, fill=False)
c.line(7, 7, 24, 7, body_highlight)  # subtle top highlight

# transparent cassette window + frame
win_path = "M 10 10 L 21 10 Q 23 10 23 12 L 23 17 Q 23 19 21 19 L 10 19 Q 8 19 8 17 L 8 12 Q 8 10 10 10 Z"
c.path(win_path, None, fill=True)      # cut transparent hole
c.path(win_path, window_frame, fill=False)

# two tape reels connected by tape
c.line(14, 14, 17, 14, tape)
c.circle(12, 14, 2, reel)
c.circle(19, 14, 2, reel)
c.set(12, 14, hub)
c.set(19, 14, hub)

# playback controls
c.rect(7, 23, 5, 5, btn)
c.rect(13, 23, 5, 5, btn)
c.rect(19, 23, 5, 5, btn)
c.poly([(11, 24), (11, 27), (9, 25)], glyph)   # rewind
c.poly([(9, 24), (9, 27), (7, 25)], glyph)
c.poly([(13, 24), (13, 27), (17, 25)], play_green)  # play
c.poly([(19, 24), (19, 27), (21, 25)], glyph)  # fast-forward
c.poly([(21, 24), (21, 27), (23, 25)], glyph)

# volume thumbwheel on right side
c.circle(28, 20, 3, vol)
c.line(27, 18, 27, 22, vol_ridge)
c.line(28, 18, 28, 22, vol_ridge)
c.line(29, 18, 29, 22, vol_ridge)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31)))
finish(c)
