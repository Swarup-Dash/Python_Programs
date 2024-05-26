class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of the strings are different, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Create dictionaries to count the frequency of characters in both strings
        count_s = {}
        count_t = {}
        
        # Count the frequency of each character in the first string
        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1
        
        # Count the frequency of each character in the second string
        for char in t:
            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1
        
        # Compare the two dictionaries
        return count_s == count_t

obj=Solution()
s = "anagram"
t = "nagaram"
res=obj.isAnagram(s, t)
print(res)