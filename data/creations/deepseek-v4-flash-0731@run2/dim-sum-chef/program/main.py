from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32, name="dimsum_chef")

WHITE    = "#fdfdfd"
WHITE_SH = "#dcdee1"
CREAM    = "#efe1bd"
SKIN     = "#f2c193"
PINK     = "#eea793"
EYE      = "#22180f"
BROWN    = "#54371f"
RED      = "#c23a3a"
RED_D    = "#962828"
BAMBOO   = "#c98f56"
BAMBOO_D = "#99652f"
BAMBOO_L = "#dcab6d"
BUN      = "#fdf4db"
BUN_SH   = "#dfcda2"
PANTS    = "#454b5c"
SHOE     = "#1f232d"

# --- chef hat ---
c.rect(11, 0, 10, 2, WHITE)          # puff rows 0-1
c.rect(10, 2, 12, 1, WHITE)          # puff flare
c.set(9, 2, WHITE_SH); c.set(22, 2, WHITE_SH)
c.rect(9, 3, 14, 2, WHITE)           # band rows 3-4
c.rect(9, 4, 14, 1, WHITE_SH)        # band shadow

# --- face ---
c.rect(10, 5, 12, 1, SKIN)
c.rect(9, 6, 14, 4, SKIN)
c.rect(10, 10, 12, 1, SKIN)
c.set(11, 7, BROWN); c.set(12, 7, BROWN)   # brows
c.set(19, 7, BROWN); c.set(20, 7, BROWN)
c.set(12, 8, EYE);   c.set(13, 8, EYE)      # eyes
c.set(18, 8, EYE);   c.set(19, 8, EYE)
c.set(13, 8, WHITE); c.set(18, 8, WHITE)    # eye highlights
c.set(10, 9, PINK);  c.set(21, 9, PINK)     # cheeks
c.set(14, 10, EYE);  c.set(15, 10, EYE)     # smile
c.set(16, 10, EYE);  c.set(17, 10, EYE)
c.set(12, 11, SKIN); c.set(13, 11, SKIN)
c.set(14, 11, SKIN); c.set(15, 11, SKIN)
c.set(16, 11, SKIN); c.set(17, 11, SKIN)
c.set(18, 11, SKIN); c.set(19, 11, SKIN)

# --- jacket (chef coat) ---
c.rect(9, 12, 14, 8, WHITE)
c.set(8, 12, WHITE); c.set(8, 13, WHITE)     # shoulders
c.set(23, 12, WHITE); c.set(23, 13, WHITE)

# --- apron (flour-dusted) ---
c.rect(11, 13, 10, 7, CREAM)
for x, y in [(12, 14), (14, 16), (16, 14), (18, 16),
             (15, 15), (13, 17), (19, 17)]:
    c.set(x, y, WHITE)

# --- red neckerchief ---
c.rect(13, 12, 6, 1, RED)
c.rect(14, 13, 4, 1, RED)
c.set(15, 13, RED_D); c.set(16, 13, RED_D)

# --- sleeves ---
c.rect(7, 13, 1, 7, WHITE)
c.rect(24, 13, 1, 7, WHITE)

# --- hands gripping the steamer ---
c.rect(6, 19, 1, 3, SKIN)
c.rect(25, 19, 1, 3, SKIN)
c.set(7, 20, SKIN); c.set(7, 21, SKIN)
c.set(24, 20, SKIN); c.set(24, 21, SKIN)

# --- buns on the steamer ---
c.rect(12, 18, 3, 2, BUN)
c.rect(18, 18, 3, 2, BUN)
c.set(12, 19, BUN_SH); c.set(14, 19, BUN_SH)
c.set(18, 19, BUN_SH); c.set(20, 19, BUN_SH)

# --- bamboo steamer basket ---
c.rect(7, 20, 18, 7, BAMBOO)
c.rect(7, 20, 18, 1, BAMBOO_D)   # top rim
c.rect(7, 22, 18, 1, BAMBOO_L)   # slat highlight
c.rect(7, 24, 18, 1, BAMBOO_L)   # slat highlight
c.rect(7, 26, 18, 1, BAMBOO_D)   # bottom rim
c.rect(7, 21, 1, 5, BAMBOO_D)    # side posts
c.rect(24, 21, 1, 5, BAMBOO_D)

# --- legs and shoes ---
c.rect(10, 27, 5, 4, PANTS)
c.rect(17, 27, 5, 4, PANTS)
c.rect(9, 30, 6, 2, SHOE)
c.rect(17, 30, 6, 2, SHOE)

print(c.stats_text())
for p in [(12,18),(13,18),(14,18),(18,18),(19,18),(12,19),(13,19),(7,19),(8,18)]:
    print(p, c.color_name(c.get(*p)))
finish(c)
