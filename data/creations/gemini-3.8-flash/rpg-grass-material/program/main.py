c = new_canvas(16, 16)

PALETTE = {
    # Grass tones - lush 16-bit RPG greens
    '.': "#458731", # Base rich grass green
    '-': "#5ea837", # Mid-light green
    '+': "#82c53f", # Bright green blade / speckle
    '^': "#ade452", # Sunlit blade tip
    ',': "#346e27", # Soft shadow green
    'x': "#23521c", # Dark blade shadow / tuft base
    'X': "#153a13", # Deep shadow crevice

    # Border between grass and dirt
    'g': "#3b5021", # Earthy mossy-green

    # Bare dirt tones (warm, natural earthy soil)
    'd': "#463019", # Dark dirt edge
    'D': "#6a4a27", # Warm brown earth
    'L': "#8e6739", # Sunlit dry earth / pebble

    # Flowers (wild yellow buttercups)
    'F': "#fed834", # Golden yellow petal
    'H': "#fff682", # Sunlit pale petal highlight
    'O': "#da7b15", # Amber orange center
    's': "#1e461b", # Flower stem / root shadow
}

grid = [
    # 0123456789012345
    ",..-..-...-..-..", # 0
    "..-..^.,.^..-..-", # 1
    ".,..+x.,+x-..-..", # 2
    "..gd.xxX.x..H...", # 3
    ".gDLd.-...FOHF.-", # 4
    ".,Dd.,..-..Fs.s.", # 5
    ".,.-..-.,..+.-..", # 6
    ".-..,.+-.H..-..^", # 7
    ",..-..-..F..-..+", # 8
    "..-..-..+s-..-xX", # 9
    ".+-,..-,xx,..+..", # 10
    "-...,..x..,..gd.", # 11
    "..HF..-...,.gDLd", # 12
    ".FOHF-..+-,..Dg.", # 13
    "..s.x,..-...,..-", # 14
    "-,..-,+..,-..-.,", # 15
]

for y, row in enumerate(grid):
    for x, ch in enumerate(row):
        c.set(x, y, PALETTE[ch])

print("Stats:", c.stats())
finish(c)
view(c)
