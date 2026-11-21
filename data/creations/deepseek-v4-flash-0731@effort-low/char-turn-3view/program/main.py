from pixelbench_api import *

# Character colour char map
CM = {
 'a':'c0','b':'c1','c':'c2','d':'c3','e':'c4','f':'c5','g':'c6','h':'c7',
 'i':'c8','j':'c9','k':'c10','l':'c11','m':'c12','n':'c13','o':'c14','p':'c15',
 'q':'c16','r':'c17','s':'c18','t':'c19','u':'c20','v':'c21','w':'c22',
}

ROWS = []
def add(s, n):
    for _ in range(n):
        ROWS.append(s)

add("................aaaaaaaaaaaa..........aaaaaaaaaaaa................",2)
add("..............aabbbccaaabbbbaaaaaaaaaabbbbaaaccbbbaa..............",3)
add("............aabbcccaabbbcccccccccbbcccccccbbbaacccbbaa............",2)
add(".........aaaaaccdddaacccccdddddccccdddddcccccaadddccaaaaa.........",4)
add(".......aabbbaaddeeeddbbbccccdddddccdddccccbbbddeeeddaabbbaa.......",2)
add(".......aacccaadddddeedddccddddddddddddddccdddeedddddaacccaa.......",2)
add(".....aabbdddbbcceeeffeeeddddccccccccccddddeeeffeeeccbbdddbbaa.....",3)
add(".....aaccdddeecccccbbdddddccaaabbbbaaaccdddddbbccccceedddccaa.....",2)
add("..aaabbddcccffddaaaeedddeeaabbbccccbbbaaeedddeeaaaddffcccddbbaaa..",2)
add("..aaaccddbbbddaacccffeeeeeaaaaaaaaaaaaaaeeeeeffcccaaddbbbddccaaa..",3)
add("..aaaccffaaaccaafffcccccffaaggggggggggaaffcccccfffaaccaaaffccaaa..",2)
add(".....aaddfffaaaadddaabbbccaaggggggggggaaccbbbaadddaaaafffddaa.....",3)
add(".....aabbdddccaaaaabbaaaaaaaaaaggggaaaaaaaaaabbaaaaaccdddbbaa.....",2)
add(".......aacccddaagggaaaaaccccggggggggggccccaaaaahhhaaddcccaa.......",2)
add(".......iiaaaaaaaccchhhhhgghhgggggggggghhgghhhhhcccaaaaaaaii.......",3)
add(".......iigggggaahhhaaaaajjhhgggggggggghhjjaaaaahhhaagghhhii.......",2)
add(".........iiiggaaaaakkiiiiikkhhhgggghhhkkiiiiikkaaaaaggiii.........",3)
add(".........iiihhjjhhhlliiimmllggggggggggllmmiiillhhhjjhhiii.........",3)
add("............iiiijjjggnnnnnllggggggggggllnnnnnggjjjiiii............",2)
add("................iiihhgggggggggggggggggggggggghhiiibbccaaa.........",3)
add("................iiijjooohhgggggggggggggghhooojjaaabbbbdddaa.......",2)
add("............pppppppppjjjjjoohhhgggghhhoojjjjjaacccccffcccaaaa.....",2)
add(".........pppqqqqqqqqqqqqppjjjjjjjjjjjjjjppaaaccdddbbaabbbaaffaaa..",3)
add("......ppqqqrrrrsssqqssspphhoooooooooohhaaeeeffdddaabbaaabbccaaa..",2)
add("....ppttrrrssrrsssqqsssqqtthhhoooohhhttaafffddaaabbccdddaabbaaa..",2)
add("....ppqqsssqqsssssqqsssssqqttthhhhtttqqaaaaaccdddaaddfffaaaa.....",3)
add("......ppqqqsssstttqqssssssstttggggtttaaffeeeeedddaabbaaapp.......",2)
add("....iijjpppppppqqqqqsssrrsssssttttsssaaddcccaaaaaccddaaajjaa.....",2)
add("....iioohhhooppqqqqqsssrrrrssssssssssrraadddbbaaaaaaaaaaaaii.....",3)
add("....iigghhhjjpppppqqqqqssssssssssssssssssaaaccaaappjjhhhggii.....",3)
add("..iiioouuooojjiippppptttttttqqqssssqqqttaaaaaaapppiijjooouuooiii..",3)
add("..iiiuuuujjjiivviiippqqqttqqssssssssssqqttqqqppiiivviijjjuuuuiii..",2)
add("iiooouuggooojjwwvvvpptttqqttssssssssssttqqtttppvvvwwjjooogguuoooii",2)
add("iiggguugggggoowwpppttpppqqttqqqssssqqqttqqpppttpppwwooggggguugggii",3)
add("iigggggggjjjvvpptttttpppppttqqqqqqqqqqttppppptttttppggjjjgggggggii",2)
add("iijjjggggjjjpptttttqqpppqqpptttqqqqtttppqqpppqqtttttppjjjggggjjjii",2)
add("..iiioogghhhppttqqqppqqqqqttqqqqqqqqqqttqqqqqppqqqttpphhhggooiii..",3)
add(".....iiiipppttqqtttqqsssttqqssssssssssqqttsssqqtttqqttpppiiii.....",3)
add(".........pppqqtttttqqsssqqsssssrrrrsssssqqsssqqtttttqqppp.........",3)
add(".......pptttqqttqqqssqqqssssqqqrrrrqqqssssqqqssqqqttqqtttpp.......",2)
add(".......ppqqqttqqsssssqqqrrssqqqrrrrqqqssrrqqqsssssqqttqqqpp.......",2)
add(".......ppsssppqqrrrqqsssrrqqqqqrrrrqqqqqrrsssqqrrrqqppssspp.......",3)
add(".....ppqqsssppssrrrttsssrrqqsssrrrrsssqqrrsssttrrrssppsssqqpp.....",2)
add(".....ppsspppttrrqqqttrrrrrqqsssrrrrsssqqrrrrrttqqqrrttpppsspp.....",2)
add(".....ppqqpppqqrrtttssrrrrrttsssrrrrsssttrrrrrsstttrrqqpppqqpp.....",3)
add(".......pppppssrrtttrrrrrssttsssrrrrsssttssrrrrrtttrrssppppp.......",3)
add(".......pppppqqsspppssrrrqqttrrrrrrrrrrttqqrrrsspppssqqppppp.......",3)
add(".........pppttqqpppqqsssttttrrrrrrrrrrttttsssqqpppqqttppp.........",2)
add("............pppppppqqqqqttppssssssssssppttqqqqqppppppp............",1)

print("base rows:", len(ROWS))

def build(head):
    c = new_canvas(66, 119)
    for y, s in enumerate(ROWS):
        for x, ch in enumerate(s):
            if ch in CM:
                c.set(x, y, CM[ch])
    # overlay head rows
    for y, s in enumerate(head):
        for x, ch in enumerate(s):
            if ch in CM:
                c.set(x, y, CM[ch])
        # clear remainder of that row in head zone
    # clear head zone fully first
    return c

fb = new_canvas(66,119)
for y, s in enumerate(ROWS):
    for x, ch in enumerate(s):
        if ch in CM:
            fb.set(x, y, CM[ch])

print("front rows", len(ROWS), fb.stats())

# --- three-quarter LEFT head (rows 0-51) ---
H1 = []
def h1(s): H1.append(s)
h1("..............aaaaaaaaaaa........aaaaaaaaaaaa...............")
h1("..............aaaaaaaaaaa........aaaaaaaaaaaa...............")
h1("............aaaaabbbcccaaabbbbaaaaaabbbbaaaccbbaa...........")
h1("............aaaaabbbcccaaabbbbaaaaaabbbbaaaccbbaa...........")
h1("..........aaaaabbbbccccaaabbbbbbbbbbbbbbbbbaaacccbbbaaa........")
h1("..........aaabbbbccccdddcccccccccccccccccccdddcccccbbbba......")
h1(".........aaabbbccccdddddccccddddddddddddcccccdddccccccbbaa....")
h1("........aaabbbccccdddddccddddddddddddddddddddccccdddddccbbaa...")
h1("........aaabbccccddddddcccdddddddddddddddddcccddddccccccbba....")
h1(".......aabbcccccdddddccccddddddddddddddddddccccddddccccccbba...")
h1("......aabbccccdddddcccfffdddddccccccccddddddccccdddddccccbba..")
h1("......aabbcccdddddcddccccffffddddddddddddddccccdddcccccccbbba..")
h1(".....aabbcccddddccddddccccffffdddddddddddddddddddccccccccbbaa..")
h1(".....aabbbcccdddccdddddcccccccddddddddddddddccccdddddcccbbaa...")
h1("....aabbbcccdddccdddddccccccccddddddddddddddccccddddddccbbaa...")
h1("....aabbbbbcccddcccdddcccffffccddddddddddddccccdddddccccccbbaa.")
h1("....aabbbbbccccddccccddccccffffddddddddddcccddddddcccccbbaa...")
h1("...aabbbbbccccdcccccccddddcccdddddddddddcccddddddccccccbbbaa..")
h1("...aabbbbbcccdccccccccdddddccccddddddddddccccdddddccccccbbaa..")
h1("...aabbbbbccdccccccccddddddcccccddddddddcccccdddddcccccccbbaa.")
h1("..aabbbbbccdcccccccdddddddccccccddddddddccccccddccccdddddbbaab.")
h1("..aabbbbbccdcccccccddddddddccccccddddddddcccccccddccccdddddbbab")
h1(".aabbbbbbcdcccccceedddddddccccccccddddddddccccccccdddddccccaaa.")
h1(".aabbbbbbcddcccccceeeddddddccccccccddddddddccccccccdddddcccaaa.")
h1("aabbbbbbcddccccccceeeedddddccccccccddddddddccccccccddddddccaaa")
h1("aabbbbbbcdddccccceeeeedddddccccccccddddddddccccccccddddddccaaa")
h1(".aabbbbbcdddccccceeeeeedddddcccccccccccccccccccddddddddcaaa.")
h1(".aabbbbbcdddccccceeeeeeeedddddccccccccccccccccccccddddddccaaa")
h1("..aabbbbcdddccccceeeeeeeeedddccccccccccccccccccddddddddccaaa.")
h1("...aabbbbcdddcccccceeeeeeeeeddddddccccccccccddddddddddcccaaa..")
h1("....aabbbcdddcccccceeeeeeeeefdddddddddddddddddddddddddddcccaa..")
h1(".....aabbccddccccceeeeeeeeffgddddddddddddddddddddddddddcccaa..")
h1("......aabbccddccccceeeeeeeeffggdddddddddddddddddddddddddcccb...")
h1(".......abbcccdccccceeeeeeeegggggggddddddddddddddddddddddddcbb..")
h1("........aabbccccccceeeeeeeeggggggggggggggdddddddddddddddccbb..")
h1("........aabbccccccceeeeeeegggggggggggggggggggdddddddddddddccb..")
h1(".........aaabccccccceeeeeegggggggggggggggggggggddddddddddccb..")
h1("..........aaabccccccceeeeegggggggggggggggggggggggggddddddddcc..")
h1("............aabccccccceeeggggggggggggggggggggggggggggdddddcc..")
h1(".............aaacccccceeggggggggggggjjgggggggggggggggggggddc...")
h1(".............aaacccccccggggggggggggjjjjggggggggggggggggggcc....")
h1("..............aaacccccccggggggggggjjjjjjggggggggggggcccc......")
h1("..............aaaccccccggggggggggjjjjjjjjgggggggggggcc........")
h1("...............aaccccccggggggggkkkkkkjjjjgggggggggccc........")
h1("................aaacccccggggggkkkkllkkkkjjggghhhhhhcc........")
h1("................aaacccggggggkkkllllllkkkkggghhhhhhhhcc.......")
h1(".................aaacccgggggkklllllllllllgggghhhhhhhhh.......")
h1("..................aaacccggggggggllllggggggggggghhh...........")
h1("....................aaacggggggggggggggggggggggghhh...........")
h1("....................aaacccgggggggggggggggggcc...............")
h1("........................aaacccccccccccchh..................")
h1("...............................aaaaccccccc.................")
print("H1 rows", len(H1))

# --- rear head (0-51) ---
HR = []
def hr(s): HR.append(s)
hr("..............aaaaaaaaaaa........aaaaaaaaaaa...............")
hr("..............aaaaaaaaaaa........aaaaaaaaaaa...............")
hr("............aaaaabbbcccaaabbbbaaaaaabbbbaaaccbbbaa...........")
hr("............aaaabbbbccccaaabbbbbbbbbbbbbbbaaaaaccccbbbbbaa....")
hr(".........aaaaabbbbccccccaaabbbbbbbbbbbbbbbbbbaacccccbbbbbbaa...")
hr("........aaaabbbbccccccdddbbbbbbbbbbbbbbbbbbbbbbbbccccccbbbbba..")
hr(".......aaabbbbbcccccdddddbbbbbbbbbbbbbbbbbbbbbddddcccccccbbbbaa.")
hr(".......aabbbbbbcccccdddddddbbbbbbbbbbbbbbbbbbbbdddddcccccccbbbaa")
hr("......aabbbbbbccccddddddddddbbbbbbbbbbbbbbbbbddddddddccccccbbbaa")
hr("......aabbbbbbcccdddddddddddddbbbbbbbbbbbbbdddddddddccccccbbbaa.")
hr(".....aabbbbbbcccdddddddddddddddbbbbbbbbbbddddddddddddccccccbbba..")
hr(".....aabbbbbbccccdddddddddddddddbbbbbbbbbdddddddddddddccccccbb..")
hr("....aabbbbbbccccdddddddddddddddddbbbbbbbbddddddddddddddccccccbb.")
hr("....aabbbbbbccccdddddddddddddddddddddddddddddddddddddddccccccbb.")
hr("...aabbbbbbcccccdddddddddddddddddddddddddddddddddddddddccccccbb.")
hr("...aabbbbbbccccddddddddddddddddddddddddddddddddddddddddccccccbb.")
hr("..aabbbbbbcccccdddddddddddddddddddddddddddddddddddddddccccccbb.")
hr("..aabbbbbcccccdddddddddddddddddddddddddddddddddddddddddccccccbb.")
hr("..aabbbbbccccccddddddddddddddddddddddddddddddddddddddddccccccbb.")
hr(".aabbbbbcccccccdddddddddddddddddddddddddddddddddddddddcccccccb..")
hr(".aabbbbbcccccccdddddddddddddddddddddddddddddddddddddddcccccccb..")
hr("aabbbbbcccccccdddddddddddddddddddddddddddddddddddddddddcccccccb.")
hr("aabbbbbcccccccdddddddddddddddddddddddddddddddddddddddddcccccccb.")
hr("aaabbbcccccccdddddddddddddddddddddddddddddddddddddddddcccccccbb.")
hr("aaabbbcccccccdddddddddddddddddddddddddddddddddddddddddcccccc b..")
hr(".aabbbcccccccddddddddddddddddddddddddddddddddddddddddddccccccb..")
hr(".aabbbcccccccddddddddddddddddddddddddddddddddddddddddddddccccbb..")
hr(".aabbbcccccccdddddddddddddddddddddddddddddddddddddddddddcccbb...")
hr(".aabbbccccccddddddddddddddddddddddddddddddddddddddddddddccbb...")
hr("..aabbbccccccddddddddddddddddddddddddddddddddddddddddddcccb....")
hr("..aabbbcccccdddddddddddddddddddddddddddddddddddddddddddccbb....")
hr("...aabbbccccddddddddddddddddddddddddddddddddddddddddddccbb.....")
hr("....aabbcccccddddddddddddddddddddddddddddddddddddddddcccbb.....")
hr("......aabbcccccdddddddddddddddddddddddddiiiiiiidddcccbba.......")
hr(".......aabbcccccdddddddddddddddddddddddddddddddddddddcccbb.....")
hr("........aabbcccccdddddddddddddiiiiiiiiiiddddddddddcccbba......")
hr(".........aabbccccdddddddddiiiiiiiiiiiiddddddddddcccbb........")
hr("..........aabbccccddddddddiiiiiiiiiiiiddddddddddcccbb........")
hr("...........aabbccccdddddiiiiiiiiiiiiddddddddddcccbb..........")
hr("............aabbccccdddiiiiiiiiiiiiddddddddcccbb............")
hr(".............aabbccccdddiiiiiiiiiiiidddccccccbb..............")
hr("..............aabbccccddiijjjjwwjjjjjjjjjjjwwjjjjjii..........")
hr("...............aabbccccddjjwwwjjjjjjjjjjjjjjwwjjjj...........")
hr("................aabbccccdjjjwwwjjjjjjjjjjjjjjwwjjj...........")
hr("..................aabbbccccjjjjjjjjjjjjjjjjjjjjjjj............")
hr("....................aabbccccjjjjjjjjjjjjjjjjjjjj..............")
hr("......................aabbccccjjjjjjjjjjjjjjjj................")
hr("...........................aabbccccjjjjjjjjj.................")
hr(".............................aabbccccjjjjjj..................")
hr("................................aabbccccjj...................")
hr("...................................aabbccj...................")
hr("......................................aacc...................")
hr("..........................................a...................")
print("HR rows", len(HR), "H1", len(H1), "expected 52")

def over(dst, head):
    for y, s in enumerate(head):
        for x, ch in enumerate(s):
            if ch in CM:
                dst.set(x, y, CM[ch])

f1 = fb.copy(name="left34")
over(f1, H1)
f2 = f1.copy(name="right34")
f2.mirror("h")
f3 = fb.copy(name="rear")
over(f3, HR)

for i,c in enumerate([f1,f2,f3]):
    print("frame",i,c.stats())

finish([f1, f2, f3])
print("submitting", len([f1,f2,f3]), "frames")
#[ ]
