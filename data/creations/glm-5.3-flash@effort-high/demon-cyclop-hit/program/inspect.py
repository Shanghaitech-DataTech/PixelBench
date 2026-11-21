c = input_canvas
# zoom on eye region and mouth/feet regions with indices
print("EYE region (12,10)-(26,22):")
print(c.matrix_text(region=(12,10,26,22), indices=True))
print("MOUTH/BODY region (6,20)-(32,27):")
print(c.matrix_text(region=(6,20,32,27), indices=True))
print("FEET region (4,26)-(34,32):")
print(c.matrix_text(region=(4,26,34,32), indices=True))
print(c.palette())
