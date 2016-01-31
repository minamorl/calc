from tokenizer import tokenize
t = tokenize.Tokenizer()
def test_tokenize():
    assert t.tokenize("1+1") == [("1", tokenize.Token.integer),
                                 ("+", tokenize.Token.operator),
                                 ("1", tokenize.Token.integer),]

def test_calc():
    parsed = t.tokenize("1+10")
    assert tokenize.calc(parsed) == 11

