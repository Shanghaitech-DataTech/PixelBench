from pixelbench_api import *
import random

c = new_canvas(128, 128, name="alley")

P = {
    'sky0': '#04050b', 'sky1': '#05070f', 'sky2': '#070b16', 'sky3': '#0a0f1e',
    'sky4': '#0e1526', 'sky5': '#131c30', 'skyh': '#1a1c34',
    'rain': '#7f9cbf', 'rainh': '#b8d4f0',
    'wallb': '#141528', 'wallb_d': '#0c0e1c',
    'interior': '#ffca66', 'deep': '#ffb84d', 'dframe': '#ff2d95', 'dglow': '#a83a78',
    'bldg_l': '#07080f', 'bldg_le': '#0a0b14', 'bldg_r': '#0b0912',
    'win': '#ffca66', 'winc': '#4ec8d8',
    'pink': '#ff2d95', 'pinkg': '#ff9cc8',
    'cyan': '#00f0ff', 'cyang': '#8af6ff',
    'yel': '#ffe600', 'yelg': '#fff2a8',
    'cable': '#000205',
    'asph': '#08080e', 'asph2': '#0e0f18',
    'pud': '#1a2030', 'pudl': '#2a3452',
    'rp': '#e06ca8', 'rc': '#44c4e8', 'ry': '#d8c878', 'rw': '#9aa8c8',
    'poolp': '#2c2038', 'poolc': '#202c40',
    'vm': '#22262f', 'vmf': '#3a3f4d', 'vms': '#0d1320', 'vmr': '#ff3840',
    'vmb': '#2d5cff', 'vmw': '#e8ecf8', 'vmb2': '#10141f',
    'fig': '#05060a', 'figr': '#1c2333',
    'roof': '#0a0814',
    'umb': '#a8c4e0', 'umbr': '#eaf4ff', 'rib': '#6a84a8', 'stick': '#39404f',
    'grate': '#1e2434', 'mh': '#202836',
}

def glowtext(x, y, s, core, glow):
    for dx in (-1, 1):
        c.text(x + dx, y, s, glow)
        c.text(x, y + dx, s, glow)
    c.text(x, y, s, core)

# ---------------- sky ----------------
for y0, y1, k in [(0, 16, 'sky0'), (16, 32, 'sky1'), (32, 48, 'sky2'),
                 (48, 64, 'sky3'), (64, 80, 'sky4'), (80, 104, 'sky5')]:
    c.rect(0, y0, 128, y1 - y0, P[k])
c.rect(42, 16, 44, 20, P['skyh'])
# rooftop silhouettes on the side buildings
c.rect(2, 0, 10, 5, P['roof'])
c.rect(18, 0, 12, 4, P['roof'])
c.rect(6, 0, 2, 6, P['roof'])
c.circle(25, 0, 3, P['roof'], False)
c.rect(88, 0, 12, 6, P['roof'])
c.rect(104, 0, 8, 10, P['roof'])
c.rect(112, 0, 2, 7, P['roof'])

# ---------------- back building / dead-end wall ----------------
c.rect(42, 30, 44, 70, P['wallb'])
c.rect(42, 92, 44, 12, P['wallb_d'])
c.rect(44, 38, 5, 5, P['winc'])
c.rect(76, 50, 5, 5, P['win'])

# BAR neon sign
c.rect(50, 40, 28, 20, P['wallb_d'])
glowtext(58, 41, "BAR", P['yel'], P['yelg'])

# glowing doorway
c.rect(53, 79, 22, 22, P['dglow'])
c.rect(56, 82, 16, 18, P['dframe'])
c.rect(58, 84, 12, 16, P['interior'])
c.rect(60, 90, 8, 10, P['deep'])
c.rect(48, 104, 32, 4, P['poolp'])

# ---------------- side buildings ----------------
# left wall
c.rect(0, 0, 42, 104, P['bldg_l'])
c.rect(34, 0, 8, 104, P['bldg_le'])
c.rect(30, 6, 8, 54, P['wallb_d'])
c.rect(31, 7, 6, 10, P['pink'])
c.rect(31, 21, 6, 10, P['pink'])
c.rect(31, 35, 6, 10, P['cyan'])
c.rect(31, 49, 6, 10, P['cyan'])
c.rect(4, 62, 26, 18, P['wallb_d'])
glowtext(8, 64, "NOIR", P['pink'], P['pinkg'])
for (wx, wy, wc) in [(15, 14, P['win']), (6, 28, P['winc']), (24, 42, P['win']),
                     (6, 56, P['winc']), (24, 14, P['winc']), (15, 42, P['win'])]:
    c.rect(wx, wy, 5, 4, wc)

# right wall
c.rect(86, 0, 42, 104, P['bldg_r'])
c.rect(86, 0, 6, 104, P['bldg_le'])
c.rect(88, 10, 34, 22, P['wallb_d'])
glowtext(90, 14, "SUSHI", P['cyan'], P['cyang'])
c.circle(116, 58, 11, P['pinkg'], False)
c.circle(116, 58, 9, P['pink'], False)
c.rect(88, 76, 30, 20, P['wallb_d'])
glowtext(90, 78, "CAFE", P['yel'], P['yelg'])
for (wx, wy, wc) in [(92, 22, P['win']), (112, 38, P['win']), (102, 52, P['winc']),
                     (92, 64, P['win'])]:
    c.rect(wx, wy, 5, 4, wc)

# ---------------- power cables ----------------
c.path("M -2 6 Q 32 30 64 20 Q 96 10 130 14", P['cable'], False)
c.path("M -2 12 Q 30 38 64 28 Q 98 16 130 22", P['cable'], False)
c.path("M 30 -2 Q 48 18 64 12 Q 84 8 100 -2", P['cable'], False)
c.line(66, 20, 66, 30, P['cable'])
c.rect(62, 28, 8, 6, P['pinkg'])
c.rect(63, 29, 6, 4, P['pink'])

# ---------------- ground ----------------
c.rect(0, 104, 128, 24, P['asph'])
c.rect(0, 110, 128, 1, P['asph2'])
c.rect(0, 116, 128, 1, P['asph2'])
c.rect(0, 124, 128, 1, P['asph2'])

# center puddle + neon reflections
c.ellipse(64, 117, 22, 5, P['pud'])
c.ellipse(64, 117, 15, 3, P['pudl'])
c.rect(56, 114, 2, 8, P['rp'])
c.rect(60, 115, 2, 7, P['rp'])
c.rect(64, 116, 2, 6, P['rw'])
c.rect(68, 115, 2, 7, P['ry'])
c.rect(72, 114, 2, 8, P['rp'])

# left puddle
c.ellipse(22, 119, 12, 4, P['pud'])
c.ellipse(22, 119, 7, 3, P['pudl'])
c.rect(18, 117, 2, 5, P['rc'])
c.rect(26, 118, 2, 4, P['rc'])
c.rect(22, 116, 2, 4, P['rw'])

# right puddle
c.ellipse(100, 118, 11, 4, P['pud'])
c.ellipse(100, 118, 7, 3, P['pudl'])
c.rect(96, 116, 2, 5, P['rp'])
c.rect(104, 117, 2, 4, P['rc'])
c.rect(100, 115, 2, 5, P['rw'])

# manhole + grate
c.ellipse(82, 121, 7, 2, P['mh'], False)
c.rect(44, 124, 38, 2, P['grate'])

# ---------------- vending machines ----------------
# left machine (warm/red light)
c.rect(12, 100, 22, 6, P['pinkg'])
c.rect(14, 101, 18, 5, P['vmr'])
c.rect(14, 106, 18, 18, P['vm'])
c.rect(16, 107, 14, 8, P['vms'])
c.rect(18, 108, 10, 2, P['vmb'])
c.rect(21, 110, 4, 2, P['vmr'])
c.rect(16, 116, 14, 4, P['vmf'])
c.rect(17, 117, 3, 2, P['vmw'])
c.rect(20, 117, 4, 2, P['vmr'])
c.rect(24, 117, 2, 2, P['vmb'])
c.rect(14, 122, 18, 2, P['vmb2'])

# right machine (cyan top, "24H")
c.rect(92, 103, 20, 4, P['cyang'])
c.rect(94, 104, 18, 3, P['cyan'])
c.rect(94, 107, 20, 17, P['vm'])
c.rect(96, 109, 16, 10, P['vms'])
glowtext(99, 110, "24H", P['vmr'], P['pinkg'])
c.rect(96, 120, 16, 3, P['vmf'])
c.rect(97, 121, 4, 2, P['vmw'])
c.rect(101, 121, 3, 2, P['vmb'])
c.rect(104, 121, 2, 2, P['vmr'])
c.rect(94, 122, 20, 2, P['vmb2'])

# ---------------- figure with transparent umbrella ----------------
# umbrella: glassy dome, ribs, stick
c.path("M 48 88 Q 64 66 80 88 Z", P['umb'], True)
c.path("M 48 88 Q 64 66 80 88", P['umbr'], False)
for rx, ry in [(52, 86), (58, 88), (70, 88), (76, 86)]:
    c.line(64, 77, rx, ry, P['rib'])
c.line(64, 77, 64, 94, P['stick'])

# body silhouette
c.circle(64, 89, 3, P['fig'])
c.rect(58, 94, 12, 18, P['fig'])
c.rect(59, 112, 4, 12, P['fig'])
c.rect(65, 112, 4, 12, P['fig'])
c.rect(57, 122, 7, 4, P['fig'])
c.rect(64, 122, 7, 4, P['fig'])
# rim light on the figure
c.line(58, 95, 58, 110, P['figr'])
c.line(69, 96, 69, 108, P['rp'])
c.line(66, 95, 69, 95, P['figr'])

# ---------------- rain ----------------
rng = random.Random(7)
for i in range(360):
    x = rng.randint(0, 126)
    y = rng.randint(0, 126)
    cc = P['rainh'] if rng.random() < 0.18 else P['rain']
    c.set(x, y, cc)
    if rng.random() < 0.55:
        c.set(x + 1, y + 1, cc)

# bright droplets near the door glow
for (x, y) in [(54, 90), (70, 84), (50, 72), (76, 92), (58, 70)]:
    c.set(x, y, P['rainh'])

# glow-catching droplets on the umbrella dome
for (x, y) in [(56, 80), (64, 76), (71, 81), (50, 83), (77, 83), (68, 73), (60, 73)]:
    c.set(x, y, P['rainh'])

print(c.stats_text())
print("palette size:", len(c.palette()))

finish(c)
