# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s = s.strip().split(" ")
#         return len(s[-1])
        
# obj=Solution()
# s=input("Enter Your Sentence: ")
# result=obj.lengthOfLastWord(s)
# print(result)

string = "Hello, World!"
substring = "World"
index = string.find(substring)
if index != -1:
    print("Substring found at index:", index)
else:
    print("Substring not found")

