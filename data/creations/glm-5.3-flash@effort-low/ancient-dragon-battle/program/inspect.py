# inspect regions of the flattened result
from pixelbench_api import *
c = load("../../../../runs/run_0001/artifacts/exports/ancient-dragon-battle.pixelart.json", add=False)
print("== dragon region ==")
print(c.matrix_text(region=(20, 10, 135, 60)))
print("== castle top ==")
print(c.matrix_text(region=(90, 30, 200, 90)))
