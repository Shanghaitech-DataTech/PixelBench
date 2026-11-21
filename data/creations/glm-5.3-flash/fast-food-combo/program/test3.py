# test blit mapping precisely
def dump(cv, label):
    w, h, rgba = cv.to_rgba()
    print(f"--- {label} {w}x{h} ---")
    print("    " + "".join(str(x % 10) for x in range(w)))
    for y in range(h):
        print(f"{y:3d} " + "".join("." if rgba[(y * w + x) * 4 + 3] == 0 else "X"
                                   for x in range(w)))


art = new_canvas(4, 3, background=None, name="art")
for y in range(3):
    for x in range(4):
        art.set(x, y, "#ff0000")
dump(art, "art 4x3 solid")

s = new_canvas(12, 10, background=None, name="s")
s.blit(art, 2, 2)
dump(s, "blit(art, 2, 2)")
