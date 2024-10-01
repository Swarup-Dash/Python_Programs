word1="gsggdhhd" 
word2="rd"   
merged_string = []
i, j = 0, 0

while i < len(word1) and j < len(word2):
    merged_string.append(word1[i])
    merged_string.append(word2[j])
    i += 1
    j += 1
    
merged_string.append(word1[i:])  
merged_string.append(word2[j:]) 
    
print(''.join(merged_string))
