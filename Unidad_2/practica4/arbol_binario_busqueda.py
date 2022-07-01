import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout


def build_graph(root, g=None):
    if g is None:
        g = nx.Graph()
    if root is not None:
        build_graph(root.left, g)
        g.add_node(root.val)
        if root.left is not None:
            g.add_edge(root.val, root.left.val)
        if root.right is not None:
            g.add_edge(root.val, root.right.val)
        build_graph(root.right, g)
    return g


class Node:
    """Representa un nodo que contendra las referencias izq y der"""
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        """Representacion de un nodo"""
        left = None if self.left is None else self.left.val
        right = None if self.right is None else self.right.val
        return f' value: {self.val}\n left: {left}\n right: {right}'

    def insert(self, val):
        """Inserta un valor donde preserve un orden.
        
        No puede haber valores repetidos, usamos busqueda binaria para inserta.
        """
        if self.val == val:
            return
        
        if val > self.val:
            if self.right is None:
                self.right = Node(val)
            else:                
                self.right.insert(val)                
        elif val < self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)

    def search(self, x):
        """Utiliza busqueda binaria dado que es un arbol de busqueda."""
        if self.val == x:
            return self
        elif x < self.val:
            if self.left is None:
                return
            else:
                return self.left.search(x)
        elif x > self.val:
            if self.right is None:
                return
            else:
                return self.right.search(x)

def in_order(root):
    """Recorre un arbol izq,node,der."""
    if root is None:
        return
    in_order(root.left)
    

(root.val)
    in_order(root.right)
        
def pre_order(root):
    if root is None:
        return
    

(root.val)
    pre_order(root.left)
    pre_order(root.right)

def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    

(root.val)
    


def min_value(root):
    """Busca el nodo minimo del lado izquiero de los mayores de nodo"""
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root

def delete(root, x):
    if root is None:
        return
    if root.val == x:
        # Tenenemos un hijo derecho
        if root.left is None:
            new = root.right
            root = None
            return new
        # Tenenemos sólo el hijo izquierdo
        elif root.right is None:
            new = root.left
            root = None
            return new
        else:
            # Tenemos ambos hijos
            new = min_value(root.right)
            root.val = new.val
            root.right = delete(root.right, new.val)
            return root
    else:
        if root.val < x:
            root.right = delete(root.right, x)
        else:
            root.left = delete(root.left, x)
        return root
        
    
    
tree = Node(4)
tree.insert(2)
tree.insert(1)
tree.insert(0)
tree.insert(3)
tree.insert(6)
tree.insert(5)
tree.insert(7)
tree.insert(8)
# print(root)
# print("Buscar 3: ", tree.search(3))
#in_order(tree)
#pre_order(tree)
post_order(tree)




g = build_graph(tree)
fig, ax = plt.subplots(figsize=(10, 8))
pos = graphviz_layout(g, prog='dot')
nx.draw(g, with_labels=True, ax=ax, pos=pos)

        
