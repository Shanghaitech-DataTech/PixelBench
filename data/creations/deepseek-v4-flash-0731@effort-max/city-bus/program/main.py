from pixelbench_api import new_canvas, finish

c = new_canvas(64, 32)

OUT = c.color("#22303C")   # dark outline
BODY = c.color("#F2F6FA") # body base
ROOF = c.color("#D7E1EA") # roof
GLASS = c.color("#9BD1F0")# window glass
SIGF = c.color("#3A4450") # sign frame
SIGN = c.color("#151A22") # sign panel
TXT  = c.color("#FF453A") # route text
STRIPE = c.color("#2E86DE")
SKIRT = c.color("#7B93A8")
HEAD = c.color("#FFE066")
TAIL = c.color("#E23B3B")
TIRE = c.color("#14171C")
HUB  = c.color("#9AA7B3")
DOT  = c.color("#3E4A55")
AC   = c.color("#46545F")
ACV  = c.color("#2F3A42")

# roof AC unit
c.rect(28, 6, 10, 2, AC)
for vx in (31, 33, 35):
    c.rect(vx, 6, 1, 2, ACV)
c.rect(6, 8, 53, 1, ROOF)

# body shell
c.rect(4, 9, 57, 18, OUT, fill=False)
c.rect(5, 10, 55, 16, BODY)

# front electronic route display "10"
c.rect(49, 9, 12, 5, SIGF, fill=False)
c.rect(50, 10, 10, 3, SIGN)
c.rect(51, 10, 1, 3, TXT)          # "1"
c.rect(54, 10, 3, 1, TXT)          # "0"
c.rect(54, 11, 1, 1, TXT)
c.rect(56, 11, 1, 1, TXT)
c.rect(54, 12, 3, 1, TXT)

# row of side windows with pillars
c.rect(12, 10, 34, 7, GLASS)
for px in (19, 26, 33, 40):
    c.rect(px, 10, 1, 7, BODY)
c.rect(48, 14, 13, 4, OUT, fill=False)  # windshield frame
c.rect(48, 14, 13, 4, GLASS)
c.line(4, 17, 60, 17, OUT)          # header under glass

# front and rear doors (front = right)
c.rect(5, 18, 6, 6, BODY)
c.rect(5, 18, 6, 3, GLASS)
c.line(8, 18, 8, 23, OUT)
c.rect(50, 18, 7, 6, BODY)
c.rect(50, 18, 7, 3, GLASS)
c.line(53, 18, 53, 23, OUT)
c.line(4, 24, 57, 24, OUT)          # door bottoms

# side stripe and skirt
c.rect(12, 19, 36, 1, STRIPE)
c.rect(12, 20, 36, 6, SKIRT)

# lights
c.rect(59, 22, 2, 2, HEAD)          # headlight
c.rect(4, 13, 3, 3, TAIL)           # taillight

# two wheels
for cx in (13, 49):
    c.circle(cx, 27, 3, TIRE)
    c.circle(cx, 27, 1, HUB)
    c.circle(cx, 27, 0, DOT)

print(c.stats_text())
print(c.matrix_text())
finish(c)
