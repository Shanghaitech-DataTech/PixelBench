from pixelbench_api import *

D='#efe9e7'; A='#3a3737'; B='#b7b3b2'; C='#827c7c'; E='#d6b39d'; F='#bc8b6d'; G='#cdae67'

# ---------- Frame 1: original content, centred on a 30x28 canvas ----------
f1 = new_canvas(30, 28, name='frame1')
f1.blit(input_canvas, 2, 0)

# ---------- Frame 2: mid-leap rabbit ----------
f2 = new_canvas(30, 28, name='frame2')

# silhouette (all white, merged)
f2.ellipse(13,14,8,5,D)                       # body, stretched horizontally
f2.circle(7,14,4,D)                           # rump / thigh
f2.circle(19,13,4,D)                          # chest / shoulder
f2.circle(23,8,3,D)                           # head
f2.rect(25,7,3,3,D)                           # muzzle
f2.circle(3,11,2,D)                           # tail puff
f2.poly([(19,6),(13,4),(15,2),(21,5)], D)     # back ear, swept back
f2.poly([(21,6),(17,4),(19,2),(23,5)], D)      # front ear, swept back
f2.poly([(8,17),(2,19),(1,21),(4,22),(10,19)], D)   # hind leg trailing back
f2.poly([(19,16),(26,17),(28,19),(26,20),(18,18)], D) # front legs reaching forward

f2.outline(A)                                 # dark outline like the original

# details
f2.set(17,4,E); f2.set(18,4,E); f2.set(19,4,E)      # inner ear
f2.set(24,7,A)                                # eye
f2.set(27,8,G); f2.set(27,9,G)                # nose
f2.line(9,18,17,18,B)                         # belly shading
f2.line(3,20,6,19,B)                          # hind-leg shading
f2.line(21,17,25,18,B)                        # front-leg separation
f2.set(2,10,B)                                # tail shading

view(f1)
view(f2)

finish([f1, f2])
