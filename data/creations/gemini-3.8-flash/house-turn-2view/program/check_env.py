import os
print("Current dir files:", os.listdir('.'))
if os.path.exists('..'):
    print("Parent dir files:", os.listdir('..'))
# Check if reference or reference_frames exist in globals
print("Globals containing 'ref':", [k for k in globals().keys() if 'ref' in k.lower()])
print("Globals containing 'mask':", [k for k in globals().keys() if 'mask' in k.lower()])
