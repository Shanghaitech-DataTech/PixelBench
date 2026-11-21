from pixelbench_api import *
import pixelbench_api as api

print("has reference?", hasattr(api, 'reference'))
try:
    print(api.reference)
except Exception as e:
    print("reference error", e)
try:
    print("reference_frames", api.reference_frames)
except Exception as e:
    print("reference_frames error", e)
try:
    print("mask", api.mask)
except Exception as e:
    print("mask error", e)
