from calc.calc import *

def test_minus():
    tree = ("-", (2, 4))
    assert calc(tree) == -6
    tree = (("-", (2, 4)), 3)
    assert calc(tree) == -3
