from pixelbench_api import new_canvas, finish

ROWS = [
    "....gGGGGGGg....",
    "....gGooooGg....",
    "...g.obhhbo.g...",
    "..g.obhHHhbo.g..",
    ".g.obhHHHHhbo.g.",
    "..g.obbBBbbo.g..",
    "..g.oooooooo.g..",
    "..g.oo.oo.oo.g..",
    "..g.ow.ow.ow.g..",
    "..g.wo.wo.wo.g..",
    "..t.t.t.t.t.....",
    "................",
    "................",
    "................",
    "................",
    "................",
]


def build():
    c = new_canvas(16, 16, name="glow-jellyfish")
    P = {}
    P['g'] = c.color('#3b93cc59', 'glow_dim')      # faint outer glow
    P['G'] = c.color('#6fcef27d', 'glow')          # glow
    P['o'] = c.color('#081526', 'outline')         # dark outline
    P['b'] = c.color('#25678f8f', 'bell_deep')     # translucent bell, deep
    P['B'] = c.color('#4fb3e0ad', 'bell_mid')      # translucent bell, mid
    P['h'] = c.color('#9be4fbbf', 'bell_light')    # bell highlight
    P['H'] = c.color('#d4f7ffd4', 'core')          # bright glowing core
    P['w'] = c.color('#8fdcf79e', 'tentacle')      # tentacle
    P['t'] = c.color('#55aed88c', 'tentacle_dim')  # tentacle tip
    P['u'] = c.color('#9fe4f88c', 'bubble')        # tiny bubble

    for y, row in enumerate(ROWS):
        if len(row) != 16:
            raise SystemExit(f"row {y} len={len(row)}: {row}")
        for x, ch in enumerate(row):
            if ch != '.':
                c.set(x, y, P[ch])

    # a couple of ambient bubbles drifting nearby
    c.set(1, 1, P['u'])
    c.set(14, 5, P['u'])

    return c


result = build()
print(result.stats_text())
print(result.matrix_text())
finish(result)
