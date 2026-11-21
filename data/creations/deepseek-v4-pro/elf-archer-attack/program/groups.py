from pixelbench_api import *

c = input_canvas

def group(idx):
    skin = {3,9,13,14,15,29,34,35,41,4}
    hair = {1,2,8,10,11,21,23}
    green = {22,24,26,28,30,39}
    gray = {31,32,33}
    dark = {25,36,37,38,40}
    bow = {20}
    gold = {7,19,27,18,6}
    string = {12,16,17,5}
    other = {42}
    if idx==0: return ' '
    if idx in skin: return 'S'
    if idx in hair: return 'H'
    if idx in green: return 'G'
    if idx in gray: return 'A'
    if idx in dark: return 'D'
    if idx in bow: return 'B'
    if idx in gold: return 'g'
    if idx in string: return 'l'
    if idx in other: return '?'
    return '?'

print("   01234567890123456789012345678901234")
for y in range(47):
    row = ''.join(group(c.get(x,y)) for x in range(35))
    print(f"{y:2d} {row}")
