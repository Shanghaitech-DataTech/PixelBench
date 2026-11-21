import runpy
ns = runpy.run_path("main.py", init_globals=dict(globals()))
o = ns['out']
view(o.select(96, 26, 80, 90).preview('zoomA'), scale=6)
