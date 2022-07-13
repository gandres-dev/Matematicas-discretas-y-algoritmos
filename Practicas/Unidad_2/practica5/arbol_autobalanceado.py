
"""
Arbol binario de busqueda baleanceado
Los hijos de un nodo rojo deben ser negros.
(No puede haber dos nodos rojos adyacentes)


Los metodos de insercion y borrado es más facil
si los nodos continene dos hijos.

La idea es crear un nodo centinela que estara fuera del arbol,
y los nodos le falten hijos los uniremos al nodo centinela

Operacion Rotacion
Para cualquier arbol binario

https://youtu.be/NXSbDId9sp8
https://youtu.be/PhY56LpCtP4
https://youtu.be/oXfWTizpiHY
https://www.cs.usfca.edu/~galles/visualization/RedBlack.html

"""

class RBNode:
    """Representa un nodo para un arbol balanceado black-red"""
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None



class RBTree:

    def __init__(self):
        self.nil = RBNode(None)  # Representa el nodo centinela
        self.root = self.nil  # Decimos que sea igual al nodo centinela

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)
        
    def rotate_left(self, x):
        """ Rotacion a la izquierda el pivote sera x y y el nodo derecho"""
        y = x.right  # y apuntara a x.right
        x.right = y.left # cortamos la arista de x.right ahora apunta y.left
        if y.left != self.nil:
            y.left.parent = x # Cambiamos el padre a x
        # Hacemos la rotatacion, y esta en la posicion del pivote
        y.parent  = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.left = y
        y.left = x
        x.parent = y
        
    def rotate_right(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.parent = y

        x.parent = y.parent
        if y.parent == None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
        
    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right: # si el padre es izquierdo
                u = new_node.parent.parent.left  # tío (hermano del padre)
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left: # Caso 2 
                        self.rotate_right(new_node.parent)
                        new_node = new_node.parent
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
                    
            else: # si el padre es derecho
                u = new_node.parent.parent.right # tío (hermano del padre)

                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
        self.root.red = False

    def __repr__(self):
        return print_tree(self.root)    
        
    def rb_transplant(self, u,v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.p.left = v
        else:
            u.parent.right = v
        v.parent = u.p


    def rb_delete(self, z):
        y = z
        y_original_color = y.red
        if z.left == T.nil:
            x = z.right
            rb_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            rb_transplant(z, z.left)
        else:
            y = min_value(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == False:
            rb_delete_fixup(x)

    def rb_delete_fixup(self, x):
        while x != self.root and x.color == False:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == True:
                    w.color = False
                    x.parent.color = True
                    rotate_left(x.parent)
                    w = x.parent.right
                if w.left.color == False and w.right.color == False:
                    w.color = True
                    x = x.p
                else:
                    if w.right.color == False:
                        w.left.color == False
                        w.color = True
                        rotate_right(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = False
                    w.right.color = False
                    rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.right
                if w.color == True:
                    w.color = False
                    x.parent.color = True
                    rotate_right(x.parent)
                    w = x.parent.right
                if w.right.color == False and w.right.color == False:
                    w.color = True
                    x = x.p
                else:
                    if w.right.color == False:
                        w.right.color == False
                        w.color = True
                        rotate_right(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = False
                    w.right.color = False
                    rotate_right(x.parent)
                    x = self.root
        x.color = False
                
                                                                              

def min_value(root):
    if root is not None:
        while root.left is not None:
            root = root.left
        return root
    else:
        return None
