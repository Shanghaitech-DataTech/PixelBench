# Design the cracked stone texture
import numpy as np

PALETTE = [
    "#1a1a1f",  # 0: Deep fissure
    "#2c2c34",  # 1: Crack shadow
    "#42424b",  # 2: Deep crevice / dark stone
    "#565660",  # 3: Dark stone cluster
    "#6d6d78",  # 4: Mid-dark stone
    "#82828d",  # 5: Main midtone
    "#9797a3",  # 6: Light stone cluster
    "#acacb8",  # 7: Crack highlight edge / bright stone
    "#c4c4d0",  # 8: Brightest glint / chipped rim
]

# Let's write a function that builds the 16x16 grid and checks tiling.
