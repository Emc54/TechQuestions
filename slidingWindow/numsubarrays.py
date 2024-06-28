"""
Find how many subarrays multiply to less than k in an array
"""


def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        ans = left = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
                
            ans += right - left + 1
        return ans

arr = [3,4,6,2,3,4,6,4,3,4,4,2,1,1,2,3,3,1,2,3,1,43,4,2]

print(numSubarrayProductLessThanK(arr,4))

