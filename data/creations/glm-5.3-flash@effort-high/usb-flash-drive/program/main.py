# USB Flash Drive - RPG item portrait, 32x32, transparent background
DARK    = "#23272e"   # dark outline
MET_L   = "#e4e8ec"   # metal highlight
MET_M   = "#aab2ba"   # metal mid
MET_D   = "#767f88"   # metal shadow
SHELL_L = "#c9cfd6"   # connector highlight
SHELL_M = "#9aa3ac"   # connector mid
SHELL_D = "#6b747d"   # connector shadow
GOLD    = "#d9b45e"   # contact gold
GOLD_D  = "#9c7c33"   # contact gold shadow
RED     = "#c0392b"   # strap
RED_D   = "#7e241a"   # strap shadow
LED     = "#7ee081"   # activity LED

c = new_canvas(32, 32, background=None, name="usb_flash_drive")

# ---------- keychain ring (dark rim + red ring) ----------
c.circle(16, 4, 4, DARK, fill=False)          # dark outline rim
c.circle(16, 4, 3, RED, fill=False)           # red keyring
c.set(19, 4, RED_D); c.set(18, 2, RED_D)      # shade right of ring
c.set(19, 5, RED_D)

# ---------- USB connector (metal shell) ----------
c.rect(11, 6, 10, 7, DARK)                    # outline block x11-20, y6-12
c.rect(12, 7, 8, 5, SHELL_M)                  # inner face
c.rect(12, 7, 2, 5, SHELL_L)                  # left highlight
c.rect(18, 7, 2, 5, SHELL_D)                  # right shadow
c.rect(13, 7, 2, 4, GOLD)                     # contact slot 1
c.rect(17, 7, 2, 4, GOLD)                     # contact slot 2
c.rect(13, 10, 2, 1, GOLD_D)
c.rect(17, 10, 2, 1, GOLD_D)
c.line(12, 6, 19, 6, SHELL_L)                 # top edge catch-light

# ---------- metal casing (rounded corners) ----------
c.rect(9, 12, 14, 15, DARK)                   # outline x9-22, y12-26
c.rect(10, 13, 12, 13, MET_M)                 # body
c.set(10, 13, DARK); c.set(21, 13, DARK)      # round top corners
c.set(10, 25, DARK); c.set(21, 25, DARK)      # round bottom corners
c.rect(10, 13, 3, 13, MET_L)                  # left highlight
c.set(10, 13, MET_L); c.set(10, 25, MET_D)
c.rect(19, 13, 3, 13, MET_D)                  # right shadow
c.set(21, 13, MET_D)
c.line(13, 17, 18, 17, MET_D)                 # engraved groove
c.line(13, 18, 18, 18, MET_L)                 # groove lower edge
c.line(10, 25, 21, 25, MET_D)                 # bottom inner shadow
c.rect(19, 14, 2, 2, LED)                     # activity LED
c.set(19, 14, MET_D); c.set(20, 16, MET_D)    # LED shadow edge

# ---------- enchanted gem (RPG flair) ----------
c.rect(14, 20, 6, 5, DARK)                    # gem outline
c.rect(15, 21, 4, 3, "#4aa3df")               # gem core
c.set(15, 21, "#9fd8f7")                      # gem sparkle
c.set(18, 23, "#2b6f9e")                      # gem shadow

print(c.stats_text())
print(c.matrix_text())
save("usb_flash_drive", c)
finish(c)
