nums = ["orange","mango","orange","mango","grape"]

numsCount = {}
for num in nums:
    if num in numsCount:
        numsCount[num] += 1
    else:
        numsCount[num] = 1
        
print(numsCount)