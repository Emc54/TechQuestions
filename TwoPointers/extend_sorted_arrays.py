"""

Example 3: Given two sorted integer arrays arr1 and arr2, return a new array 
that combines both of them and is also sorted.

"""

def extend_arrays(a,b):
    left = 0
    right = 0
    result = []

    while left < len(a) and right < len(b):
        if a[left] < b[right]:
            result.append(a[left])
            left += 1
        else:
            result.append(b[right])
            right += 1
        
    while left < len(a):
        result.append(a[left])
        left += 1

    while right < len(b):
        result.append(b[right])
        right += 1

    return result


list1 = [3,4,5,6,8,9,0,6,4,2,4]
list1.sort()

list2 = [3,1,4,6,7,8,9,7,6,5,4,3]
list2.sort()

print(extend_arrays(list1,list2))
