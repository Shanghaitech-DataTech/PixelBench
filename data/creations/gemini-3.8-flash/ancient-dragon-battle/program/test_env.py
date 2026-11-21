import sys
print("Python version:", sys.version)
try:
    import numpy as np
    print("numpy available:", np.__version__)
except ImportError:
    print("no numpy")

try:
    import PIL
    print("PIL available:", PIL.__version__)
except ImportError:
    print("no PIL")
