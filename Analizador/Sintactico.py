import ply.yacc as yacc
from Analizador.Lexico import tokens
from Instrucciones.Declaracion import DeclaracionVariable


# ?-------------------PRODUCCIONES--------------------------
def p_inicio1(t):
    'inicio : instrucciones main'

    t.lexer.lineno = 1
    t.lineno = 1
    t[1].append(t[2])
    t[0] = t[1]


def p_inicio2(t):
    'inicio : main'

    t[0] = t[1]


def p_main(t):
    'main : FN MAIN PARIZQ PARDER LLAVEIZQ instrucciones LLAVEDER'
    t[0] = t[6]


def p_instrucciones1(t):
    'instrucciones : instrucciones instruccion'

    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones2(t):
    'instrucciones : instruccion'

    t[0] = [t[1]]


def p_instrucion(t):
    'instruccion : declaracion'

    t[0] = t[1]


def p_declaracion1(t):
    'declaracion : LET MUT ID DOSPT tipo IGUAL expresion PTCOMA'

    t[0] = DeclaracionVariable(t.lineno(2), t[5], t[3], t[7], True)


def p_declaracion2(t):
    'declaracion : LET MUT ID IGUAL expresion PTCOMA'
    t[0] = DeclaracionVariable(t.lineno(2), None, t[3], t[5], True)


def p_declaracion3(t):
    'declaracion : LET ID DOSPT tipo IGUAL expresion PTCOMA'
    t[0] = DeclaracionVariable(t.lineno(2), t[4], t[2], t[6],False)


def p_declaracion4(t):
    'declaracion : LET ID IGUAL expresion PTCOMA'
    t[0] = DeclaracionVariable(t.lineno(2), None, t[2], t[4], False)


def p_tipo(t):
    '''tipo : I64
            | F64
            | BOOL
            | CHAR
            | STR
            | STRING
    '''
    t[0] = t[1]


def p_expresion(t):
    '''expresion : ID
                | ENTERO
                | DECIMAL
                | TRUE
                | FALSE
                | CADENA
                | CARACTER
    '''
    t[0] = t[1]


def p_error(t):
    print("Error sintáctico. %s" % t.value[0])


# ? Se ejecuta el parser
parser = yacc.yacc()

entrada = ''' 
fn main() {
let mut var1 : i64 = 1;
let var2 : i64 = 2;
let mut var3 = 3;
let var4 = 4;
let mut var5 : bool = true;
let mut var6 : String = "hola";
let mut var7 : char = 'a';
let mut var8 : &str = "hola";
}
'''
print("inicia analizador...")
instruc = parser.parse(entrada)

for instru in instruc:
    instru.ejecutar(None)
