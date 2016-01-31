import enum

class Token(enum.Enum):
    parenthesis = 1
    space = 2
    integer = 3
    operator = 4


def consume(s):
    if s is None:
        return None, None
    if len(s) > 1:
        return s[0], s[1:]
    elif len(s) == 1:
        return s[0], None
    elif len(s) == 0:
        return None, None

def is_integer(c):
    if c is not None:
        return c in "1234567890"
    return False

class Tokenizer():
    def tokenize(self, string):
        current_state = 0
        tokens = []
        temp = ""
        while True:
            x, xs = consume(string)
            string = xs


            if current_state is Token.integer:
                if not is_integer(x):
                    tokens.append(temp)
                    temp = ""
            
            if x is None:
                return tokens

            if is_integer(x):
                current_state = Token.integer
                temp += x

            if x in "+/-*":
                current_state = Token.operator
                tokens.append(x)
            
            


t = Tokenizer()
def test_tokenize():
    assert t.tokenize("1+11") == ["1", "+", "11"]
    assert t.tokenize("1+*11") == ["1", "+", "*", "11"]
