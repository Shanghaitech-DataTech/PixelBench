from pixelbench_api import *

f1 = input_canvas.copy(name="f1")
f2 = input_canvas.copy(name="f2")

# ============ 1. erase raised hammer, handle, arm ============
er = [(16,0,14,8),
      (24,8,6,1),(25,9,6,1),(24,10,10,1),(26,11,9,1),(28,12,8,1),
      (29,13,8,1),(30,14,7,1),(30,15,8,1),(30,16,9,1),(30,17,11,1),
      (30,18,13,1),(29,19,14,1),(28,20,15,1),(28,21,9,1),(38,21,5,1)]
for x,y,w,h in er:
    f2.rect(x,y,w,h,None)

# ============ 2. left foot steps forward (left 2, down 2) ============
DX,DY = -2,2
src = {}
for y in range(43,53):
    for x in range(11,18):
        src[(x,y)] = f2.get(x,y)
pal = {p['index']: p['rgba'] for p in f2.palette()}
def transparent(idx):
    v = pal[idx]
    if isinstance(v,str):
        v = v.lstrip('#')
        if len(v)==8: return int(v[6:8],16)==0
        return False
    return v[3]==0
SHADOW = 41  # c40 #17003599 ground shadow
def skip(idx):
    return idx==SHADOW or transparent(idx)
for (x,y),idx in src.items():
    if not skip(idx):
        f2.set(x,y,None)
for (x,y),idx in src.items():
    if not skip(idx):
        f2.set(x+DX,y+DY,idx)
# patch the hole left behind
f2.rect(11,43,7,2,'c7')      # dark tunic-shade band under belly
f2.rect(16,45,2,5,'c7')      # gap between legs
f2.rect(16,50,2,3,'c40')     # ground shadow

# ============ 3. arm swung down across body ============
f2.line(29,24,25,32,'c0')
f2.line(30,24,26,32,'c0')
f2.line(31,24,27,32,'c0')
f2.line(30,24,26,32,'c14')
f2.set(30,25,'c4'); f2.set(29,26,'c4'); f2.set(28,28,'c4'); f2.set(27,30,'c4')

# ============ 4. hammer slammed down front-left ============
f2.poly([(31,30),(29,28),(11,44),(13,46)],'c0')        # handle outline
f2.line(29,29,12,45,'c9')                              # gold core
f2.poly([(11,50),(15,47),(10,42),(6,45)],'c0')         # head outline
f2.poly([(11,49),(14,47),(7,45),(10,43)],'c4')         # head face
f2.line(10,43,14,47,'c1')                              # lit face
f2.line(7,46,10,49,'c3')                               # shaded face
# fist gripping the handle
f2.rect(24,31,5,5,'c0')
f2.rect(25,32,3,3,'c14')
f2.set(26,32,'c4'); f2.set(25,33,'c4')

# ============ 5. white motion trail ============
f2.path("M 24 4 C 11 3 4 9 2 21 C 1 31 4 42 9 47",'c30',fill=False)
f2.path("M 24 6 C 14 5 6 11 4 21 C 3 29 6 39 12 45",'#ffffff78',fill=False)
# impact ticks
f2.set(5,48,'c30'); f2.set(4,46,'c30'); f2.set(12,51,'c30')

# re-erase sky shadow cells + add upper trail arc + impact dust
f2.rect(3,53,1,1,None)
f2.rect(36,53,2,1,None)
f2.rect(34,54,1,1,None)
f2.rect(30,56,1,1,None)
f2.path("M 27 3 C 15 2 8 7 6 17",'#ffffff50',fill=False)
f2.set(14,51,'#ffffff99'); f2.set(6,52,'#ffffff66'); f2.set(11,53,'#ffffff50')
f2.set(7,47,'c30')

view(f1, scale=6)
view(f2, scale=6)
finish([f1,f2])
