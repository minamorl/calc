from tokenizer import tokenize
t = tokenize.Tokenizer()
def test_tokenize():
    assert t.tokenize("1+11") == ["1", "+", "11"]
    assert t.tokenize("1+(1321)") == ["1", "+", "(", "1321", ")"]
