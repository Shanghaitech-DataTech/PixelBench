c = new_canvas(16, 16, name="mushroomling")

OUT = "#2a1a1a"   # dark outline
RED = "#c8342c"   # red cap
WHT = "#f2ede0"   # white spots / eye whites
CRM = "#e8d3ae"   # cream body

# --- cap: rows 1..7, wide dome ---
# outline of cap
c.line(4, 1, 11, 1, OUT)          # top
c.line(2, 4, 2, 6, OUT)           # left side
c.line(13, 4, 13, 6, OUT)         # right side
c.line(3, 3, 3, 3, OUT)
c.line(12, 3, 12, 3, OUT)
c.line(1, 7, 14, 7, OUT)          # cap brim bottom

# red fill of cap
c.rect(4, 2, 8, 1, RED)
c.rect(3, 3, 10, 1, RED)
c.rect(3, 4, 10, 3, RED)
c.rect(4, 1, 8, 1, RED)
# clean top corners red
c.rect(5, 1, 6, 1, RED)

# white spots
c.rect(5, 2, 2, 2, WHT)
c.set(10, 3, WHT); c.set(10, 4, WHT); c.set(11, 4, WHT)
c.set(3, 5, WHT); c.set(3, 6, WHT)

# --- body: rows 8..13 ---
c.line(4, 8, 11, 8, OUT)
c.line(3, 9, 3, 12, OUT)
c.line(12, 9, 12, 12, OUT)
c.line(4, 13, 11, 13, OUT)
c.rect(4, 9, 8, 4, CRM)
c.rect(4, 9, 8, 1, CRM)

# eyes: white with dark pupils
c.rect(5, 10, 2, 2, WHT)
c.rect(9, 10, 2, 2, WHT)
c.set(6, 11, OUT); c.set(9, 11, OUT)

# mouth
c.set(7, 12, OUT); c.set(8, 12, OUT)

# --- stubby arms ---
c.set(2, 10, OUT); c.set(1, 10, OUT); c.set(1, 11, OUT)
c.set(13, 10, OUT); c.set(14, 10, OUT); c.set(14, 11, OUT)

# --- feet: rows 14..15 ---
c.rect(4, 14, 3, 2, OUT)
c.rect(9, 14, 3, 2, OUT)

print(c.stats_text())
print(c.matrix_text())
save("mushroomling", c)
finish(c)
