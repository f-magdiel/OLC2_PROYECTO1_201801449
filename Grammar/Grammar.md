inicio -> instrucciones main
        | main

main -> FN MAIN PARIZQ PARDER LLAVEIZQ instrucciones LLAVEDER

instrucciones -> instrucciones instruccion
                | instruccion

instruccion -> declaracion
                | imprimir
                | asignacion


declaracion -> LET MUT ID DOSPT tipo IGUAL expresion PTCOMA
                | LET MUT ID IGUAL expresion PTCOMA
                | LET ID DOSTP tipo IGUAL expresion PTCOMA
                | LET ID IGUAL expresion PTCOMA

asignacion -> ID IGUAL expresion PTCOMA

imprimir -> PRINTLN EX PARIZQ expresion PARDER PTCOMA
        | PRINTLN EX PARIZQ expresion COMA expresiones PARDER PTCOMA

expresiones -> expresiones COMA expresion
        | expresion

expresion -> ID
        | ENTERO
        | DECIMAL
        | TRUE
        | FALSE
        | CADENA
        | CARACTER
        | STR
        | NULO
        | string
        | expresion MAS expresion
        | expresion MENOS expresion
        | expresion POR expresion
        | expresion DIVIDIDO expresion
        | expresion MODULO expresion
        | MENOS expresion %prec UMENOS 
        | NOT expresion
        | expresion IGUALQUE expresion
        | expresion NIGUALQUE expresion
        | expresion MENORQUE expresion
        | expresion MAYORQUE expresion
        | expresion MENORIQUE expresion
        | expresion MAYORIQUE expresion
        | tipo DOSPT DOSPT POW PARIZQ expresion COMA expresion PARDER
        | tipo DOSPT DOSPT POWF PARIZQ expresion COMA expresion PARDER
        | expresion IGUALQUE expresion
        | expresion NOGUALQUE expresion
        | expresion MENORQUE expresion
        | expresion MAYORQUE expresion
        | expresion MENORIQUE expresion
        | expresion MAYORIQUE expresion
        | expresion OR expresion
        | expresion AND expresion
        | PARIZQ expresion PARDER        


string -> tostring
        | toowned

tostring -> CADENA PT TOSTRING PARIZ PARDER PTCOMA

toowned -> CADENA PT TOOWNED PARIZ PARDER PTCOMA

tipo -> I64
        | F64
        | BOOL
        | CHAR
        | SIGNO STR
        | STRING


                