class Solution:
    def threeSumClosest(self, nums, target) -> int:
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target
        
        return closest_sum

obj = Solution()
nums = [-1, 2, 1, -4]
target = 1
res = obj.threeSumClosest(nums, target)
print(res)  # Output should be 2
