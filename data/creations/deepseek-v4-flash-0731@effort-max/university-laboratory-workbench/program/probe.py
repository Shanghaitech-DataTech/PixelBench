import pixelbench_api

def stub(*a, **k):
    return None
pixelbench_api.finish = stub

exec(open("main.py").read())
c = pixelbench_api.canvas(-1)

L = {
    "#e6ddc8": "A", "#f4f0e2": "P", "#ded6c0": "p", "#8a8a94": "C", "#f0ead8": "c",
    "#3a3a44": "k", "#a07048": "S", "#7d5330": "s", "#c8945c": "T", "#d9a96f": "t",
    "#9c6a38": "F", "#6d4526": "f", "#23232c": "W", "#43434f": "w", "#666675": "g",
    "#8f8fa0": "G", "#3c6a9e": "L", "#cfe0f2": "l", "#2d2d38": "K", "#cfe0ee": "G",
    "#a9c0d6": "d", "#eef4fa": "h", "#d94f4f": "R", "#4f7fd9": "B", "#4f9e4f": "N",
    "#e8c93d": "Y", "#3fa39e": "Q", "#d9a04f": "O", "#bd8238": "o", "#e8e4d8": "V",
    "#b8b2a0": "v", "#a05a3a": "U", "#f2efe4": "W", "#b0a888": "I", "#3f6f94": "J",
    "#31587a": "j", "#4f83a8": "D", "#f6f2e4": "M", "#d8cbb4": "m", "#d9b33d": "X",
    "#c98a6a": "x", "#d97a8a": "E", "#b8453a": "e", "#8f322b": "q",
}
for y0, y1 in [(2, 16), (30, 50)]:
    print(f"--- rows {y0}..{y1} x0..63 ---")
    for y in range(y0, y1 + 1):
        row = "".join(L.get(c.color_name(c.get(x, y))[0] and c.color_name(c.get(x, y))[:7], "?") for x in range(64))
        print(f"{y:02d} {row}")
