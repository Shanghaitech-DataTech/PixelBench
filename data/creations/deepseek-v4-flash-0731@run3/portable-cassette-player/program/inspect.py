from pixelbench_api import load

c = load("exports/cassette-player.pixelart.json", add=False)
print(c.matrix_text())
