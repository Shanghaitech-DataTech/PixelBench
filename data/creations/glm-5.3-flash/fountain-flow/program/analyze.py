c = input_canvas
W, H = c.stats()['size']
pal = {p['index']: p['rgba'] for p in c.palette()}

def hexv(idx):
    rgba = pal.get(idx)
    return None if rgba is None else '#%02x%02x%02x%02x' % tuple(rgba)

WATER = {'#1d8baaff', '#2ec7dcff'}
GREY = {'#413e51ff', '#b9ab90ff', '#645d72ff', '#ffffffff', '#e1e2baff', '#a58d8bff'}
GOLD = {'#492d1cff', '#593904ff', '#c19000ff', '#e7d906ff', '#8a5c01ff'}

def spans(chars):
    """given list of category chars for a row, return spans per category"""
    out = {}
    for target in 'WGS':
        runs = []
        start = None
        for i, ch in enumerate(chars):
            if ch == target and start is None:
                start = i
            elif ch != target and start is not None:
                runs.append((start, i - 1))
                start = None
        if start is not None:
            runs.append((start, len(chars) - 1))
        out[target] = runs
    return out

for y in range(H):
    row = []
    for x in range(W):
        idx = c.get(x, y)
        if idx is None:
            row.append('.')
        else:
            hv = hexv(idx)
            row.append('W' if hv in WATER else ('G' if hv in GOLD else ('S' if hv in GREY else '?')))
    s = spans(row)
    sil = s['W'] + s['G'] + s['S']
    lo = min(r[0] for r in sil) if sil else '-'
    hi = max(r[1] for r in sil) if sil else '-'
    print(f"{y:2d} sil={lo:2d}-{hi:2d}  W={s['W']}  S={s['S']}")
