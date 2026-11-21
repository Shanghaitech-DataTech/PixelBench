# Build canvas for testing
w, h = 37, 27
dx, dy = 5, 4

f1 = new_canvas(w, h, name="f1")
f1.blit(input_canvas, dx, dy)

# Create f2 with the same body
f2 = new_canvas(w, h, name="f2")
# Blit input canvas, but we will erase the drooping wings
f2.blit(input_canvas, dx, dy)

# Erase original wings on f2:
# In input_canvas, original body was columns 9..17, rows 0..15.
# Wait, let's precisely check which pixels of input_canvas belong to the body vs wings!
