"""
Koko loves to eat bananas.  
There are N piles of bananas, the i-th pile has piles[i] bananas.  
The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.  
Each hour, she chooses some pile of bananas, and eats K bananas from that pile.
If the pile has less than K bananas, she eats all of them instead, and won't 
eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas 
before the guards come back.

Return the minimum integer K such that she can eat all the bananas within 
H hours.
"""

# bananas-per-hour = K
# piles_num = n
# hours = H

# min K to eat all N within H hours
# N is an unsorted list of integers.
# H is a counter.

piles = [3,6,7,11]
hours = 8
answer = 4
import math

def visiting_pile(k: int,pile: int) -> int: 
    if k > pile:
        return 0
    else:
        return pile - k

def all_bananas_eaten(piles, hours,K) -> bool:
    temp_piles = piles
    temp_hours = hours

    while temp_hours > 0:
        
        for i in range(len(temp_piles)):
            
            if temp_hours < 0:
                return False
            
            if sum(temp_piles) == 0:
                return True 

            temp_piles[i] = visiting_pile(K, temp_piles[i])
            
            temp_hours -= 1

    return False

### convoluted solution, not optimal

def minimise_K(piles: list[int],hours: int)-> int:
   
    # if the num of piles > hours total then impossible
    # therefore, the largest pile is the biggest K needs to get
    # in the worst case

    K_list = [x for x in range(1,max(piles)+1)]

    left, right = 1, len(K_list) -1

    while left < right:

        mid = left + (right - left) // 2
        
        if all_bananas_eaten(piles,hours,K_list[mid]):
            right = mid
        else:
            left = mid +1 
    return left
   


### better solution, simpler checking for the condition

def min_speed(piles: list[int], hours: int) -> int:

    def all_bans_eaten(speed: int) -> bool:
        all_bans_per_hour = sum(math.ceil((pile)/speed) for pile in piles)
        return all_bans_per_hour <= hours
    
    left, right = 1, max(piles)

    while left < right:
        mid = left + (right-left)//2
        
        if all_bans_eaten(mid):
            right = mid
        else:
            left = mid+1
    return left


print(min_speed(piles,hours))


