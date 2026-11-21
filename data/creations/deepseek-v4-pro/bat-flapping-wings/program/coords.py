from pixelbench_api import *

c = input_canvas
names = {0:'.',1:'k',2:'b',3:'p',4:'P',5:'g',6:'r',7:'y',8:'m'}
for y in range(22):
    line = []
    for x in range(27):
        i = c.get(x,y)
        if i:
            line.append(f"{x}:{names[i]}")
    print(f"y{y:02d}: " + " ".join(line))
