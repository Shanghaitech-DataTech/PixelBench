from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32, name="cassette-player")

BODY = c.color("#3f5270")
BODY_HL = c.color("#5d7296")
BODY_DK = c.color("#2a3852")
INK = c.color("#0f1520")
WIN_B = c.color("#aebdd4")
REEL = c.color("#1d2940")
REEL_L = c.color("#6b7f9e")
HUB = c.color("#e8eef7")
TAPE = c.color("#6b5940")
GLYPH = c.color("#e8eef7")
CABLE = c.color("#1b2330")
JACK = c.color("#9fb0c8")
JACK_L = c.color("#d7e0ec")

# --- body (rounded rect) ---
body = "M 4,3 H 27 A 3 3 0 0 1 30,6 V 25 A 3 3 0 0 1 27,28 H 4 A 3 3 0 0 1 1,25 V 6 A 3 3 0 0 1 4,3 Z"
c.path(body, BODY, fill=True)
c.path(body, INK, fill=False)

# --- subtle shading bands ---
c.rect(3,5,26,1, BODY_HL)
c.rect(3,5,1,1, BODY_HL)   # small left accent
c.rect(3,27,26,1, BODY_DK)

# --- transparent cassette window (x4..21, y7..16) ---
c.rect(4, 7, 18, 10, WIN_B, fill=False)
c.clear(5, 8, 16, 8)          # window interior fully transparent
c.rect(5, 9, 16, 7, TAPE)     # tape behind reels
c.circle(8, 11, 3, REEL)
c.circle(16, 11, 3, REEL)
c.circle(8, 11, 3, REEL_L, fill=False)
c.circle(16, 11, 3, REEL_L, fill=False)
c.circle(8, 11, 1, HUB)
c.circle(16, 11, 1, HUB)

# --- playback controls ---
c.poly([(8, 20), (5, 22), (8, 24)], GLYPH)      # rewind
c.poly([(11, 20), (8, 22), (11, 24)], GLYPH)     # rewind
c.poly([(14, 19), (18, 21), (14, 23)], GLYPH)    # play
c.rect(20, 19, 3, 3, GLYPH)                      # stop

# --- volume dial (right) ---
c.circle(27, 13, 3, WIN_B, fill=False)
c.rect(26, 11, 3, 3, GLYPH)                      # knob

# --- headphone cable & plug (top) ---
c.rect(14, 0, 4, 3, JACK)     # plug body x14..17 y0..2
c.rect(15, 0, 2, 1, JACK_L)   # plug tip
c.line(15, 3, 16, 3, CABLE)   # cable enters player

print(c.stats_text())
finish(c)
