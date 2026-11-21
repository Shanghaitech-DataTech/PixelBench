from pixelbench_api import *

S = {0:'.', 1:'#', 2:'l', 3:'w', 4:'t', 5:'L', 6:'r', 7:'b', 8:'M', 9:'P', 10:'g',
     11:'n', 12:'p', 13:'p', 14:'m', 15:'G', 16:'o', 17:'d', 18:'c', 19:'B', 20:'y',
     21:'D', 22:'Y', 23:'T', 24:'s', 25:'W', 26:'e', 27:'N', 28:'S', 29:'R', 30:'O',
     31:'Z', 32:'E', 33:'V', 34:'U', 35:'u', 36:'v', 37:'Q', 38:'K', 39:'k', 40:'X', 41:'z'}

c = input_canvas
if len(c.stats()["size"]) and False:
    pass
f2 = canvas("frame2")
w, h = f2.stats()["size"]
pal = f2.palette()
bg = pal[0]["rgba"]
for y in range(h):
    line = []
    for x in range(w):
        i = f2.get(x, y)
        if i == 0:
            line.append('.')
        else:
            rgba = tuple(pal[i]["rgba"])
            # map to the same letters by matching against input palette
            matched = False
            for j, e in enumerate(c.palette()):
                if tuple(e["rgba"]) == rgba:
                    line.append(S.get(j, '?'))
                    matched = True
                    break
            if not matched:
                line.append('*')
    print(f"{y:2d}|{''.join(line)}")
print("  |" + "".join(str(x % 10) for x in range(w)))
