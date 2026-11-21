from pixelbench_api import *

C = {
 'K':'#3a2a20',  # dark outline / pants
 'H':'#f5f2ec',  # hat
 'B':'#cfc9c0',  # hat band
 'S':'#e8b58c',  # skin
 'D':'#c99668',  # skin shadow
 'E':'#2b1d16',  # eyes
 'M':'#4a352a',  # mustache
 'W':'#ffffff',  # coat
 'A':'#e0d2b4',  # apron
 'F':'#f7f1e0',  # flour speckle
 'R':'#d9a95f',  # bamboo light
 'r':'#a97b3c',  # bamboo dark
 'U':'#f7ecd4',  # bun
 'u':'#ddc9a0',  # bun shadow
 's':'#e8b58c',  # hands (skin)
}

ROWS = [
"............HHHHHHHH............",
"...........HHHHHHHHHH...........",
"..........HHHHHHHHHHHH..........",
"..........HHHHHHHHHHHH..........",
"..........HHHHHHHHHHHH..........",
"..........BBBBBBBBBBBB..........",
"..........KSSSSSSSSSSK..........",
"..........KSEESSSSEESK..........",
"..........KSSSSDDSSSSK..........",
"..........KSMMMMMMMMSK..........",
"..........KSSSDDDDSSSK..........",
"...........KSSSSSSSSK...........",
"............KSSSSSSK............",
"........WWWWWWWssWWWWWWW........",
"......WWWWWWWWs..sWWWWWWWW......",
"......WWWWWWWW.ss.WWWWWWWW......",
".....WWWWWWWWWWWWWWWWWWWWWW.....",
".....WWWWWrrrrrrrrrrrrWWWWW.....",
".....WWWWWRRRRRRRRRRRRWWWWW.....",
".....WWWWWsUUuUUuUUuUsWWWWW.....",
".....WWWWWsUuUUUuUUUUsWWWWW.....",
".....WWWWWsuuuuuuuuuusWWWWW.....",
".....WWWWWRRRRRRRRRRRRWWWWW.....",
".....WWWWWrrrrrrrrrrrrWWWWW.....",
".....WWWWWAAAAAAAAAAAAWWWWW.....",
".....WWWWWAFAAAAAFAAAAWWWWW.....",
"......WWAAAAAAAAAAAAAAWW........",
"......WAAAAAAAAAAAAAAAAW........",
"........KKKKKKKKKKKKKK..........",
"........KKKKKK..KKKKKK..........",
"........KKKKKK..KKKKKK..........",
"........KKKKK....KKKKK..........",
]

c = new_canvas(32, 32, background=None, name="dim-sum-chef")
for y, row in enumerate(ROWS):
    assert len(row) == 32, (y, len(row))
    for x, ch in enumerate(row):
        if ch != '.':
            c.set(x, y, C[ch])

print(c.stats_text())
save("dim-sum-chef", c)
finish(c)
