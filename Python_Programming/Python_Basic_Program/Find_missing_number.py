# 1,3,4,5,4,3,1  Missing Number is 2.....

def missing_number(number):
    for i in range(len(number) - 1):
        if number[i + 1] != number[i] + 1:
            return number[i] + 1

number = [1, 3, 4, 5, 4, 3, 1]
missing_number = missing_number(number)
print("The missing number is:", missing_number) 

# Dry Run ----

# range(7-1)-->6
# number[i+1]-->number[0+1]-->number[1]-->3 != number[i]+1--> number[0]+1--> 1+1-->2
# return number[i] + 1--> 2