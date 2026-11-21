from pixelbench_api import new_canvas, finish

# Create a 64x64 canvas with transparent background
c = new_canvas(64, 64, background=None, name="explosion")

# Define colors for the explosion
# Core colors (bright yellow fireball)
c.color("#FFFF00", name="yellow_core")      # 0 - bright yellow core
c.color("#FFD700", name="yellow_bright")    # 1 - golden yellow
c.color("#FFA500", name="orange_mid")       # 2 - orange middle
c.color("#FF6600", name="orange_dark")      # 3 - dark orange

# Outer blast colors (orange-red)
c.color("#FF4500", name="red_orange")       # 4 - red-orange
c.color("#FF3300", name="red_bright")       # 5 - bright red
c.color("#CC3300", name="red_dark")         # 6 - dark red
c.color("#992200", name="red_deep")         # 7 - deep red

# Spark colors
c.color("#FFFFFF", name="spark_white")      # 8 - white sparks
c.color("#FFFFAA", name="spark_yellow")     # 9 - yellow sparks
c.color("#FFAA00", name="spark_orange")     # 10 - orange sparks

# Smoke/ash colors
c.color("#663300", name="smoke_dark")       # 11 - dark smoke
c.color("#442200", name="smoke_darker")     # 12 - darker smoke

# Center of explosion
cx, cy = 32, 32

# Draw the bright yellow core (inner circle, radius ~8)
c.circle(cx, cy, 8, "#FFFF00", fill=True)

# Draw expanding orange-yellow layer (radius ~12)
c.circle(cx, cy, 12, "#FFD700", fill=True)

# Draw orange middle layer (radius ~16)
c.circle(cx, cy, 16, "#FFA500", fill=True)

# Draw orange-red outer layer (radius ~20)
c.circle(cx, cy, 20, "#FF6600", fill=True)

# Draw red-orange blast ring (radius ~24)
c.circle(cx, cy, 24, "#FF4500", fill=True)

# Draw red outer blast (radius ~28)
c.circle(cx, cy, 28, "#FF3300", fill=True)

# Add irregular explosion shapes for dynamic effect
# Upper right burst
c.poly([(35, 10), (45, 8), (50, 15), (42, 20), (38, 18)], "#FF6600", fill=True)
c.poly([(38, 12), (44, 10), (46, 16), (40, 18)], "#FFD700", fill=True)

# Lower left burst
c.poly([(20, 40), (15, 50), (22, 55), (30, 48), (28, 42)], "#FF4500", fill=True)
c.poly([(24, 42), (18, 48), (24, 52), (28, 46)], "#FFA500", fill=True)

# Upper left burst
c.poly([(18, 20), (10, 15), (8, 25), (15, 30), (20, 25)], "#FF3300", fill=True)
c.poly([(16, 22), (12, 18), (11, 26), (17, 28)], "#FF6600", fill=True)

# Lower right burst
c.poly([(45, 40), (55, 45), (52, 55), (42, 52), (44, 44)], "#FF4500", fill=True)
c.poly([(47, 42), (53, 46), (50, 52), (45, 48)], "#FFA500", fill=True)

# Add sparks radiating outward
# Top sparks
c.set(32, 5, "#FFFFFF")
c.set(30, 6, "#FFFFAA")
c.set(34, 6, "#FFAA00")
c.set(28, 8, "#FFFFFF")
c.set(36, 8, "#FFFFAA")

# Bottom sparks
c.set(32, 58, "#FFFFFF")
c.set(30, 57, "#FFFFAA")
c.set(34, 57, "#FFAA00")
c.set(28, 55, "#FFFFFF")
c.set(36, 55, "#FFFFAA")

# Left sparks
c.set(5, 32, "#FFFFFF")
c.set(6, 30, "#FFFFAA")
c.set(6, 34, "#FFAA00")
c.set(8, 28, "#FFFFFF")
c.set(8, 36, "#FFFFAA")

# Right sparks
c.set(58, 32, "#FFFFFF")
c.set(57, 30, "#FFFFAA")
c.set(57, 34, "#FFAA00")
c.set(55, 28, "#FFFFFF")
c.set(55, 36, "#FFFFAA")

# Diagonal sparks
c.set(12, 12, "#FFFFFF")
c.set(14, 14, "#FFFFAA")
c.set(10, 10, "#FFAA00")

c.set(52, 12, "#FFFFFF")
c.set(50, 14, "#FFFFAA")
c.set(54, 10, "#FFAA00")

c.set(12, 52, "#FFFFFF")
c.set(14, 50, "#FFFFAA")
c.set(10, 54, "#FFAA00")

c.set(52, 52, "#FFFFFF")
c.set(50, 50, "#FFFFAA")
c.set(54, 54, "#FFAA00")

# Add more scattered sparks
spark_positions = [
    (20, 8), (44, 8), (8, 20), (56, 20),
    (8, 44), (56, 44), (20, 56), (44, 56),
    (25, 10), (39, 10), (10, 25), (54, 25),
    (10, 39), (54, 39), (25, 54), (39, 54),
]

for i, (x, y) in enumerate(spark_positions):
    color = ["#FFFFFF", "#FFFFAA", "#FFAA00"][i % 3]
    c.set(x, y, color)

# Add some smoke/ash at edges
c.set(15, 15, "#663300")
c.set(49, 15, "#663300")
c.set(15, 49, "#663300")
c.set(49, 49, "#663300")

c.set(18, 12, "#442200")
c.set(46, 12, "#442200")
c.set(12, 46, "#442200")
c.set(52, 46, "#442200")

# Add irregular flame tongues
# Top flame
c.poly([(28, 8), (32, 3), (36, 8), (34, 12), (30, 12)], "#FFD700", fill=True)
c.poly([(30, 6), (32, 4), (34, 6), (33, 10), (31, 10)], "#FFFF00", fill=True)

# Bottom flame
c.poly([(28, 56), (32, 61), (36, 56), (34, 52), (30, 52)], "#FF4500", fill=True)
c.poly([(30, 58), (32, 60), (34, 58), (33, 54), (31, 54)], "#FF6600", fill=True)

# Left flame
c.poly([(8, 28), (3, 32), (8, 36), (12, 34), (12, 30)], "#FF6600", fill=True)
c.poly([(10, 30), (5, 32), (10, 34), (11, 33), (11, 31)], "#FFA500", fill=True)

# Right flame
c.poly([(56, 28), (61, 32), (56, 36), (52, 34), (52, 30)], "#FF4500", fill=True)
c.poly([(54, 30), (59, 32), (54, 34), (53, 33), (53, 31)], "#FF6600", fill=True)

# Add some extra detail with smaller circles for texture
c.circle(cx, cy, 4, "#FFFF00", fill=True)  # Bright core center
c.circle(cx - 5, cy - 3, 3, "#FFD700", fill=True)
c.circle(cx + 6, cy + 4, 3, "#FFD700", fill=True)
c.circle(cx - 3, cy + 5, 2, "#FFA500", fill=True)
c.circle(cx + 4, cy - 4, 2, "#FFA500", fill=True)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63), indices=False))

finish(c)
