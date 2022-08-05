inicio -> instrucciones main
        | main

main -> FN MAIN PARIZQ PARDER LLAVEIZQ instrucciones LLAVEDER

instrucciones -> instrucciones instruccion
                | instruccion

instruccion -> declaracion
                | imprimir


declaracion -> LET MUT ID DOSPT tipo IGUAL expresion PTCOMA
                | LET MUT ID IGUAL expresion PTCOMA
                | LET ID DOSTP tipo IGUAL expresion PTCOMA
                | LET ID IGUAL expresion PTCOMA

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

tipo -> I64
        | F64
        | BOOL
        | CHAR
        | SIGNO STR
        | STRING


                