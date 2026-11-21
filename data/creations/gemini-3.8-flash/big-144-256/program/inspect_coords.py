# Inspect doorway area
# Let's find coordinates around x=30..90, y=150..230
print("Canvas size:", input_canvas.stats())

# Let's inspect the colors used in input_canvas
palette = input_canvas.palette()
print(f"Total colors: {len(palette)}")

# Let's write out some coordinate checks
# Archway doorway:
# Lanterns are visible around x=45, y=185 and x=75, y=185 approximately.
# Let's inspect the slice
output = input_canvas.copy(name='output')
finish(output)
