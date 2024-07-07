"""
Given an array nums which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""



# worst_sum = sum(array)
# best_sum, = max(array)
# binary search in this space

# Given a sum try to make cuts to create a smaller one
# Check if we need more subarrays than the given m (subarrays are 1 more 
# than the number of cuts)

def minimise_max_sum(nums: list[int], m:int) -> int:

    def max_sum_possible(sum:int) -> bool:
        
        cuts, min_sum  = 0, 0
        
        for x in nums:
            min_sum +=x
            
            if min_sum > sum:
                cuts += 1
                min_sum = x
        
        subs = cuts + 1

        return (subs > m)
    
    left,right = max(nums),sum(nums)

    while left < right:
        mid = left + (right-left)//2

        if max_sum_possible(mid):
            left = mid + 1
        else:
            right = mid
    return left

nums = [7,2,5,10,8]
m = 2

print(minimise_max_sum(nums,m))
