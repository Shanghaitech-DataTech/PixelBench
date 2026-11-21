import pixelbench_api as api
src = open("main.py").read()
g = dict(vars(api))
g["__name__"] = "__main__"
exec(compile(src, "main.py", "exec"), g)
c = g["c"]

LET = {0: ".", 1: "_", 2: ",", 3: "W", 4: "w", 5: "F", 6: "T", 7: "t", 8: "D",
       9: "d", 10: "s", 11: "M", 12: "m", 13: "l", 14: "K", 15: "P", 16: "g",
       17: "r", 18: "G", 19: "h", 20: "a", 21: "b", 22: "c", 23: "o", 24: "O",
       25: "R", 26: "e", 27: "N"}

def runs(x0, x1, y):
    out, prev, start = [], None, x0
    for x in range(x0, x1 + 1):
        i = c.get(x, y)
        if i != prev:
            if prev is not None:
                out.append((start, x - 1, prev))
            prev, start = i, x
    out.append((start, x1, prev))
    return out

for y in range(45, 55):
    print(f"y{y:2d}: " + " ".join(
        f"{LET[i]}{a}" + (f"-{b}" if b > a else "") for a, b, i in runs(14, 40, y)))
