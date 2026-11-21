src = open("main.py").read().replace("finish(result)", "pass\nRESULT = result")
ns = {}
exec(src, ns)
P = ns["P"]
badx = bady = 0
for y in range(96):
    for x in range(64):
        if P.get(x + 32, y) != P.get(x, y):
            badx += 1
for y in range(64):
    for x in range(96):
        if P.get(x, y + 32) != P.get(x, y):
            bady += 1
print("horizontal mismatches:", badx, " vertical mismatches:", bady)
c = ns["RESULT"]
print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31), indices=True))
