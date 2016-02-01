from calc.calc import *

def test_calc():
    tree = Tree(3, 2)
    assert calc(tree) == 5
    tree = Tree(3, Tree(2, 4))
    assert calc(tree) == 9

