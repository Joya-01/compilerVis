import ply.lex as lex

# Tokens must be defined at the top-level (not inside functions)
tokens = (
    'NUMBER', 'PLUS', 'MINUS',
    'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN'
)

# Token regex rules
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ignore  = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("Illegal character:", t.value[0])
    t.lexer.skip(1)

def tokenize(data):
    lexer = lex.lex()
    lexer.input(data)
    return [{"type": tok.type, "value": tok.value} for tok in lexer]
