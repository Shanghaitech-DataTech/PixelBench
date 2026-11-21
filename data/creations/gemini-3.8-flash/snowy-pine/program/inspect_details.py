import json

with open('../config.json') as f:
    cfg = json.load(f)
    print("config keys:", cfg.keys())
    # print keys and types
    for k, v in cfg.items():
        if k != 'prelude':
            print(k, type(v), str(v)[:200])

with open('../workspace.json') as f:
    ws = json.load(f)
    print("workspace keys:", ws.keys())
    for k, v in ws.items():
        print(k, type(v))
        if k == 'outputs':
            print("outputs len:", len(v))
            for i, o in enumerate(v):
                print(f"output[{i}] keys:", o.keys())
