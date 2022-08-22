inicio -> instrucciones main
        | main

main -> FN MAIN PARIZQ PARDER LLAVEIZQ instrucciones LLAVEDER

instrucciones -> instrucciones instruccion
                | instruccion

instruccion -> imprimir 
                | declaracion
                | asignacion
                | if       
                | match
                | break PTCOMA
                | continue PTCOMA
                | loop 
                | while
                | return PTCOMA
                | funcion
                | llamada_funcion PTCOMA
                
imprimir -> PRINTLN EX PARIZQ expresion PARDER PTCOMA
        | PRINTLN EX PARIZQ expresion COMA expresiones PARDER PTCOMA

declaracion -> LET MUT ID DOSPT tipo IGUAL expresion PTCOMA
                | LET MUT ID IGUAL expresion PTCOMA
                | LET ID DOSTP tipo IGUAL expresion PTCOMA
                | LET ID IGUAL expresion PTCOMA

asignacion -> ID IGUAL expresion PTCOMA

if -> IF expresion LLAVEIZQ instrucciones LLAVEDER      
      | IF expresion LLAVEIZQ instrucciones LLAVEDER else
      | IF expresion LLAVEIZQ instrucciones LLAVEDER lelseif 
      | IF expresion LLAVEIZQ instrucciones LLAVEDER lelseif else 

lelseif -> lelseif elseif 
        | elseif

elseif -> ELSE IF expresion LLAVERIZQ instrucciones LLAVEDER

else -> ELSE LLAVEIZQ instrucciones LLAVEDER
        


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
        | if_asig  

#!--------------------------------------IF CON ASIGNACION------------------------------------
if_asig -> IF expresion LLAVEIZQ bloque_expresion LLAVEDER
        | IF expresion LLAVEIZQ bloque_expresion LLAVEDER else
        | IF expresion LLAVEIZQ bloque_expresion LLAVEDER elseif
        | IF expresion LLAVEIZQ bloque_expresion LLAVEDER elseif else

elseif -> elseif lif
        | lif

lif -> ELSE IF expresion LLAVEIZQ bloque_expresion LLAVEDER


else -> ELSE LLAVEIZQ bloque_expresion LLAVEDER

bloque_expresion -> bloque_expresion PTCOMA expresion
             | expresion



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


                