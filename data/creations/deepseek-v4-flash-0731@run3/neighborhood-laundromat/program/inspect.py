from pixelbench_api import *
import main as m
c = m.c
out = []
out.append(c.matrix_text(region=(0,0,63,31)))
out.append(c.matrix_text(region=(0,32,63,63)))
print("\n".join(out))
