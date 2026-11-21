import pixelbench_api

def stub(*a, **k):
    return None
pixelbench_api.finish = stub

exec(open("main.py").read())
c = pixelbench_api.canvas(-1)

print("=== TOP (0,0)-(60,17) ===")
print(c.matrix_text(region=(0, 0, 59, 17)))
print("=== MICROSCOPE (0,8)-(26,48) ===")
print(c.matrix_text(region=(0, 8, 25, 48)))
print("=== RACK (20,24)-(40,48) ===")
print(c.matrix_text(region=(20, 24, 39, 48)))
print("=== DROPPER+NOTEBOOK (24,36)-(63,62) ===")
print(c.matrix_text(region=(24, 36, 63, 62)))
