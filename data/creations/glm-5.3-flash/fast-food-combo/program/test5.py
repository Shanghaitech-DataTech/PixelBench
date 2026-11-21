# definitive test of sprite pipeline with transparent pixels
INK = "#1a1310"


def grow_outline(cv, colour=INK):
    w, h, rgba = cv.to_rgba()

    def op(x, y):
        return 0 <= x < w and 0 <= y < h and rgba[(y * w + x) * 4 + 3] != 0

    pts = []
    for y in range(h):
        for x in range(w):
            if not op(x, y) and any(op(x + dx, y + dy)
                                    for dx in (-1, 0, 1)
                                    for dy in (-1, 0, 1) if dx or dy):
                pts.append((x, y))
    for x, y in pts:
        cv.set(x, y, colour)
    return cv


def sprite(w, h, name, fn):
    art = new_canvas(w, h, background=None, name=name)
    fn(art)
    s = new_canvas(w + 2, h + 2, background=None, name=name + "_o")
    s.blit(art, 1, 1)
    grow_outline(s)
    return s


ART = (
    ".RR.",
    "RGGG",
    "RGBB",
    ".RR.",
)


def paint(cv):
    m = {'R': "#ff0000", 'G': "#00ff00", 'B': "#0000ff"}
    for y, row in enumerate(ART):
        for x, ch in enumerate(row):
            if ch in m:
                cv.set(x, y, m[ch])


def dump(cv, label):
    w, h, rgba = cv.to_rgba()
    lut = {("#ff0000"): "R", ("#00ff00"): "G", ("#0000ff"): "B", INK: "#"}
    print(f"--- {label} {w}x{h} ---")
    print("    " + "".join(str(x % 10) for x in range(w)))
    for y in range(h):
        row = ""
        for x in range(w):
            o = (y * w + x) * 4
            if rgba[o + 3] == 0:
                row += "."
                continue
            key = "#%02x%02x%02x" % (rgba[o], rgba[o + 1], rgba[o + 2])
            row += lut.get(key, "?")
        print(f"{y:3d} " + row)


art = new_canvas(4, 4, background=None, name="art")
paint(art)
dump(art, "art 4x4")

s = sprite(4, 4, "art", paint)
dump(s, "sprite (should be art at 1,1 + outline)")
