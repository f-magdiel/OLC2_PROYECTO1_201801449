
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftIGUALQUENOIGUALQUEMENORQUEMENORIQUEMAYORQUEMAYORIQUEleftMASMENOSleftDIVIDIDOPORMODULOleftASleftUMENOSNOTAND AS BOOL CADENA CARACTER CHAR COMA DECIMAL DIVIDIDO DOSPT ENTERO EX F64 FALSE FN I64 ID IGUAL IGUALQUE LET LLAVEDER LLAVEIZQ MAIN MAS MAYORIQUE MAYORQUE MENORIQUE MENORQUE MENOS MODULO MUT NOIGUALQUE NOT OR PARDER PARIZQ POR POW POWF PRINTLN PTCOMA PTO SIGNOI STR STRING TOOWNED TOSTRING TRUEinicio : instrucciones maininicio : mainmain : FN MAIN PARIZQ PARDER LLAVEIZQ instrucciones LLAVEDERinstrucciones : instrucciones instruccioninstrucciones : instruccioninstruccion : declaracion\n                    | imprimir\n                    | asignacion\n    imprimir : PRINTLN EX PARIZQ expresion COMA expresiones PARDER PTCOMAimprimir : PRINTLN EX PARIZQ expresion PARDER PTCOMAdeclaracion : LET MUT ID DOSPT tipo IGUAL expresion PTCOMAdeclaracion : LET MUT ID IGUAL expresion PTCOMAdeclaracion : LET ID DOSPT tipo IGUAL expresion PTCOMAdeclaracion : LET ID IGUAL expresion PTCOMAasignacion : ID IGUAL expresion PTCOMAtipo : I64\n            | F64\n            | BOOL\n            | CHAR\n            | STRING\n    tipo : SIGNOI STR expresiones : expresiones COMA expresionexpresiones : expresionexpresion : IDexpresion : ENTEROexpresion : DECIMALexpresion : TRUEexpresion : FALSEexpresion : tostring\n                | toownedtostring : CADENA PTO TOSTRING PARIZQ PARDER toowned : CADENA PTO TOOWNED PARIZQ PARDER expresion : STRexpresion : CADENAexpresion : CARACTERexpresion : expresion MAS expresion\n                    | expresion MENOS expresion\n                    | expresion POR expresion\n                    | expresion DIVIDIDO expresion\n                    | expresion MODULO expresionexpresion : tipo DOSPT DOSPT POW PARIZQ expresion COMA expresion PARDER\n                | tipo DOSPT DOSPT POWF PARIZQ expresion COMA expresion PARDERexpresion : MENOS expresion %prec UMENOS\n                | NOT expresion'
    
_lr_action_items = {'FN':([0,2,4,6,7,8,13,49,65,78,86,89,96,100,],[5,5,-5,-6,-7,-8,-4,-15,-14,-12,-10,-13,-11,-9,]),'LET':([0,2,4,6,7,8,13,49,61,65,76,78,86,89,96,100,],[9,9,-5,-6,-7,-8,-4,-15,9,-14,9,-12,-10,-13,-11,-9,]),'PRINTLN':([0,2,4,6,7,8,13,49,61,65,76,78,86,89,96,100,],[11,11,-5,-6,-7,-8,-4,-15,11,-14,11,-12,-10,-13,-11,-9,]),'ID':([0,2,4,6,7,8,9,13,15,17,22,34,36,43,46,49,50,51,52,53,54,61,64,65,74,76,77,78,86,89,92,93,94,96,100,101,102,],[10,10,-5,-6,-7,-8,16,-4,20,23,23,23,23,23,23,-15,23,23,23,23,23,10,23,-14,23,10,23,-12,-10,-13,23,23,23,-11,-9,23,23,]),'$end':([1,3,12,87,],[0,-2,-1,-3,]),'LLAVEDER':([4,6,7,8,13,49,65,76,78,86,89,96,100,],[-5,-6,-7,-8,-4,-15,-14,87,-12,-10,-13,-11,-9,]),'MAIN':([5,],[14,]),'MUT':([9,],[15,]),'IGUAL':([10,16,20,37,38,39,40,41,47,59,62,],[17,22,46,-16,-17,-18,-19,-20,64,-21,77,]),'EX':([11,],[18,]),'PARIZQ':([14,18,71,72,82,83,],[19,43,80,81,92,93,]),'DOSPT':([16,20,35,37,38,39,40,41,57,59,],[21,45,57,-16,-17,-18,-19,-20,73,-21,]),'ENTERO':([17,22,34,36,43,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'DECIMAL':([17,22,34,36,43,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'TRUE':([17,22,34,36,43,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'FALSE':([17,22,34,36,43,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'STR':([17,22,34,36,42,43,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[31,31,31,31,59,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'CADENA':([17,22,34,36,43,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'CARACTER':([17,22,34,36,43,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'MENOS':([17,22,23,24,25,26,27,28,29,30,31,32,33,34,36,43,46,48,50,51,52,53,54,56,58,60,63,64,66,67,68,69,70,74,77,79,84,88,90,91,92,93,94,97,98,99,101,102,103,104,105,106,],[34,34,-24,51,-25,-26,-27,-28,-29,-30,-33,-34,-35,34,34,34,34,51,34,34,34,34,34,-43,-44,51,51,34,-36,-37,-38,-39,-40,34,34,51,51,51,-31,-32,34,34,34,51,51,51,34,34,51,51,-41,-42,]),'NOT':([17,22,34,36,43,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'I64':([17,21,22,34,36,43,45,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'F64':([17,21,22,34,36,43,45,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'BOOL':([17,21,22,34,36,43,45,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'CHAR':([17,21,22,34,36,43,45,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'STRING':([17,21,22,34,36,43,45,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'SIGNOI':([17,21,22,34,36,43,45,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'PARDER':([19,23,25,26,27,28,29,30,31,32,33,56,58,60,66,67,68,69,70,80,81,84,85,90,91,99,103,104,105,106,],[44,-24,-25,-26,-27,-28,-29,-30,-33,-34,-35,-43,-44,75,-36,-37,-38,-39,-40,90,91,-23,95,-31,-32,-22,105,106,-41,-42,]),'PTCOMA':([23,24,25,26,27,28,29,30,31,32,33,48,56,58,63,66,67,68,69,70,75,79,88,90,91,95,105,106,],[-24,49,-25,-26,-27,-28,-29,-30,-33,-34,-35,65,-43,-44,78,-36,-37,-38,-39,-40,86,89,96,-31,-32,100,-41,-42,]),'MAS':([23,24,25,26,27,28,29,30,31,32,33,48,56,58,60,63,66,67,68,69,70,79,84,88,90,91,97,98,99,103,104,105,106,],[-24,50,-25,-26,-27,-28,-29,-30,-33,-34,-35,50,-43,-44,50,50,-36,-37,-38,-39,-40,50,50,50,-31,-32,50,50,50,50,50,-41,-42,]),'POR':([23,24,25,26,27,28,29,30,31,32,33,48,56,58,60,63,66,67,68,69,70,79,84,88,90,91,97,98,99,103,104,105,106,],[-24,52,-25,-26,-27,-28,-29,-30,-33,-34,-35,52,-43,-44,52,52,52,52,-38,-39,-40,52,52,52,-31,-32,52,52,52,52,52,-41,-42,]),'DIVIDIDO':([23,24,25,26,27,28,29,30,31,32,33,48,56,58,60,63,66,67,68,69,70,79,84,88,90,91,97,98,99,103,104,105,106,],[-24,53,-25,-26,-27,-28,-29,-30,-33,-34,-35,53,-43,-44,53,53,53,53,-38,-39,-40,53,53,53,-31,-32,53,53,53,53,53,-41,-42,]),'MODULO':([23,24,25,26,27,28,29,30,31,32,33,48,56,58,60,63,66,67,68,69,70,79,84,88,90,91,97,98,99,103,104,105,106,],[-24,54,-25,-26,-27,-28,-29,-30,-33,-34,-35,54,-43,-44,54,54,54,54,-38,-39,-40,54,54,54,-31,-32,54,54,54,54,54,-41,-42,]),'COMA':([23,25,26,27,28,29,30,31,32,33,56,58,60,66,67,68,69,70,84,85,90,91,97,98,99,105,106,],[-24,-25,-26,-27,-28,-29,-30,-33,-34,-35,-43,-44,74,-36,-37,-38,-39,-40,-23,94,-31,-32,101,102,-22,-41,-42,]),'PTO':([32,],[55,]),'LLAVEIZQ':([44,],[61,]),'TOSTRING':([55,],[71,]),'TOOWNED':([55,],[72,]),'POW':([73,],[82,]),'POWF':([73,],[83,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'instrucciones':([0,61,],[2,76,]),'main':([0,2,],[3,12,]),'instruccion':([0,2,61,76,],[4,13,4,13,]),'declaracion':([0,2,61,76,],[6,6,6,6,]),'imprimir':([0,2,61,76,],[7,7,7,7,]),'asignacion':([0,2,61,76,],[8,8,8,8,]),'expresion':([17,22,34,36,43,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[24,48,56,58,60,63,66,67,68,69,70,79,84,88,97,98,99,103,104,]),'tostring':([17,22,34,36,43,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'toowned':([17,22,34,36,43,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'tipo':([17,21,22,34,36,43,45,46,50,51,52,53,54,64,74,77,92,93,94,101,102,],[35,47,35,35,35,35,62,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'expresiones':([74,],[85,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> instrucciones main','inicio',2,'p_inicio1','Sintactico.py',29),
  ('inicio -> main','inicio',1,'p_inicio2','Sintactico.py',38),
  ('main -> FN MAIN PARIZQ PARDER LLAVEIZQ instrucciones LLAVEDER','main',7,'p_main','Sintactico.py',44),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones1','Sintactico.py',49),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones2','Sintactico.py',56),
  ('instruccion -> declaracion','instruccion',1,'p_instrucion','Sintactico.py',62),
  ('instruccion -> imprimir','instruccion',1,'p_instrucion','Sintactico.py',63),
  ('instruccion -> asignacion','instruccion',1,'p_instrucion','Sintactico.py',64),
  ('imprimir -> PRINTLN EX PARIZQ expresion COMA expresiones PARDER PTCOMA','imprimir',8,'p_imprimir1','Sintactico.py',72),
  ('imprimir -> PRINTLN EX PARIZQ expresion PARDER PTCOMA','imprimir',6,'p_imprimir2','Sintactico.py',77),
  ('declaracion -> LET MUT ID DOSPT tipo IGUAL expresion PTCOMA','declaracion',8,'p_declaracion1','Sintactico.py',84),
  ('declaracion -> LET MUT ID IGUAL expresion PTCOMA','declaracion',6,'p_declaracion2','Sintactico.py',89),
  ('declaracion -> LET ID DOSPT tipo IGUAL expresion PTCOMA','declaracion',7,'p_declaracion3','Sintactico.py',94),
  ('declaracion -> LET ID IGUAL expresion PTCOMA','declaracion',5,'p_declaracion4','Sintactico.py',99),
  ('asignacion -> ID IGUAL expresion PTCOMA','asignacion',4,'p_asignacion1','Sintactico.py',105),
  ('tipo -> I64','tipo',1,'p_tipo1','Sintactico.py',112),
  ('tipo -> F64','tipo',1,'p_tipo1','Sintactico.py',113),
  ('tipo -> BOOL','tipo',1,'p_tipo1','Sintactico.py',114),
  ('tipo -> CHAR','tipo',1,'p_tipo1','Sintactico.py',115),
  ('tipo -> STRING','tipo',1,'p_tipo1','Sintactico.py',116),
  ('tipo -> SIGNOI STR','tipo',2,'p_tipo2','Sintactico.py',132),
  ('expresiones -> expresiones COMA expresion','expresiones',3,'p_expresiones1','Sintactico.py',138),
  ('expresiones -> expresion','expresiones',1,'p_expresiones2','Sintactico.py',144),
  ('expresion -> ID','expresion',1,'p_expresion_id','Sintactico.py',149),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','Sintactico.py',154),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','Sintactico.py',159),
  ('expresion -> TRUE','expresion',1,'p_expresion_true','Sintactico.py',164),
  ('expresion -> FALSE','expresion',1,'p_expresion_false','Sintactico.py',169),
  ('expresion -> tostring','expresion',1,'p_expresion_to','Sintactico.py',174),
  ('expresion -> toowned','expresion',1,'p_expresion_to','Sintactico.py',175),
  ('tostring -> CADENA PTO TOSTRING PARIZQ PARDER','tostring',5,'p_expresion_tostring','Sintactico.py',180),
  ('toowned -> CADENA PTO TOOWNED PARIZQ PARDER','toowned',5,'p_expresion_toowned','Sintactico.py',185),
  ('expresion -> STR','expresion',1,'p_expresion_cadena2','Sintactico.py',190),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena1','Sintactico.py',195),
  ('expresion -> CARACTER','expresion',1,'p_expresion_caracter','Sintactico.py',200),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_aritmetica1','Sintactico.py',205),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_aritmetica1','Sintactico.py',206),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_aritmetica1','Sintactico.py',207),
  ('expresion -> expresion DIVIDIDO expresion','expresion',3,'p_expresion_aritmetica1','Sintactico.py',208),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion_aritmetica1','Sintactico.py',209),
  ('expresion -> tipo DOSPT DOSPT POW PARIZQ expresion COMA expresion PARDER','expresion',9,'p_expresion_aritmetica2','Sintactico.py',225),
  ('expresion -> tipo DOSPT DOSPT POWF PARIZQ expresion COMA expresion PARDER','expresion',9,'p_expresion_aritmetica2','Sintactico.py',226),
  ('expresion -> MENOS expresion','expresion',2,'p_exp_unaria','Sintactico.py',231),
  ('expresion -> NOT expresion','expresion',2,'p_exp_unaria','Sintactico.py',232),
]
