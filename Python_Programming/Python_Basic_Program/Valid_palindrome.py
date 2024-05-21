import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = re.sub(r'[^a-zA-Z]', '', s)
        lwr=cleaned_string.lower()
        reverse=lwr[::-1]
        if lwr==reverse:
            print(s, "is palindrome")
        else:
            print(s, "is not palindrome")
        
obj=Solution()
s="A man, a plan, a canal: Panama"
obj.isPalindrome(s)
