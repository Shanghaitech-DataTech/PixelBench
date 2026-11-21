from pixelbench_api import *

exec(open('main.py').read().split('print(out.stats_text())')[0])

name = {0:'.',1:'W',2:'K',3:'D',4:'R',5:'F',6:'G',7:'H',8:'I',9:'S',10:'J',11:'L',12:'M',
        13:'N',14:'O',15:'P',16:'Q',17:'R',18:'$',19:'t',20:'u',21:'v',22:'a',23:'b',
        24:'c',25:'d',26:'e',27:'f',28:'*',29:'%',30:'g',31:'C',32:'B'}
print("=== staff region x=38..50 ===")
for y in range(12, 58):
    row = "".join(name[out.get(x, y)] for x in range(38, 51))
    print(f"{y:2d} " + row)
print("   " + "".join(str(x % 10) for x in range(38, 51)))
print("g=GEM_L C=GEM_M B=GEM_D *=gold_l %=gold_m")
