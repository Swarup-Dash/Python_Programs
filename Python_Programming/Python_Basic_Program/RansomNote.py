# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         rans=''.join(sorted(ransomNote))
#         mang=''.join(sorted(magazine))
#         # print(rans)
#         # print(mang)
#         if rans in mang:
#             return True
#         else:
#             return False 

from collections import Counter
       
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False
        return True
obj=Solution()
ransomNote = "aab"
magazine = "baa"
res=obj.canConstruct(ransomNote, magazine)
print(res)
