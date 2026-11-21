# 16x16 chibi female lab researcher, two-heads-tall
c = new_canvas(16, 16, background=None, name="researcher")

palette = {
    'h': '#26262e',  # black hair
    'H': '#4a4a58',  # hair highlight
    's': '#ffd6ad',  # skin
    'S': '#f0b98c',  # skin shade
    'e': '#7a4a1e',  # brown eyes
    'E': '#5c3410',  # brown eye shade
    'b': '#f5a88c',  # blush
    'm': '#d97f6a',  # mouth
    'w': '#f4f4f8',  # white lab coat
    'W': '#c9ccd8',  # coat shade
    't': '#6ea8e0',  # blue shirt under coat
    'p': '#3a3a55',  # dark pants
    'f': '#2e2e38',  # shoes
}

rows = [
    ".....hhhhhh.....",  # y0  hair top
    "....hHHhhhhh....",  # y1  hair + highlight
    "....hhhhhhhh....",  # y2  hair / bangs
    "....hhsssshh....",  # y3  forehead
    "....hsessesh....",  # y4  eyes (brown)
    "....hsEssEsh....",  # y5  eyes, darker lower row
    "....hbsmmsbh....",  # y6  blush + mouth
    ".....hssssh.....",  # y7  chin
    "....hwwSSwwh....",  # y8  neck + coat collar
    "...whwwttwwhw...",  # y9  shoulders, shirt V
    "...whwwttwwhw...",  # y10 arms + torso
    "...shwwwwwwhs...",  # y11 hands, coat
    "....wwwwwwww....",  # y12 coat hem
    ".....pp..pp.....",  # y13 legs
    "....fff..fff....",  # y14 shoes
    "................",  # y15
]

for y, row in enumerate(rows):
    for x, ch in enumerate(row):
        if ch != '.':
            c.set(x, y, palette[ch])

view(c)
finish(c)
