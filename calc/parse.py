from .tokenize import Token


def parse(child, tokens):
    try:
        token, context = tokens[0]
        next_tokens = tokens[1:]
    except IndexError:
        return child

    if child is None:
        child = 0

    if context is Token.integer:
        _child = (child, int(token))
        if len(tokens) > 0:
            return parse(_child, next_tokens)

    if context is Token.operator:
        return parse(child, next_tokens)
    
    if context is Token.minus:
        return ("-", parse(child, next_tokens))
