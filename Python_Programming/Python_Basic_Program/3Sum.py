class Solution:
    def threeSum(self, nums):
        nums.sort() 
        res = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:  
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  
                        right -= 1
                    left += 1
                    right -= 1
        
        return res

# Examples
obj = Solution()
num = [-1, 0, 1, 2, -1, -4]
ans = obj.threeSum(num)
print(ans)
