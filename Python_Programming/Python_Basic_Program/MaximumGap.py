nums = [3, 6, 9, 1]
nums.sort()
print(nums)

if len(nums)<2:
    print(0)
    
maxDiff = 0
for i in range(1, len(nums)):
    diff = nums[i] - nums[i-1]
    if diff > maxDiff:
        maxDiff = diff
        i+=1

        
print(maxDiff) 