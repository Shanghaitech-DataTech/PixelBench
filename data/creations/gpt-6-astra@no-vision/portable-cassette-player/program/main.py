c = new_canvas(32, 32, name='cassette_player')
# Restrained cool casing, warm controls and ivory reel hubs.
ink = '#172639'
dark = '#263e50'
shadow = '#38596a'
blue = '#4e8192'
mid = '#78aab4'
light = '#b9d8d7'
white = '#e5eee0'
glass = '#203947'
glint = '#628795'
tape = '#a16b47'
orange = '#e99b4f'
# Headphone lead loops around the upper and right edges.
c.path('M22 7 L22 3 Q22 1 25 1 L27 1 Q30 1 30 5 L30 18 Q30 21 28 22', ink, fill=False)
c.line(29,5,29,17,shadow)
c.rect(21,4,3,4,ink)
c.rect(22,4,1,2,light)
c.rect(21,6,3,2,dark)
# Single earpiece on the free end of the cord.
c.rect(27,21,2,4,ink)
c.rect(26,24,4,4,ink)
c.rect(26,24,3,2,mid)
c.rect(27,26,2,2,shadow)
# Stepped, front-facing chassis with a shallow right edge.
c.rect(5,6,18,1,ink)
c.rect(3,7,22,22,ink)
c.rect(4,29,20,1,ink)
c.rect(25,9,1,18,ink)
c.rect(4,8,20,20,blue)
c.rect(5,7,18,1,light)
c.rect(4,8,1,19,mid)
c.rect(5,28,18,1,shadow)
c.rect(24,9,1,18,shadow)
c.line(23,9,23,27,mid)
# Top fascia: ridged volume slider and small printed marks.
c.rect(6,8,8,3,dark)
c.line(7,9,12,9,ink)
c.rect(9,8,3,3,light)
c.line(10,8,10,10,white)
c.set(7,8,shadow)
c.rect(16,9,5,1,light)
c.set(21,9,orange)
# Cassette window bevel and transparent smoked glass.
c.rect(5,12,18,11,ink)
c.rect(6,12,16,1,shadow)
c.rect(6,13,16,9,glass)
c.line(6,22,21,22,light)
c.line(22,13,22,21,mid)
# Cassette shell visible through the window.
c.rect(7,14,14,6,shadow)
c.rect(8,13,12,1,glint)
c.rect(8,20,12,1,dark)
c.line(10,19,18,19,tape)
c.line(11,18,17,18,ink)
# Two tape spools, with bright ring rims and toothed dark centres.
for x in (10,18):
    c.circle(x,16,3,ink)
    c.circle(x,16,2,light)
    c.set(x-1,15,white)
    c.set(x,16,ink)
    c.set(x-1,16,dark)
    c.set(x+1,16,dark)
    c.set(x,15,dark)
    c.set(x,17,dark)
c.rect(13,15,3,3,dark)
c.line(13,18,15,18,tape)
# Small glass reflections kept away from the reels.
c.line(6,14,8,12,glint)
c.line(19,21,21,19,glint)
# Lower fascia transport buttons.
c.rect(6,24,16,3,shadow)
c.rect(6,24,5,3,orange)
c.set(7,24,white)
c.poly([(8,24),(10,25),(8,27)],ink)
c.rect(12,24,4,3,light)
c.rect(13,25,2,2,dark)
c.rect(17,24,5,3,light)
c.line(18,25,18,26,dark)
c.line(20,25,20,26,dark)
# Case screws and small bottom edge slots.
c.set(5,10,white)
c.set(5,27,ink)
c.set(22,27,ink)
c.line(8,28,11,28,dark)
c.line(15,28,19,28,dark)
print(c.stats_text())
print(c.matrix_text())
save('portable_cassette_player', c)
finish(c)
