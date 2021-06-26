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
    
    def del_max(self):
        v, prev = self, self
        while v.right:
            prev = v
            v = v.right
        prev.right = None
        return v.val
    
    def rm(self, val):
        if self.val == val:
            if self.left:
                self.val = self.left.del_max()
            else:
                return self.right
        else:
            if val < self.val:
                self.left = self.left.rm(val)
            else:
                self.right = self.right.rm(val)
        return self

    def __contains__(self, val):
        t = self.left if val < self.val else self.right
        return val == self.val or (t and val in t)
