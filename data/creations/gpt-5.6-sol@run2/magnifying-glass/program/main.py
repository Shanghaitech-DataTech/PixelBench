from pixelbench_api import new_canvas, view, finish

# 16x16 detective-game magnifying glass icon.
result = new_canvas(16, 16, background=None, name="magnifying-glass")

outline = "#171820"
deep = "#33333d"
brass_dark = "#8a5525"
brass = "#d5963c"
brass_light = "#f0c66b"
lens_dark = "#3f7187"
lens = "#75b6c5"
lens_light = "#bde8e5"
wood_dark = "#6f3624"
wood = "#a95732"
wood_light = "#d57a43"

# Round lens silhouette and heavy noir-style outline.
result.rect(4, 1, 5, 1, outline)
result.rect(2, 2, 9, 1, outline)
result.rect(1, 3, 2, 6, outline)
result.rect(10, 3, 2, 6, outline)
result.rect(2, 9, 2, 2, outline)
result.rect(4, 10, 6, 2, outline)
result.rect(9, 9, 2, 2, outline)

# Brass ring.
result.rect(4, 2, 5, 1, brass_light)
result.set(3, 2, brass)
result.set(9, 2, brass_dark)
result.rect(2, 3, 1, 5, brass)
result.set(3, 3, brass_light)
result.rect(10, 4, 1, 4, brass_dark)
result.set(9, 3, brass)
result.set(3, 9, brass_dark)
result.rect(4, 10, 5, 1, brass_dark)
result.set(9, 9, brass_dark)
result.set(2, 8, brass_dark)

# Cool glass interior, with stepped highlights and lower shadow.
result.rect(4, 3, 5, 1, lens)
result.rect(3, 4, 7, 4, lens)
result.rect(4, 8, 5, 2, lens_dark)
result.set(3, 8, lens)
result.set(9, 8, lens_dark)
result.rect(4, 4, 2, 1, lens_light)
result.set(3, 5, lens_light)
result.set(6, 4, "#9bd5d6")
result.set(8, 7, "#5d93a4")
result.set(7, 8, "#56899a")

# Reinforced neck joining lens to handle.
result.set(10, 9, outline)
result.set(11, 9, outline)
result.rect(10, 10, 3, 3, outline)
result.set(9, 10, outline)
result.set(12, 12, outline)
result.set(10, 10, brass_light)
result.set(11, 10, brass)
result.set(11, 11, brass_dark)

# Diagonal wooden handle, outlined for game-inventory readability.
result.set(12, 11, outline)
result.set(13, 11, outline)
result.rect(12, 12, 3, 3, outline)
result.set(11, 13, outline)
result.set(13, 15, outline)
result.set(14, 15, outline)
result.set(15, 13, outline)
result.set(15, 14, outline)
result.set(12, 12, wood_light)
result.set(13, 12, wood)
result.set(12, 13, wood)
result.set(13, 13, wood_light)
result.set(14, 13, wood_dark)
result.set(13, 14, wood)
result.set(14, 14, wood_dark)

view(result, scale=24, margin=1, edges="all")
finish(result)
