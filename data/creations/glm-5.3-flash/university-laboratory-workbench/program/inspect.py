import pixelbench_api as api
src = open("main.py").read()
g = dict(vars(api))
g["__name__"] = "__main__"
exec(compile(src, "main.py", "exec"), g)
c = g["c"]

regions = [
    ("TOP WALL", (0, 0, 63, 23)),
    ("MICROSCOPE", (4, 8, 24, 46)),
    ("RACK", (22, 24, 42, 44)),
    ("BOTTLES+DROPPER", (42, 17, 63, 55)),
    ("NOTEBOOK+PENCIL", (0, 43, 42, 60)),
]
for name, r in regions:
    print("=" * 20, name, r)
    print(c.matrix_text(region=r, indices=True))
