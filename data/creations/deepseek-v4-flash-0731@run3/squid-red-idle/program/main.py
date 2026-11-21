from pixelbench_api import *

src = input_canvas
w, h = src.stats()['size']          # 58x57
H = h + 2                            # 58x59 canvas: spare transparent row above and below

# Split the sprite for a "tentacles planted, mantle bobs" breathing idle.
mantle = new_canvas(w, 45); mantle.blit(src, 0, 0)      # src rows 0..44   (the red mantle/body)
row44  = new_canvas(w, 1);  row44.blit(src, 0, -44)     # src row 44        (jungle seam filler)
tent   = new_canvas(w, 12); tent.blit(src, 0, -45)      # src rows 45..56  (tentacles, stay planted)

# Frame 1: original picture content, unchanged pixels, natural rest position (y=1).
f1 = new_canvas(w, H, name="f1")
f1.blit(src, 0, 1)

# Frame 2: breathe in -> mantle rises 1px; the seam below is filled with the
# mantle's own bottom row (a slight stretch), tentacle tips stay planted.
f2 = new_canvas(w, H, name="f2")
f2.blit(mantle, 0, 0)
f2.blit(row44, 0, 45)
f2.blit(tent, 0, 46)

# Frame 3: breathe out -> mantle settles 1px down; it overlaps onto the top of
# the tentacle slice (a slight squash), tentacle tips stay planted.
f3 = new_canvas(w, H, name="f3")
f3.blit(tent, 0, 46)
f3.blit(mantle, 0, 2)

for name, f in (("f1", f1), ("f2", f2), ("f3", f3)):
    st = f.stats()
    print(name, st['size'], "visible:", st['visible_pixels'], "bbox:", st['bbox'])
    print(name, "rows 0-2:")
    print(f.matrix_text(region=(0, 0, 57, 2)))
    print(name, "rows 44-49 (seam):")
    print(f.matrix_text(region=(0, 44, 57, 49)))

finish([f1, f2, f3])
