# Debug: run-length dump of the current monarch canvas
c = canvas("monarch")
palette = {p["index"]: p["rgba"] for p in c.palette()}
letter = {}
alpha = "abcdefghijklmnopqrstuvwxyz"
for i, (idx, p) in enumerate(sorted(palette.items())):
    letter[idx] = alpha[i]

for y in range(32):
    runs = []
    prev = None
    start = 0
    for x in range(32):
        v = c.get(x, y)
        if v != prev:
            if prev is not None:
                runs.append(f"{letter.get(prev,'?')}{x-start}")
            prev = v
            start = x
    runs.append(f"{letter.get(prev,'?')}{32-start}")
    print(f"{y:2d} " + " ".join(runs))

print(c.palette())
