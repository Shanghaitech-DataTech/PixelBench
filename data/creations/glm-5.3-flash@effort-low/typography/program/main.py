from pixelbench_api import *

c = new_canvas(64, 64, background="#101830", name="title")

# subtle dithered sky
c.dither(0, 0, 64, 64, ["#101830", "#141d3a"], pattern="bayer4")

# border frame
c.rect(0, 0, 64, 64, "#3a4a7a", fill=False)
c.rect(1, 1, 62, 62, "#1c2750", fill=False)

# stars
for (x, y) in [(8,6),(20,4),(33,7),(45,5),(55,9),(6,20),(57,22),(10,44),(54,46),(16,54),(48,55),(31,58)]:
    c.set(x, y, "#cfd8ff")

def outlined_text(x, y, s, main, outline, shadow=None):
    if shadow:
        c.text(x+1, y+1, s, shadow, font="8px")
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]:
        c.text(x+dx, y+dy, s, outline, font="8px")
    c.text(x, y, s, main, font="8px")

# PIXEL — large, gold, outline + drop shadow
outlined_text(12, 12, "PIXEL", "#ffd23f", "#5a3208", "#000000")

# QUEST — smaller weight via darker teal, with shadow
outlined_text(12, 30, "QUEST", "#7fe0ff", "#0b3a55", "#000000")

# decorative rule with diamonds
c.line(10, 44, 26, 44, "#ffd23f")
c.line(38, 44, 54, 44, "#ffd23f")
c.set(28, 44, "#ffd23f"); c.set(27,44,"#b8860b"); c.set(29,44,"#b8860b")
c.set(35, 44, "#ffd23f"); c.set(34,44,"#b8860b"); c.set(36,44,"#b8860b")
c.set(28, 43, "#fff2a8"); c.set(35, 43, "#fff2a8")

# PRESS START hint
c.text(0, 48, "PRESS", "#9aa7d0", font="5x7")
c.text(21, 48, "START", "#9aa7d0", font="5x7")
c.set(16, 54, "#9aa7d0"); c.set(17, 54, "#9aa7d0"); c.set(18, 54, "#9aa7d0")
c.set(45, 54, "#9aa7d0"); c.set(46, 54, "#9aa7d0"); c.set(47, 54, "#9aa7d0")

print(c.stats_text())
finish(c)
