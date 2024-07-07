"""
Given an integer array, return the k-th smallest distance among all the pairs. 
The distance of a pair (A, B) is defined as the absolute difference 
between A and B.

Input:
nums = [1,3,1]
k = 1
Output: 0 
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
"""

### Binary Search through the space of possible distances
### Max distance is max(nums) - min(nums)
### Min distance is 0
### Use Two Pointers to gather distances:
### count, fast pointer, slow pointer
### check all distances less than the dist being checked:
###     while "nums[fast]-nums[slow] <= dist" - increment fast
### increment count by pointer difference
### increment slow pointer    

def ksmallest_distance(nums: list[int], k:int) -> int:


    # smallest distance, min and second min
    max_dist = max(nums) - min(nums)

    left, right = 0, max_dist

    def distance_exists(dist):
        count, slow, fast = 0, 0, 0
        n = len(nums)

        while slow < n or fast < n:

            while fast < n and nums[fast] - nums[slow] <= dist:  # move fast pointer
                fast += 1
        
            count += fast - slow - 1  # count pairs
            slow += 1  # move slow pointer
        return count >= k       
    
    while left < right:
        
        mid = left + (right-left)//2
        
        if distance_exists(mid):
            right = mid
        else:
            left = mid + 1

    return left

nums = [1,3,67]

k = 1 

print(ksmallest_distance(nums,k))      
