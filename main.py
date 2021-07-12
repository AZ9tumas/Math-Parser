from lexer import Lexer
from tokens import *

class Term:

    def __init__(self, type_, constant=None, var=None) -> None:
        self.constant = constant
        self.var = var
        self.type = type_

    def __repr__(self) -> str:
        return f'{self.type}{self.constant and self.constant or ""}{self.var and self.var or ""}'

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

    def term(self):
        pass

    def expression(self):
        pass

    def bin_op(self, func, ops):
        left = func()
        
        while self.current_token.type in ops:
            op_tok = self.current_token
            right = func()

class getValues():
    def __init__(self, hand) -> None:
        self.hand = hand
        self.idx = -1
        self.current_token = None
        self.advance()
        self.vars = []
        self.constants = []
        self.get()
    
    def advance(self, itr = 1):
        self.idx +=itr
        self.current_token = self.idx < len(self.hand) and self.hand[self.idx] or None

    def goBack(self, itr=1):
        self.idx-=itr
        self.current_token = self.idx < len(self.hand) and self.idx >=0 and self.hand[self.idx] or None

    def get(self):
        while self.current_token != None:
            op = '+'
            if self.current_token.type in (TT_PLUS, TT_MINUS, TT_MUL, TT_DIV):
                op = self.current_token.value
                self.advance()
            token = self.current_token
            if not token: return
            self.advance()
            if self.current_token and self.current_token.type == token:return
            if self.current_token and self.current_token.type == TT_VAR:
                self.vars.append(Term(type_=op, constant=token.value, var=self.current_token.value))
                
                self.advance()
            else:
                if token.type == TT_VAR:
                    self.vars.append(Term(type_=op, var=token.value))
                elif token.type==TT_NUM:
                    self.constants.append(Term(type_=op, constant=token.value))

class evaluate:
    def __init__(self, values) -> None:
        self.constant_expr = str(values[0]).replace(',','').strip('[').strip(']')
        self.vars_expr = str(values[1]).replace(',','').strip('[').strip(']')
        self.constant = f"{eval(self.constant_expr)}{self.vars_expr}"

    
    def eval_var(self):
        pass
        

def run(statement):
    lxr = Lexer(statement)
    tokens = lxr.Make_Tokens()
    # print(tokens)

    if isinstance(tokens, str) or tokens==None:return

    # Get LHS and RHS
    hands = Hands(tokens)
    # print('LHS:',hands.LHS)
    # print('RHS:',hands.RHS, end = '\n\n')

    if isinstance(hands, str) or hands == None or hands.LHS == None or hands.RHS == None: return

    # Get Constants and Variables
    LHSvalues = getValues(hands.LHS)
    RHSvalues = getValues(hands.RHS)
    
    print('LHS vars:',LHSvalues.vars,'LHS constants:',LHSvalues.constants)
    print('RHS vars:',RHSvalues.vars,'RHS constants:',RHSvalues.constants, end = '\n\n')
    
    lhs_evaluation = evaluate([LHSvalues.constants, LHSvalues.vars]).constant
    rhs_evaluation = evaluate([RHSvalues.constants, RHSvalues.vars]).constant

    print(f"{lhs_evaluation} = {rhs_evaluation}")

