for p in input_canvas.palette():
    r, g, b, a = p['rgba']
    hex_col = f"#{r:02x}{g:02x}{b:02x}"
    print(f"Index {p['index']:2d}: {p['name']:5s} {hex_col} rgba=({r},{g},{b},{a})")
