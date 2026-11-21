result = new_canvas(48, 48, name='magic_staff')
c = result
ink='#291c30'
dark='#493044'
wood='#754239'
mid='#a46143'
light='#d28c56'
gold='#efbb75'
# Tapered, gently irregular wooden shaft.
c.poly([(27,17),(31,20),(27,26),(24,29),(21,34),(17,38),(14,43),(11,46),(8,44),(9,40),(13,35),(16,32),(19,27),(23,23)],ink)
c.poly([(27,19),(29,21),(25,27),(22,31),(19,35),(15,40),(12,44),(10,44),(11,40),(15,35),(19,30),(21,26),(25,22)],wood)
c.poly([(26,21),(28,21),(24,27),(21,31),(17,36),(14,41),(11,43),(12,39),(16,34),(20,29),(22,25)],mid)
c.line(25,22,22,26,light)
c.line(20,30,16,35,light)
c.line(14,38,11,42,light)
c.line(25,26,23,29,dark)
c.line(19,34,16,38,dark)
c.set(10,43,gold)
# Broad carved crook with an open centre.
c.path('M 27 22 L 24 18 Q 22 13 25 8 L 29 4 Q 34 1 39 4 L 42 7 Q 45 12 41 16 L 38 18 L 35 16 L 35 13 L 37 13 L 39 11 L 38 8 L 35 7 L 31 8 L 29 11 L 29 15 L 32 19 L 30 23 Z',ink)
c.path('M 27 20 L 25 17 Q 24 13 26 9 L 30 5 Q 34 3 38 5 L 41 8 L 42 11 L 40 15 L 38 16 L 36 15 L 36 14 L 38 14 L 40 11 L 39 8 L 35 6 L 31 7 L 28 10 L 27 14 L 29 18 L 30 20 L 29 22 Z',wood)
c.path('M 26 17 L 25 14 L 27 9 L 31 5 L 35 4 L 38 5 L 41 8 L 41 11 L 40 12 L 39 8 L 35 6 L 31 7 L 28 10 L 27 14 L 28 18 Z',mid)
c.line(26,12,27,9,light)
c.line(28,8,31,5,light)
c.line(32,5,35,4,gold)
c.line(36,5,38,6,light)
c.set(40,8,light)
c.line(25,15,27,18,light)
c.line(29,18,30,20,dark)
c.line(39,15,41,13,dark)
c.set(38,15,mid)
# Grain and a knot in the wood.
c.line(29,7,27,10,wood)
c.set(26,13,gold)
c.line(33,5,35,5,wood)
c.set(28,19,gold)
c.set(17,35,wood)
c.set(16,36,gold)
# Amethyst bindings around the neck, with warm metal rims.
c.poly([(24,23),(26,21),(30,24),(28,27)],ink)
c.line(25,22,29,25,gold)
c.line(24,24,27,26,'#77518c')
c.line(25,24,27,25,'#bc84ce')
c.line(23,26,27,28,ink)
c.line(23,25,27,28,'#c88d62')
c.set(24,25,gold)
# Small dangling charm.
c.line(28,27,29,30,dark)
c.line(29,30,28,33,'#bb825c')
c.poly([(28,32),(30,34),(28,37),(26,35)],ink)
c.poly([(28,33),(29,34),(28,36),(27,35)],'#9a52d0')
c.set(28,34,'#f4c7ff')
# Floating faceted violet core in the crook.
c.poly([(32,9),(35,10),(36,13),(33,16),(30,14),(30,12)],'#4b245f')
c.poly([(32,10),(34,10),(35,13),(33,15),(31,13)],'#a45ae1')
c.poly([(32,10),(33,10),(33,12),(31,13)],'#f5d2ff')
c.poly([(33,12),(35,12),(33,15)],'#713bb4')
c.set(33,13,'#ca88f2')
# Discrete, crisp particles; the gaps remain transparent.
def spark(x,y,col,bright):
    c.line(x-1,y,x+1,y,col)
    c.line(x,y-2,x,y+2,col)
    c.set(x,y,bright)
spark(21,6,'#a467d3','#f4d9ff')
spark(42,22,'#9353c6','#ecc3ff')
spark(20,19,'#9a59cf','#e8b9ff')
c.set(44,10,'#bd80e7')
c.set(44,11,'#75439e')
c.set(37,22,'#bd80e7')
c.set(36,24,'#75439e')
c.set(17,12,'#75439e')
c.set(23,2,'#be8be2')
c.set(32,2,'#8251a6')
c.set(32,28,'#b177d9')
view(result)
finish(result)
