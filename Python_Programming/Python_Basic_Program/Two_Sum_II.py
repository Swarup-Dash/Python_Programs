class Solution:
    def twoSum(self, numbers, target):
        num_to_index = {}
        for index, number in enumerate(numbers):
            complement = target - number
            if complement in num_to_index:
                return [num_to_index[complement] + 1, index + 1] 
            num_to_index[number] = index
        return []
obj=Solution()
numbers = [2,7,11,15]
target = 9
result=obj.twoSum(numbers, target)
print(result)