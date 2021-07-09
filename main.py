from lexer import Lexer

class expression:

    pass



def run(statement):
    lxr = Lexer(statement)
    tokens = lxr.Make_Tokens()
    print(tokens)

    

