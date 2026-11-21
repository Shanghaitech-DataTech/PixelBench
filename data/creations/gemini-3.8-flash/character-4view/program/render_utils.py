from pixelbench_api import new_canvas, view, finish

COLOR_MAP = {
    '..': None,
    'OO': '#151424', # Dark outline
    'KK': '#2b233a', # Softer outline
    's0': '#fff0e5', # Skin highlight
    's1': '#fcd8b8', # Skin base
    's2': '#e2a482', # Skin shadow
    'bl': '#f89ca2', # Blush
    'mu': '#c75868', # Mouth / lip
    'h0': '#ffec88', # Hair light
    'h1': '#f2ba32', # Hair base
    'h2': '#c27b14', # Hair shadow
    'h3': '#7d4508', # Hair deep shadow
    'r0': '#ff6078', # Red bow light
    'r1': '#de1c3e', # Red bow base
    'r2': '#910f27', # Red bow shadow
    'b0': '#5c8eff', # Blue uniform light
    'b1': '#2255d4', # Blue uniform base
    'b2': '#133596', # Blue uniform shadow
    'w0': '#ffffff', # White
    'w1': '#dce3f0', # White shadow
    'w2': '#9daac2', # White dark shadow
    'g0': '#ffea6c', # Gold / pompom light
    'g1': '#f5b800', # Gold / pompom base
    'g2': '#ba7b00', # Gold / pompom shadow
    'e0': '#42b4f5', # Eye blue
    'e1': '#124896', # Eye dark
    't0': '#42485e', # Sole / tread
}

def render_view(canvas, ox, oy, grid_rows):
    for y, row in enumerate(grid_rows):
        tokens = [row[i:i+2] for i in range(0, len(row), 2)]
        for x, tok in enumerate(tokens):
            if tok in COLOR_MAP and COLOR_MAP[tok] is not None:
                canvas.set(ox + x, oy + y, COLOR_MAP[tok])
