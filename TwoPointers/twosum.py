'''
Given an unsorted integer array, find a pair with the given sum in it.
• Each input can have multiple solutions. The output should match with either one of them.
Input : nums[] = [8, 7, 2, 5, 3, 1], target = 10
Output: (8, 2) or (7, 3)
• The solution can return pair in any order. If no pair with the given sum exists, the solution should return an empty tuple.
Input : nums[] = [5, 2, 6, 8, 1, 9], target = 12
Output: ()
'''


nums1 = [8,7,2,5,3,1]
nums2 = [5,2,6,8,1,9]
target1 = 10
target2 = 12


### Sorting Approach

def findPair(nums: list[int], target: int) -> tuple:
    

    # Sort the list
    nums.sort()
    
    # Keep track of two indices in the list, beginning and end
    low, high = 0 , len(nums)-1

    # Search for a match
    while low < high:
    
        currSum = nums[low]+nums[high]

        if currSum  == target:
            return (nums[low],nums[high])
        
        elif currSum < target:
            low += 1 
        else:
            high -= 1 
    
    #Failed to match
    return ()

res = findPair(nums1, target1)
res2 = findPair(nums2, target2)
print(res,res2)

for i in range(20):
    print(f"Target:",i,"pair",findPair(nums2,i))


## Hash Map approach


