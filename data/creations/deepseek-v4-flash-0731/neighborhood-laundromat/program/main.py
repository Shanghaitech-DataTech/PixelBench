from pixelbench_api import new_canvas, finish, save

c = new_canvas(64, 64)

OUT = "#31414f"

# --- room structure (one-point perspective interior) ---
c.poly([(0,0),(63,0),(50,18),(14,18)], "#9fb2c4")      # ceiling
c.poly([(14,18),(50,18),(50,44),(14,44)], "#d9e6f0")   # back wall
c.poly([(0,0),(14,18),(14,44),(0,63)], "#c7d6e2")      # left wall
c.poly([(63,0),(50,18),(50,44),(63,63)], "#c0d0de")    # right wall
c.poly([(14,44),(50,44),(63,63),(0,63)], "#aebfd0")    # floor

# tile seams / cool floor hints
c.line(23,44,14,63,"#a2b4c6")
c.line(32,44,32,63,"#a2b4c6")
c.line(41,44,50,63,"#a2b4c6")
c.line(9,49,55,49,"#a2b4c6")
c.line(4,57,60,57,"#a2b4c6")

# baseboards and corner seams
c.line(14,44,0,63,"#8fa4b8")
c.line(50,44,63,63,"#8fa4b8")
c.line(14,18,14,44,"#8fa4b8")
c.line(50,18,50,44,"#8fa4b8")
c.line(0,0,14,18,"#8fa4b8")
c.line(63,0,50,18,"#8fa4b8")

# ceiling fluorescent tubes (cool white lighting)
for x in (12,26,40):
    c.rect(x,4,14,2,"#d8e6f2")
    c.rect(x+1,5,12,1,"#eef6ff")
    c.rect(x+2,3,12,1,"#f4fbff")
    c.rect(x+2,6,12,1,"#f4fbff")
    c.rect(x+1,4,12,1,"#ffffff")

# wall clock on the back wall
c.circle(32,21,3,OUT)
c.circle(32,21,2,"#f4f8fc")
c.line(32,21,32,19,"#2a3a48")
c.line(32,21,34,21,"#2a3a48")
c.circle(32,21,1,OUT)
c.set(32,18,"#e05a5a")

# posters on the back wall
c.rect(19,18,4,4,"#8ec8ee"); c.rect(19,18,4,4,OUT,fill=False)
c.rect(41,18,4,4,"#f2b8c8"); c.rect(41,18,4,4,OUT,fill=False)

def machine(x, y, w, h, side):
    cx = x + w // 2
    # contact shadow
    c.rect(x-1, y+h, w+2, 1, "#8fa4b8")
    # body
    c.rect(x, y, w, h, "#eef4f9")
    if side == "R":
        c.rect(x+w, y+1, 2, h-2, "#ccd9e4")
        c.rect(x+w+1, y+2, 1, h-4, "#b3c6d6")
    else:
        c.rect(x-2, y+1, 2, h-2, "#ccd9e4")
        c.rect(x-2, y+2, 1, h-4, "#b3c6d6")
    # base
    c.rect(x+1, y+h-2, w-2, 2, "#2e4052")
    c.rect(x+3, y+h-1, w-6, 1, "#1e2c38")
    # control panel
    c.rect(x, y, w, 3, "#41566a")
    c.rect(x+1, y+1, 4, 1, "#1e2c38")
    c.set(x+7, y+1, "#ffd166")
    c.set(x+6, y+2, "#5ad0a0")
    # front-loading door
    c.circle(cx, y+8, 3, "#7d94a8")
    c.circle(cx, y+7, 3, "#a8d8ee")
    c.circle(cx, y+7, 2, "#7fc0e0")
    c.circle(cx-1, y+6, 1, "#d8f2fc")
    c.set(cx-1, y+4, "#f4fbff")
    # outline + top highlight
    c.rect(x, y, w, h, OUT, fill=False)
    c.rect(x+1, y+1, w-2, 1, "#ffffff")

# back row of three machines along the wall
machine(15,25,10,12,"R")
machine(27,25,10,12,"R")
machine(39,25,10,12,"L")

# front row of two machines on the floor
machine(14,44,10,12,"R")
machine(41,44,10,12,"L")

# folding table with folded laundry, between the front machines
c.rect(27,47,12,3,"#cfe4f2")
c.rect(28,47,10,1,"#eaf6ff")
c.rect(27,47,12,3,OUT,fill=False)
c.rect(28,50,2,7,"#9cb8cc")
c.rect(36,50,2,7,"#9cb8cc")
c.rect(27,57,12,1,"#9cb8cc")
c.rect(29,45,5,2,"#8ec8ee")
c.rect(35,45,4,2,"#f2b8c8")
c.rect(31,44,3,1,"#f4e4b8")

# laundry basket on the floor, left of the front-left machine
c.rect(7,56,7,7,"#d8a878")     # body
c.rect(7,58,7,1,"#b07e50")
c.rect(7,60,7,1,"#b07e50")
c.rect(7,62,7,1,"#b07e50")
c.rect(8,55,5,2,"#eef4f9")      # laundry peeking out
c.rect(6,55,8,2,"#c08a5a")     # rim
c.rect(6,55,8,2,OUT,fill=False)
c.rect(7,56,7,7,OUT,fill=False)

print(c.stats_text())
save("laundromat", c)
finish(c)
