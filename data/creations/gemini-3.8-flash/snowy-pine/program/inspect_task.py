import json, os

for f in ['../config.json', '../workspace.json']:
    if os.path.exists(f):
        print(f"=== {f} ===")
        with open(f) as fp:
            print(fp.read()[:1000])

for d in ['../source', '../images', '../artifacts']:
    if os.path.exists(d):
        print(f"=== {d} ===")
        print(os.listdir(d))
