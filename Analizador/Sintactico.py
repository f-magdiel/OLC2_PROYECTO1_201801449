import ply.yacc as yacc
from Analizador.Lexico import tokens
from Instrucciones.Arreglo import Arreglo
from Instrucciones.Declaracion import DeclaracionVariable
from Instrucciones.Imprimir import Imprimir
from Entorno.Entorno import Entorno
from Expresiones.Id import Id
from Expresiones.Primitiva import Primitiva
from Enumeradas.Primitivo import tipoPrimitivo
from Instrucciones.Asignacion import AsignacionVariable, AsignacionArreglo
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
from Instrucciones.MatchAsignacion import MatchAsignacion
from Instrucciones.Loop import Loop
from Instrucciones.While import While
from Instrucciones.Break import Break
from Instrucciones.BreakExpresion import BreakExpresion
from Instrucciones.Continue import Continue
from Instrucciones.MainInstru import MainInstru
from Funciones.Funciones import Funciones, Parametros
from Instrucciones.LLamadaFunciones import LlamadaFunciones
from Instrucciones.Return import Return
from Instrucciones.DeclaracionArreglos import DeclaracionArreglos
from Instrucciones.Arregloacceso import Arregloacceso
from Instrucciones.ForIn import ForIn
from Instrucciones.Vector import Vector
from Instrucciones.CreacionVector import CreacionVector
from Instrucciones.DeclaracionVector import DeclaracionVector
from Instrucciones.NativasVectores import NativasVectores
from Enumeradas.NativeVectores import NATIVE_VECTORES
from Expresiones.Casteos import Casteos
from Expresiones.FuncionesNativas import FuncionesNativas
from Enumeradas.Nativas import NATIVAS
from Reportes.TipoError import TIPIN_ERROR
from Reportes.Contenido import Tabla_Errorres, Errores

# ?--------------------------------------------------PRECEDENCIAS-----------------------------------------------------
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'IGUALQUE', 'NOIGUALQUE', 'MENORQUE', 'MENORIQUE', 'MAYORQUE', 'MAYORIQUE'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'DIVIDIDO', 'POR', 'MODULO'),
    ('left', 'AS'),
    ('right', 'UMENOS', 'NOT'),
    ('nonassoc', 'PTO'),

)


# ?--------------------------------------------PRODUCCIONES------------------------------------------------------------
def p_inicio_inicio(t):
    'inicio : instrucciones main instrucciones'
    ins = t[3]
    for ele in ins:
        t[1].append(ele)
    t[1].append(t[2])
    t[0] = t[1]


def p_inicio1(t):
    'inicio : instrucciones main'
    t.lexer.lineno = 1
    t.lineno = 1
    t[1].append(t[2])  # ?----> como una lista
    t[0] = t[1]


def p_inicio3(t):
    'inicio : main instrucciones'
    t[2].append(t[1])
    t[0] = t[2]


def p_inicio2(t):
    'inicio : main'
    t.lexer.lineno = 1
    t.lineno = 1
    t[0] = [t[1]]  # ? ----> como una lista


def p_main(t):
    'main : FN MAIN PARIZQ PARDER LLAVEIZQ instrucciones LLAVEDER'
    t[0] = MainInstru(t.lineno(1), t[6])


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
                    | loop
                    | while
                    | break
                    | return
                    | continue
                    | funciones
                    | llamada_funciones PTCOMA
                    | declaracion_arreglos
                    | declaracion_vector
                    | forin
                    | nativas_vector

    '''
    t[0] = t[1]


# !-------------------------------------VECTORES-----------------------------------------------------------------
def p_declaracion_vec1(t):
    'declaracion_vector : LET MUT ID DOSPT VVEC MENORQUE tipo MAYORQUE IGUAL expresion PTCOMA'
    t[0] = DeclaracionVector(t.lineno(1), t[3], t[10], t[7], True)


def p_declaracion_vec2(t):
    'declaracion_vector : LET ID DOSPT VVEC MENORQUE tipo MAYORQUE IGUAL expresion PTCOMA'
    t[0] = DeclaracionVector(t.lineno(1), t[2], t[9], t[6], False)


def p_vector_inicio(t):
    'expresion : VEC NOT CORIZQ expresiones CORDER'
    vec = Arreglo(t.lineno(1), t[4])
    t[0] = Vector(t.lineno(1), vec)


def p_vector1(t):
    'expresion : VVEC DOSPT DOSPT NEW PARIZQ PARDER'
    t[0] = CreacionVector(t.lineno(1))


def p_vecto2(t):
    'expresion : VVEC DOSPT DOSPT WITH_CAPACITY PARIZQ expresion PARDER'
    t[0] = CreacionVector(t.lineno(1), t[6])


# !-------------------------------------NATIVAS VECTORES-------------------------------------------
# * --------------------------------LEN-------------------------------------
def p_nativa_vec(t):
    'expresion : nativas_vec'
    t[0] = t[1]


def p_nativa_len(t):
    'nativas_vec : expresion PTO LEN PARIZQ PARDER'
    # nat = Id(t.lineno(1), t[1])
    t[0] = NativasVectores(t.lineno(1), t[1], NATIVE_VECTORES.LEN)


# * -------------------------------CAPACITY-------------------------------
def p_nativa_capacity(t):
    'expresion : expresion PTO CAPACITY PARIZQ PARDER '
    # nat = Id(t.lineno(1), t[1])
    t[0] = NativasVectores(t.lineno(1), t[1], NATIVE_VECTORES.CAPACITY)


# * ---------------------------------PUSH------------------------------------
def p_nativa_push(t):
    'nativas_vector : expresion PTO PUSH PARIZQ expresion PARDER PTCOMA'
    # nat = Id(t.lineno(1), t[1])
    t[0] = NativasVectores(t.lineno(1), t[1], NATIVE_VECTORES.PUSH, t[5])


# * -------------------------------INSERT--------------------------------------
def p_nativa_insert(t):
    'nativas_vector : expresion PTO INSERT PARIZQ expresion COMA expresion PARDER PTCOMA'
    # nat = Id(t.lineno(1), t[1])
    t[0] = NativasVectores(t.lineno(1), t[1], NATIVE_VECTORES.INSERT, t[5], t[7])


# * --------------------------REMOVE-------------------------------------------
def p_nativa_remove(t):
    'nativas_vector : expresion PTO REMOVE PARIZQ expresion PARDER PTCOMA'
    # nat = Id(t.lineno(1), t[1])
    t[0] = NativasVectores(t.lineno(1), t[1], NATIVE_VECTORES.REMOVE, t[5])


def p_nativa_remove_expre(t):
    'expresion : expresion PTO REMOVE PARIZQ expresion PARDER'
    # nat = Id(t.lineno(1), t[1])
    t[0] = NativasVectores(t.lineno(1), t[1], NATIVE_VECTORES.REMOVE_EXPRE, t[5])


# * ---------------------------------CONTAINS----------------------------------
def p_nativa_contain(t):
    'expresion : expresion PTO CONTAINS PARIZQ SIGNOI expresion PARDER'
    # nat = Id(t.lineno(1), t[1])
    t[0] = NativasVectores(t.lineno(1), t[1], NATIVE_VECTORES.CONTAINS, t[6])


# !----------------------------------------ARREGLOS---------------------------------------------------------------
def p_arreglo_inicio(t):
    'declaracion_arreglos : LET MUT ID DOSPT tipo_arreglo IGUAL expresion PTCOMA'
    t[0] = DeclaracionArreglos(t.lineno(1), t[3], t[5], t[7], True)


def p_arreglo_inicio2(t):
    'declaracion_arreglos : LET ID DOSPT tipo_arreglo IGUAL expresion PTCOMA'
    t[0] = DeclaracionArreglos(t.lineno(1), t[2], t[4], t[6], False)


def p_arreglo_tipo(t):
    'tipo_arreglo : CORIZQ tipo_arreglo PTCOMA expresion CORDER'
    t[2].append(t[4])
    t[0] = t[2]


def p_arreglo_tipo2(t):
    'tipo_arreglo : CORIZQ tipo PTCOMA expresion CORDER'
    t[0] = [t[2], t[4]]


# !----------------------------------------------FUNCIONES---------------------------------------------------------

def p_funciones_2(t):
    'funciones : FN ID PARIZQ lparametros PARDER MENOS MAYORQUE tipo LLAVEIZQ instrucciones LLAVEDER'
    t[0] = Funciones(t.lineno(2), t[8], t[2], t[4], t[10])


def p_funciones_3(t):
    'funciones : FN ID PARIZQ PARDER MENOS MAYORQUE tipo LLAVEIZQ instrucciones LLAVEDER'
    t[0] = Funciones(t.lineno(1), t[7], t[2], [], t[9])


def p_funciones_1(t):
    'funciones : FN ID PARIZQ lparametros PARDER LLAVEIZQ instrucciones LLAVEDER '
    t[0] = Funciones(t.lineno(1), tipoPrimitivo.NULO, t[2], t[4], t[7])


def p_funciones_4(t):
    'funciones : FN ID PARIZQ PARDER LLAVEIZQ instrucciones LLAVEDER'
    t[0] = Funciones(t.lineno(1), tipoPrimitivo.NULO, t[2], [], t[6])


def p_parametros(t):
    'lparametros : lparametros COMA lparame'
    t[1].append(t[3])
    t[0] = t[1]


def p_parametro_1(t):
    'lparametros : lparame'
    t[0] = [t[1]]


def p_parametro_2(t):
    'lparame : ID DOSPT tipo'
    t[0] = Parametros(t[3], t[1], False, None)


def p_parametro_3(t):
    'lparame : ID DOSPT SIGNOI MUT tipo_arreglo'
    t[0] = Parametros(tipoPrimitivo.ARREGLO, t[1], True, t[5])


def p_parametro_4(t):
    'lparame : ID DOSPT SIGNOI MUT VVEC MENORQUE tipo MAYORQUE'
    t[0] = Parametros(tipoPrimitivo.VECTOR, t[1], False, [t[7]])


def p_llamada_funcion_inicio(t):
    'llamada_funciones : ID PARIZQ largumentos PARDER'
    t[0] = LlamadaFunciones(t.lineno(1), t[1], t[3])


def p_llamada_funcion_1(t):
    'llamada_funciones : ID PARIZQ PARDER'
    t[0] = LlamadaFunciones(t.lineno(1), t[1], [])


def p_argumentos_0(t):
    'largumentos : largumentos COMA largumento'  # se quito expresion por largunto
    t[1].append(t[3])
    t[0] = t[1]


def p_argumentos_2(t):
    'largumentos : largumento'
    t[0] = [t[1]]


def p_argumentos_3(t):
    'largumento : expresion'
    li = [t[1], False]
    t[0] = li


def p_argumentos_4(t):
    'largumento : SIGNOI MUT expresion'
    li = [t[3], True]
    t[0] = li


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


def p_asignacionarreglo(t):
    'asignacion : ID lindices IGUAL expresion PTCOMA'
    t[0] = AsignacionArreglo(t.lineno(1), t[1], t[2], t[4])


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


# * --------------------------------------------------LOOP--------------------------------------------------
# ! -----------------------LOOP----------------------------
def p_loop_inicio(t):
    'loop : LOOP LLAVEIZQ instrucciones LLAVEDER'
    t[0] = Loop(t.lineno(1), t[3])


# ! -------------------WHILE-------------------------------
def p_while_inicio(t):
    'while : WHILE expresion LLAVEIZQ instrucciones LLAVEDER'
    t[0] = While(t.lineno(1), t[2], t[4])


# ! ------------------------------FORIN--------------------------------
def p_forin_inicio(t):
    'forin : FOR ID IN expresion LLAVEIZQ instrucciones LLAVEDER'
    t[0] = ForIn(t.lineno(1), t[2], t[4], t[6])


def p_forin_2(t):
    'forin : FOR ID IN expresion PTO PTO expresion LLAVEIZQ instrucciones LLAVEDER'
    t[0] = ForIn(t.lineno(1), t[2], t[4], t[9], t[7])


# * ---------------------------------------BREAK------------------------------------
def p_break_inicio(t):
    'break : BREAK PTCOMA'
    t[0] = Break(t.lineno(1))


def p_break_expresion(t):
    'break : BREAK expresion PTCOMA'
    t[0] = BreakExpresion(t.lineno(1), t[2])


# * --------------------------------------CONTINUE-------------------------------------
def p_continue_inicio(t):
    'continue : CONTINUE PTCOMA'
    t[0] = Continue(t.lineno(2))


# * -------------------------------------------RETURN-----------------------------------

def p_instruccion_return(t):
    'return : RETURN expresion PTCOMA'
    t[0] = Return(t.lineno(1), t[2])


# !----------------------------------------------------TIPO-----------------------------------------------------------

def p_tipo1(t):
    '''tipo : I64
            | F64
            | BOOL
            | CHAR
            | STRING
            | USIZE
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
        t[0] = tipoPrimitivo.TOS
    elif (tipo == 'usize'):
        t[0] = tipoPrimitivo.I64


def p_tipo2(t):
    'tipo : SIGNOI STR'
    t[0] = tipoPrimitivo.STR


# !------------------------------------------------EXPRESIONES---------------------------------------------------------
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
    'tostring : expresion PTO TOSTRING PARIZQ PARDER '
    t[0] = FuncionesNativas(t.lineno(2), NATIVAS.TOSTRING, t[1])


def p_expresion_toowned(t):
    'toowned : expresion PTO TOOWNED PARIZQ PARDER '
    t[0] = FuncionesNativas(t.lineno(2), NATIVAS.TOOWNED, t[1])


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


def p_exp_unaria(t):
    '''expresion : MENOS expresion %prec UMENOS
                | NOT expresion'''

    operador = str(t[1])

    if operador == '-':
        t[0] = Unaria(t.lineno(1), OPERADOR_UNARIO.MENOS, t[2])
    elif operador == '!':
        t[0] = Unaria(t.lineno(1), OPERADOR_UNARIO.NOT, t[2])


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


def p_exp_agrupa(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]


def p_llamada_funcion_asig(t):
    'expresion : llamada_funciones'
    t[0] = t[1]


def p_expresion_arreglo(t):
    'expresion : CORIZQ expresiones CORDER '
    t[0] = Arreglo(t.lineno(1), t[2])


def p_expresion_Accesarreglo(t):
    'expresion : ID lindices'
    t[0] = Arregloacceso(t.lineno(1), t[1], t[2])


def p_indices1(t):
    'lindices : lindices CORIZQ expresion CORDER'
    t[1].append(t[3])
    t[0] = t[1]


def p_indices2(t):
    'lindices : CORIZQ expresion CORDER'
    t[0] = [t[2]]


# *----------------------------------------------- IF ASIGNACION--------------------------------------------------


def p_if_asignacion_inicio(t):
    'expresion : if_asig'
    t[0] = t[1]


def p_if_asig(t):
    'if_asig : IF expresion LLAVEIZQ bloque_expresion LLAVEDER'
    t[0] = IfAsignacion(t.lineno(1), t[2], t[4], [])


def p_if_else_asig(t):
    'if_asig : IF expresion LLAVEIZQ bloque_expresion LLAVEDER elsea'
    t[0] = IfAsignacion(t.lineno(1), t[2], t[4], t[6])


def p_else_if_else_if_asignacion(t):
    'if_asig : IF expresion LLAVEIZQ bloque_expresion LLAVEDER elseifa'
    t[0] = ElseIfAsignacion(t.lineno(1), t[2], t[4], t[6], [])


def p_else_if_else_asignacion(t):
    'if_asig : IF expresion LLAVEIZQ bloque_expresion LLAVEDER elseifa elsea'
    t[0] = ElseIfAsignacion(t.lineno(1), t[2], t[4], t[6], t[7])


def p_elseif1_asig(t):
    'elseifa : elseifa lif'
    t[1].append(t[2])
    t[0] = t[1]
    print(t[0])


def p_elseif2_asig(t):
    'elseifa : lif'
    t[0] = [t[1]]


def p_lif_asig(t):
    'lif : ELSE IF expresion LLAVEIZQ bloque_expresion LLAVEDER'
    t[0] = [t[3], t[5]]


def p_else_asig(t):
    'elsea : ELSE LLAVEIZQ bloque_expresion LLAVEDER'
    t[0] = t[3]


def p_bloque_expre_asig(t):
    ' bloque_expresion : bloque_expresion PTCOMA expresion'
    t[1].append(t[3])
    t[0] = t[1]


def p_bloque_expre2_asig(t):
    'bloque_expresion : expresion'
    t[0] = [t[1]]


# *-----------------------------------MATCH ASIGNACION-------------------------------------------
#
def p_match_inicio_asig(t):
    'expresion : match_asig'
    t[0] = t[1]


def p_match_asig(t):
    'match_asig : MATCH expresion LLAVEIZQ imatch_asig LLAVEDER '
    t[0] = MatchAsignacion(t.lineno(1), t[2], t[4])


def p_imatch_asig(t):
    'imatch_asig : opmatch_asig COMA dmatch_asig '
    t[1].append(t[3])
    t[0] = t[1]


def p_dmatch_asig(t):
    'dmatch_asig : GUIONB IGUAL MAYORQUE LLAVEIZQ bloque_expresion LLAVEDER'
    t[0] = [[t[1]], t[5], TIPO_MATCH.MATCHDEFAULT]


def p_dmatch_asig2(t):
    'dmatch_asig : GUIONB IGUAL MAYORQUE expresion'
    t[0] = [[t[1]], [t[4]], TIPO_MATCH.MATCHDEFAULT]


def p_opmatch_asig1(t):
    'opmatch_asig : opmatch_asig COMA cmatch_asig'
    t[1].append(t[3])
    t[0] = t[1]


def p_opmatch_asig2(t):
    'opmatch_asig : cmatch_asig'
    t[0] = [t[1]]


def p_cmatch_asig(t):
    'cmatch_asig : bloque_match_asig IGUAL MAYORQUE LLAVEIZQ bloque_expresion LLAVEDER'
    t[0] = [t[1], t[5], TIPO_MATCH.MATCHBARRAS]


def p_cmatch_asig2(t):
    'cmatch_asig : bloque_match_asig IGUAL MAYORQUE expresion'
    t[0] = [t[1], [t[4]], TIPO_MATCH.MATCHBARRAS]


def p_bloque_match_asig(t):
    'bloque_match_asig : bloque_match_asig BARRAS expresion'
    t[1].append(t[3])
    t[0] = t[1]


def p_bloque_match_asign2(t):
    'bloque_match_asig : expresion'
    t[0] = [t[1]]


# !---------------------------------------------LOOP EXPRESION-----------------------------------------------
def p_loop_expresion_inicio(t):
    'expresion : loop_asig'
    t[0] = t[1]


def p_lopp_expresion(t):
    'loop_asig : LOOP LLAVEIZQ instrucciones LLAVEDER'
    t[0] = Loop(t.lineno(2), t[3])


# !------------------------------------CASTEO---------------------------------------------------------------------
def p_casteo(t):
    'expresion : PARIZQ expresion AS tipo PARDER'
    t[0] = Casteos(t.lineno(1), t[2], t[4])


# !----------------------------------------FUNCIONES NATIVAS--------------------------------------------------
def p_funciones_nat_inicio(t):
    'expresion : nativas_fun '
    t[0] = t[1]


def p_funciones_nat1(t):
    '''nativas_fun : expresion PTO ABS PARIZQ PARDER
                    | expresion PTO SQRT PARIZQ PARDER'''
    fun = t[3]

    if fun == 'abs':
        t[0] = FuncionesNativas(t.lineno(1), NATIVAS.ABS, t[1])
    elif fun == 'sqrt':
        t[0] = FuncionesNativas(t.lineno(1), NATIVAS.SQRT, t[1])


def p_funciones_nat2(t):
    'nativas_fun : expresion PTO CLONE PARIZQ PARDER'
    t[0] = FuncionesNativas(t.lineno(2), NATIVAS.CLONE, t[1])


# !-----------------------------------------------ERROR----------------------------------------------------------------
def p_error(t):
    if t:
        alert = "El token '{}' es inválido en está posición".format(t.value)
        error_syntaxis = Errores(t.lexer.lineno, alert, TIPIN_ERROR.SINTACITO)
        Tabla_Errorres.append(error_syntaxis)
        while True:
            car = parser.token()
            if not car or car.type in ['LLAVEDER', 'PTCOMA']:
                break
        print(alert)
        parser.restart()
    else:
        alert = "Se detecto un error al final"
        error_syntaxis = Errores(0, alert, TIPIN_ERROR.SINTACITO)
        Tabla_Errorres.append(error_syntaxis)
        print(alert)


def report(self):
    return self.errors


# !---------------------------------------Se ejecuta el parser---------------------------------------------------------
parser = yacc.yacc()

# entrada = r'''
#
#
# fn main(){
#
#     println!(" valor casteo: {}", );
#
# }
# '''
# print("Inicia analizador...")
# instruc = parser.parse(entrada)
# entorno_global = [Entorno(None, None, None, None)]
# if instruc:
#     for instru in instruc:
#         # print("Instrucciones fuera del main {}".format(instru))
#         if isinstance(instru, MainInstru):
#             instru.ejecutar(entorno_global[0])
#         elif isinstance(instru, Funciones):
#             instru.ejecutar(entorno_global[0])
# else:
#     print("Error al ejecutar instrucciones del analizador")
#
# print("Finaliza analizador...")
