strg="I am an Indian"
count_char={}
for char in strg:
    if char.isalpha():
        char=char.lower()
        
        if char in count_char:
            count_char[char]+=1
        else:
            count_char[char]=1

print(count_char)