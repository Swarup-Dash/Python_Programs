class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        sorted_words = sorted(words, key=lambda word: int(word[-1]))
        sorted_sentence = ' '.join(word[:-1] for word in sorted_words)
        
        return sorted_sentence
        
obj = Solution()
s = "is2 sentence4 This1 a3"
res=obj.sortSentence(s)
print(res)