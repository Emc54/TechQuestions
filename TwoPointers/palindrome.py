def palindrome(a):
    left = 0
    right = len(a)-1

    while left < right:
        
        if a[left] != a[right]:
            return False
        left += 1
        right -= 1

    return True


print(palindrome("racecar"),palindrome("otto"),palindrome("meatem"))
