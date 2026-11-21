from pixelbench_api import new_canvas, finish

c = new_canvas(48, 48)

colors = {
    ' ': None,
    'X': '#2A1813',
    'x': '#4A2E20',
    'o': '#6E452D',
    'O': '#8F5C38',
    'p': '#5E2282',
    '+': '#9A46D4',
    '*': '#D49DFF',
    'W': '#FFFFFF',
}

for k, v in colors.items():
    if v:
        c.color(v, k)

art = [
"                                                ", # 0
"                                                ", # 1
"                                                ", # 2
"                       *                        ", # 3
"                                                ", # 4
"                   +                            ", # 5
"                 XXXX                           ", # 6
"                XXXoxX                          ", # 7
"                  ppXXooxX       +              ", # 8
"             XX  p+*+p XOooxX                   ", # 9
"            XXOXp+WWW+p XOooxX                  ", # 10
"          XOOoxXp+WWW+p  XOooxX                 ", # 11
"        XOOooxX p+WWW+p   XOooxX                ", # 12
"       XOOooxX   p+*+p     XOooxX    *          ", # 13
"      XOOooxX     pp        XOooxX              ", # 14
"      XOxooxX                XOooxX             ", # 15
"       XOOooxX   +            XOooxX            ", # 16
"        XOOooxX              XOooxX             ", # 17
"         XOOooxX            XOooxX              ", # 18
"          XOOooooooooooooooxX                   ", # 19
"            XXooooooooooooxX                    ", # 20
"              XXXXXXXXOooxX            p        ", # 21
"                    XOooxX                      ", # 22
"                   XOooxX                       ", # 23
"         *        XOooxX                        ", # 24
"                 XOooxX                         ", # 25
"                XOooxX                          ", # 26
"      p        XOooxX                           ", # 27
"              XOooxX                            ", # 28
"             XOooxX           +                 ", # 29
"            XOxoxX                              ", # 30
"           XOooxX                               ", # 31
"  +       XOooxX                                ", # 32
"         XOooxX                                 ", # 33
"        XOooxX                                  ", # 34
"       XOooxX                                   ", # 35
"      XOooxX               *                    ", # 36
"     XOooxX                                     ", # 37
"    XOooxX                                      ", # 38
"   XOooxX                                       ", # 39
"  XOooxX                                        ", # 40
" XOooxX                                         ", # 41
"XOooxX                                          ", # 42
"XooxX                                           ", # 43
"XXXX                                            ", # 44
"                                                ", # 45
"                                                ", # 46
"                                                ", # 47
]

for y, row in enumerate(art):
    for x, char in enumerate(row):
        if char != ' ':
            c.set(x + 5, y, char)

finish(c)
