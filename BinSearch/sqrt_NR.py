"""
    Implement a square root function
"""


def binSearchSqrt(x:float,e=0.001) -> float:

    # y = sqrt(x)
    # y*y = x
    # y*y - x = 0
    root = x 

    bottom, top = 0, x
    while abs(root*root-x)>e:
        root = bottom + (top - bottom) / 2
        if root*root > x:
            top = root
        else:
            bottom = root
   
    return root 

print(binSearchSqrt(2))


def NR_Sqrt(x:float,e=0.001) -> float:

    root = x

    # f(y) = y^2-x
    # f'(y) = 2y
    # NR: y1 = y0 - (y0^2-x)/(2y0)

    while abs(root*root-x)>e:
        root = root - (root*root-x)/(2*root)

    return root

print(NR_Sqrt(2))
