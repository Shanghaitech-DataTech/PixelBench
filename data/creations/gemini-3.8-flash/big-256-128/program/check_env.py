import numpy as np
print("numpy available:", np.__version__)
try:
    import PIL
    print("PIL available:", PIL.__version__)
except Exception as e:
    print("PIL not available:", e)
