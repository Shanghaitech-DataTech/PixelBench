from pixelbench_api import new_canvas, finish

W = H = 32
c = new_canvas(W, H)

# palette
dark      = c.color("#1c1510")  # thick dark outline
gold      = c.color("#e8b93a")
gold_light= c.color("#ffdf7e")
gold_dark = c.color("#b07f1a")
blue_deep = c.color("#0d3670")
blue_mid  = c.color("#1e6ccf")
blue_light= c.color("#4da3ff")
blue_pale = c.color("#a8dcff")
white     = c.color("#ffffff")
needle    = c.color("#2b3c52")

cx, cy = 15, 15

# body: dark outline -> gold ring -> dark band -> crystal
c.circle(cx, cy, 15, dark)
c.circle(cx, cy, 11, gold)
c.circle(cx, cy, 7, dark)
c.circle(cx, cy, 10, gold_light, fill=False)   # rim highlight ring
c.circle(cx, cy, 6, blue_deep)                # crystal base
c.circle(cx, cy, 4, blue_mid)
c.circle(cx, cy, 3, blue_light, fill=False)   # facet ring

# cardinal ticks on the gold rim
c.rect(15, 4, 1, 3, dark)    # N
c.rect(15, 24, 1, 3, dark)   # S
c.rect(4, 14, 3, 1, dark)    # W
c.rect(24, 14, 3, 1, dark)   # E

# gold studs on the outer dark border
c.rect(14, 1, 3, 2, gold_light)
c.rect(14, 29, 3, 2, gold_light)
c.rect(1, 14, 2, 3, gold_light)
c.rect(29, 14, 2, 3, gold_light)

# needle over the crystal
c.poly([(15, 9), (13, 15), (17, 15)], gold_light)   # north half
c.poly([(15, 21), (13, 15), (17, 15)], needle)      # south half
c.circle(cx, cy, 1, gold_dark)                      # hub

# sparkle highlights
c.set(12, 12, white)
c.set(11, 13, blue_pale)

# center the 31px icon in the 32px canvas (bbox 1..31)
c.shift(1, 1)

print(c.stats_text())
finish(c)
