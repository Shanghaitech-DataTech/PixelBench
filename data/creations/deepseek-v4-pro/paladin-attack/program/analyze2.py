from pixelbench_api import *

c = input_canvas
w, h = c.stats()['size']

def pixels_of(idx):
    return [(x,y) for y in range(h) for x in range(w) if c.get(x,y)==idx]

# ids per legend: name cN -> id N+1
ids = {
 'E white': 31,
 'j gold': 10,
 'g brown': 7,
 'y yellow': 25,
 'v gold2': 22,
 'N gold3': 40,
 't pale': 20,
 'A brown': 27,
 'B skin': 28,
 'F lightgold': 32,
 'H red': 34,
 'I pink': 35,
 'J cream': 36,
 'M dark': 39,
 'D olive': 30,
 's brown2': 19,
 'c cream': 3,
 'b gray': 2,
 'd brown3': 4,
 'e gray2': 5,
 'f darkred': 6,
 'k darkred2': 11,
 'l pink2': 12,
 'n magenta': 14,
 'o gray3': 15,
 'p gray4': 16,
 'q darkmag': 17,
 'u dark': 21,
 'w tan': 23,
 'x skin2': 24,
 'z tan2': 26,
 'h maroon': 8,
 'i magenta2': 9,
 'm pink3': 13,
 'r light': 18,
 'C dark3': 29,
 'G olive2': 33,
 'K dark4': 37,
 'L darkmag2': 38,
}
for label, idx in ids.items():
    px = pixels_of(idx)
    print(f"{label} (id {idx}) n={len(px)}: {px}")
