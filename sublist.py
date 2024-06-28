""" Check if a contiguous subarray with 0 sum exists in an array"""

def hasZeroSumSub(nums):
 
    s = set()

    s.add(0)
    total = 0

    for i in nums:
        total += i

        if total in s:
            return True
        
        s.add(total)

    return False

nums = [4, -6, 3, 1, -2, 7]

print(hasZeroSumSub(nums))


""" Print all contiguous subarrays with 0 sum in an array"""


def util_insert(d,key,val):
    # If the key in new, initialise a list
    d.setdefault(key,[]).append(val)

def printSublists(nums):
    
    d={}
    util_insert(d,0,-1)

    total = 0

    for i in range(len(nums)):
        
        total += nums[i]

        if total in d:
            l = d.get(total)

            for val in l:
                print("Sublist:", (val+1,i))
        
        util_insert(d,total,i)

printSublists(nums)
