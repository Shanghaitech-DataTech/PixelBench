work = input_canvas.copy(name="work")
work.mirror("h")
rec = work.select(0, 0, 93, 128).rotate(53.0, algorithm="rotsprite")
preview = rec.preview()
bx0, by0, bx1, by1 = preview.stats()["bbox"]
bw, bh = bx1 - bx0 + 1, by1 - by0 + 1
knife = new_canvas(bw, bh, background=None, name="knife")
preview.select(bx0, by0, bw, bh).copy_to(0, 0, knife)
view(knife, scale=4, margin=2, edges="all")
