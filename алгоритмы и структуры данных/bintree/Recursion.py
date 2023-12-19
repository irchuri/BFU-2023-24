class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

    def total(self):
        if self == None: return 0
        return total(self.left) + total(self.right) +self.cargo

t = Tree(1,Tree(2),Tree(3))
print(t)