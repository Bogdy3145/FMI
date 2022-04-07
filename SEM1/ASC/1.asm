bits 32 ;asamblare si compilare pentru arhitectura de 32 biti
; definim punctul de intrare in programul principal
global  start 

extern  exit ; indicam asamblorului ca exit exista, chiar daca noi nu o vom defini
import  exit msvcrt.dll; exit este o functie care incheie procesul, este definita in msvcrt.dll
        ; msvcrt.dll contine exit, printf si toate celelalte functii C-runtime importante
segment  data use32 class=data ; 
segment  code use32 class=code ; 
start: 
	
    mov al,0
    add al,6h
    mov dh,0
    add dh,3h
    
    mul dh
    
	
push   dword 0 
call   [exit]
