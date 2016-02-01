class Tree():
    def __init__(self, left, right):
        self.left = left
        self.right = right

def calc(tree):
    if isinstance(tree, Tree):
        return calc(tree.left) + calc(tree.right)
    return tree

