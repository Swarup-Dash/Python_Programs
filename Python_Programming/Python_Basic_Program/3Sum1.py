class Solution:
    def threeSum(self, nums):
        nums.sort() 
        res = set()
        
        for i in range(len(nums) - 2):
            left = i+1
            right = len(nums)-1
              
                
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if sum == 0:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
                    
        
        return list(res)

obj = Solution()
num = [-1, 0, 1, 2, -1, -4]
ans = obj.threeSum(num)
print(ans)
