import numpy as np
c = input_canvas
w,h,rgba = c.to_rgba()
a = np.array(rgba).reshape(h,w,4)

# Find pixels of distinctive warm colors (character / machine)
warm = ((a[:,:,0].astype(int) - a[:,:,2].astype(int)) > 30)
ys,xs = np.nonzero(warm)
print('warm bbox', xs.min(), xs.max(), ys.min(), ys.max(), warm.sum())

# cluster by connected region roughly: print row ranges
import collections
# print column histogram of warm pixels
colcount = warm.sum(axis=0)
rowcount = warm.sum(axis=1)
print('cols with warm:', [i for i,v in enumerate(colcount) if v>0][:200])
print('rows with warm:', [i for i,v in enumerate(rowcount) if v>0])
