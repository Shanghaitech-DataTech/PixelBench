from pixelbench_api import *

c = input_canvas

def row_runs(y, x0=0, x1=169):
    runs=[]
    prev=None
    start=x0
    for x in range(x0,x1+1):
        idx = c.get(x,y)
        if idx != prev:
            if prev is not None:
                runs.append((start,x-1,prev))
            start=x
            prev=idx
    if prev is not None:
        runs.append((start,x1,prev))
    return runs

def show(y, x0=90, x1=145):
    runs = row_runs(y,x0,x1)
    print(f'--- y={y} ---')
    for a,b,idx in runs:
        p = c.palette()[idx]
        print(f'x{a:3d}-{b:3d} idx{idx:3d} {p["name"]:6s} {p["rgba"]}')

for y in range(48, 60):
    show(y)
