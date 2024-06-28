
"""
    Find the greatest common divisor of two numbers recursively
"""

def gcd(a: int, b: int)->int:
    
    # ensure inputs are positive
    a = abs(a)
    b = abs(b)

    if b == 0: 
        return a

    return gcd(b,a%b)

print(gcd(234,324))

