import ply.yacc as yacc
from Analizador.Lexico import tokens
from Instrucciones.Declaracion import DeclaracionVariable
from Instrucciones.Imprimir import Imprimir
from Entorno.Entorno import Entorno
from Expresiones.Id import Id
from Expresiones.Primitva import Primitiva
from Enumeradas.Primitivo import tipoPrimitivo
from Instrucciones.Asignacion import AsignacionVariable
from Instrucciones.Imprimir import listimpresion
from Expresiones.Aritmetica import Aritmetica
from Enumeradas.OperadorAritmetica import OPERADOR_ARITMETICO
from Enumeradas.OperadorUnario import OPERADOR_UNARIO
from Expresiones.Unaria import Unaria

# ?---------------------PRECEDENCIAS----------------------------
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'IGUALQUE', 'NOIGUALQUE', 'MENORQUE', 'MENORIQUE', 'MAYORQUE', 'MAYORIQUE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'DIVIDIDO', 'POR', 'MODULO'),
    ('left', 'AS'),
    ('left', 'UMENOS', 'NOT'),

)


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
    '''instruccion : declaracion
                    | imprimir
                    | asignacion
    '''
    t[0] = t[1]


# !---------------------------------------------------IMPRIMIR-----------------------------------------------------

def p_imprimir1(t):
    'imprimir : PRINTLN EX PARIZQ expresion COMA expresiones PARDER PTCOMA'
    t[0] = Imprimir(t.lineno(2), t[4], t[6])


def p_imprimir2(t):
    'imprimir : PRINTLN EX PARIZQ expresion PARDER PTCOMA'
    t[0] = Imprimir(t.lineno(2), t[4], None)


# !-------------------------------------DECLARACION-------------------------------------------------------

def p_declaracion1(t):
    'declaracion : LET MUT ID DOSPT tipo IGUAL expresion PTCOMA'
    t[0] = DeclaracionVariable(t.lineno(2), t[5], t[3], t[7], True)


def p_declaracion2(t):
    'declaracion : LET MUT ID IGUAL expresion PTCOMA'
    t[0] = DeclaracionVariable(t.lineno(2), tipoPrimitivo.NULO, t[3], t[5], True)


def p_declaracion3(t):
    'declaracion : LET ID DOSPT tipo IGUAL expresion PTCOMA'
    t[0] = DeclaracionVariable(t.lineno(2), t[4], t[2], t[6], False)


def p_declaracion4(t):
    'declaracion : LET ID IGUAL expresion PTCOMA'
    t[0] = DeclaracionVariable(t.lineno(2), tipoPrimitivo.NULO, t[2], t[4], False)


# !---------------------------------ASIGNACION------------------------------------------
def p_asignacion1(t):
    'asignacion : ID IGUAL expresion PTCOMA'
    t[0] = AsignacionVariable(t.lineno(1), t[1], t[3])


# !----------------------------------------TIPO----------------------------------------------

def p_tipo1(t):
    '''tipo : I64
            | F64
            | BOOL
            | CHAR
            | STRING
    '''
    tipo = t[1]
    if (tipo == 'i64'):
        t[0] = tipoPrimitivo.I64
    elif (tipo == 'f64'):
        t[0] = tipoPrimitivo.F64
    elif (tipo == 'bool'):
        t[0] = tipoPrimitivo.BOOL
    elif (tipo == 'char'):
        t[0] = tipoPrimitivo.CHAR
    elif (tipo == 'String'):
        t[0] = tipoPrimitivo.STRING


def p_tipo2(t):
    'tipo : SIGNOI STR'
    t[0] = tipoPrimitivo.STR


# !------------------------------------------------EXPRESION--------------------------------------------------
def p_expresiones1(t):
    ' expresiones : expresiones COMA expresion'
    t[1].append(t[3])
    t[0] = t[1]


def p_expresiones2(t):
    'expresiones : expresion'
    t[0] = [t[1]]


def p_expresion_id(t):
    'expresion : ID'
    t[0] = Id(t.lineno(1), str(t[1]))


def p_expresion_entero(t):
    'expresion : ENTERO'
    t[0] = Primitiva(t.lineno(1), tipoPrimitivo.I64, int(t[1]))


def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = Primitiva(t.lineno(1), tipoPrimitivo.F64, float(t[1]))


def p_expresion_true(t):
    'expresion : TRUE'
    t[0] = Primitiva(t.lineno(1), tipoPrimitivo.BOOL, True)


def p_expresion_false(t):
    'expresion : FALSE'
    t[0] = Primitiva(t.lineno(1), tipoPrimitivo.BOOL, False)


def p_expresion_to(t):
    '''expresion : tostring
                | toowned'''
    t[0] = t[1]


def p_expresion_tostring(t):
    'tostring : CADENA PTO TOSTRING PARIZQ PARDER '
    t[0] = Primitiva(t.lineno(1), tipoPrimitivo.TOS, t[1])


def p_expresion_toowned(t):
    'toowned : CADENA PTO TOOWNED PARIZQ PARDER '
    t[0] = Primitiva(t.lineno(1), tipoPrimitivo.TOW, t[1])


def p_expresion_cadena2(t):
    'expresion : STR'
    t[0] = Primitiva(t.lineno(1), tipoPrimitivo.STR, t[1])


def p_expresion_cadena1(t):
    'expresion : CADENA'
    t[0] = Primitiva(t.lineno(1), tipoPrimitivo.STR, str(t[1]))


def p_expresion_caracter(t):
    'expresion : CARACTER'
    t[0] = Primitiva(t.lineno(1), tipoPrimitivo.CHAR, str(t[1]))


def p_expresion_aritmetica1(t):
    '''expresion : expresion MAS expresion
                    | expresion MENOS expresion
                    | expresion POR expresion
                    | expresion DIVIDIDO expresion
                    | expresion MODULO expresion'''

    operador = t[2]
    if operador == '+':
        t[0] = Aritmetica(t.lineno(2), t[1], OPERADOR_ARITMETICO.MAS, t[3], None)
    elif operador == '-':
        t[0] = Aritmetica(t.lineno(2), t[1], OPERADOR_ARITMETICO.MENOS, t[3], None)
    elif operador == '*':
        t[0] = Aritmetica(t.lineno(2), t[1], OPERADOR_ARITMETICO.POR, t[3], None)
    elif operador == '/':
        t[0] = Aritmetica(t.lineno(2), t[1], OPERADOR_ARITMETICO.DIVIDIDO, t[3], None)
    elif operador == '%':
        t[0] = Aritmetica(t.lineno(2), t[1], OPERADOR_ARITMETICO.MODULO, t[3], None)


def p_expresion_aritmetica2(t):
    '''expresion : tipo DOSPT DOSPT POW PARIZQ expresion COMA expresion PARDER
                | tipo DOSPT DOSPT POWF PARIZQ expresion COMA expresion PARDER'''
    reserv = t[4]

    if reserv == 'powf':
        t[0] = Aritmetica(t.lineno(2), t[6], OPERADOR_ARITMETICO.POTENCIAF, t[8], t[1])
    elif reserv == 'pow':
        t[0] = Aritmetica(t.lineno(2), t[6], OPERADOR_ARITMETICO.POTENCIA, t[8], t[1])
    else:
        print("Error de potencia")


def p_exp_unaria(t):
    '''expresion : MENOS expresion %prec UMENOS
                | NOT expresion'''
    operador = str(t[1])
    if operador == '-':
        t[0] = Unaria(t.lineno(1), OPERADOR_UNARIO.MENOS, t[2])
    else:
        t[0] = t[2]


# !--------------------------------------------ERROR-----------------------------------------------
def p_error(t):
    print("Error sintáctico. %s" % t.value[0])


# ? Se ejecuta el parser
parser = yacc.yacc()

entrada = ''' 
//hola
fn main() {
let mut var1 : i64 = -10*50;
let var2 : f64 = 1.0;
let mut var3 = 6%3;
let var4 = 4;
let mut var5 : bool = true;
let mut var6 : String = "mundo".to_owned();
let mut var7 : &str = "hola";
let mut con = var6 + var7;
let mut pot = i64::pow(2,5);
println!("{}",var1);
}
'''
print("Inicia analizador...")
instruc = parser.parse(entrada)
entorno_global = [Entorno(None, None)]

for instru in instruc:
    instru.ejecutar(entorno_global[0])
print("------Consola-------")
for i in listimpresion:
    print(i)
print("Finaliza analizador...")
