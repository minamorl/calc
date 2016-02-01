from calc.tokenize import *
from calc.parse import *

def test_parse1():
    expr = "1"
    tokens = Tokenizer().tokenize(expr)

    assert (0, 1) == parse(None, tokens)

def test_parse():
    expr = "1+1"
    tokens = Tokenizer().tokenize(expr)

    assert ((0, 1), 1) == parse(None, tokens)

def test_parse2():
    expr = "1+2+3+4+5"
    tokens = Tokenizer().tokenize(expr)

    assert (((((0, 1), 2), 3), 4), 5) == parse(None, tokens)
