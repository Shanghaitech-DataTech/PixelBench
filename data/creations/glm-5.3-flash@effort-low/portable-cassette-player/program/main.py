from pixelbench_api import *

c = new_canvas(32, 32, background=None, name="cassette_player")

# palette
DK   = c.color("#2b2b3a")   # dark body
BODY = c.color("#4a4a68")   # body
LT   = c.color("#6b6b90")   # body light
WIN  = c.color("#1a1a26")   # window dark
REEL = c.color("#c9c9d6")   # reels
TAPE = c.color("#7a4a2a")   # tape brown
BTN  = c.color("#d94f4f")   # red button
BTNG = c.color("#4fd97a")   # green button
BTNB = c.color("#4f7ad9")   # blue button
BTNY = c.color("#d9c14f")   # yellow
MET  = c.color("#a8a8b8")   # metal
CABL = c.color("#e8e8f0")   # cable white

# body 6..26 x 3..28
c.rect(5, 3, 22, 26, DK)
c.rect(6, 4, 20, 24, BODY)
# top highlight
c.line(6, 4, 25, 4, LT)
c.line(6, 5, 6, 27, LT)
c.line(25, 5, 25, 27, DK)

# speaker grille left
for gy in range(19, 27):
    c.line(7, gy, 11, gy, DK)

# cassette window (transparent hole in middle-top)
c.rect(8, 6, 16, 10, WIN)
# reels (transparent centers)
c.circle(12, 11, 3, REEL)
c.circle(20, 11, 3, REEL)
c.circle(12, 11, 1, None)   # transparent hub
c.circle(20, 11, 1, None)
# tape between reels
c.rect(14, 9, 4, 4, TAPE)
c.set(12, 8, MET); c.set(20, 8, MET)
c.set(12, 14, MET); c.set(20, 14, MET)
# hub teeth
c.set(12, 10, DK); c.set(11, 11, DK); c.set(12, 12, DK); c.set(13, 11, DK)
c.set(20, 10, DK); c.set(19, 11, DK); c.set(20, 12, DK); c.set(21, 11, DK)

# playback buttons bottom right
c.rect(14, 19, 2, 4, BTN)    # play
c.rect(17, 19, 2, 4, BTNG)   # stop
c.rect(20, 19, 2, 4, BTNB)   # ff
c.rect(23, 19, 2, 4, BTNY)   # rew

# volume slider right side
c.rect(24, 6, 2, 12, DK)
c.rect(24, 9, 2, 2, MET)

# headphone jack + cable
c.rect(4, 25, 2, 2, MET)
c.line(4, 27, 2, 29, CABL)
c.line(2, 29, 1, 31, CABL)
c.line(1, 31, 2, 31, CABL)

print(c.stats_text())
save("cassette_player", c)
finish(c)
