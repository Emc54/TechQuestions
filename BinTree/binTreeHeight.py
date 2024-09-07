"""
Calculate the height of a binary tree
"""



class Node:

    def __init__(self,key=None,left=None,right=None) -> None:
        self.key=key
        self.left=left
        self.right=right


def height(node: Node)->int:

    if node is None:
        return 0 
        
    return 1 + max(height(node.left), height(node.right))
    
if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    print(height(root))
