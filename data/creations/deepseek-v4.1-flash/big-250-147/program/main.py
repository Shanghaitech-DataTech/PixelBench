import numpy as np
from statistics import median

src = input_canvas
W, H = src.stats()['size']
pal = {p['index']: p['rgba'] for p in src.palette()}

arr = np.zeros((H, W, 3), float)
for y in range(H):
    for x in range(W):
        r, g, b, a = pal[src.get(x, y)]
        arr[y, x] = (r, g, b)

R, G, B = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
lum = 0.299 * R + 0.587 * G + 0.114 * B

result = input_canvas.copy(name="output")

try:
    # ---------- 1. locate the sky / horizon line ----------
    raw = np.empty(W, int)
    for x in range(W):
        col = lum[:, x]
        s = 120
        for y in range(0, H - 4):
            if col[y] < 70 and col[y:y + 5].max() < 95:
                s = y
                break
        raw[x] = s
    sl = np.empty(W, int)
    for x in range(W):
        sl[x] = int(median(raw[max(0, x - 3):x + 4]))
    sl = np.clip(sl, 8, 118)

    ys = np.arange(H)[:, None] * np.ones((1, W), int)
    sky = ys < sl[None, :]
    # bright warm halo just under the detected line still belongs to the sky
    spill = (ys < (sl[None, :] + 16)) & (lum > 135) & (B > G + 4) & (R > G + 25)
    sky = sky | spill

    # ---------- 2. blank out the sun (and any bright cloud) ----------
    def dil(m, it=1):
        for _ in range(it):
            p = np.pad(m, 1, mode='edge')
            m = (p[1:-1, 1:-1] | p[:-2, 1:-1] | p[2:, 1:-1] | p[1:-1, :-2] |
                 p[1:-1, 2:] | p[:-2, :-2] | p[:-2, 2:] | p[2:, :-2] | p[2:, 2:])
        return m

    valid = sky & (lum <= 172)          # ordinary sky pixels = donor material
    take = dil(sky & (lum > 168), 2) & sky
    filled = lum.copy()
    remaining = take.copy()
    for off in (72, -72, 144, -144, 40, -40, 200, -200):
        if not remaining.any():
            break
        idx = np.clip(np.arange(W) + off, 0, W - 1)
        ok = remaining & valid[:, idx]
        if ok.any():
            filled[ok] = lum[:, idx][ok]
        remaining = remaining & ~ok
    if remaining.any():
        for y in range(H):
            m = valid[y]
            if m.any() and remaining[y].any():
                filled[y, remaining[y]] = float(np.median(lum[y, m]))
    remaining = remaining & sky
    filled[remaining] = 126.0

    # ---------- 3. paint a clear noon sky ----------
    hor = np.maximum(sl.astype(float), 10.0)
    t = np.clip(ys / hor[None, :], 0.0, 1.0) ** 0.85
    ts = np.array([0.0, 0.55, 1.0])
    stop = [(66, 126, 198), (128, 182, 227), (203, 232, 246)]
    skycol = np.stack([np.interp(t, ts, [c[i] for c in stop]) for i in range(3)],
                      axis=-1)

    noise = np.clip((filled - 128.0) / 30.0, -1.0, 1.0)
    kpos = np.clip(noise, 0.0, 1.0)[..., None]
    kneg = np.clip(-noise, 0.0, 1.0)[..., None]
    white = np.array([238.0, 248.0, 253.0])
    skycol = skycol * (1.0 - 0.30 * kpos) + white * (0.30 * kpos)
    skycol = skycol * (1.0 - 0.16 * kneg)

    # ---------- 4. gentle noon lighting on the landscape ----------
    grayv = lum[..., None] * np.ones((1, 1, 3))
    land = 0.85 * arr + 0.15 * grayv
    land[..., 0] *= 0.94
    land[..., 1] *= 0.975
    land[..., 2] *= 1.07
    land *= 0.985

    new = np.where(sky[..., None], skycol, land)
    new = np.clip(np.round(new / 4.0) * 4.0, 0, 252)

    idx_of = {}
    for y in range(H):
        for x in range(W):
            key = (int(new[y, x, 0]), int(new[y, x, 1]), int(new[y, x, 2]))
            result.set(x, y, key)
    print("edit applied, sky pixels:", int(sky.sum()), "sun pixels removed:", int(take.sum()))
    print("bright sky left (lum>200):", int((sky & (new[:, :, 0] * 0.299 + new[:, :, 1] * 0.587 + new[:, :, 2] * 0.114 > 200)).sum()))
except Exception as e:
    print("EDIT FAILED:", repr(e))

print(result.stats_text())
