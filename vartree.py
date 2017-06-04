##Dreese, HW5

class VarTree:
    class Node:
        __slots__ = "_var","_val","_left","_right"
        def __init__(self, left, var, val, right):
            self._left = left
            self._var = var
            self._val = val
            self._right = right

    def __init__(self):
        self._root = None
        self._size = 0
        self._nextLoc = -1

    def getNextLoc(self):
        self._nextLoc += 1
        return self._nextLoc

    def _search(self, here, var):
        if here is None:
            return None
        elif var < here._var:
            return self._search(here._left, var)
        elif var > here._var:
            return self._search(here._right, var)
        else:
            return here

    def _insert(self, here, var, val):
        if here is None:
            self._size +=1
            return self.Node(None, var, val, None)
        elif var < here._var:
            return self.Node(self._insert(here._left, var, val), here._var, here._val, here._right)
        elif var > here._var:
            return self.Node(here._left, here._var, here._val, self._insert(here._right, var, val))
        else:
            here._val = val
            return here
        
    def assign(self, var, val):
        self._root = self._insert(self._root, var, val)

    def lookup(self, var):
        node = self._search(self._root, var)
        if node is None:
            self.assign(var, 0)
            return 0
        else:
            return node._val

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False
