text ="The quick brown fox jumps over the lazy dog"

text = text.casefold()

count = True
sequence =("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
for i in sequence:
    if i in text:
        count = True

    else:
        count = False
        break

if count == True:
    print('pangram')

else:
    print('not pangram')

