from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64, background="#dce7ed", name="lab_workbench")

P = {
    "wall":    "#dce7ed",
    "tile":    "#c9d7df",
    "poster":  "#f2e8c8",
    "desk_top":"#c58a52",
    "desk_mid": "#a06a3a",
    "desk_dark":"#7c4e26",
    "desk_line":"#5f3a16",
    "shadow":  "#9a6036",
    "shelf":   "#b5844f",
    "shelf_dk":"#8a5c30",
    "mb":      "#50545e",
    "md":      "#3d4048",
    "mm":      "#6a6f7a",
    "met":     "#a8b0bc",
    "metd":    "#7e8896",
    "gls":     "#d8e6ee",
    "glsd":    "#9fb6c6",
    "knob":    "#2c2e36",
    "tgl":     "#d6eaf2",
    "topen":   "#3e5a6e",
    "lr":      "#d94f4f",
    "lb":      "#3f7fd6",
    "lg":      "#4caf60",
    "capb":    "#2f6fb0",
    "capr":    "#c0392b",
    "capg":    "#3f9e4d",
    "bgl":     "#cfe6ee",
    "bout":    "#8fb8c8",
    "bliq":    "#8fd0ee",
    "bhi":     "#eaf4f8",
    "rub":     "#3f3f46",
    "rubh":    "#5a5a64",
    "page":    "#f6f2e8",
    "psh":     "#d8d0bc",
    "rule":    "#c9d2dd",
    "mg":      "#d8706a",
    "ink":     "#33415c",
    "pen":     "#2c4a8a",
    "ptip":    "#b98a3c",
}
for n, v in P.items():
    c.color(v, name=n)

# ---- room / wall ----
for yy in (6, 14, 22, 30, 38):
    c.rect(0, yy, 64, 1, "tile")

# ---- wall poster (chart) ----
c.rect(52, 20, 10, 11, "poster")   # paper, rows 20..30
c.rect(57, 24, 2, 6, "lg")         # green bar, rows 24..29
c.rect(60, 26, 2, 4, "lr")         # red bar, rows 26..29

# ---- shelf + labeled bottles ----
c.rect(26, 12, 3, 3, "shelf_dk")
c.rect(42, 12, 3, 3, "shelf_dk")
c.rect(24, 10, 22, 3, "shelf")     # shelf board rows 10..12
c.rect(24, 12, 22, 1, "shelf_dk")

def bottle(cx, cap):
    c.rect(cx, 1, 4, 4, cap)        # cap
    c.rect(cx, 5, 6, 5, "bgl")      # glass body rows 5..9
    c.rect(cx, 6, 6, 3, "page")     # label rows 6..8

bottle(25, "capb")
bottle(33, "capr")
bottle(40, "capg")

# ---- microscope (left) ----
c.rect(2, 40, 19, 6, "mb")         # base rows 40..45
c.rect(2, 40, 19, 1, "mm")
c.rect(13, 20, 8, 21, "mb")         # back arm rows 20..40
c.rect(4, 16, 17, 5, "mb")          # head rows 16..20
c.rect(4, 12, 6, 4, "mb")           # eyepiece rows 12..15
c.rect(4, 12, 6, 1, "md")           # eyepiece rim
c.rect(5, 20, 8, 9, "mb")           # tube rows 20..28
c.rect(1, 29, 17, 2, "met")         # stage rows 29..30
c.rect(1, 30, 17, 1, "metd")
c.rect(6, 26, 7, 4, "mb")           # objective rows 26..29
c.rect(3, 29, 9, 1, "gls")          # slide on stage
c.rect(12, 41, 5, 2, "knob")        # focus knob

# ---- test-tube rack ----
c.rect(25, 32, 16, 14, "shelf")     # rack block rows 32..45
c.rect(25, 35, 1, 10, "shelf_dk")
c.rect(40, 35, 1, 10, "shelf_dk")
for x, liq in ((27, "lr"), (31, "lb"), (35, "lg")):
    c.rect(x, 21, 3, 11, "tgl")      # tube rows 21..31
    c.rect(x, 21, 3, 1, "topen")     # tube mouth
    c.rect(x, 26, 3, 6, liq)         # liquid rows 26..31
    c.rect(x, 22, 1, 2, "bhi")       # shine

# ---- beaker + dropper ----
c.rect(41, 31, 11, 1, "bout")       # rim
c.rect(42, 32, 9, 14, "bgl")         # beaker rows 32..45
c.rect(43, 33, 1, 9, "bhi")          # highlight
c.rect(43, 37, 6, 8, "bliq")         # liquid rows 37..44
c.line(48, 28, 46, 40, "bgl")    # pipette glass
c.line(47, 28, 45, 40, "bhi")    # pipette glass
c.circle(47, 27, 2, "rub")            # rubber bulb rows 25..29

# ---- desk ----
c.rect(0, 43, 64, 6, "desk_top")     # desk top rows 43..48
c.rect(0, 49, 64, 15, "desk_mid")     # desk front rows 49..63
c.rect(0, 49, 64, 1, "desk_dark")
c.rect(0, 54, 64, 1, "desk_dark")
c.rect(0, 60, 64, 1, "desk_dark")
for hx in (12, 30, 48):
    c.rect(hx, 57, 5, 2, "desk_line")

# ---- open laboratory notebook (on desk) ----
c.rect(51, 41, 13, 4, "page")        # pad rows 41..44
c.rect(52, 42, 1, 3, "mg")           # red margin line
c.rect(53, 43, 10, 1, "rule")
c.rect(53, 45, 10, 1, "rule")
c.line(54, 44, 60, 41, "pen")
c.set(61, 40, "ptip")

# ---- contact shadows ----
c.rect(3, 46, 18, 1, "shadow")
c.rect(25, 46, 16, 1, "shadow")
c.rect(42, 46, 8, 1, "shadow")
c.rect(51, 45, 13, 1, "shadow")

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 31)))
print(c.matrix_text(region=(0, 32, 63, 63)))

finish(c)
