class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate

# Test the Solution class
obj = Solution()
nums = [3, 2, 3]
result = obj.majorityElement(nums)
print(result)  # Output: 3

        
