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
from Enumeradas.OperadorRelacional import OPERADOR_RELACIONAL
from Enumeradas.OperadorLogico import OPERADOR_LOGICO
from Expresiones.Unaria import Unaria
from Expresiones.Relacional import Relacional
from Expresiones.Logica import Logica
from Instrucciones.If import If
from Instrucciones.ElseIf import ElseIf
from Instrucciones.IfAsignacion import IfAsignacion, ElseIfAsignacion
from Enumeradas.TipoMatch import TIPO_MATCH
from Instrucciones.Match import Match

# ?--------------------------------------------------PRECEDENCIAS-----------------------------------------------------
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'IGUALQUE', 'NOIGUALQUE', 'MENORQUE', 'MENORIQUE', 'MAYORQUE', 'MAYORIQUE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'DIVIDIDO', 'POR', 'MODULO'),
    ('left', 'AS'),
    ('right', 'UMENOS', 'NOT'),

)


# ?--------------------------------------------PRODUCCIONES------------------------------------------------------------
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
                    | if
                    | match
    '''
    t[0] = t[1]


# !---------------------------------------------------IMPRIMIR---------------------------------------------------------

def p_imprimir1(t):
    'imprimir : PRINTLN NOT PARIZQ expresion COMA expresiones PARDER PTCOMA'
    t[0] = Imprimir(t.lineno(2), t[4], t[6])


def p_imprimir2(t):
    'imprimir : PRINTLN NOT PARIZQ expresion PARDER PTCOMA'
    t[0] = Imprimir(t.lineno(2), t[4], None)


# !--------------------------------------------DECLARACION-------------------------------------------------------------

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


# !-----------------------------------------------ASIGNACION----------------------------------------------------------
def p_asignacion1(t):
    'asignacion : ID IGUAL expresion PTCOMA'
    t[0] = AsignacionVariable(t.lineno(1), t[1], t[3])


# !---------------------------------------------------IF------------------------------------------------------------
def p_if(t):
    'if : IF expresion LLAVEIZQ instrucciones LLAVEDER '
    t[0] = If(t.lineno(1), t[2], t[4], [])


def p_else_if(t):
    'if : IF expresion LLAVEIZQ instrucciones LLAVEDER else'
    t[0] = If(t.lineno(2), t[2], t[4], t[6])


def p_else_if_else_if(t):
    'if : IF expresion LLAVEIZQ instrucciones LLAVEDER lelseif'
    t[0] = ElseIf(t.lineno(1), t[2], t[4], t[6], [])


def p_else_if_else(t):
    'if : IF expresion LLAVEIZQ instrucciones LLAVEDER lelseif else'
    t[0] = ElseIf(t.lineno(1), t[2], t[4], t[6], t[7])


def p_else_if1(t):
    'lelseif : lelseif elseif'
    t[1].append(t[2])
    t[0] = t[1]


def p_else_if2(t):
    'lelseif : elseif'
    t[0] = [t[1]]


def p_else_if3(t):
    'elseif : ELSE IF expresion LLAVEIZQ instrucciones LLAVEDER'
    t[0] = [t[3], t[5]]


def p_else(t):
    'else : ELSE LLAVEIZQ instrucciones LLAVEDER'
    t[0] = t[3]


# !-------------------------------------------MATCH---------------------------------------------------
def p_match_inicio(t):
    'match : MATCH expresion LLAVEIZQ imatch LLAVEDER'
    t[0] = Match(t.lineno(1), t[2], t[4])


def p_imatch(t):
    'imatch : opmatch COMA dmatch'
    t[1].append(t[3])
    t[0] = t[1]


def p_opmatch(t):
    '''opmatch : opmatch COMA cmatch
                | opmatch COMA rmatch'''
    t[1].append(t[3])
    t[0] = t[1]


def p_opmatch2(t):
    '''opmatch : cmatch
                | rmatch '''
    t[0] = [t[1]]


def p_cmatch(t):
    'cmatch : bloque_match IGUAL MAYORQUE LLAVEIZQ instrucciones LLAVEDER'
    t[0] = [t[1], t[5], TIPO_MATCH.MATCHBARRAS]


def p_cmatch2(t):
    'cmatch : bloque_match IGUAL MAYORQUE instruccion'
    t[0] = [t[1], [t[4]], TIPO_MATCH.MATCHBARRAS]


def p_bloque_match(t):
    'bloque_match : bloque_match BARRAS expresion'
    t[1].append(t[3])
    t[0] = t[1]


def p_bloque_match2(t):
    'bloque_match : expresion'
    t[0] = [t[1]]


def p_dmatch(t):
    'dmatch : GUIONB IGUAL MAYORQUE  LLAVEIZQ instrucciones LLAVEDER'
    t[0] = [[t[1]], [t[5]], TIPO_MATCH.MATCHDEFAULT]


def p_dmatch2(t):
    'dmatch : GUIONB IGUAL MAYORQUE instruccion'
    t[0] = [[t[1]], [t[4]], TIPO_MATCH.MATCHDEFAULT]


def p_rmatch(t):
    'rmatch : expresion PTO PTO IGUAL expresion IGUAL MAYORQUE rrmatch'
    var = []
    var.append(t[1])
    var.append(t[5])
    t[0] = [var, t[8], TIPO_MATCH.MATCHRANGO]


def p_rrmatch2(t):
    'rrmatch : instruccion'
    t[0] = [t[1]]


def p_rrmatch(t):
    'rrmatch : LLAVEIZQ instrucciones LLAVEDER'
    t[0] = t[2]


# !----------------------------------------------------TIPO-----------------------------------------------------------

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


# !------------------------------------------------EXPRESION---------------------------------------------------------
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


def p_expresion_relacional(t):
    '''expresion : expresion IGUALQUE expresion
            | expresion NOIGUALQUE expresion
            | expresion MENORQUE expresion
            | expresion MAYORQUE expresion
            | expresion MENORIQUE expresion
            | expresion MAYORIQUE expresion '''

    operador = str(t[2])
    if operador == '==':
        t[0] = Relacional(t.lineno(2), t[1], OPERADOR_RELACIONAL.IGUALQUE, t[3])
    elif operador == '>':
        t[0] = Relacional(t.lineno(2), t[1], OPERADOR_RELACIONAL.MAYORQUE, t[3])
    elif operador == '<':
        t[0] = Relacional(t.lineno(2), t[1], OPERADOR_RELACIONAL.MENORQUE, t[3])
    elif operador == '>=':
        t[0] = Relacional(t.lineno(2), t[1], OPERADOR_RELACIONAL.MAYORIQUE, t[3])
    elif operador == '<=':
        t[0] = Relacional(t.lineno(2), t[1], OPERADOR_RELACIONAL.MENORIQUE, t[3])
    elif operador == '!=':
        t[0] = Relacional(t.lineno(2), t[1], OPERADOR_RELACIONAL.NOGUALQUE, t[3])


def p_expresion_logica(t):
    '''expresion : expresion OR expresion
                | expresion AND expresion
                '''
    operador = t[2]
    if operador == '&&':
        t[0] = Logica(t.lineno(2), t[1], OPERADOR_LOGICO.AND, t[3])
    elif operador == '||':
        t[0] = Logica(t.lineno(2), t[1], OPERADOR_LOGICO.OR, t[3])


def p_exp_unaria(t):
    '''expresion : MENOS expresion %prec UMENOS
                | NOT expresion'''
    operador = str(t[1])
    if operador == '-':
        t[0] = Unaria(t.lineno(1), OPERADOR_UNARIO.MENOS, t[2])
    elif operador == '!':

        t[0] = Unaria(t.lineno(1), OPERADOR_UNARIO.NOT, t[2])


def p_exp_agrupa(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]


def p_if_asignacion_inicio(t):
    'expresion : if_asig'
    t[0] = t[1]


def p_if_asig(t):
    'if_asig : IF expresion LLAVEIZQ bloque_expresion LLAVEDER'
    t[0] = IfAsignacion(t.lineno(1), t[2], t[4], [])


def p_if_else_asig(t):
    'if_asig : IF expresion LLAVEIZQ bloque_expresion LLAVEDER else'
    t[0] = IfAsignacion(t.lineno(1), t[2], t[4], t[6])


def p_else_if_else_if_asignacion(t):
    'if_asig : IF expresion LLAVEIZQ bloque_expresion LLAVEDER elseif'
    t[0] = ElseIfAsignacion(t.lineno(1), t[2], t[4], t[6], [])


def p_else_if_else_asignacion(t):
    'if_asig : IF expresion LLAVEIZQ bloque_expresion LLAVEDER elseif else'
    t[0] = ElseIfAsignacion(t.lineno(1), t[2], t[4], t[6], t[7])


def p_elseif1_asig(t):
    'elseif : elseif lif'
    t[1].append(t[2])
    t[0] = t[1]
    print(t[0])


#
#
def p_elseif2_asig(t):
    'elseif : lif'
    t[0] = [t[1]]


def p_lif_asig(t):
    'lif : ELSE IF expresion LLAVEIZQ bloque_expresion LLAVEDER'
    t[0] = [t[3], t[5]]


def p_else_asig(t):
    'else : ELSE LLAVEIZQ bloque_expresion LLAVEDER'
    t[0] = t[3]


def p_bloque_expre_asig(t):
    ' bloque_expresion : bloque_expresion PTCOMA expresion'
    t[1].append(t[3])
    t[0] = t[1]


def p_bloque_expre2_asig(t):
    'bloque_expresion : expresion'
    t[0] = [t[1]]


# !-----------------------------------------------ERROR----------------------------------------------------------------
def p_error(t):
    print("Error sintáctico. %s" % t.value[0])


# !---------------------------------------Se ejecuta el parser---------------------------------------------------------
parser = yacc.yacc()

entrada = ''' 
fn main() {
match 4 {
    1 ..= 3 => {
    println!("Rango {}","1");
    println!("Rango {}","2");
    },
    4 => println!("{}","4 al 5");,
    6|7|8 => {
        let n =1;
        if n ==1 {
            println!("{}","Entramos al brazo con if");
        }
        
    },
    _ => println!("{}","def");
    
}


}
'''
print("Inicia analizador...")
instruc = parser.parse(entrada)
entorno_global = [Entorno(None, None)]

for instru in instruc:
    instru.ejecutar(entorno_global[0])

print("Finaliza analizador...")
