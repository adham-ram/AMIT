x="##$$$@!yalpstcejorp EPUVT****9887 "
syn =x[x.index('y'):x.index('T')+1]
word1, word2 = syn.split()
word1_reversed = word1[::-1]
word2_edited = ""
for char in word2:
    if char.lower() == 'e':
        word2_edited += 'A'
    elif char.lower() == 'u':
        word2_edited += 'O'
    else:
        word2_edited += char
print(word1_reversed, word2_edited)