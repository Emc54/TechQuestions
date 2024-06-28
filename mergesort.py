

import math
### Merge Sort

def merge_sort (l: list): 
    
    if len(l) <= 1:
        return l

    left = []
    right = []

    for idx,item in enumerate(l):

        if idx < math.floor(len(l)/2):
            left.append(item)
        else:
            right.append(item)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

def merge(left: list, right: list):
        
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)

    return result



example_list = [3,5,2,5,34,5,1203,323,43,2]

print(merge_sort(example_list))
