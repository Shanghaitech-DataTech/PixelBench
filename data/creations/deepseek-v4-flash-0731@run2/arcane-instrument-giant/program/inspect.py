from pixelbench_api import view, load
import main

m = main.c
print(m.matrix_text(region=(64, 12, 192, 60), indices=False))
print('---')
print(m.matrix_text(region=(48, 128, 208, 178), indices=False))
view(m)
