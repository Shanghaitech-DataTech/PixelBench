"""Glow-jellyfish: 16x16 RPG enemy sprite.

Small bioluminescent jellyfish drifting in deep water.
- translucent glowing bell (dome) with specular highlight + mint glow core
- short wavy tentacles hanging from a dark rim
- dark navy outline all round
- fully transparent background
"""

from pixelbench_api import new_canvas, view, save, finish

W = H = 16

PAL = {
    'K': '#0a1424',   # dark outline (abyssal navy)
    'D': '#1d4f7d',   # bell deep shade
    'M': '#3a86c4',   # bell mid tone
    'L': '#63c6ef',   # bell light tone
    'H': '#eafcff',   # specular highlight
    'G': '#9dffe6',   # bioluminescent glow core
    'T': '#8fe9f5',   # tentacle lit
    'S': '#3f8fc0',   # tentacle shade / tips
}

grid = {}


def R(y, *runs):
    """Fill row y from x=0 with (char, count) runs; '.' means transparent."""
    x = 0
    for ch, n in runs:
        for i in range(n):
            if ch != '.':
                grid[(x + i, y)] = ch
        x += n
    assert x == W, (y, x)


# ---------------------------------------------------------------- bell ------
R(0,  ('.', 16))
R(1,  ('.', 6), ('K', 4), ('.', 6))
R(2,  ('.', 5), ('K', 1), ('H', 2), ('L', 2), ('K', 1), ('.', 5))
R(3,  ('.', 4), ('K', 1), ('H', 2), ('L', 2), ('M', 2), ('K', 1), ('.', 4))
R(4,  ('.', 3), ('K', 1), ('H', 1), ('L', 1), ('G', 2), ('M', 2), ('D', 2),
      ('K', 1), ('.', 3))
R(5,  ('.', 2), ('K', 1), ('L', 2), ('G', 3), ('M', 1), ('D', 4), ('K', 1),
      ('.', 2))
R(6,  ('.', 2), ('K', 1), ('M', 2), ('G', 3), ('M', 1), ('D', 4), ('K', 1),
      ('.', 2))
R(7,  ('.', 2), ('K', 1), ('D', 2), ('M', 1), ('G', 2), ('M', 1), ('D', 4),
      ('K', 1), ('.', 2))
R(8,  ('.', 2), ('K', 12), ('.', 2))

# ----------------------------------------------------------- tentacles -----
# six short strands, roots at x = 3,5,7,9,11,13; gentle wave, tapered tips
R(9,  ('.', 3), ('T', 1), ('.', 1), ('T', 1), ('.', 1), ('T', 1), ('.', 1),
      ('T', 1), ('.', 1), ('T', 1), ('.', 1), ('T', 1), ('.', 2))
R(10, ('.', 3), ('T', 1), ('.', 1), ('T', 1), ('.', 1), ('T', 1), ('.', 1),
      ('T', 1), ('.', 1), ('T', 1), ('.', 1), ('T', 1), ('.', 2))
R(11, ('.', 2), ('T', 1), ('.', 2), ('T', 1), ('.', 1), ('T', 1), ('.', 2),
      ('T', 1), ('.', 1), ('T', 1), ('.', 3))
R(12, ('.', 2), ('S', 1), ('.', 2), ('S', 1), ('.', 2), ('T', 1), ('.', 1),
      ('T', 1), ('.', 1), ('S', 1), ('.', 3))
R(13, ('.', 8), ('T', 1), ('.', 1), ('T', 1), ('.', 5))
R(14, ('.', 8), ('S', 1), ('.', 1), ('S', 1), ('.', 5))
R(15, ('.', 16))

# ---------------------------------------------------------------- paint -----
c = new_canvas(W, H, name="glow_jellyfish")
for (x, y), ch in sorted(grid.items(), key=lambda kv: (kv[0][1], kv[0][0])):
    c.set(x, y, PAL[ch])

print(c.stats_text())
print(c.matrix_text())
p = view(c)
print("preview:", p)
save("glow_jellyfish", c)

finish(c)
