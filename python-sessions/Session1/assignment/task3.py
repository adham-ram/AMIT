x = "&&&**$gnirtS PLIO!!@1234"
syntax = x[x.index('g') : x.index('O') + 1]
word1, word2 = syntax.split()
word1_reversed = word1[::-1]

word2_edited = ""
for char in word2:
    if char.lower() == 'i':
        word2_edited += 'E'
    elif char.lower() == 'o':
        word2_edited += 'U'
    else:
        word2_edited += char
print(word1_reversed, word2_edited)