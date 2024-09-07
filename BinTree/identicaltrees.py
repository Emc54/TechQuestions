"""
    Check if two binary trees are identical
"""

class Node:    

    def __init__(self,key=None,left=None,right=None) -> None:
        self.key = key
        self.left = left
        self.right = right


def isIdentical(x,y):

    # Check if both trees are empty
    if x is None and y is None:
        return True

    result = \
        (x is not None and y is not None) and \
        (x.key == y.key) and \
        isIdentical(x.left,y.left) and \
        isIdentical(x.right,y.right)

    return result


if __name__ == '__main__':
 
    # construct the first tree
    x = Node(15)
    x.left = Node(10)
    x.right = Node(20)
    x.left.left = Node(8)
    x.left.right = Node(12)
    x.right.left = Node(16)
    x.right.right = Node(25)
 
    # construct the second tree
    y = Node(15)
    y.left = Node(10)
    y.right = Node(20)
    y.left.left = Node(8)
    y.left.right = Node(12)
    y.right.left = Node(16)
    y.right.right = Node(25)

    print(f"Are the trees identical? -- {isIdentical(x,y)}")

    print(x.key, x.left.key, x.right.key)
