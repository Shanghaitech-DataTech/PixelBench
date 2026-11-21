import sys
from pixelbench_api import *

c = new_canvas(32, 32)

PAL = {
    ".": None,
    
    # Outlines & dark crevices
    "#": "#11141a", # deepest outline
    "O": "#1e2530", # dark outline
    "o": "#2e3846", # soft outline / dark metal
    
    # Body Enamel (Crisp laboratory white / cool grey)
    "W": "#ffffff", # pure specular highlight
    "1": "#f1f5f9", # bright white enamel
    "2": "#e2e8f0", # light enamel
    "3": "#cbd5e1", # mid-light enamel
    "4": "#94a3b8", # mid enamel
    "5": "#64748b", # shadow enamel
    "6": "#475569", # deep shadow enamel
    "7": "#334155", # dark crevice
    
    # Dark Stage (Mechanical Slate Metal)
    "S": "#141820", # stage deepest shadow
    "s": "#1e2430", # stage dark
    "m": "#333d4e", # stage mid
    "l": "#4a566c", # stage top plate
    "k": "#718096", # stage edge highlight
    
    # Chrome / Silver
    "C": "#ffffff", # chrome specular
    "c": "#e2e8f0", # chrome highlight
    "h": "#94a3b8", # chrome mid
    "d": "#475569", # chrome shadow
    "e": "#1e293b", # chrome deep
    
    # Gold / Brass Accents (10x objective ring, fine focus knob)
    "Y": "#fef08a", # gold highlight
    "y": "#facc15", # gold bright
    "g": "#ca8a04", # gold mid
    "b": "#854d0e", # gold shadow
    
    # Secondary objective ring (cyan 40x band)
    "v": "#38bdf8", # cyan ring
    "V": "#0284c7", # deep cyan ring
    
    # Optics / Lens Glass / Illuminator Light
    "P": "#ffffff", # bright light source / gleam
    "p": "#e0f2fe", # pale cyan glass
    "t": "#38bdf8", # cyan lens / light beam
    "u": "#0284c7", # deep cyan optical glass
    
    # Glass Slide & Specimen
    "A": "#f0f9ff", # slide highlight
    "a": "#bae6fd", # slide pale cyan glass
    "i": "#7dd3fc", # slide cyan rim
    "R": "#fb7185", # specimen highlight
    "r": "#e11d48", # specimen magenta stain
    "q": "#9f1239", # specimen deep stain
    "z": "#cbd5e1", # slide clip metal (silver)
    
    # Contact Shadow
    "x": "#0a0d12", # ground shadow
}

grid = [
# 00
"................................",
# 01
"................................",
# 02: Eyepiece top rubber eyecup
".......####.....................",
# 03: Eyepiece ocular lens & rim
"......#WPtu#....................",
# 04: Eyepiece chrome ocular collar
"......#chde#....................",
# 05: Eyepiece angled tube
".......#chde#...................",
# 06: Eyepiece tube entering head
"........#1235#..................",
# 07: Head prism block & Arm top arch
".........#112345##..............",
# 08: Head connecting smoothly to Arm arch
"........#1122334455#............",
# 09: Arm arch down right & Turret top left
".......#112345#...#3456#........",
# 10: Turret disc plate
".....##omkhdee##...#246#........",
# 11: 4x obj (left angled) & 10x obj (center)
"....#vV##chde#.....#246#........",
# 12: 4x tip & 10x chrome barrel
"...#u##.#chde#.....#246#........",
# 13: 10x Objective GOLD band
"........#Yygb#.....#245#........",
# 14: 10x Objective tapered dark nose tip
".........#ede#.....#135#........",
# 15: Clear air gap above slide!
"...................#135#........",
# 16: Slide on Stage with Specimen & Clips
"...#OlzAaaRraaaAzlmO##135#......",
# 17: Stage front rim with bevel & clips
"..#OkkkziiiqqiiizkmO#135#.......",
# 18: Stage bevel & Focus Knob top
"..#OmmmmmmmmmmmmmmmmOs#chd#.....",
# 19: Stage thickness & Coarse/Fine Focus Knob
"..#OssssssssssssssssOs#chYye#...",
# 20: Stage bottom, Condenser, Focus Knob
"......#OuteO#...#ssss#hdgbd#....",
# 21: Condenser lower body & Knob bottom
".......#de#.......##24#dede#....",
# 22: Vertical light beam from lamp to condenser
"........#pt#......#1245##.......",
# 23: Illuminator lamp top lens (on base)
"......#cPtde#....#12356#........",
# 24: Illuminator lamp body
"......#hdede#...#112356#........",
# 25: Illuminator collar & Arm base
"......#OdddO#..#1123456#........",
# 26: Base top deck (3/4 perspective)
"....##11112222334455566#........",
# 27: Base upper slope with specular highlight
"..#W1111222334445556666#........",
# 28: Base front beveled face
".#111222333444555666777#........",
# 29: Base bottom rim
".#OOOOOOOOOOOOOOOOOOOOO#........",
# 30: Ground contact shadow
"..xxxxxxxxxxxxxxxxxxxxx.........",
# 31
"................................",
]

for y, row in enumerate(grid):
    assert len(row) == 32, f"Row {y} has length {len(row)}"
    for x, ch in enumerate(row):
        col = PAL[ch]
        if col is not None:
            c.set(x, y, col)

view(c)
finish(c)
