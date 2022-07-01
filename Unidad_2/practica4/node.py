
"""
          4
        /    \
       2      6
      / \    / \
     1   3  5   7
    /            \
   0              8
"""

class Node:
    """Representa un nodo que contendra las referencias izq y der"""
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        """Representacion de un nodo"""
        left = None if self.left is None else self.left.value
        right = None if self.right is None else self.right.value
        return f' value: {self.value}\n left: {left}\n right: {right}'



n = Node(4)
n.left = Node(2)
n.right = Node(6)


(n)
    
    
        
        
