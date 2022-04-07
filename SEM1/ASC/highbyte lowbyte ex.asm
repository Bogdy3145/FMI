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
segment  data use32 class=data ; segmentul de date in care se vor defini variabilele 
	
   
     
     a db '213342655'
     l_a equ $-a
     b db '457621'
     l_b equ $-b
     l_r equ l_a+l_b
     r times l_r db 0
     
    ;Two byte strings A and B are given. Obtain the string R by concatenating the elements of B in reverse order and the odd elements of A.
    ;Example:
    ;A: 2, 1, 3, 3, 4, 2, 6
    ;B: 4, 5, 7, 6, 2, 1
    ;R: 1, 2, 6, 7, 5, 4, 1, 3, 3
    
segment  code use32 class=code ; segmentul de cod
start: 
    
    mov esi,0
    mov ecx,l_b ;nr de repetari din loop si indexul lui b descrescator
    start_loop:
        mov al,[b+ecx-1]
        mov [r+esi],al
        inc esi ;indexul lui R
        
    loop start_loop
    
    mov edx,0   ;indexul lui a
    repeat:
        mov al,[a+edx]
        shr al,1        ;verificam paritatea
        jnc even
            mov bl,[a+edx]
            mov [r+esi],bl
            inc esi ;indexul lui R
        even:
        inc edx
        cmp edx,l_a
        jb repeat
            
    
    
    
	push   dword 0 ;se pune pe stiva codul de retur al functiei exit
	call   [exit] ;apelul functiei sistem exit pentru terminarea executiei programului
    
    
    