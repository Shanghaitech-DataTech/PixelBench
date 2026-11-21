from collections import Counter
def build(alg, ang, name):
    work = new_canvas(260, 260, background=None, name=name)
    sel = input_canvas.select(0, 0, 93, 128)
    r = sel.rotate(ang, algorithm=alg)
    print(alg, ang, 'size', r.size)
    r.copy_to(0, 0, work)
    w,h,data = work.to_rgba()
    n=sum(1 for y in range(h) for x in range(w) if data[(y*w+x)*4+3]>0)
    cnt=Counter()
    for y in range(h):
        for x in range(w):
            if data[(y*w+x)*4+3]>0:
                cnt[tuple(data[(y*w+x)*4:(y*w+x)*4+4])]+=1
    print('visible', n, 'colors', len(cnt))
    return work

wr = build('rotsprite', 125, 'wr')
print(wr.matrix_text(region=(0,55,159,92)))
