from .tokenize import Token



class Parser():
    def __init__(self):
        self.stack_size = 20
        self.stack = [None] * self.stack_size

    def parse(self, child, tokens, stack_level=0):

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
                return self.parse(_child, next_tokens, stack_level)

        if context is Token.operator:
            return self.parse(child, next_tokens, stack_level)

        if context is Token.minus:
            return ("-", self.parse(child, next_tokens, stack_level))

        if context is Token.parenthesis_start:
            self.stack[stack_level] = child
            return self.parse(None, next_tokens, stack_level=stack_level + 1)

        if context is Token.parenthesis_end:
            _child = child, self.stack[stack_level - 1]
            return self.parse(_child, next_tokens, stack_level - 1)
