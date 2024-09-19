def charCount(lst):
    counter = {}
    for i in lst:
        if i in counter:
            counter[i]+=1
        else:
            counter[i] = 1
            
    return counter
    

    
lst = ['a', 'b', 'a', 'c', 'a', 'b']
res = charCount(lst)
print(res)