"""
Suppose you have n versions [1, 2, ..., n] and you want to find out the first 
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version 
is bad. Implement a function to find the first bad version. You should 
minimize the number of calls to the API.

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
"""

import random

versions = [n for n in range(20)]
bad_version = random.randint(2,19)

def isBadVersion(n):
    return n >= bad_version

def find_first_bad(versions: list[int]) -> int:
    
    left, right = versions[0], versions[-1]
    
    while left < right:
        mid = left + (right-left)//2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left

print(f"First bad version is {bad_version}")
print(f"The finder got {find_first_bad(versions)}")
