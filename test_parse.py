from calc.tokenize import *
from calc.parse import *
from calc.calc import calc

parse = Parser().parse
def test_parse1():
    expr = "1"
    tokens = Tokenizer().tokenize(expr)

    assert (0, 1) == parse(None, tokens)


def test_parse2():
    expr = "1+2+3+4+5"
    tokens = Tokenizer().tokenize(expr)

    assert (((((0, 1), 2), 3), 4), 5) == parse(None, tokens)


def test_parse3():
    expr = "1+2+3+4+-5"
    tokens = Tokenizer().tokenize(expr)

    assert (((((0, 1), 2), 3), 4), -5) == parse(None, tokens)
    assert calc(parse(None, tokens)) == 5


def test_parse4():
    expr = "1+(2+3)+((-4)+-5)"
    tokens = Tokenizer().tokenize(expr)

    assert (((((0, 1), (2, 3)), 4), -5)) == parse(None, tokens)
    assert calc(parse(None, tokens)) == 5
