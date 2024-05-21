class Solution:
    def removeElement(self, nums):
        index=0
        for i in range(0, len(nums)):
            if (nums[index]==nums[index+1] or nums[index+1]==nums[index+2]):
                nums.remove(nums[index+1])
                index+=1
        return nums
    
obj=Solution()
nums = [1,1,1,2,2,3,3,3]
result=obj.removeElement(nums)
print(result)