from pixelbench_api import *

c = new_canvas(64, 64, background="#8fb8d8", name="wind_platform")

SKY_TOP="#a9cfe8"; SKY_MID="#8fb8d8"; SKY_LOW="#c3d9e6"
SEA_DK="#2e5f7a"; SEA="#3f7d99"; SEA_LT="#5b9db8"; FOAM="#dceef5"
STEEL="#c8cdd2"; STEEL_DK="#8b939b"; STEEL_SH="#5a6169"; RUST="#a8623a"
YELLOW="#f2c53d"; ORANGE="#e07b2a"; DARK="#2b2f36"; SKIN="#e0a878"
WHITE="#f2f6f8"

# --- sky gradient ---
for y in range(0, 42):
    col = SKY_TOP if y < 14 else (SKY_MID if y < 30 else SKY_LOW)
    c.rect(0, y, 64, 1, col)

# clouds
c.rect(8, 8, 12, 2, WHITE); c.rect(10, 6, 8, 2, WHITE)
c.rect(40, 14, 14, 2, WHITE); c.rect(43, 12, 7, 2, WHITE)
c.rect(24, 20, 8, 1, WHITE)

# --- sea ---
for y in range(42, 64):
    c.rect(0, y, 64, 1, SEA if y < 46 else SEA_DK)
# horizon shimmer
for x in range(0, 64, 3):
    c.set(x, 42, SEA_LT)

# --- distant turbines (left area) ---
def distant(tx, base_y, h):
    # tower
    for i in range(h):
        c.set(tx, base_y - i, STEEL_DK)
    # nacelle + blades
    c.rect(tx-1, base_y-h-1, 2, 2, STEEL_DK)
    c.line(tx, base_y-h, tx+4, base_y-h-4, STEEL_DK)
    c.line(tx, base_y-h, tx-3, base_y-h-5, STEEL_DK)
    c.line(tx, base_y-h, tx-1, base_y-h+4, STEEL_DK)
distant(10, 42, 10)
distant(22, 42, 8)

# --- main turbine: tower from sea y=42 up to nacelle y=8 ---
tx = 44  # tower center x
for y in range(9, 43):
    w = 1 if y < 22 else (2 if y < 34 else 3)
    c.rect(tx - w//2, y, w+1, 1, STEEL)
    c.set(tx + w//2 + 1, y, STEEL_DK)
# tower base flare into water
c.rect(tx-3, 40, 7, 2, STEEL_DK)

# nacelle
c.rect(tx-2, 5, 6, 4, STEEL)
c.set(tx+4, 6, STEEL_DK)
# hub
c.rect(tx+3, 6, 2, 2, STEEL_SH)
# blades from hub (tx+4,7)
c.line(tx+4, 7, tx+13, 1, STEEL)
c.line(tx+4, 7, tx+15, 9, STEEL)
c.line(tx+4, 7, tx+3, 17, STEEL)
# blade shading
c.set(tx+12, 1, STEEL_DK); c.set(tx+14, 9, STEEL_DK); c.set(tx+3, 16, STEEL_DK)

# --- maintenance platform at y=30, attached to tower ---
c.rect(24, 30, 22, 2, STEEL)
c.rect(24, 32, 22, 1, STEEL_DK)
# railings
for x in range(24, 46, 2):
    c.set(x, 27, STEEL_DK)
c.rect(24, 26, 22, 1, STEEL_DK)
# support struts down to sea
c.line(26, 32, 24, 44, STEEL_DK)
c.line(28, 32, 27, 44, STEEL_DK)
c.line(44, 32, 46, 44, STEEL_DK)
c.line(42, 32, 43, 44, STEEL_DK)
# platform legs in water
c.rect(24, 42, 1, 3, STEEL_SH)
c.rect(46, 42, 1, 3, STEEL_SH)

# --- ladder on left side of platform down to water ---
for y in range(32, 44):
    c.set(31, y, STEEL_SH); c.set(33, y, STEEL_SH)
for y in range(33, 43, 2):
    c.set(32, y, STEEL_DK)

# --- technician climbing ladder (head ~y=26, on ladder at x=32) ---
c.rect(31, 24, 3, 3, ORANGE)      # torso hi-vis
c.set(31, 24, YELLOW); c.set(33, 24, YELLOW)
c.set(32, 22, SKIN)               # head
c.set(32, 21, WHITE)              # helmet
c.set(31, 22, WHITE); c.set(33, 22, WHITE)  # helmet brim
c.set(31, 27, DARK); c.set(33, 27, DARK)    # arms gripping rails
c.set(31, 29, DARK); c.set(33, 29, DARK)
c.set(32, 28, DARK)               # legs
c.set(32, 30, DARK)

# safety line from technician's harness up to railing
c.set(30, 25, DARK); c.set(29, 26, DARK); c.set(28, 26, DARK); c.set(27, 26, DARK)
# toolbox on platform
c.rect(37, 28, 3, 2, RUST)
c.set(38, 27, STEEL_DK)
# rust patches at tower waterline
c.set(tx-2, 41, RUST); c.set(tx+2, 41, RUST); c.set(tx-1, 40, RUST)

# --- waves ---
for x, y, l in [(4,47,5),(14,50,6),(30,49,4),(52,47,6),(8,55,7),(22,57,5),(40,55,6),(54,58,5),(18,61,6),(34,62,5)]:
    c.rect(x, y, l, 1, FOAM)
    c.rect(x+1, y+1, max(1,l-2), 1, SEA_LT)
# wave foam at turbine/platform bases
c.rect(22, 43, 12, 1, FOAM)
c.rect(40, 44, 10, 1, FOAM)
c.rect(2, 44, 8, 1, FOAM)

# reflection hint of tower
for y in range(44, 50, 2):
    c.set(tx, y, STEEL_DK)

print(c.stats_text())
view(c)
save("offshore-wind-turbine-maintenance", c)
finish(c)
save("offshore-wind-turbine-maintenance", c)
