"""Given a binary array, sort it in linear time and constant space.
Output should be all zeroes and then all ones"""

def countBinlist(l):
    ones = 0

    for i in l:
        if i:
            ones+=1
   
    sorted_list = [0]*(len(l)-ones)
    sorted_list.extend([1]*ones)
    return sorted_list 


print(countBinlist([0,1,0,0,0,0,1,1,1,0,1,0,1,0]))
