def arr_sum(arr):
    sum=0
    for i in arr:
        sum=sum+i
    return(sum)

arr=[20,12,42,24]
n=len(arr)

print("Sum of the array is:", arr_sum(arr))
        