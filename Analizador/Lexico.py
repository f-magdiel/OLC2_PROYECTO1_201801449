import ply.lex as lex
import re

reservadas={
    'i64': 'I64',
    'f64': 'F64',
    'bool': 'BOOL',
    'true': 'TRUE',
    'false': 'FALSE',
    'char': 'CHAR',
    'str': 'STR',
    'string': 'STRING',
    'mut': 'MUT',
    'let': 'LET',
    'fn': 'FN',
    'main': 'MAIN',



}

tokens=[
    'ID',
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'CARACTER',
    'LLAVEIZQ',
    'LLAVEDER',
    'PTCOMA',
    'PARIZQ',
    'PARDER',
    'IGUAL',
    'DOSPT'

]
tokens += list(reservadas.values())

#tokens
t_LLAVEIZQ = r'{'
t_LLAVEDER = r'}'
t_PTCOMA = r';'
t_DOSPT = ':'
t_IGUAL = r'='
t_PARIZQ = r'\('
t_PARDER = r'\)'

#?---------------FUNCIONES----------------------------
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        desc = f'Valor decimal incorrecto {t.value}'
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        desc = f'Valor entero incorrecto {t.value}'
        t.value = 0
    return t

def t_CARACTER(t):
    r'\'([^\"\n\r\\]|\\n|\\r|\\t|\\"|\\\'|\\\\)?\''
    t.value = t.value[1:-1]  # remuevo las comillas
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\N', '\n')
    t.value = t.value.replace('\\r', '\r')
    t.value = t.value.replace('\\R', '\r')
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\T', '\t')
    t.value = t.value.replace('\\\"', '\"')
    t.value = t.value.replace('\\\'', '\'')
    t.value = t.value.replace('\\\\', '\\')
    return t

def t_CADENA(t):
    r'"([^\"\n\r\\]|\\n|\\r|\\t|\\"|\\\'|\\\\)*?"'
    t.value = t.value[1:-1]  # remuevo las comillas
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\N', '\n')
    t.value = t.value.replace('\\r', '\r')
    t.value = t.value.replace('\\R', '\r')
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\T', '\t')
    t.value = t.value.replace('\\\"', '\"')
    t.value = t.value.replace('\\\'', '\'')
    t.value = t.value.replace('\\\\', '\\')
    return t

def t_COMENTARIO_SIMPLE(t):
    r'\\[^\*].*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = ' \t\r'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    desc = 'Caracter invalido %s' % t.value[0]
    #lista_errores.append(Error(TIPO_ERROR.LEXICO, desc, t.lexer.lineno))
    t.lexer.skip(1)

#?Construyendo el analizador léxico
lexer = lex.lex()



