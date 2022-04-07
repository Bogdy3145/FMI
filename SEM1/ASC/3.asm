; Scrieți un program în limbaj de asamblare care să rezolve expresia aritmetică, considerând domeniile de definiție ale variabilelor
; a - byte, b - word
; (b / a * 2 + 10) * b - b * 15;
; ex. 1: a = 10; b = 40; Rezultat: (40 / 10 * 2 + 10) * 40 - 40 * 15 = 18 * 40 - 1600 = 720 - 600 = 120
; ex. 2: a = 100; b = 50; Rezultat: (50 / 100 * 2 + 10) * 50 - 50 * 15 = 12 * 50 - 750 = 600 - 750 = - 150
bits 32 ;asamblare si compilare pentru arhitectura de 32 biti
; definim punctul de intrare in programul principal
global  start 

extern  exit ; indicam asamblorului ca exit exista, chiar daca noi nu o vom defini
import  exit msvcrt.dll; exit este o functie care incheie procesul, este definita in msvcrt.dll
        ; msvcrt.dll contine exit, printf si toate celelalte functii C-runtime importante
segment  data use32 class=data ; 

    a db 10
    b db 8
    c db 5
    d db 2

segment  code use32 class=code ; 
start: 
	
    mov ax,0
    mov dx,0
    
    mov al, [a]
    mov dl, [b]
   
    sub eax,edx
    
    mov dx,0
    mov dl,[d]
    
    sub eax,edx
    
    add eax,2
    
    add eax,[c] 
    
    mov ebx,0
    add bl,10
    sub ebx,[b] 
    
    add eax,ebx
	
	push   dword 0 
	call   [exit]



    