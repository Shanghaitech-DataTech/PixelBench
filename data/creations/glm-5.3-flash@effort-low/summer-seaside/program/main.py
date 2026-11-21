import math, random
from pixelbench_api import *

c = new_canvas(128, 128, background="#87CEEB", name="beach")
random.seed(7)

# --- sky gradient ---
SKY = ["#8FD4F0", "#87CDEE", "#7FC6EC", "#77BFEA", "#6FB6E6", "#67AEE2", "#5FA6DE"]
for i, col in enumerate(SKY):
    c.rect(0, i*7, 128, 7, col)

# --- sun ---
c.circle(102, 15, 9, "#FFF7C0")
c.circle(102, 15, 7, "#FFE873")
c.circle(102, 15, 5, "#FFF3A0")

# --- clouds ---
def cloud(cx, cy, s=1.0):
    for dx, dy, r in [(-8,2,4),(-3,-1,5),(3,0,5),(8,2,4),(0,3,4),(-12,3,3),(12,3,3)]:
        c.circle(int(cx+dx*s), int(cy+dy*s), max(2,int(r*s)), "#FFFFFF")
cloud(26, 13)
cloud(60, 26, 0.8)
cloud(16, 33, 0.6)

# --- sea: horizon y=49 to shore y=83 ---
SEA = [
    (49, "#155CA8"), (50, "#1B6BC0"), (54, "#1E74C6"), (58, "#2280CC"),
    (62, "#2A8ED2"), (66, "#35A0D8"), (70, "#42B2DE"), (74, "#4FC2E4"),
    (78, "#63D0EA"),
]
for y, col in SEA:
    c.rect(0, y, 128, 4, col)

# --- sailboat far out ---
c.line(90, 43, 90, 48, "#F5F5F5")
c.poly([(90,43),(84,48),(90,48)], "#FFFFFF")
c.line(86, 48, 94, 48, "#E0E0E0")
c.line(87, 49, 93, 49, "#B8B8B8")

# --- foam waves near shore ---
for y in range(76, 83):
    x = 0
    while x < 120:
        w = random.randint(3, 10)
        if random.random() < 0.55:
            c.rect(x, y, w, 1, "#FFFFFF")
        x += w + random.randint(1, 5)

# --- sand ---
c.rect(0, 83, 128, 45, "#F0D48A")
c.rect(0, 83, 128, 2, "#DCC078")  # wet sand
for _ in range(70):
    x, y = random.randint(0,127), random.randint(87,127)
    c.set(x, y, random.choice(["#E4C67E", "#F8E0A0", "#D8B870"]))

# --- foam edge on sand ---
for x in range(128):
    y = 83 + (1 if (x//6) % 2 == 0 else 0)
    c.set(x, y, "#FFFFFF")

# --- beach umbrella ---
c.line(38, 62, 38, 108, "#8B5A2B")
c.set(38, 109, "#6B4423")
CX, CY, R = 38, 64, 22
for dy in range(0, 21):
    half = int(math.sqrt(max(0, R*R - (20-dy)*(20-dy))))
    y = CY - 20 + dy
    for x in range(CX-half, CX+half+1):
        ang = math.degrees(math.atan2(y-CY, x-CX))
        seg = int(((ang + 180) // 30)) % 2
        c.set(x, y, "#E03030" if seg == 0 else "#FFFFFF")
# scalloped bottom edge highlight
for dx in range(-R, R+1):
    y = CY - 20 + 20
    c.set(CX+dx, y+1, "#C02828" if int(((math.degrees(math.atan2(1, dx))+180)//30))%2 else "#F0F0F0")
c.set(38, 42, "#E03030")

# --- striped towel ---
for i in range(7):
    c.rect(72, 100+i*3, 34, 3, "#3CB8C8" if i % 2 == 0 else "#FFFFFF")

# --- flip-flops ---
def flipflop(x, y, flip=False):
    # sole
    for dy in range(10):
        w = 7 - abs(dy-5)//2
        for dx in range(-w//2-1, w//2+2):
            c.set(x+dx, y+dy, "#FF8C42")
    # strap V
    c.line(x, y+1, x-2, y+5, "#E03030")
    c.line(x, y+1, x+2, y+5, "#E03030")
flipflop(62, 112)
flipflop(72, 114)

# --- gulls ---
def gull(x, y):
    c.line(x-4, y, x, y-2, "#FFFFFF")
    c.line(x, y-2, x+4, y, "#FFFFFF")
    c.set(x-4, y, "#E8E8E8"); c.set(x+4, y, "#E8E8E8")
gull(30, 52)
gull(48, 46)

print(c.stats_text())
finish(c)
