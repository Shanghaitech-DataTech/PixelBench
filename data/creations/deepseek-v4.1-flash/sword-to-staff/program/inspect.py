from pixelbench_api import *

c = input_canvas
name = {0:'.',1:'W',2:'K',3:'D',4:'R',5:'F',6:'G',7:'H',8:'I',9:'S',10:'J',11:'L',12:'M',
        13:'N',14:'O',15:'P',16:'Q',17:'R',18:'$',19:'t',20:'u',21:'v',22:'a',23:'b',
        24:'c',25:'d',26:'e',27:'f'}
for y in range(10, 59):
    runs = []
    prev = None
    start = None
    for x in range(20, 52):
        ch = name[c.get(x, y)]
        if ch != prev:
            if prev is not None:
                runs.append(f"{prev}:{start}-{x-1}")
            prev = ch
            start = x
    runs.append(f"{prev}:{start}-51")
    print(f"{y:2d} " + "  ".join(runs))
