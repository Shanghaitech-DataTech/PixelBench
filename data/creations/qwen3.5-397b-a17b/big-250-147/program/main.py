from pixelbench_api import *

# Make a copy to work on
output = input_canvas.copy(name='output')

# Get canvas dimensions
stats = output.stats()
width, height = stats['size']

# Register blue colors for a clear noon sky
sky_blue = output.color('#87CEEB', 'sky_blue')      # Light sky blue
sky_blue2 = output.color('#5BA3D0', 'sky_blue2')    # Medium sky blue  
bright_blue = output.color('#89CFF0', 'bright_blue') # Baby blue
horizon_blue = output.color('#6BA3C7', 'horizon_blue')  # Horizon blue

# For a noon scene on a clear day:
# 1. Sky should be bright blue gradient
# 2. Sun should NOT be visible (overhead at noon, not in frame)

# Create blue sky gradient, removing the original sunset colors and sun
for y in range(height):
    for x in range(width):
        if y < 60:
            # Top sky - lightest blue
            output.set(x, y, sky_blue)
        elif y < 85:
            # Middle sky - medium blue
            output.set(x, y, bright_blue)
        elif y < 100:
            # Lower sky approaching horizon
            output.set(x, y, sky_blue2)
        elif y < 115:
            # Horizon area - slightly deeper blue
            output.set(x, y, horizon_blue)
        # y >= 115: keep original foreground

print("Final result:")
print(output.stats_text())

# Submit the result
finish(output)
