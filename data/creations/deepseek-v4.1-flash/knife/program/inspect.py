c = input_canvas
print(c.stats_text())
print(c.canvases() if hasattr(c, 'canvases') else '')
print([ (p['index'], p['name'], p['rgba']) for p in c.palette() ])
print(c.matrix_text())
