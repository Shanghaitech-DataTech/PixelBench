import time, math
import pixelbench_api as P

print("API names:", sorted([n for n in dir(P) if not n.startswith('_')])[:80])

c = P.new_canvas(256, 256, name="probe")

t0 = time.time()
n = 0
for i in range(60000):
    x = i % 256
    y = (i * 7) % 256
    c.set(x, y, (i % 100, 10, 20))
    n += 1
t1 = time.time()
print("set(): %.2f us/call" % ((t1 - t0) / n * 1e6))

t0 = time.time()
n = 0
for i in range(20000):
    c.line(0, i % 256, 200, i % 256, (5, 5, 5))
    n += 1
t1 = time.time()
print("line(200px): %.2f us/call" % ((t1 - t0) / n * 1e6))

t0 = time.time()
for i in range(20000):
    c.rect(0, i % 256, 200, 1, (6, 6, 6))
t1 = time.time()
print("rect(200x1): %.2f us/call" % ((t1 - t0) / 20000 * 1e6))

# index-based set speed
idx = c.color((1, 2, 3))
t0 = time.time()
for i in range(60000):
    c.set(i % 256, (i * 3) % 256, idx)
t1 = time.time()
print("set(idx): %.2f us/call" % ((t1 - t0) / 60000 * 1e6))
print(c.stats_text())
