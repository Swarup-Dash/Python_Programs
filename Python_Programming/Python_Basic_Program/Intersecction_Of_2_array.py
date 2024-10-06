class Solution:
    def intersect(self, nums1, nums2):
        
        res = []
        for num in nums1:
            if num in nums2:
                res.append(num)

        return res
        
nums1 = [1,2,2,1]
nums2 = [2,2]
obj = Solution()
ans = obj.intersect(nums1, nums2)

print(ans)