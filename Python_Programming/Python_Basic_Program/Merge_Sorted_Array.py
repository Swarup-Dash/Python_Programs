class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        nums1[m:m+n] = nums2
    
    # Sort the merged array
        nums1.sort()
    #     p1 = m - 1
    #     p2 = n - 1
    
    # # Start from the end of nums1
    #     for i in range(m + n - 1, -1, -1):
    #         if p2 < 0:
    #             break
    #         if p1 >= 0 and nums1[p1] > nums2[p2]:
    #             nums1[i] = nums1[p1]
    #             p1 -= 1
    #         else:
    #             nums1[i] = nums2[p2]
    #             p2 -= 1
solution = Solution()
nums1 = list(map(int, input("Enter elements of nums1 separated by space: ").split()))
m = int(input("Enter value of m: "))

nums2 = list(map(int, input("Enter elements of nums2 separated by space: ").split()))
n = int(input("Enter value of n: "))
# nums1 = input("Input number separated with space: ").split(" ")
# m = 3
# nums2 = input("Input number separated with space: ").split(" ")
# n = 3

solution.merge(nums1, m, nums2, n)
print(nums1)
    