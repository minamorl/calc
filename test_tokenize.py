from calc.tokenize import *
t = Tokenizer()
def test_tokenize():
    assert t.tokenize("1+1") == [("1", Token.integer),
                                 ("+", Token.operator),
                                 ("1", Token.integer),]

def test_tokenize():
    assert t.tokenize("-(-(1))") == [("-", Token.minus),
                                 ("(", Token.parenthesis_start),
                                 ("-", Token.minus),
                                 ("(", Token.parenthesis_start),
                                 ("1", Token.integer),
                                 (")", Token.parenthesis_end),
                                 (")", Token.parenthesis_end),]
