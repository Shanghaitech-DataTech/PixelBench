from pixelbench_api import *

# Two 32x64 animation cells on one transparent 64x64 sprite sheet.
result = new_canvas(64, 64, background=None, name="explosion_effect")

# Compact shared fire palette.
outline = result.color("#7a1f18", "deep_red")
red = result.color("#b92a18", "blast_red")
orange_red = result.color("#e94a16", "orange_red")
orange = result.color("#ff7b18", "orange")
gold = result.color("#ffb51b", "gold")
yellow = result.color("#ffe23b", "yellow")
hot = result.color("#fff59a", "hot_core")
white = result.color("#fffde0", "white_hot")

# Frame 1: compact, bright ignition fireball centered at (16, 32).
# Dark/red outer pixels give the small fireball a crisp irregular contour.
result.rect(12, 20, 8, 2, outline)
result.rect(9, 22, 14, 2, outline)
result.rect(7, 24, 18, 3, outline)
result.rect(5, 27, 22, 4, outline)
result.rect(4, 31, 24, 5, outline)
result.rect(6, 36, 20, 4, outline)
result.rect(8, 40, 16, 3, outline)
result.rect(11, 43, 10, 2, outline)
# Silhouette notches and tongues.
result.clear(4, 31, 2, 2)
result.clear(26, 28, 2, 2)
result.clear(6, 38, 2, 2)
result.set(10, 19, outline)
result.set(21, 21, outline)
result.set(3, 34, outline)
result.set(28, 33, outline)
result.set(9, 45, outline)
result.set(23, 42, outline)

# Outer orange-red shell.
result.rect(10, 23, 12, 2, red)
result.rect(8, 25, 16, 4, orange_red)
result.rect(6, 29, 20, 7, orange_red)
result.rect(8, 36, 16, 5, orange_red)
result.rect(11, 41, 10, 2, red)
result.set(6, 27, red)
result.set(25, 31, red)
result.set(7, 37, red)

# Golden body and blazing yellow center.
result.rect(11, 24, 10, 2, orange)
result.rect(9, 26, 14, 4, orange)
result.rect(7, 30, 18, 5, gold)
result.rect(9, 35, 14, 4, orange)
result.rect(12, 39, 8, 2, orange)
result.rect(12, 27, 8, 2, yellow)
result.rect(10, 29, 12, 8, yellow)
result.rect(12, 37, 8, 2, yellow)
result.rect(13, 29, 6, 9, hot)
result.rect(14, 31, 4, 5, white)
result.set(11, 28, hot)
result.set(20, 31, hot)
result.set(11, 36, hot)

# Small ignition motes around frame 1.
result.set(5, 20, gold)
result.set(3, 24, orange_red)
result.set(27, 22, orange)
result.set(29, 27, yellow)
result.set(2, 39, red)
result.set(27, 42, orange)
result.set(6, 47, orange_red)
result.set(24, 48, gold)

# Frame 2: expanded blast centered at (48, 32), with radial lobes.
# Deep-red silhouette and long jagged spikes.
result.poly([(33,29),(37,27),(34,22),(40,23),(39,17),(44,21),(47,12),(50,21),(55,16),(55,23),(62,21),(59,27),(63,29),(60,33),(63,38),(57,38),(58,45),(52,42),(49,51),(46,43),(40,48),(41,40),(33,42),(37,35)], outline)
# Secondary red mass.
result.poly([(35,30),(40,27),(38,23),(44,25),(44,20),(48,24),(53,20),(53,26),(59,24),(57,29),(62,31),(57,34),(60,38),(54,37),(54,43),(49,39),(46,46),(44,39),(38,42),(41,36),(35,35),(40,32)], red)
# Orange expansion body.
result.poly([(38,30),(43,28),(42,24),(47,27),(50,23),(52,28),(57,27),(55,31),(60,32),(55,34),(57,38),(52,36),(51,41),(48,37),(45,42),(44,36),(39,38),(42,34)], orange_red)
# Bright folded interior.
result.poly([(41,31),(45,29),(45,26),(48,29),(51,26),(52,30),(56,30),(53,33),(55,36),(51,35),(49,39),(47,35),(43,37),(44,33)], orange)
result.poly([(44,31),(47,30),(48,27),(50,30),(53,31),(51,33),(52,36),(49,34),(47,37),(47,34),(44,35),(46,32)], gold)
result.rect(47, 30, 4, 5, yellow)
result.set(48, 31, hot)
result.set(49, 32, white)
result.set(48, 33, hot)

# Interior shadow pockets add motion and separation between blast lobes.
result.set(40, 28, outline)
result.set(42, 25, red)
result.set(55, 28, red)
result.set(57, 32, outline)
result.set(53, 38, red)
result.set(43, 38, outline)
result.set(39, 34, red)

# Expanding sparks and debris trails, contained within frame 2.
result.set(35, 16, orange_red)
result.set(37, 19, gold)
result.set(42, 12, red)
result.set(44, 15, orange)
result.set(49, 8, gold)
result.set(50, 13, yellow)
result.set(57, 11, orange_red)
result.set(56, 15, gold)
result.set(62, 17, red)
result.set(60, 22, orange)
result.set(33, 25, red)
result.set(32, 32, gold)
result.set(34, 38, orange)
result.set(36, 45, red)
result.set(39, 49, orange_red)
result.set(44, 53, gold)
result.set(48, 57, red)
result.set(52, 52, orange)
result.set(58, 48, red)
result.set(61, 43, gold)
result.set(63, 36, orange)
# Two-pixel spark streaks.
result.line(33, 20, 35, 21, orange)
result.line(59, 18, 61, 16, gold)
result.line(34, 47, 36, 49, orange_red)
result.line(58, 44, 60, 45, orange)
result.line(53, 55, 53, 57, gold)

view(result, scale=8, margin=0, edges="none")
finish(result)
