class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans=''.join(sorted(ransomNote))
        mang=''.join(sorted(magazine))
        # print(rans)
        # print(mang)
        if rans in mang:
            return True
        else:
            return False 
obj=Solution()
ransomNote = "aab"
magazine = "baa"
res=obj.canConstruct(ransomNote, magazine)
print(res)
