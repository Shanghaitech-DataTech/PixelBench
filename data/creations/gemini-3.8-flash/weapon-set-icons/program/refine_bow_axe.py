from pixelbench_api import *
from generate_icons import build_palette, paste_ascii

# Refined Bow ASCII (32x32)
bow_ascii = [
#01234567890123456789012345678901
"................................", # 0
"................................", # 1
".........................kk.....", # 2
"........................kwhlk...", # 3
".......................khlskk...", # 4
"......................kYjlsok...", # 5
"....................kkTYgkok....", # 6
"...................kTTtbook.....", # 7
".................kkTTtbok.......", # 8
"................kTTtbukok.......", # 9
"...............kTtbbuk.ok.......", # 10
"..............kTtbuko...ok......", # 11
".............kTtbuko.....ok.....", # 12
"............kjYuko........ok....", # 13
"...........kGYasko.........ok...", # 14
"....kk....kgaekooo..........ok..", # 15
"..khwhkkkkgaekwtCok..........ok.", # 16
"....kk....kgaekooo..........ok..", # 17
"...........kGYasko.........ok...", # 18
"............kjYuko........ok....", # 19
".............kTtbuko.....ok.....", # 20
"..............kTtbuko...ok......", # 21
"...............kTtbbuk.ok.......", # 22
"................kTTtbukok.......", # 23
".................kkTTtbok.......", # 24
"...................kTTtbook.....", # 25
"....................kkTYgkok....", # 26
"......................kYjlsok...", # 27
".......................khlskk...", # 28
"........................kwhlk...", # 29
".........................kk.....", # 30
"................................", # 31
]

# Let's fix the arrow in bow_ascii:
# Arrow runs horizontally at row 16:
# Arrowhead from x=3 to x=8
# Shaft from x=9 to x=22
# Fletching at x=19..23
# String crosses at x=18: string is at (18, 16)
# Let's hand-craft rows 14-18 of the bow:
bow_rows_center = {
    14: "...........kGYaskoo........ok...",
    15: "...kk.....kgaekooo.ok.......ok..",
    16: ".kwhhlskkkkgaetttttYcoCko....ok.",
    17: "...kk.....kgaekooo.ok.......ok..",
    18: "...........kGYaskoo........ok..."
}
for r, text in bow_rows_center.items():
    bow_ascii[r] = text


# Refined Axe ASCII (32x32)
# Fully connecting left blade to the socket, making a massive double-bitted axe!
axe_ascii = [
#01234567890123456789012345678901
"..........................kk....", # 0
".........................kwk....", # 1
"........................khlsk...", # 2
".......................khlmssk..", # 3
"...........kkk........khlmssk...", # 4
".........kkhwhk......kGgYjYgk...", # 5
"........khhlmmsk....kGvVpYjYgk..", # 6
".......khlmmsssskk.kGrvVpYjYgk..", # 7
"......khlmmssssSsskkGYjrRpgkkkkk", # 8
".....khlmssssSssmskkGgYgkkshhlwk", # 9
"....khlmssssSssmsk.kYjGk..kssmml", # 10
"....khmssssSssmsk.kjYgk...kSssml", # 11
"....kwhmssSssmsk..kYjGk....kSssm", # 12
".....khlmsssssk..kaeLk.....kSssm", # 13
"......kkhlsssk..kaeLk......kSssm", # 14
"........kkkkk.kTaGLk.......kSssm", # 15
".............kTaGLk.......kSssml", # 16
"............kTaGLk.......kssmmlh", # 17
"...........kTaGLk.......kGshhlwk", # 18
"..........kTaGLk........kkkkkk..", # 19
".........kTaGLk.................", # 20
"........kTaGLk..................", # 21
".......kTaGLk...................", # 22
"......kTaGLk....................", # 23
".....kTaGLk.....................", # 24
"....kYjYjGk.....................", # 25
"...kjvVpYk......................", # 26
"..kGjrRvYk......................", # 27
"..kwhGgGkk......................", # 28
"..khwhkk........................", # 29
"...kkhk.........................", # 30
"....kk..........................", # 31
]

c = new_canvas(64, 64)
pal = build_palette(c)

from preview_all import draw_sword, draw_shield
draw_sword()
draw_shield()

paste_ascii(c, 32, 0, bow_ascii, pal)
paste_ascii(c, 32, 32, axe_ascii, pal)

view(c)
