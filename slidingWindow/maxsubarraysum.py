"""
Find the longest subarray in a positive int array that sums to 10
"""

def subarray_finder(arr, req):
    
    curr = arr[0]
    left = right = 0
    max_distance = 0
    window_idxs = [left,right]
   
    while right < len(arr)-1:
        
        right += 1
        curr += arr[right]
        
        while curr > req:
            curr -= arr[left]
            left += 1
        
        if curr == req and (right - left) > max_distance:
                max_distance = right - left
                window_idxs = [left,right+1]
    
    return arr[window_idxs[0]:window_idxs[1]]


arr = [2,4,5,3,1,2,3,4,5,3,2,2,1,3,3,2,5,3,2,1,1,1,1,2,3,4,2,3,4,2,1,2,3,4,5,1,5,2,2,2]

print(subarray_finder(arr,10))



