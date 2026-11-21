import sys
try:
    import PIL
    from PIL import Image
    print("PIL is available:", PIL.__version__)
except Exception as e:
    print("PIL not available:", e)
