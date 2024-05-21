# Create43 a function that takes a list of numbers and return the number that's unique.

def unique(numbers):
    count_dict={}
    
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
            
        else:
            count_dict[num]=1
            
    for num, count in count_dict.items():
        if count == 1:
            return num