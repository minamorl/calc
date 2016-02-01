def calc(tree):
    if isinstance(tree, tuple):
        if calc(tree[0]) is not "-":
            return calc(tree[0]) + calc(tree[1])
        return -1 * calc(tree[1])
    return tree
