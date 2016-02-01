
import enum

class Token(enum.Enum):
    minus = 1
    space = 2
    integer = 3
    operator = 4
    parenthesis_start = 5
    parenthesis_end = 6
    


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
                    tokens.append((temp, Token.integer))
                    temp = ""
            
            if x is None:
                return tokens

            if is_integer(x):
                current_state = Token.integer
                temp += x

            if x == "(":
                current_state = Token.parenthesis_start
                tokens.append((x, Token.parenthesis_start))
                if consume(xs)[0] == "-":
                    current_state = Token.integer
                    temp = "-"
                    string = consume(xs)[1]
                    continue

            if x == ")":
                current_state = Token.parenthesis_end
                tokens.append((x, Token.parenthesis_end))

            if x in " ":
                current_state = Token.space
                if x == "(" and consume(xs)[0] == "-":
                    current_state = Token.space
                    temp = "-"
                    string = consume(xs)[1]
                    continue

            if x in "+":
                current_state = Token.operator
                tokens.append((x, Token.operator))

            if x in "-":
                if is_integer(consume(xs)[0]):
                    current_state = Token.integer
                    temp = "-"
                    continue
                current_state = Token.minus
                tokens.append((x, Token.minus))


