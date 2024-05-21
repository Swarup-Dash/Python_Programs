def can_jump(nums):
    max_reach = 0  # Maximum reachable index
    for i in range(len(nums)):
        # If the current index is not reachable, return False
        if i > max_reach:
            return False
        # Update the maximum reachable index
        max_reach = max(max_reach, i + nums[i])
        # If the last index is within reach, return True
        if max_reach >= len(nums) - 1:
            return True
    return False  # Return False if the loop completes without reaching the last index

nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]

print(can_jump(nums1))  # Output: True
print(can_jump(nums2))  # Output: False
