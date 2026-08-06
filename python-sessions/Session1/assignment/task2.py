
x = "###!!@mocleW EPGTQ!!!6789"

core = x[x.index('m') : x.index('Q') + 1]  


word1, word2 = core.split()

word1_reversed = word1[::-1]  

word2_edited = ""
for i in range(len(word2)):
    if word2[i] in ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']:
        continue
    else:
        word2_edited += word2[i]

print(word1_reversed, word2_edited)