from pixelbench_api import *

O  = '#241a1f'   # dark outline
S  = '#f2c69e'   # skin
SD = '#d9a077'   # skin shade
H  = '#5a3320'   # hair
HL = '#7d4b2a'   # hair highlight
W  = '#ffffff'
R  = '#c0392b'   # mouth interior
T  = '#2f6f6b'   # outfit
TD = '#22504d'   # outfit shade
Y  = '#e8b64c'   # accent

def face(c, ox, oy, emo):
    def px(x, y, col): c.set(ox+x, oy+y, col)
    def rect(x, y, w, h, col): c.rect(ox+x, oy+y, w, h, col)
    # neck
    rect(13, 22, 6, 6, S)
    px(13, 22, SD); px(19, 22, SD)
    # head
    c.ellipse(ox+16, oy+14, 9, 10, S)
    c.ellipse(ox+16, oy+14, 9, 10, O, fill=False)
    # ears
    rect(6, 14, 2, 4, S); rect(24, 14, 2, 4, S)
    px(6, 14, O); px(7, 17, SD)
    px(25, 14, O); px(24, 17, SD)
    # hair cap
    rect(7, 3, 18, 6, H)
    c.ellipse(ox+16, oy+5, 9, 4, H)
    # fringe: per-column bottom
    fringe = {7:11,8:12,9:11,10:11,11:11,12:11,13:11,14:11,15:12,
              16:12,17:11,18:11,19:11,20:11,21:11,22:11,23:12,24:11,25:12}
    for x, fy in fringe.items():
        rect(x, 9, 1, fy-8, H)
    # side locks
    rect(6, 6, 2, 11, H); rect(24, 6, 2, 11, H)
    px(6, 16, O); px(6, 17, O); px(25, 16, O); px(25, 17, O)
    px(7, 18, O); px(24, 18, O)
    px(8, 19, O); px(23, 19, O)
    px(9, 20, O); px(22, 20, O)
    px(10, 21, O); px(21, 21, O)
    px(11, 22, O); px(20, 22, O)
    px(12, 23, O); px(19, 23, O)
    px(13, 24, O); px(18, 24, O)
    px(14, 25, O); px(17, 25, O)
    px(15, 26, O); px(16, 26, O)
    px(14, 26, O); px(17, 26, O)
    px(13, 25, O); px(18, 25, O)
    px(12, 24, O); px(19, 24, O)
    px(11, 23, O); px(20, 23, O)
    px(10, 22, O); px(21, 22, O)
    px(9, 21, O); px(22, 21, O)
    px(8, 20, O); px(23, 20, O)
    px(7, 19, O); px(24, 19, O)
    px(6, 18, O); px(25, 18, O)
    px(5, 17, O); px(26, 17, O)
    px(5, 16, O); px(26, 16, O)
    px(4, 15, O); px(27, 15, O)
    px(4, 14, O); px(27, 14, O)
    px(3, 13, O); px(28, 13, O)
    px(3, 12, O); px(28, 12, O)
    px(2, 11, O); px(29, 11, O)
    px(2, 10, O); px(29, 10, O)
    px(2, 9, O); px(29, 9, O)
    px(2, 8, O); px(29, 8, O)
    px(3, 7, O); px(28, 7, O)
    px(4, 6, O); px(27, 6, O)
    px(5, 5, O); px(26, 5, O)
    px(6, 4, O); px(25, 4, O)
    px(8, 3, O); px(23, 3, O)
    px(10, 2, O); px(21, 2, O)
    px(12, 1, O); px(19, 1, O)
    px(14, 0, O); px(17, 0, O)
    px(15, 0, O); px(16, 0, O)
    # hair outline top
    for x in range(7, 26): px(x, 3, O)
    px(6, 6, O); px(25, 6, O)
    px(6, 7, O); px(25, 7, O)
    # highlight
    for x, y in [(10,5),(11,4),(12,4),(20,5),(21,5),(9,6),(22,6)]:
        px(x, y, HL)
    # eyebrows + eyes + mouth per emotion
    if emo == 'calm':
        for x in range(10, 14): px(x, 13, O)
        for x in range(18, 22): px(x, 13, O)
        for x in range(10, 13): px(x, 16, O)
        for x in range(19, 22): px(x, 16, O)
        for x in range(13, 20): px(x, 20, O)
    elif emo == 'smiling':
        for x, y in [(9,12),(10,11),(11,11),(12,12),(18,12),(19,11),(20,11),(21,12)]:
            px(x, y, O)
        for x in range(10, 13): px(x, 15, O)
        for x in range(19, 22): px(x, 15, O)
        px(10, 16, O); px(12, 16, O); px(19, 16, O); px(21, 16, O)
        px(11, 15, W); px(20, 15, W)
        px(9, 18, SD); px(23, 18, SD)  # blush-ish
        smile = [(12,19),(13,20),(14,20),(15,21),(16,21),(17,21),(18,20),(19,20),(20,19)]
        for x, y in smile: px(x, y, O)
        px(14, 20, R); px(15, 20, R); px(16, 20, R); px(17, 20, R)
        px(15, 21, R); px(16, 21, R)
    elif emo == 'angry':
        for i in range(5):
            px(9+i, 12+i//2, O)
            px(23-i, 12+i//2, O)
        for x in range(10, 13): px(x, 16, O)
        for x in range(19, 22): px(x, 16, O)
        px(12, 15, O); px(20, 15, O)
        frown = [(13,21),(14,20),(15,20),(16,20),(17,20),(18,20),(19,21)]
        for x, y in frown: px(x, y, O)
    else:  # surprised
        for x in range(9, 14): px(x, 11, O)
        for x in range(18, 23): px(x, 11, O)
        for x, y in [(10,14),(11,14),(12,14),(10,15),(12,15),(10,16),(11,16),(12,16),(10,17),(11,17),(12,17)]:
            px(x, y, O)
        px(11, 15, W); px(11, 16, W)
        for x, y in [(20,14),(21,14),(22,14),(20,15),(22,15),(20,16),(21,16),(22,16),(20,17),(21,17),(22,17)]:
            px(x, y, O)
        px(21, 15, W); px(21, 16, W)
        c.ellipse(ox+16, oy+20, 1, 2, O)
        px(16, 20, R)
    # outfit
    rect(3, 28, 26, 4, T)
    rect(3, 28, 26, 1, O)
    # shoulders slope
    px(4, 27, T); px(5, 27, T); px(26, 27, T); px(27, 27, T)
    px(4, 27, O); px(27, 27, O)
    px(6, 27, T); px(25, 27, T)
    # collar
    px(13, 28, O); px(19, 28, O)
    for i in range(3):
        px(14+i, 28+i, TD)
        px(17-i, 28+i, TD)
    px(14, 28, O); px(18, 28, O)
    px(16, 28, Y); px(16, 29, Y)

c = new_canvas(64, 64, background=None, name='emotions')
face(c, 0, 0, 'calm')
face(c, 32, 0, 'smiling')
face(c, 0, 32, 'angry')
face(c, 32, 32, 'surprised')
print(c.stats_text())
print(c.matrix_text(region=(0,0,31,31)))
finish(c)
