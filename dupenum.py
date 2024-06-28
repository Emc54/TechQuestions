"""
Find the duplicate number in a list
"""
import random

def sum_and_diff(arr):
    
    arr_sum = sum(arr)
    calc_sum = len(arr) * (len(arr)-1)//2 
    
    return  arr_sum - calc_sum


test_array = [i for i in range(1,100)]
test_array.append(98)
random.shuffle(test_array)

print(sum_and_diff(test_array))
