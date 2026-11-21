import numpy as np
c = input_canvas
w,h,rgba = c.to_rgba()
a = np.frombuffer(rgba, dtype=np.uint8).reshape(h,w,4)[:,:,:3].astype(float)
for y in range(0, h, 7):
    row = ""
    for x in range(0, w, 7):
        blk = a[y:y+7, x:x+7]
        r,g,b = blk.mean(axis=(0,1))
        lum = 0.3*r+0.6*g+0.1*b
        if b>r+15 and b>g+10: ch='B'
        elif g>r+10 and g>b+10: ch='G'
        elif r>g+20 and r>b+20: ch='R'
        elif lum>170: ch='W'
        elif lum>110: ch='+'
        elif lum>60: ch='o'
        else: ch='#'
        row += ch
    print(f"{y:3d} {row}")
