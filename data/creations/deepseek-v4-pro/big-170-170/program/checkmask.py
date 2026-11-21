from pixelbench_api import *

print('mask type', type(mask))
if mask is not None:
    print(mask.shape)
    print(mask.sum())
