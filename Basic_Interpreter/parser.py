from lexer import Lexer

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        return self._parse_expression()

    def _parse_expression(self):
        left = self._parse_term()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in ('PLUS', 'MINUS'):
            op = self.tokens[self.pos]
            self.pos += 1
            right = self._parse_term()
            left = (left, op, right)  # Simple binary tree structure
        return left

    def _parse_term(self):
        token = self.tokens[self.pos]
        if token[0] == 'NUMBER':
            self.pos += 1
            return int(token[1])  # Return the value of the number
        elif token[0] == 'ID':
            self.pos += 1
            return token[1]  # Return the variable name
        else:
            raise SyntaxError('Expected number or variable')