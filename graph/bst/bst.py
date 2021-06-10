class BST:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    
    def add(self, val):
        if val < self.val:
            if not self.left:
                self.left = BST(val)
            else:
                self.left.add(val)
        elif not self.right:
            self.right = BST(val)
        else:
            self.right.add(val)
    
    def __contains__(self, val):
        t = self.left if val < self.val else self.right
        return val == self.val or (t and val in t)
