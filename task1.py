import ply.lex as lex

tokens = [
    'INT', 'FLOAT', 'CHAR',
    'IF', 'ELSE', 'WHILE', 'RETURN',
    'ID', 'NUMBER', 'FLOAT_NUMBER',
    'ASSIGN',
    'PLUS', 'MINUS', 'MULT', 'DIV',
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'SEMI', 'COMMA',
    'STRING',
    'EQ', 'NEQ', 'AND', 'OR',
    'LT', 'LE', 'GT', 'GE',
    'COLON'
]

t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_COMMA = r','
t_COLON = r':'

t_EQ = r'=='
t_NEQ = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='

def t_STRING(t):
    r'"([^\\"]|\\.)*"'
    t.value = t.value[1:-1]
    return t

reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'return': 'RETURN'
}

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_FLOAT_NUMBER(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    pass

def t_COMMENT_SINGLE_LINE(t):
    r'//.*'
    pass  # Token is ignored

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

code = '''
problem:
int x (float y) {
    if (y == 5.6)
        if (z == y)
            return z;
    else if (z == 5)
        return (z + 5);
    else 
        return (z + z);
}
'''

lexer.input(code)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
