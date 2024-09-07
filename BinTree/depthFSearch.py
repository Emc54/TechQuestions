"""
    Postorder Tree Traversal – Iterative and Recursive
"""

class Node:

    def __init__(self,key=None,left=None,right=None) -> None:
        self.key=key
        self.left=left
        self.right=right



def DFS(node):

    # Recursive postoder
    """
    Traverse all the left nodes first, then all the right nodes,
    _then_ process any data.
    """

    if node is None:
        return

    DFS(node.left)
    DFS(node.right)

    print(node.key, end=' ')




from collections import deque

def iterativeDFS(node):


    #Iterative postorder uses a stack
    if node is None:    
        return 
    
    stack = deque()
    stack.append(node)

    
    out = [] 

    while stack:

        curr = stack.pop()
        out.append(curr.key)

        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)

    # This is depth first but collected in reverse. So print it from the end
    # to the start
    print(out[::-1])

if __name__=='__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    DFS(root)
    iterativeDFS(root)



