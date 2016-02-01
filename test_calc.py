from calc.calc import *

def test_normal_calc():
    tree = Tree(3, 2)
    assert calc(tree) == 5
    tree = Tree(3, Tree(2, 4))
    assert calc(tree) == 9

def test_minus():
    tree = Tree("-", Tree(2, 4))
    assert calc(tree) == -6
    tree = Tree(Tree("-", Tree(2, 4)), 3)
    assert calc(tree) == -3
