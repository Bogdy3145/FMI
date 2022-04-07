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
	
   
     
     s dw 0abcdh, 12, 800h, 8000h, 10
     s_w equ($-s)/2
     ;d times s_w db -1
     d resb s_w
     
    ;Given an array S of doublewords, build the array of bytes D formed from bytes of doublewords sorted as unsigned numbers in descending order.
    ;Example:
    ;s DD 12345607h, 1A2B3C15h
    ;d DB 56h, 3Ch, 34h, 2Bh, 1Ah, 15h, 12h, 07h
   
    
segment  code use32 class=code ; segmentul de cod
start: 
    
    mov esi, s+1
    mov edi, d
    
    mov ecx, s_w
    
    cld
    rep_1:
        lodsb; al <--  <ds:esi>, if df=0 => esi<-- esi+1
        inc esi
        cmp al,0
        jge next_el
            stosb; <es:edi> <-- al, if df==0 => edi<-- edi+1
        next_el:
        loop rep_1
        
        
       
    
    
    
            
    
    
    
	push   dword 0 ;se pune pe stiva codul de retur al functiei exit
	call   [exit] ;apelul functiei sistem exit pentru terminarea executiei programului
    
    
    