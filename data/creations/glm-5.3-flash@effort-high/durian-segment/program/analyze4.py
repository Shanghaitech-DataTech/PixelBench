ic = input_canvas
letters = {1:'.', 2:'#', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i'}
print("colors used in bottom segment region (y 52-57):")
from collections import Counter
cnt = Counter()
for y in range(52, 58):
    for x in range(0, 64):
        cnt[letters[ic.get(x, y)]] += 1
print(cnt)

print()
print("colors used in upper flesh regions (y 12-51):")
cnt2 = Counter()
for y in range(12, 52):
    for x in range(0, 64):
        cnt2[letters[ic.get(x, y)]] += 1
print(cnt2)
