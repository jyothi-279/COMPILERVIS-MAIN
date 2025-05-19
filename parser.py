import ply.yacc as yacc
from lexer import tokens, t_PLUS, t_MINUS, t_TIMES, t_DIVIDE, t_LPAREN, t_RPAREN, t_NUMBER, t_ignore

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = {"op": p[2], "left": p[1], "right": p[3]}

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = {"num": p[1]}

def p_error(p):
    print("Syntax error in input!")

def parse_expression(tokens_list):
    import ply.lex as lex  # do NOT redefine lexer here
    lexer = lex.lex()
    import ply.yacc as yacc
    parser = yacc.yacc()
    input_str = ''.join(str(t["value"]) for t in tokens_list)
    return parser.parse(input=input_str, lexer=lexer)
