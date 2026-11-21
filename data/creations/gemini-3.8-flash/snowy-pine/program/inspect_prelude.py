import json

with open('../config.json') as f:
    cfg = json.load(f)
    print("Prelude:\n", cfg.get('prelude', ''))

with open('../workspace.json') as f:
    ws = json.load(f)
    out0 = ws['outputs'][0]
    import numpy as np
    arr = np.array(out0['canvas'])
    print("out0 canvas shape:", arr.shape)
    print("unique values in out0 canvas:", np.unique(arr))
    print("count of values:", {v: int(np.sum(arr == v)) for v in np.unique(arr)})
