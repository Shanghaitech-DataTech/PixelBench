output = input_canvas.copy(name="output")

# Palette shortcuts
BG = 1
DKC = 5       # [94, 54, 62] (dark chocolate outline/shadow)
DKC_ALT = 6   # [97, 54, 61]
DKC_DARK = 14 # [83, 52, 68]
DKC_WARM = 28 # [93, 57, 61]
DKC2 = 2      # [97, 57, 66]

MDC = 18      # [149, 82, 76] (mid chocolate body)
MDC_DARK = 26 # [154, 84, 82]
LTC = 34      # [196, 111, 91] (light chocolate highlight)
LTC2 = 35     # [195, 113, 91]

WHI = 31      # [254, 244, 245] (white sparkle)
LAV = 9       # [197, 196, 228] (lavender specular shine)
LAV2 = 40     # [202, 195, 228]

# Cone colors
GLD = 7       # [253, 189, 99] (golden cone)
YEL = 50      # [253, 251, 213] (light yellow waffle)
YEL_ALT = 51  # [254, 251, 218]
CSH = 48      # [228, 134, 100] (cone shadow)
CSH_DK = 14   # [194, 82, 45] (cone dark shadow)
CSH_MID = 42  # [238, 150, 102]
CSH_DEEP = 54 # [229, 136, 102]

def p(x, y, c):
    output.set(x, y, c)

# =========================================================================
# 1. SCOOP MELTING FLOW (y=28..32)
# Liquid chocolate melting down from the scoop towards the drips
# =========================================================================
# Flow toward the main center drip:
p(26, 29, DKC)
p(27, 29, MDC)
p(28, 29, MDC)
p(29, 29, LTC)

p(26, 30, DKC)
p(27, 30, MDC)
p(28, 30, MDC)
p(29, 30, LTC)

p(26, 31, DKC)
p(27, 31, MDC)
p(28, 31, MDC)
p(29, 31, LTC)

# Flow toward the right drip:
p(35, 28, MDC)
p(36, 28, LTC)
p(37, 28, LTC)

p(35, 29, MDC)
p(36, 29, LTC)
p(37, 29, LTC)

p(35, 30, MDC)
p(36, 30, LTC)
p(37, 30, LTC)

p(35, 31, MDC)
p(36, 31, LTC)
p(37, 31, LTC)

# Arc of scoop rim between center drip and right drip (x=30..34, y=32):
p(30, 32, DKC)
p(31, 32, DKC)
p(32, 32, DKC)
p(33, 32, DKC)
p(34, 32, DKC)

# Cone showing cleanly under the scoop rim at y=33..34 (between drips):
p(30, 33, GLD); p(31, 33, GLD); p(32, 33, GLD); p(33, 33, GLD); p(34, 33, GLD)
p(30, 34, GLD); p(31, 34, GLD); p(32, 34, GLD); p(33, 34, GLD); p(34, 34, GLD)

# =========================================================================
# 2. LEFT MELTING DROOP (x=19..22, y=32..34)
# An organic rounded droop of chocolate sagging down the left rim
# =========================================================================
p(19, 32, DKC)
p(20, 32, DKC)
p(21, 32, DKC)
p(22, 32, DKC)

p(19, 33, DKC)
p(20, 33, DKC_ALT)
p(21, 33, DKC)

p(20, 34, DKC)
p(20, 35, CSH_DK) # cast shadow under droop

# =========================================================================
# 3. HERO CENTER DRIP (x=24..30, y=32..44)
# Long, luscious drip running down the cone with specular shine
# =========================================================================
# Base (y=32)
p(25, 32, DKC)
p(26, 32, MDC)
p(27, 32, MDC)
p(28, 32, LTC)
p(29, 32, DKC)

# Upper neck (y=33..34)
p(25, 33, DKC); p(26, 33, MDC); p(27, 33, MDC); p(28, 33, LTC); p(29, 33, DKC)
p(25, 34, DKC); p(26, 34, MDC); p(27, 34, MDC); p(28, 34, LTC); p(29, 34, DKC)

# Tapered neck (y=35..37)
p(26, 35, DKC); p(27, 35, MDC); p(28, 35, LTC); p(29, 35, DKC)
p(26, 36, DKC); p(27, 36, MDC); p(28, 36, LTC); p(29, 36, DKC)
p(26, 37, DKC); p(27, 37, MDC); p(28, 37, LTC); p(29, 37, DKC)

# Swelling into bulb (y=38..39)
p(25, 38, DKC); p(26, 38, MDC); p(27, 38, MDC); p(28, 38, LTC); p(29, 38, DKC)
p(25, 39, DKC); p(26, 39, MDC); p(27, 39, MDC); p(28, 39, LTC); p(29, 39, DKC)

# Bulb widest section (y=40..42)
p(24, 40, DKC); p(25, 40, MDC); p(26, 40, MDC); p(27, 40, MDC); p(28, 40, LTC); p(29, 40, LTC); p(30, 40, DKC)
# Specular highlight on glossy liquid chocolate:
p(24, 41, DKC); p(25, 41, MDC); p(26, 41, MDC); p(27, 41, LAV); p(28, 41, WHI); p(29, 41, LTC); p(30, 41, DKC)
p(24, 42, DKC); p(25, 42, MDC); p(26, 42, MDC); p(27, 42, MDC); p(28, 42, LTC); p(29, 42, DKC)

# Bulb bottom rounding (y=43..44)
p(25, 43, DKC); p(26, 43, MDC); p(27, 43, MDC); p(28, 43, DKC)
p(26, 44, DKC); p(27, 44, DKC)

# Cast shadows on cone surface to give 3D depth:
p(25, 35, CSH_DK)
p(25, 36, CSH_DK)
p(25, 37, CSH_DK)
p(24, 38, CSH_DK)
p(24, 39, CSH_DK)
p(23, 40, CSH_DK)
p(23, 41, CSH_DK)
p(23, 42, CSH_DK)
p(24, 43, CSH_DK)
p(25, 44, CSH_DK)
p(26, 45, CSH_DK)
p(27, 45, CSH_DK)

# =========================================================================
# 4. DETACHED FALLING DROPLET (x=26..28, y=48..51)
# Droplet falling down the cone
# =========================================================================
p(27, 48, DKC)
p(26, 49, DKC); p(27, 49, MDC); p(28, 49, DKC)
p(26, 50, DKC); p(27, 50, LAV); p(28, 50, DKC)
p(27, 51, DKC)
p(27, 52, CSH_DK) # cast shadow

# =========================================================================
# 5. RIGHT DRIP (x=35..38, y=32..39)
# Secondary drip on the right side of the cone
# =========================================================================
p(35, 32, DKC); p(36, 32, MDC); p(37, 32, LTC); p(38, 32, DKC)
p(35, 33, DKC); p(36, 33, MDC); p(37, 33, LTC); p(38, 33, DKC)
p(35, 34, DKC); p(36, 34, MDC); p(37, 34, LTC); p(38, 34, DKC)
p(35, 35, DKC); p(36, 35, MDC); p(37, 35, LTC); p(38, 35, DKC)

# Bulb with shine (y=36..37)
p(34, 36, DKC); p(35, 36, MDC); p(36, 36, LTC); p(37, 36, LAV); p(38, 36, DKC)
p(34, 37, DKC); p(35, 37, MDC); p(36, 37, LTC); p(37, 37, DKC)

# Bulb rounding and tip (y=38..39)
p(35, 38, DKC); p(36, 38, MDC); p(37, 38, DKC)
p(36, 39, DKC)
p(36, 40, CSH_DK) # cast shadow

# Clean cone highlights on the right of right drip:
p(39, 33, GLD); p(39, 34, GLD); p(39, 35, GLD); p(39, 36, GLD); p(39, 37, GLD)
p(38, 38, GLD)
p(37, 39, GLD)

view(output)
finish(output)
