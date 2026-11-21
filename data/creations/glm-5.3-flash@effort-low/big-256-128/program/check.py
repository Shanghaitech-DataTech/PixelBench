c = input_canvas.copy(name='probe')
import math
# replicate remap quickly on a small region to verify palette shift
print(c.stats_text())
print(c.matrix_text(region=(50, 25, 75, 45)))
