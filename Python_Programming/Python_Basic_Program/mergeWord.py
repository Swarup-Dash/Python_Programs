word1 = "abc"
word2 = "pqr"

res = ""

for i in range(len(word2)):
    res += " "+word1[i]+" "+ word2[i]
        
print(res)