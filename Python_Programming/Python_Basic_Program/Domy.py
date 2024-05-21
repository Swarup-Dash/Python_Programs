# fruits = ['apple', 'banana', 'cherry']
# for index, fruit in enumerate(fruits):
#     print(index, fruit)
    
# class A():
#     a=10  #public
#     _b=20 #protected
#     __c=30  #private
#     print(a, _b, __c)

class Solution:
    def removeDuplicates(self, nums) -> int:
        nums1=set(nums)
        finalres=list(nums1)
        return finalres
obj=Solution()
nums=[2,3,4,2,5,4,3,4,5]
result=obj.removeDuplicates(nums)
print(result)