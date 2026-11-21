from pixelbench_api import *

output = input_canvas.copy(name='output')

deep  = output.color('#145a78')
water = output.color('#1d8baa')
light = output.color('#2ec7dc')
foam  = output.color('#d9f6f8')
white = output.color('#ffffff')

def fill_span(y, x0, x1, colour):
    for x in range(x0, x1 + 1):
        output.set(x, y, colour)

for y in (4, 5, 6, 7):
    output.set(31, y, light)
    output.set(32, y, light)
output.set(31, 6, white)
output.set(32, 4, white)
output.set(32, 5, white)

fill_span(8, 23, 40, light)
fill_span(9, 22, 41, water)
fill_span(10, 22, 41, deep)
for x in (27, 28, 29, 30, 31, 32, 33, 34, 35, 36):
    output.set(x, 8, foam)
output.set(31, 8, white)
output.set(32, 8, white)

for y in range(14, 34):
    if y % 2 == 0:
        output.set(18, y, light)
        output.set(19, y, deep)
    else:
        output.set(18, y, deep)
        output.set(19, y, light)
    if y % 2 == 0:
        output.set(44, y, light)
        output.set(45, y, deep)
    else:
        output.set(44, y, deep)
        output.set(45, y, light)
    if y in (16, 21, 27, 31):
        output.set(18, y, foam)
        output.set(45, y, foam)

lower_fill = {34:(18,45),35:(20,43),36:(23,40),37:(23,40),38:(22,41),39:(20,43),40:(19,44)}
for y,(x0,x1) in lower_fill.items():
    fill_span(y, x0, x1, deep)
fill_span(34, 18, 45, light)
fill_span(35, 20, 43, water)
fill_span(36, 23, 40, deep)
fill_span(37, 23, 40, deep)
fill_span(38, 22, 41, water)
fill_span(39, 20, 43, water)
fill_span(40, 19, 44, deep)
for x in range(19, 45, 2):
    output.set(x, 34, foam)
output.set(18, 34, foam)
output.set(44, 34, foam)
for x in (19, 20, 21, 43, 44):
    output.set(x, 34, white)
for x in (18, 19):
    output.set(x, 34, foam)
for x in (44, 45):
    output.set(x, 34, foam)

name = {0:'.',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
print("     " + "".join(str(x//10) if x%10==0 else " " for x in range(64)))
print("     " + "".join(str(x%10) for x in range(64)))
for y in range(0, 76):
    row = []
    for x in range(64):
        v = output.get(x, y)
        row.append(name[v] if v in name else '?')
    print(f"y={y:2d}: " + "".join(row))

finish(output)
