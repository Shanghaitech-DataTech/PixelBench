from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32)

OUT = "#1e1e1e"       # dark outline
MID = "#99a3ac"       # casing mid metal
LIGHT = "#c6d0d8"     # casing light
LIGHTER = "#e8eef3"   # bright highlight
SHADOW = "#75808a"    # casing shadow
DARKM = "#57616a"     # dark metal / label
CONN = "#b0bac2"      # connector shell
CONN_D = "#8d979f"    # connector shade
GOLD = "#dcb65e"      # gold contact
GOLD_D = "#a3802c"
STRAP = "#c94f4f"      # red keychain strap
STRAP_L = "#e07a6a"
RING = "#b9c3cc"       # keyring metal
LED = "#4fbf6a"        # indicator led

# --- casing ---
c.rect(8, 11, 17, 14, MID)
c.set(8, 11, None)
c.set(24, 11, None)
c.rect(9, 12, 1, 12, LIGHT)      # left highlight column
c.rect(10, 11, 14, 1, LIGHTER)    # top edge
c.rect(23, 12, 1, 12, SHADOW)     # right shadow
c.rect(9, 23, 15, 2, SHADOW)      # bottom shade
# led + gloss
c.rect(20, 13, 2, 2, LED)
c.set(20, 13, LIGHTER)
# label plate
c.rect(12, 17, 9, 5, DARKM)
c.rect(13, 18, 7, 1, LIGHTER)
# casing outline (rounded top corners)
c.line(9, 11, 23, 11, OUT)
c.line(8, 12, 8, 23, OUT)
c.line(24, 12, 24, 23, OUT)
c.line(8, 24, 24, 24, OUT)

# --- usb connector ---
c.rect(11, 24, 11, 7, CONN)
c.rect(12, 24, 9, 1, LIGHTER)
c.rect(11, 29, 11, 2, CONN_D)
c.rect(12, 25, 9, 4, DARKM)       # open slot
c.rect(13, 26, 7, 2, GOLD)        # gold contacts
c.rect(13, 27, 7, 1, GOLD_D)
c.set(15, 26, DARKM)
c.set(17, 26, DARKM)
c.set(15, 27, DARKM)
c.set(17, 27, DARKM)
c.rect(11, 24, 11, 7, OUT, fill=False)

# --- keychain strap ---
c.rect(14, 7, 5, 5, STRAP)
c.rect(15, 7, 2, 5, STRAP_L)
c.rect(14, 7, 5, 5, OUT, fill=False)

# --- keyring ---
c.circle(16, 5, 3, RING)
c.circle(16, 5, 1, None)
c.circle(16, 5, 3, OUT, fill=False)
c.circle(16, 5, 1, OUT, fill=False)
c.set(14, 3, LIGHTER)

print(c.stats_text())
print(c.matrix_text(region=(8, 2, 24, 30), indices=False))
finish(c)
