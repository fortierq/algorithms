class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BST:
    def __init__(self, val):
        self.root = None
    
    def add_node(self, val, node):
        if not node:
            return Node(val)
        if val < node.val:
            node.left = self.add_node(val, node.left)
        else:
            node.right = self.add_node(val, node.right)
        return node
    
    def add(self, val):
        self.root = self.add_node(val, self.root)

    def del_max(self):  # does not work if root is max
        v, prev = self, self
        while v.right:
            prev = v
            v = v.right
        prev.right = None
        return v.val
    
    def rm(self, val):
        def aux(node):
            if node.val == val:
                if not node.left:
                    return node.right
                if self.left.right:  # can call self.left.del_max
                    self.val = self.left.del_max()
                else:
                    self = self.left
            elif val < self.val:
                self.left = self.left.rm(val)
            else:
                self.right = self.right.rm(val)
            return self

    def __contains__(self, val):
        def aux(node):
            if not node:
                return False
            if node.val == val:
                return True
            if val < node.val:
                return aux(node.left)
            else:
                return aux(node.right)
        return aux(self.root)
