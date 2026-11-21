from pixelbench_api import *

out = input_canvas.copy(name='output')

# ---- register colours ----
robe   = out.color((46,36,60))
robe_hi= out.color((64,52,82))
robe_sh= out.color((28,22,40))
hood   = out.color((20,16,30))
glow_c = out.color((240,255,224))
glow_m = out.color((176,232,178))
glow_o = out.color((96,176,124))
glow_w = out.color((120,200,140))
wood   = out.color((96,70,37))
vine_d = out.color((22,52,40))
vine_l = out.color((46,104,66))
vine_h = out.color((74,148,92))
vine_x = out.color((30,72,52))

def rectcols(c,x0,x1,y,colour):
    for x in range(x0,x1+1):
        c.set(x,y,colour)

rows = [
    (166, 37,37, hood),
    (167, 36,38, hood),
    (168, 35,39, hood),
    (169, 34,40, hood),
    (170, 35,39, hood),
    (171, 36,38, hood),
    (172, 37,38, robe_sh),
    (173, 34,40, robe),
    (174, 33,42, robe),
    (175, 32,44, robe),
    (176, 31,45, robe),
    (177, 31,45, robe),
    (178, 31,45, robe),
    (179, 31,45, robe),
    (180, 31,45, robe),
    (181, 31,45, robe),
    (182, 32,44, robe),
    (183, 32,44, robe),
    (184, 33,43, robe),
    (185, 33,43, robe),
    (186, 34,42, robe),
    (187, 34,42, robe),
    (188, 34,42, robe),
    (189, 35,41, robe),
    (190, 35,41, robe),
    (191, 36,40, robe),
    (192, 36,40, robe),
    (193, 36,40, robe),
    (194, 37,39, robe_sh),
]
for (y,x0,x1,colour) in rows:
    rectcols(out,x0,x1,y,colour)

for (y,x,c) in [
    (176,34,robe_sh),(176,42,robe_hi),(177,34,robe_sh),(177,42,robe_hi),
    (178,34,robe_sh),(178,42,robe_hi),(179,35,robe),(179,41,robe_hi),
    (180,35,robe),(180,41,robe),(181,35,robe),(181,41,robe),
    (182,36,robe),(182,40,robe),(183,36,robe),(183,40,robe),
    (184,37,robe),(185,37,robe),(186,38,robe),(187,38,robe),
    (184,39,robe_hi),(185,40,robe_hi),(186,39,robe_hi),
]:
    out.set(x,y,c)

for (y,x) in [(178,30),(179,30),(180,30),(181,31),(182,31),(183,32),(184,33)]:
    out.set(x,y,robe_hi)

for y in range(163,191):
    out.set(46,y,wood)
out.set(45,181,robe)
out.set(45,182,robe_hi)
out.set(45,183,robe)
out.set(45,180,robe_hi)
out.set(44,179,robe_hi)
out.set(44,180,robe_hi)

for (y,x0,x1,c) in [
    (156,45,47,glow_w),(157,44,48,glow_o),(158,43,49,glow_m),
    (159,43,49,glow_c),(160,43,49,glow_c),(161,44,48,glow_m),
    (162,45,47,glow_o),(163,46,46,glow_w),
]:
    for x in range(x0,x1+1):
        out.set(x,y,c)

def vine(c,x,top,bot,colour):
    rr=[colour,vine_d]
    for y in range(top,bot+1):
        c.set(x,y,rr[y%2])
def leaf(c,x,y):
    if y%2==0:
        c.set(x,y,vine_h); c.set(x+1,y,vine_l)
    else:
        c.set(x,y,vine_l); c.set(x-1,y,vine_d)

for (x,top,bot) in [(27,150,214),(29,156,206),(25,160,198)]:
    vine(out,x,top,bot,vine_x)
    for yy in range(top+2,bot,7):
        leaf(out,x,yy)
for (x,top,bot) in [(50,148,216),(53,154,210),(55,160,204)]:
    vine(out,x,top,bot,vine_x)
    for yy in range(top+2,bot,7):
        leaf(out,x,yy)

# inspect
pal = out.palette()
def namech(px):
    col = pal[px] if px is not None and px<len(pal) else None
    if not col: return ' '
    r,g,b,a=col['rgba']
    if a==0: return ' '
    if (r,g,b)==(46,36,60): return 'R'
    if (r,g,b)==(64,52,82): return 'r'
    if (r,g,b)==(28,22,40): return 'D'
    if (r,g,b)==(20,16,30): return 'H'
    if (r,g,b)==(240,255,224): return 'C'
    if (r,g,b)==(176,232,178): return 'M'
    if (r,g,b)==(96,176,124): return 'o'
    if (r,g,b)==(120,200,140): return 'w'
    if (r,g,b)==(96,70,37): return 'W'
    if (r,g,b)==(22,52,40): return 'v'
    if (r,g,b)==(46,104,66): return 'V'
    if (r,g,b)==(74,148,92): return '+'
    if (r,g,b)==(30,72,52): return 'x'
    return '.'
finish(out)
