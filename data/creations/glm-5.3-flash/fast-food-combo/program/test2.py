# test sprite/blit offsets
def grow_outline(cv, colour="#1a1310"):
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


def dump(cv, label):
    w, h, rgba = cv.to_rgba()
    print(f"--- {label} {w}x{h} ---")
    print("    " + "".join(str(x % 10) for x in range(w)))
    for y in range(h):
        print(f"{y:3d} " + "".join("." if rgba[(y * w + x) * 4 + 3] == 0 else "X"
                                   for x in range(w)))


art = new_canvas(8, 7, background=None, name="art")
art.set(0, 0, "#ff0000")
art.set(7, 6, "#00ff00")
dump(art, "art")

s = new_canvas(10, 9, background=None, name="sprite")
s.blit(art, 1, 1)
grow_outline(s)
dump(s, "sprite (art blitted at 1,1)")

big = new_canvas(14, 14, background=None, name="big")
big.blit(s, 2, 0)
dump(big, "big (sprite blitted at 2,0)")
