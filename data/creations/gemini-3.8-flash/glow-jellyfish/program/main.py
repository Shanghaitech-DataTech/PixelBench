from pixelbench_api import *

c = new_canvas(16, 16)

# Palette
OUT = "#080b18"        # Crisp dark outline
OUT_SOFT = "#081b2e"   # Deep shadow outline for tentacles
WHT = "#ffffff"        # Specular glint & glowing core center

# Translucent Cyan Bell ramp
C_RIM = "#d8ffff"      # Specular top rim
C_LGT = "#5cf2ff"      # Glowing cyan
C_MID = "#20c2eb"      # Vibrant cyan
C_BLU = "#1088b8"      # Mid-dark cyan
C_DRK = "#0a557a"      # Deep translucent cyan
C_SHD = "#063650"      # Shadow tone of bell
C_CAV = "#041e30"      # Underside cavity depth

# Inner Core ramp (bioluminescent organ)
M_WHT = "#ffffff"      # Core white-hot center
M_LGT = "#ffbbf2"      # Pink glow halo
M_VIB = "#ee22b4"      # Vibrant electric magenta
M_DRK = "#850965"      # Deep purple core edge
M_DEEP = "#440338"     # Dark core shadow

# Tentacle tones
T_TIP = "#ffffff"      # Bioluminescent tip
T_HL  = "#a6fcff"      # Bright highlight
T_CYAN= "#42e4ff"      # Main glowing tentacle
T_MID = "#149ec9"      # Mid tone
T_SHD = "#0a4563"      # Shadow tone

pattern = [
    # 0123456789012345
    "................", # 0
    "......BBBB......", # 1  Top outline
    "....BBCCCCBB....", # 2  Upper dome
    "...BCWWCCCrrB...", # 3  Highlight & mid cyan
    "..BCWCCMMCrmdB..", # 4  Translucent dome, core top
    "..BCmCMWWMrmdB..", # 5  Core bright center
    "..BCmMMWWMMmdB..", # 6  Core mid
    "..BCuCMDDMCudB..", # 7  Core base, cavity starts
    "..BBddvssvddBB..", # 8  Scalloped rim & cavity
    "..B1.s2..2s.1B..", # 9  Tentacles emerge
    "..B1.sT..Ts.1B..", # 10 Tentacles wave
    "...B*.sTTs.*B...", # 11 Outer tips curl inward
    ".......**.......", # 12 Inner tips glowing
    "................", # 13
    "................", # 14
    "................", # 15
]

cmap = {
    'B': OUT,
    's': OUT_SOFT,
    'W': WHT,
    'C': C_RIM,
    'r': C_MID,
    'm': C_LGT,
    'd': C_DRK,
    'u': C_CAV,
    'v': C_CAV,
    'M': M_VIB,
    'D': M_DRK,
    '1': T_CYAN,
    '2': T_MID,
    'T': T_HL,
    '*': T_TIP,
}

for y, row in enumerate(pattern):
    for x, ch in enumerate(row):
        if ch in cmap:
            c.set(x, y, cmap[ch])

view(c)
finish(c)
