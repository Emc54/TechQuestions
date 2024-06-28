"""
Example 4: 392. Is Subsequence.

Given two strings s and t, return true if s is a subsequence of t, or false 
otherwise.

A subsequence of a string is a sequence of characters that can be obtained by 
deleting some (or none) of the characters from the original string, while 
maintaining the relative order of the remaining characters. For example, "ace"
is a subsequence of "abcde" while "aec" is not.
"""

def check_subsequence(string,substring):
    
    i = j = 0

    while i < len(string):
        
        if string[i] == substring[j]:
            i += 1
            j += 1
        else:
            i += 1
            
                
        if j == len(substring):
            return True

    return False


print(check_subsequence("flairs","ars"), check_subsequence("abcde","fg"))


"""
    LeetCode compact answer
"""

def subs(subsequence,teststring):
    i=j=0

    while i<len(subsequence) and j < len(teststring):
        if subsequence[i] == teststring[j]:
            i+=1
        j+=1

    return i == len(subsequence)
