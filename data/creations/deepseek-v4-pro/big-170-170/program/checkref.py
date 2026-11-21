from pixelbench_api import *

print('reference exists:', 'reference' in dir())
try:
    r = reference
    print('reference type', type(r))
    if r is not None:
        print(r.stats_text())
except Exception as e:
    print('err', e)
print('mask?', 'mask' in dir())
