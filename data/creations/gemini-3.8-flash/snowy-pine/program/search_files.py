import os, sys

def search(dirpath, max_depth=3):
    try:
        for root, dirs, files in os.walk(dirpath):
            depth = root[len(dirpath):].count(os.sep)
            if depth > max_depth:
                continue
            for f in files:
                if 'snowy' in f.lower() or 'pine' in f.lower():
                    print("Found file:", os.path.join(root, f))
    except Exception as e:
        print("Error searching", dirpath, e)

search('..', 3)
search('/host', 4)
