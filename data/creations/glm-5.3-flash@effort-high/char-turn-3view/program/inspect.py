c = input_canvas
w, h = 66, 119
rgba = c.to_rgba()[2]
# print rows as compact text: map colors to chars
from collections import Counter
cnt = Counter()
for y in range(h):
    for x in range(w):
        cnt[bytes(rgba[(y*w+x)*4:(y*w+x)*4+4])] += 1
chars = {}
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
i = 0
for col, n in cnt.most_common():
    ch = '.' if col[3] == 0 else letters[i % len(letters)]
    chars[col] = ch
    i += 1
    print(ch, col, n)
print()
for y in range(h):
    row = ""
    for x in range(w):
        col = bytes(rgba[(y*w+x)*4:(y*w+x)*4+4])
        row += chars[col]
    print(row)
