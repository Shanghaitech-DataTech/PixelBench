from pixelbench_api import *

print("globals:", [k for k in globals().keys() if not k.startswith('_')])
try:
    print("reference:", reference)
except:
    print("no reference")
