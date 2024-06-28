""" 
Initialize an element m and a counter i = 0  
for each element x of the input sequence:   
    if i = 0, then     
        assign m = x and i = 1   
    else     
        if m = x, then 
            assign i = i + 1   
        else     
            assign i = i – 1 
    return m 
"""

def Boyer_Moore_majority_vote(nums):

    counter = 0
    maj = -1

    for j in range(len(nums)):
        
        if counter == 0:
            maj = nums[j]
            counter = 1

        elif maj == nums[j]:
            counter += 1
        else: 
            counter -= 1 
    return maj

nums = [2,4,5,2,4,2,3,4,5,6,5,3,2,43,45,24,3,2]
nums2 = [1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2]
print(Boyer_Moore_majority_vote(nums))


"""
Produces correct results only if a majority is present, otherwise garbage.
Linear time, linear space.
"""
