# Let's inspect circle templates for 14x14 and 12x12
# A standard 14x14 pixel art circle:
circle_14 = [
    (12, 14, 17), # 4 px
    (13, 12, 19), # 8 px (+2 each side)
    (14, 11, 20), # 10 px (+1 each side)
    (15, 10, 21), # 12 px (+1 each side)
    (16,  9, 22), # 14 px (+1 each side)
    (17,  9, 22), # 14 px (vertical run = 4)
    (18,  9, 22), # 14 px
    (19,  9, 22), # 14 px
    (20, 10, 21), # 12 px (-1 each side)
    (21, 11, 20), # 10 px (-1 each side)
    (22, 12, 19), # 8 px (-1 each side)
    (23, 14, 17), # 4 px (-2 each side)
]
# Wait, y=12 to 23 is 12 rows!
# If it's 14 rows:
# 4, 8, 10, 12, 12, 14, 14, 14, 14, 12, 12, 10, 8, 4 -> that is 14 rows!
circle_14_exact = [
    (12, 14, 17), # 4 px
    (13, 12, 19), # 8 px
    (14, 11, 20), # 10 px
    (15, 10, 21), # 12 px
    (16, 10, 21), # 12 px
    (17,  9, 22), # 14 px
    (18,  9, 22), # 14 px
    (19,  9, 22), # 14 px
    (20,  9, 22), # 14 px
    (21, 10, 21), # 12 px
    (22, 10, 21), # 12 px
    (23, 11, 20), # 10 px
    (24, 12, 19), # 8 px
    (25, 14, 17), # 4 px
]
print("14-row circle valid:", len(circle_14_exact) == 14)
for y, x0, x1 in circle_14_exact:
    w = x1 - x0 + 1
    print(f"y={y}: x={x0}..{x1} (w={w})")
