from collections import Counter
p={e['index']:e['rgba'] for e in input_canvas.palette()}
for idx in range(1,72):
    pts=[(x,y) for y in range(147) for x in range(250) if input_canvas.get(x,y)==idx]
    if pts:
        print(idx,p[idx][:3],len(pts),(min(x for x,y in pts),min(y for x,y in pts),max(x for x,y in pts),max(y for x,y in pts)))
for y in [0,15,40,50,53,56,60,64,68,72,76,80,84,90,100,110,120,135]:
    print('ROW',y,Counter(input_canvas.get(x,y) for x in range(250)).most_common(15))
# Region analysis: sky dominant in cyan, cloud tones in blue, sun in yellow,
# distant mountain families in gray, forest in green.
m=new_canvas(250,147)
for y in range(147):
    for x in range(250):
        idx=input_canvas.get(x,y)
        r,g,b,a=p[idx]
        if idx==1 or idx==6: co='#52c7f5'
        elif idx<71: co='#fee6a5' if g>145 else '#5583c1'
        elif b>r*0.6: co='#a6a8bb'
        else: co='#456c47'
        m.set(x,y,co)
view(m,scale=3,margin=0)
view(input_canvas.select(0,45,250,65).preview(),scale=4,margin=0)
