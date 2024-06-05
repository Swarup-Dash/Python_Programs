class Solution:
    def addTwoNumbers(self, l1, l2):
        strg1 = int("".join([str(item) for item in l1[::-1]]))
        strg2 = int("".join([str(item) for item in l2[::-1]]))
        
        result=strg1+strg2
        return result
        
obj=Solution()
l1 = [2,4,3]
l2 = [5,6,4]
res=obj.addTwoNumbers(l1, l2)
print(res)