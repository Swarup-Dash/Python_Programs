class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0

        numSet=set(nums)
        print(numSet)
        longestSeq=0
        for num in numSet:
            if num-1 not in numSet:
                currentNum=num
                count=1

                while currentNum+1 in numSet:
                    currentNum+=1
                    count+=1
                longestSeq=max(longestSeq, count)
        return longestSeq


obj=Solution()
nums = [100,4,200,1,3,2]
res=obj.longestConsecutive(nums)
print(res)
