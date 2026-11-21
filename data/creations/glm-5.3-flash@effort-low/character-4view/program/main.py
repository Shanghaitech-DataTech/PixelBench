from pixelbench_api import *

O  = '#2b2233'   # dark outline / eyes
SK = '#ffd9b3'   # skin
HR = '#8a4b2a'   # hair
RD = '#e63946'   # uniform red
WH = '#ffffff'   # white trim
YL = '#ffd23f'   # pom-poms
PK = '#f49ab5'   # blush

def head_front(c):
    c.circle(16, 7, 5, SK)
    c.rect(11, 2, 10, 4, HR)            # top hair
    c.rect(10, 4, 2, 5, HR)             # side locks
    c.rect(20, 4, 2, 5, HR)
    c.rect(12, 5, 8, 1, HR)             # bangs
    c.set(13, 8, O); c.set(18, 8, O)    # eyes
    c.set(13, 9, PK); c.set(18, 9, PK)  # blush
    c.set(15, 10, O); c.set(16, 10, O)  # smile

def head_back(c):
    c.circle(16, 7, 5, HR)
    c.rect(11, 2, 10, 4, HR)
    c.rect(10, 4, 2, 6, HR)
    c.rect(20, 4, 2, 6, HR)
    c.rect(14, 11, 4, 3, HR)            # ponytail
    c.set(15, 11, RD); c.set(16, 11, RD)  # tie

def head_side(c):
    c.circle(16, 7, 5, SK)
    c.rect(12, 2, 10, 4, HR)            # top hair
    c.rect(19, 4, 3, 7, HR)             # back hair
    c.rect(13, 5, 6, 1, HR)             # bangs
    c.set(12, 8, O)                     # eye
    c.set(10, 8, SK); c.set(10, 9, SK)  # nose
    c.set(11, 10, O)                    # mouth
    c.set(19, 9, PK)

def body_front(c):
    c.rect(15, 11, 2, 2, SK)            # neck
    c.rect(12, 12, 8, 5, RD)            # top
    c.rect(12, 12, 8, 1, WH)            # collar trim
    c.set(14, 14, WH); c.set(15, 15, WH); c.set(16, 14, WH)  # V
    c.line(12, 13, 9, 15, SK)           # arms
    c.line(19, 13, 22, 15, SK)
    c.circle(8, 17, 2, YL)              # pom-poms
    c.circle(23, 17, 2, YL)
    c.rect(12, 17, 8, 2, RD)            # skirt
    c.rect(10, 19, 12, 3, RD)
    for x in (12, 15, 18, 21):
        c.line(x, 19, x - 1, 21, WH)    # pleats
    c.rect(13, 22, 2, 5, SK)            # legs
    c.rect(17, 22, 2, 5, SK)
    c.rect(12, 27, 4, 2, WH)            # shoes
    c.rect(16, 27, 4, 2, WH)

def body_back(c):
    c.rect(15, 11, 2, 2, SK)
    c.rect(12, 12, 8, 5, RD)
    c.rect(12, 12, 8, 1, WH)
    c.line(12, 13, 9, 15, SK)
    c.line(19, 13, 22, 15, SK)
    c.circle(8, 17, 2, YL)
    c.circle(23, 17, 2, YL)
    c.rect(12, 17, 8, 2, RD)
    c.rect(10, 19, 12, 3, RD)
    for x in (11, 14, 17, 20):
        c.line(x, 19, x, 21, WH)
    c.rect(13, 22, 2, 5, SK)
    c.rect(17, 22, 2, 5, SK)
    c.rect(12, 27, 4, 2, WH)
    c.rect(16, 27, 4, 2, WH)

def body_side(c):
    c.rect(15, 11, 2, 2, SK)
    c.rect(13, 12, 6, 5, RD)
    c.rect(13, 12, 6, 1, WH)
    c.rect(13, 14, 6, 1, WH)
    c.line(14, 13, 10, 15, SK)          # arm forward
    c.circle(9, 17, 2, YL)
    c.rect(13, 17, 6, 2, RD)
    c.rect(12, 19, 8, 3, RD)
    c.line(15, 19, 14, 21, WH)
    c.line(18, 19, 18, 21, WH)
    c.rect(14, 22, 2, 5, SK)
    c.rect(16, 22, 2, 5, SK)
    c.rect(12, 27, 4, 2, WH)
    c.rect(16, 27, 4, 2, WH)

def sprite(head, body):
    s = new_canvas(32, 32)
    head(s); body(s)
    return s

front = sprite(head_front, body_front)
back  = sprite(head_back, body_back)
side  = sprite(head_side, body_side)

result = new_canvas(64, 64)
result.blit(front, 0, 0)
result.blit(back, 32, 0)
result.blit(side, 0, 32)
side.mirror("h")
result.blit(side, 32, 32)
result.outline(O)

print(result.stats_text())
finish(result)
