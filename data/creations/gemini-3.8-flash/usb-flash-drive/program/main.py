# Ultra-refined USB Flash Drive RPG Item Portrait
c = new_canvas(32, 32)

palette = {
    'X': "#0c0e12",  # Crisp dark outline
    'x': "#1a212b",  # Internal soft shadow / crease
    
    # USB Connector (Metal Plug - Chrome / Stainless Steel)
    'W': "#ffffff",  # Specular white rim/lip
    'a': "#e2e8f0",  # Plug bright face highlight
    'b': "#94a3b8",  # Plug mid steel
    'c': "#64748b",  # Plug dark steel (side face)
    'd': "#3b4754",  # Plug shadow steel
    'K': "#0c1017",  # Cavity interior deep dark
    'u': "#0284c7",  # USB 3.0 blue tongue
    'U': "#38bdf8",  # Blue tongue highlight
    'h': "#111720",  # Stamped hole recess (dark)
    'e': "#cbd5e1",  # Stamped hole bottom highlight rim
    
    # Metal Casing (Brushed Titanium / Anodized Aluminum)
    'H': "#ffffff",  # Top bevel specular ridge
    '1': "#e2e8f0",  # Top face bright highlight
    '2': "#cbd5e1",  # Casing top face bright
    '3': "#94a3b8",  # Casing top face midtone
    '4': "#64748b",  # Casing top face shade
    '5': "#475569",  # Side face shadow
    '6': "#2b3440",  # Side face deep shadow / bottom rim
    '7': "#1e252e",  # Casing front shoulder face
    'z': "#f1f5f9",  # Brushed metal highlight streak
    
    # High-Tech LED
    'Y': "#e0ffff",  # LED core white
    'y': "#00e5ff",  # LED cyan bright
    'g': "#0891b2",  # LED cyan glow
    
    # Metal Split Ring (Keyring)
    'k': "#ffffff",  # Ring specular
    'j': "#cbd5e1",  # Ring bright steel
    'J': "#64748b",  # Ring dark steel
    'q': "#2d3744",  # Ring shadow
    
    # Metal Clasp / Crimp / Rivet
    'm': "#e2e8f0",  # Clasp highlight
    'M': "#526273",  # Clasp shadow
    'v': "#ffffff",  # Silver rivet specular
    'V': "#475569",  # Silver rivet shadow
    
    # Keychain Strap (Woven crimson lanyard)
    'S': "#ff758f",  # Strap stitch / highlight
    's': "#ff2a55",  # Strap bright red face
    'r': "#d90429",  # Strap main crimson
    'R': "#8d0801",  # Strap shadow red
    'D': "#470000",  # Strap fold deep shadow
}

rows = [
#01234567890123456789012345678901
"................................", # 0
".................XXXXX..........", # 1
"................XH1122XX........", # 2
"...............XH1122336X..XXXX.", # 3
"..............XH112233356XXkkjjX", # 4
".............XH11223..356Xk...jX", # 5
"............XH11223..j.56Xj...JX", # 6
"...........XH112233..J.66Xj...JX", # 7
"..........XH11223333366XXX.XqJJX", # 8
".........XH1122gyg3333556X.XmMmX", # 9
"........XH11223yYy333556X..XMMMX", # 10
".......XH112233gyg33556X..XssrrX", # 11
"......XH112233333333556X..XssrrX", # 12
".....XH112233333333556X...XsVvrX", # 13
"....XH112233333333556X....XssrrX", # 14
"....X711122223333556X.....XssrrX", # 15
".....X7777122333556X......XssrrX", # 16
"......XaaaaabbbcccX6X.....XssrrX", # 17
".....XaahhaahhbbccXX......XssrrX", # 18
"....XWaaeebaeeccccX.......XssrrX", # 19
"...XWXaabbbbbbccccX.......XssrrX", # 20
"..XWXaaabbbbbbcccX........XssrrX", # 21
".XWKKaaaabbbbcccX.........XssRRX", # 22
".XKuUUaaabbbcccX..........XssRRX", # 23
".XKuUUabbbccccX...........XsrRDX", # 24
".XKKuuabbccXXX............XSRDDX", # 25
"..XKuUabccX................XDDX.", # 26
"...XdddccX..................XX..", # 27
"....XXXXXX......................", # 28
"................................", # 29
"................................", # 30
"................................", # 31
]

for y, row in enumerate(rows):
    assert len(row) == 32, f"Row {y} length is {len(row)}, expected 32"
    for x, ch in enumerate(row):
        if ch != '.':
            c.set(x, y, palette[ch])

print("Stats:", c.stats_text())
print("Colors used:", c.stats()['colors_used'])
view(c)
finish(c)
