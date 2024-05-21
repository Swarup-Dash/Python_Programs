def find_smallest_common(lst1, lst2, lst3):
    common_elements = set(lst1) & set(lst2) & set(lst3)
    
    if common_elements:
        smallest_common = min(common_elements)
        return smallest_common
    else:
        return None  # No common elements found

# Example usage:
list1 = [6, 8, 4, 18, 25]
list2 = [3, 6, 4, 15, 21]
list3 = [5, 6, 7, 4, 32]
# common=set(list1).intersection_update(set(list2)) #Wrong
# print(common) XXXXXXXXXXXXXXXXXXXXXXX

result = find_smallest_common(list1, list2, list3)  #Right
print(result)