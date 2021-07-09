from lexer import Lexer
from tokens import *

class term:

    def __init__(self, type_, constant=None, var=None) -> None:
        self.constant = constant
        self.var = var
        self.type = type_

    def __repr__(self) -> str:
        return f'{self.type=="positive"and"+"or"-"}{self.constant and self.constant or ""}{self.var and self.var or ""}'

class Hands:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.LHS = None
        self.RHS = None
        self.getHands()


    def getHands(self):
        LHS = []
        RHS = []

        a=False
        for i in self.tokens:
            if i.type==TT_EQUALS:
                if a==True: return
                a=True
                continue
            if a:
                RHS.append(i)
            else: LHS.append(i)

        self.LHS = LHS
        self.RHS = RHS
            
class Parser:
    def __init__(self, hand) -> None:

        self.tokens = hand
        self.idx = -1
        self.current_token = None

        self.advance()

    def advance(self):
        self.idx +=1
        self.current_token = self.idx < len(self.tokens) and self.tokens[self.idx] or None

    def factor(self):
        pass
        

def run(statement):
    lxr = Lexer(statement)
    tokens = lxr.Make_Tokens()
    print(tokens)

    # Get LHS and RHS
    hands = Hands(tokens)
    print('LHS:',hands.LHS)
    print('RHS:',hands.RHS)

    # Get Constants and Variables
