class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        
        res = []
        start = end = nums[0]
        
        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                if start == end:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{end}")
                start = end = num
        
        if start == end:
            res.append(str(start))
        else:
            res.append(f"{start}->{end}")
        
        return res
obj=Solution()
nums = [0,1,2,4,5,7]
result=obj.summaryRanges(nums)
print(result)