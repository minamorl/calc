from calc.tokenize import *
t = Tokenizer()
def test_tokenize():
    assert t.tokenize("1+1") == [("1", Token.integer),
                                 ("+", Token.operator),
                                 ("1", Token.integer),]

