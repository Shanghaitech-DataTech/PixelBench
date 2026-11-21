from pixelbench_api import *
import random

# Rebuild the scene by reading main.py - actually let me just import and run the build logic
# Since main.py runs finish(c), let me read it as a module

# Actually let me just check the output from the previous run
# I'll create a small verification script that re-creates key elements

print("Checking last canvas state...")

# We need to re-run the scene building. Let me just create a minimal check.
# Actually the main.py finish(c) completed. The canvas c2 should be available.

c2 = canvas("c2")
print(c2.stats_text())

# Check person area 
print("\nPerson area stats:")
stats = c2.stats()
print(f"Coverage: {stats['coverage']}")
print(f"Colors: {stats['colors_used']}")
