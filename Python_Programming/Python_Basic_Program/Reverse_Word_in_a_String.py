class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s.split(" "))
        result=s[::-1]
        revrs= " ".join(result)
        return revrs
    
obj=Solution()
s="the sky is blue"
res=obj.reverseWords(s)
print(res)