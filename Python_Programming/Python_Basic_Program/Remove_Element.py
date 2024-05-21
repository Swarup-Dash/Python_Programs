class Solution:
    def removeElement(self, nums, val) -> int:
        exceptedNums = []
        for num in nums:
            if num != val:
                exceptedNums.append(num)
        exceptedNums.sort()
        return exceptedNums

obj = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = int(input("Value to be removed"))
result = obj.removeElement(nums, val)
print(result)
