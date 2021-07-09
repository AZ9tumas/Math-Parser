from tokens import *
import string

DIGITS = '0123456789'
LETTERS = string.ascii_letters

class Lexer:
    def __init__(self, expression):
        self.expression = expression
        self.idx = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.idx += 1
        self.current_char = self.idx < len(self.expression) and self.expression[self.idx] or None

    def Make_Tokens(self):
        tokens = []
        
        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char in LETTERS:
                tokens.append(self.make_identifier())
            elif self.current_char == '+':
                tokens.append(Token(type_=TT_PLUS))
                self.advance()
            elif self.current_char == '=':
                tokens.append(Token(type_=TT_EQUALS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(type_=TT_MINUS))
                self.advance()
            else:
                return f'Error, unsupported token type "{self.current_char}"'
        return tokens

    def make_number(self):
        num_str = ''
        dot_count = 0
        
        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        return Token(value=num_str, type_=TT_NUM)

    def make_identifier(self):
        identifier = ''

        while self.current_char != None and self.current_char in LETTERS:
            identifier += self.current_char
            self.advance()
        
        return Token(TT_VAR, identifier)