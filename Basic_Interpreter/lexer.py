
import re

class Lexer:
    token_specification = [
        ('NUMBER', r'\d+'),       # Integer
        ('PLUS', r'\+'),          # Addition operator
        ('MINUS', r'-'),          # Subtraction operator
        ('ID', r'[A-Za-z]+'),     # Identifiers (variables)
        ('ASSIGN', r':='),        # Assignment operator
        ('LPAREN', r'\('),        # Left parenthesis
        ('RPAREN', r'\)'),        # Right parenthesis
        ('SKIP', r'[ \t\n]+'),    # Skip spaces, tabs, and newlines
        ('MISMATCH', r'.'),       # Any other character (error)
    ]

    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.tokens = []
        self._tokenize()

    def _tokenize(self):
        tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in self.token_specification)
        get_token = re.compile(tok_regex).match
        while self.pos < len(self.code):
            match = get_token(self.code, self.pos)
            if match:
                type = match.lastgroup
                value = match.group(type)
                if type == 'SKIP':
                    pass
                elif type == 'MISMATCH':
                    raise RuntimeError(f'Unexpected character: {value!r}')
                else:
                    self.tokens.append((type, value))
                self.pos = match.end()
            else:
                raise RuntimeError(f'Unexpected character: {self.code[self.pos]!r}')

    def get_tokens(self):
        return self.tokens