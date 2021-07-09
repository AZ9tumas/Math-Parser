
TT_NUM      = 'NUMBER'
#Operators
TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
TT_MUL      = 'MUL'
TT_DIV      = 'DIV'
TT_MOD      = 'MOD'
TT_POW      = 'POW'
TT_EQUALS   = 'EQUAL'

#Round Brackets
TT_LPAREN   = 'LPAREN'
TT_RPAREN   = 'RPAREN'

TT_VAR      = 'VAR'

class Token:
    def __init__(self, type_, value=None):
        self.value = value
        self.type = type_

    def matches(self, token):
        return token.value == self.value and token.type == self.type

    def __repr__(self) -> str:
        return f'{self.type}:{self.value}' if self.value != None else str(self.type)

