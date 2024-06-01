class Solution:
    def findSubstring(self, s: str, words):
        conCat="".join(words)
        # conCat2="".join(words, reverse=True)  XXXXX
        conCat2="".join(reversed(words))
        print(conCat)
        print(conCat2)
        index1 = s.find(conCat) if conCat in s else -1
        index2 = s.find(conCat2) if conCat2 in s else -1
        
        return index1, index2
        
        
obj=Solution()
s = "barfoothefoobarman"
words = ["foo","bar"]
result=obj.findSubstring(s, words)
print(result)