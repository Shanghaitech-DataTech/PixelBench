from pixelbench_api import *
import main as m
c = m.c
print("--- sun/sky region 20..95 x 55..95 ---")
print(c.matrix_text(region=(20, 55, 95, 95), indices=False))
print("--- sea+rocks region 0..127 x 86..127 ---")
print(c.matrix_text(region=(0, 86, 127, 127), indices=False))
