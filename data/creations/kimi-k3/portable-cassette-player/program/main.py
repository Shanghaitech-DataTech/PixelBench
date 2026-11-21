# 32x32 portable cassette player (Walkman-style), front-facing icon
c = new_canvas(32, 32, name="walkman")

OUT   = c.color('#1d2129')  # outline / dark detail
MAIN  = c.color('#4c566a')  # body
DARK  = c.color('#3b4252')  # body shade
LIGHT = c.color('#6d7b93')  # body highlight
FRAME = c.color('#242933')  # window frame
INNER = c.color('#2b303b')  # cassette interior
REEL  = c.color('#eceff4')  # tape reels
TAPE  = c.color('#7a4f33')  # magnetic tape
GLASS = c.color('#ffffff42')  # window glare (semi transparent)
GRAY  = c.color('#8a94a6')  # button face
GRAYD = c.color('#6b7484')
ORAN  = c.color('#d08770')  # play button
ORAND = c.color('#b06950')
RED   = c.color('#bf616a')  # stop button
REDD  = c.color('#9d4e56')
KNOB  = c.color('#ebcb8b')  # volume knob
SILV  = c.color('#d8dee9')  # headphone plug
GREEN = c.color('#a3be8c')  # LED

# --- body: rounded outline + fill + shading ---
c.line(6, 5, 21, 5, OUT)
c.line(5, 6, 22, 6, OUT)
c.rect(4, 7, 20, 20, OUT)
c.line(5, 27, 22, 27, OUT)
c.line(6, 28, 21, 28, OUT)
c.rect(5, 7, 18, 20, MAIN)
c.rect(5, 7, 18, 1, LIGHT)   # top highlight
c.rect(5, 8, 1, 18, DARK)    # left shade
c.rect(22, 8, 1, 18, LIGHT)  # right highlight
c.rect(5, 26, 18, 1, DARK)   # bottom shade
c.set(6, 8, OUT); c.set(21, 8, OUT)  # screws

# --- cassette window with two reels ---
c.rect(7, 9, 14, 9, FRAME)
c.rect(8, 10, 12, 7, INNER)
c.line(8, 16, 19, 16, TAPE)              # tape along the bottom
c.circle(10, 13, 2, REEL)
c.circle(17, 13, 2, REEL)
for cx in (10, 17):                      # hubs + spokes
    c.set(cx, 13, OUT); c.set(cx - 1, 13, OUT); c.set(cx + 1, 13, OUT)
    c.set(cx, 12, OUT); c.set(cx, 14, OUT)
c.line(15, 10, 19, 10, GLASS)            # glass glare

# --- stripe + power LED ---
c.line(7, 19, 13, 19, LIGHT)
c.set(20, 19, GREEN)

# --- playback controls: rewind, play, next, stop ---
def btn(x, face, faced):
    c.rect(x, 21, 3, 4, face)
    c.rect(x, 24, 3, 1, faced)

btn(6, GRAY, GRAYD); btn(10, ORAN, ORAND); btn(14, GRAY, GRAYD); btn(18, RED, REDD)
c.line(6, 21, 6, 23, OUT); c.line(8, 21, 8, 23, OUT); c.set(7, 22, OUT)      # |<
c.line(10, 21, 10, 23, OUT); c.set(11, 22, OUT)                              # >
c.line(14, 21, 14, 23, OUT); c.set(15, 22, OUT); c.line(16, 21, 16, 23, OUT) # >|
c.rect(18, 21, 2, 2, OUT)                                                    # stop

# --- volume dial on the right edge ---
c.circle(25, 18, 2, OUT)
c.circle(25, 18, 1, KNOB)
c.set(25, 17, OUT)  # pointer notch

# --- headphone plug + cable out the top ---
c.rect(7, 2, 4, 3, OUT)
c.rect(8, 3, 2, 1, SILV)
c.path("M 8 2 Q 9 0 11 1 T 14 1 Q 16 0 18 1 T 22 0", OUT)  # coiled cord off-frame

view(c)
finish(c)
