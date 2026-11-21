from pixelbench_api import *

c = input_canvas
w, h = c.stats()['size']
m = {
    0: '.', 1: '#', 2: 'b', 3: 'C', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h',
    9: 'i', 10: '$', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p',
    17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: '$', 23: 'w', 24: 'x',
    25: '$', 26: 'z', 27: 'A', 28: 'S', 29: 'C', 30: 'D', 31: 'W', 32: '$',
    33: 'G', 34: 'H', 35: 'I', 36: 'J', 37: 'K', 38: 'L', 39: 'M', 40: '$', 41: 'O'
}
for y in range(42, 61):
    row = ''.join(m.get(c.get(x,y), '?') for x in range(w))
    print(f"{y:02d} {row}")
