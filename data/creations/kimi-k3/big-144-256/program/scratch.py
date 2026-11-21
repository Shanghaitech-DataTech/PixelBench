from pixelbench_api import *

c = load("runs/run_0005/images/0000.png", name="prev", add=False) if False else None
out = input_canvas.copy(name="output")
# rebuild by exec-ing previous file body is complex; instead just re-view crops of the finished output
# simplest: rerun previous main by importing? No — redraw by reading exported state isn't saved.
# We'll just crop from the last view: not possible. Instead, re-run the whole edit here.
exec(open("main_prev.py").read()) if False else None
