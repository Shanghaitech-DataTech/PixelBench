# Quick inspection of regions
from pixelbench_api import *
from main_import import get_canvas  # placeholder - won't work

# Actually let me just check by reading the current main and looking at regions
exec(open("main.py").read().replace("finish(c)", ""))
import sys

# print a small region near the core
print("=== CORE REGION ===")
print(c.matrix_text(region=(118, 98, 138, 118), indices=True))
