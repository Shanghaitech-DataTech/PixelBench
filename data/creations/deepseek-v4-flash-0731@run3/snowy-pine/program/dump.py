from pixelbench_api import input_canvas

c = input_canvas
# Dump matrix in 3 vertical chunks
for y0 in (0, 45, 90):
    print(f"=== rows {y0}-{y0+44} ===")
    print(c.matrix_text(region=(0, y0, 81, min(y0+44, 134)), indices=True))
