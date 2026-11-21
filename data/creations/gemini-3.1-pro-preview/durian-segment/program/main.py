from pixelbench_api import input_canvas, view, finish

output = input_canvas.copy(name="output")

x_crease_map = {}
last_x = 40
for y in range(33, 64):
    xc = -1
    for x in range(64):
        if output.get(x, y) == 4:
            xc = x
            break
    if xc == -1:
        xc = last_x
    else:
        last_x = xc
    x_crease_map[y] = xc

queue = [(18, 40)]
visited = set()
while queue:
    x, y = queue.pop(0)
    if (x, y) in visited:
        continue
    visited.add((x, y))
    
    if 0 <= x < 64 and 0 <= y < 64:
        c = output.get(x, y)
        if c in (6, 8):
            output.set(x, y, 1)
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 33 <= ny < 64 and nx < x_crease_map.get(ny, 0):
                    queue.append((nx, ny))

finish(output)
