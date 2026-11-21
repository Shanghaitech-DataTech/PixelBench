from collections import Counter
def hist(c, label):
    w,h,data=c.to_rgba()
    cnt=Counter()
    for y in range(h):
        for x in range(w):
            a=data[(y*w+x)*4+3]
            if a>0:
                cnt[tuple(data[(y*w+x)*4:(y*w+x)*4+4])]+=1
    print(label, sorted(cnt.items(), key=lambda kv:-kv[1]))

hist(input_canvas,'INPUT')
work = new_canvas(220, 220, background=None, name='wn')
sel = input_canvas.select(0, 0, 93, 128)
r = sel.rotate(125, algorithm='nearest')
r.copy_to(0, 0, work)
hist(work,'ROT125')
