"""
Given an integer array bloomDay, an integer m and an integer k.

We need to make m bouquets. To make a bouquet, you need to use k adjacent 
flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i]
and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m 
bouquets from the garden. If it is impossible to make m bouquets return -1.

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let's see what happened in the first three days. x means flower 
bloomed and _ means flower didn't bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
"""


# if k*m > len(array):
#   return -1

def minDays(bloomday: list[int],m: int,k: int) -> int:
    
    def feasable(days: int) -> bool:
        bouquets, flowers = 0,0
        for bloom in bloomday:
            if bloom > days:
                flowers = 0
                print(f"NO, Days:{days},B:{bouquets},F:{flowers}")
            else:
                bouquets += (flowers + 1) // k
                flowers = (flowers + 1) % k
                print(f"YES, Days:{days},B:{bouquets},F:{flowers}")
        return bouquets >= m

    if k*m > len(bloomday):
        return -1

    left, right = 1, max(bloomday)

    while left < right:

        mid = left + (right-left)//2
        if feasable(mid):
            right = mid
        else:
            left = mid + 1 

    return left


blooms = [7,7,7,7,12,9,7]
m=2
k=3

# Day 01 [_,_,_,_,_,_,_]
# Day 02 [_,_,_,_,_,_,_]
# Day 03 [_,_,_,_,_,_,_]
# Day 04 [_,_,_,_,_,_,_]
# Day 05 [_,_,_,_,_,_,_]
# Day 06 [_,_,_,_,_,_,_]
# Day 07 [x,x,x,x,_,_,x] B=1,  F=1
# Day 08 [x,x,x,x,_,_,x] B=1,  F=1
# Day 09 [x,x,x,x,_,x,x] B=2,  F=1
# Day 10 [x,x,x,x,_,x,x] B=2,  F=0
# Day 11 [x,x,x,x,_,x,x] B=2,  F=0
# Day 12 [x,x,x,x,x,x,x] B=3,  F=0
# Day 13 [_,_,_,_,_,_,_]


print(minDays(blooms,m,k))

