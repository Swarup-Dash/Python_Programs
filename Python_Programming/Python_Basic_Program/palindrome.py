# Palindrome: Number is same as its reverse i.e 2332 reverse is also 2332
n=int(input("Enter a number"))
temp=n
reverse=0
while temp>0:
    remainder=temp%10
    reverse=(reverse*10)+remainder
    temp=temp//10
if n==reverse:
    print(n,"is palindrome")
else:
    print(n,"is not palindrme")
    

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x_str=str(x)
#         return x_str==x_str[::-1]