"""

Given a sorted array of distinct integers and a target value, return the index 
if the target is found. If not, return the index where it would be if it were 
inserted in order.

"""


sorted_arr = [1,2,4,5,7,8,9]

def indexFinder(arr: list, target: int)-> int:
    
    left, right = 0, len(arr) 

    while left < right:

        mid = (right + left) // 2

        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    
    return left

for i in range(10):
    print(f"The number {i} goes at {indexFinder(sorted_arr,i)} in the array")
         
