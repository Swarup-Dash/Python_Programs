class Solution:
    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right) // 2
            
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1
    
nums = [4,5,6,7,0,1,2]
target = 0

obj = Solution()
result = obj.search(nums, target)


        

        