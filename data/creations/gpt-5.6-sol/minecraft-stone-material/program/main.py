from pixelbench_api import *

# 16x16 seamless Minecraft-like stone material tile
c = new_canvas(16, 16, background="#777b7a", name="stone_tile")

# restrained stone palette: 8 visible colors total
base = "#777b7a"
dark = "#4f5554"
darker = "#3d4342"
light = "#929694"
light2 = "#a6aaa7"
mid = "#686d6c"
chip = "#b7bbb7"
shadow = "#5b605f"

# Subtle blocky mottling, deliberately touching borders for seamless repetition
for x,y,w,h,col in [
    (1,1,2,1,mid),(5,0,2,1,light),(10,1,2,1,shadow),(14,0,2,2,mid),
    (0,4,2,2,light),(3,3,1,2,shadow),(7,2,2,1,light2),(12,4,2,2,mid),
    (1,7,2,1,shadow),(5,6,2,2,light),(9,7,2,1,mid),(14,6,2,2,light),
    (0,10,2,2,mid),(3,9,2,1,light2),(7,10,2,2,shadow),(11,9,2,1,light),
    (14,11,2,2,mid),(1,14,2,2,light),(5,13,2,1,shadow),(9,14,2,1,light2),
    (12,13,2,2,shadow),(15,15,1,1,light),
]: c.rect(x,y,w,h,col)

# Small angular mineral flecks
for x,y,col in [(4,1,light2),(8,4,chip),(13,2,light),(2,5,dark),(6,4,shadow),
                (15,4,chip),(4,8,mid),(8,8,light2),(12,7,dark),(2,11,light),
                (6,12,chip),(10,11,shadow),(4,15,mid),(8,13,light),(13,15,light2)]:
    c.set(x,y,col)

# Pixel cracks: dark channels with a few lit lower lips, with border endpoints matched
# upper/left network
c.line(0,2,2,2,dark)
c.line(2,2,3,4,dark)
c.line(3,4,5,5,darker)
c.set(4,5,shadow)
c.line(15,2,14,3,dark)
c.line(14,3,13,5,dark)
c.line(13,5,11,6,darker)
c.set(12,6,shadow)
# central branching crack; x=5 joins the matching bottom-edge endpoint
c.line(5,0,6,2,darker)
c.line(6,2,6,4,darker)
c.line(6,4,7,6,darker)
c.line(7,6,9,7,darker)
c.line(9,7,9,9,dark)
c.line(9,9,8,11,darker)
c.line(8,11,6,12,dark)
c.line(6,12,5,14,dark)
c.set(5,15,dark)
# right/lower network; opposite side crossings share y=8 and y=13
c.line(15,8,13,9,darker)
c.line(13,9,12,11,dark)
c.line(12,11,13,13,dark)
c.line(13,13,15,13,darker)
c.line(0,8,1,9,darker)
c.line(1,9,2,11,dark)
c.line(0,13,2,13,darker)
c.line(2,13,3,12,darker)
c.line(3,12,4,10,dark)
# crack highlights / chipped rim
for x,y in [(3,3),(5,4),(14,4),(10,7),(8,10),(7,12),(4,11),(12,10),(14,13)]:
    c.set(x,y,light)

view(c, scale=24, margin=0, edges="none")
finish(c)
