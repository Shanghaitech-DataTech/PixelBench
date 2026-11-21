exec(open('main.py').read().split("print(\"F1:")[0])
# verify frame 1 == original content, shifted by 6
orig = input_canvas
ok = True
for y in range(orig.height):
    for x in range(orig.width):
        if orig.get(x, y) != f1.get(x + 6, y):
            ok = False
print("frame1 preserves original content:", ok)
print("F1 bbox:", f1.stats()['bbox'], " F2 bbox:", f2.stats()['bbox'])
print("sizes:", f1.stats()['size'], f2.stats()['size'])
