from pixelbench_api import finish, new_canvas

W = H = 64
c = new_canvas(W, H)

C = {
    'ceiling': '#e3edf6', 'fixture': '#fbfdff', 'housing': '#c3d5e6',
    'wall': '#b2c3d5', 'wall_d': '#97abbf', 'base': '#73869a',
    'floor': '#8d9bab', 'floor_l': '#9cabba', 'ftile': '#748495',
    'machine': '#eef2f5', 'mshade': '#c1cbd4', 'outline': '#2b333d',
    'glass': '#8fc8e0', 'glass_d': '#4d8db2', 'hl': '#e9f9ff',
    'panel': '#45515e', 'panel_d': '#2f3944', 'led': '#59a6e8',
    'btn': '#63c07a', 'btn_r': '#d2534f',
    'clockf': '#f5f7f9', 'clockr': '#39424c', 'clockh': '#2a3038', 'clkred': '#cf5562',
    'bask': '#c78c3c', 'baskd': '#8a5c22', 'baskr': '#6f4a1a',
    'c_red': '#c95050', 'c_blue': '#497fbf', 'c_gre': '#6cae63',
    'c_yel': '#ddc05a', 'c_pin': '#d081ad', 'c_whi': '#e8eef2',
    'tbl': '#d7dde2', 'tbld': '#a7b0b9', 'leg': '#5b6671', 'shad': '#5f6f80',
}
idx = {n: c.color(h, name=n) for n, h in C.items()}

# --- room shell ---
c.rect(0, 0, 64, 8, idx['ceiling'])
c.rect(4, 2, 24, 3, idx['housing'])
c.rect(6, 3, 20, 1, idx['fixture'])
c.rect(36, 2, 24, 3, idx['housing'])
c.rect(38, 3, 20, 1, idx['fixture'])
c.rect(0, 8, 64, 36, idx['wall'])
c.rect(0, 8, 2, 36, idx['wall_d'])
c.rect(62, 8, 2, 36, idx['wall_d'])
c.rect(0, 42, 64, 2, idx['base'])
c.rect(20, 44, 24, 6, idx['floor_l'])
c.rect(0, 44, 64, 20, idx['floor'])
for gx in range(0, 64, 8):
    c.line(gx, 44, gx, 63, idx['ftile'])
for gy in (48, 52, 56, 60):
    c.line(0, gy, 63, gy, idx['ftile'])

# --- wall clock ---
c.circle(32, 13, 5, idx['clockr'])
c.circle(32, 13, 4, idx['clockf'])
c.line(32, 13, 32, 9, idx['clockh'])
c.line(32, 13, 35, 12, idx['clockh'])
c.line(32, 13, 34, 10, idx['clkred'])

# --- washing machines (two rows flanking the aisle) ---
def machine(x, y, inside):
    c.rect(x, y, 14, 16, idx['machine'])
    c.rect(x, y, 14, 16, idx['outline'], fill=False)
    c.rect(x + 12, y + 1, 1, 14, idx['mshade'])
    c.rect(x + 1, y + 2, 12, 4, idx['panel'])
    c.rect(x + 2, y + 3, 4, 2, idx['panel_d'])
    c.set(x + 6, y + 4, idx['led'])
    c.set(x + 8, y + 4, idx['btn'])
    c.set(x + 10, y + 4, idx['btn_r'])
    c.set(x + 11, y + 4, idx['led'])
    c.circle(x + 7, y + 11, 4, idx['outline'])
    c.circle(x + 7, y + 11, 3, idx['glass'])
    c.set(x + 6, y + 9, idx['hl'])
    c.set(x + 9, y + 11, idx['glass_d'])
    c.set(x + 8, y + 13, idx['glass_d'])
    a, b = inside
    c.set(x + 5, y + 11, idx[a])
    c.set(x + 6, y + 12, idx[b])
    c.set(x + 7, y + 13, idx[a])
    c.set(x + 9, y + 12, idx[b])
    c.rect(x + 1, y + 16, 3, 2, idx['leg'])
    c.rect(x + 10, y + 16, 3, 2, idx['leg'])

machine(2, 26, ('c_whi', 'c_blue'))
machine(17, 26, ('c_blue', 'c_yel'))
machine(34, 26, ('c_gre', 'c_whi'))
machine(49, 26, ('c_red', 'c_pin'))

# --- laundry basket (left, foreground) ---
c.rect(14, 42, 5, 5, idx['c_red'])
c.rect(18, 43, 6, 4, idx['c_blue'])
c.rect(21, 41, 5, 6, idx['c_yel'])
c.rect(24, 43, 4, 3, idx['c_gre'])
c.rect(15, 42, 3, 3, idx['c_pin'])
c.rect(13, 46, 16, 2, idx['baskr'])
c.rect(15, 48, 12, 10, idx['bask'])
c.rect(15, 48, 12, 10, idx['baskd'], fill=False)
for i in range(3):
    c.line(17 + i * 4, 48, 17 + i * 4, 57, idx['baskd'])
c.line(15, 53, 26, 53, idx['baskd'])
c.rect(14, 58, 14, 1, idx['shad'])

# --- folding table (right, foreground) ---
c.rect(38, 41, 7, 1, idx['c_whi'])
c.rect(38, 42, 7, 1, idx['c_blue'])
c.rect(38, 43, 7, 1, idx['c_pin'])
c.rect(38, 44, 7, 1, idx['c_yel'])
c.rect(35, 41, 2, 1, idx['c_blue'])
c.rect(35, 42, 2, 4, idx['c_whi'])
c.rect(31, 45, 17, 2, idx['tbl'])
c.rect(31, 47, 17, 1, idx['tbld'])
c.rect(33, 48, 2, 10, idx['leg'])
c.rect(45, 48, 2, 10, idx['leg'])
c.rect(34, 53, 12, 1, idx['leg'])
c.rect(30, 58, 16, 1, idx['shad'])

print(c.stats_text())
finish(c)
