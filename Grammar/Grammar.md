inicio -> instrucciones main
        | main

main -> FN MAIN PARIZQ PARDER LLAVEIZQ instrucciones LLAVEDER

instrucciones -> instrucciones instruccion
                | instruccion

instruccion -> declaracion


declaracion -> LET MUT ID DOSPT tipo IGUAL expresion PTCOMA
                | LET MUT ID IGUAL expresion PTCOMA
                | LET ID DOSTP tipo IGUAL expresion PTCOMA
                | LET ID IGUAL expresion PTCOMA

tipo -> I64
        | F64
        | BOOL
        | CHAR
        | STR
        | STRING

expresion -> ID
        | ENTERO
        | DECIMAL
        | TRUE
        | FALSE
        | CADENA
        | CARACTER


                