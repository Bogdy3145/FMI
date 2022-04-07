; Scrieți un program în limbaj de asamblare care să rezolve expresia aritmetică, considerând domeniile de definiție ale variabilelor
; a - byte, b - word
; (b / a * 2 + 10) * b - b * 15;
; ex. 1: a = 10; b = 40; Rezultat: (40 / 10 * 2 + 10) * 40 - 40 * 15 = 18 * 40 - 1600 = 720 - 600 = 120
; ex. 2: a = 100; b = 50; Rezultat: (50 / 100 * 2 + 10) * 50 - 50 * 15 = 12 * 50 - 750 = 600 - 750 = - 150
bits 32 ;asamblare si compilare pentru arhitectura de 32 biti
; definim punctul de intrare in programul principal
global  start 

extern  exit,printf,scanf,fopen,fclose,fprintf ;
import  exit msvcrt.dll; 

import fopen msvcrt.dll
import fclose msvcrt.dll
import fprintf msvcrt.dll

import printf msvcrt.dll
import scanf msvcrt.dll

        
segment  data use32 class=data ; segmentul de date in care se vor defini variabilele 
    
    m dd 0
    n dd 0
    
    text times 100 dd 0
    format_nr dd "%d",0
    format_string dd "%s",0
    counter dd 0
    second_counter dd 0
    cuvinte_pare dd 0
    vocale_counter dd 0
    
    
    
    
        
segment  code use32 class=code ; segmentul de cod
start: 
    
    push dword m
    push dword format_nr
    call [scanf]
    add esp,4*2
    
    push dword n
    push dword format_nr
    call [scanf]
    add esp,4*2
    
    push dword [m]
    push dword format_nr
    call [printf]
    add esp,4*2
    
    
    
    
    mov ecx,[m]
    
    a_loop
        
        mov [counter],ecx
        
        push dword text
        push dword format_string
        call [scanf]
        add esp,4*2
        
        mov edx,0
        mov eax,0
        mov ebx,0
        mov [vocale_counter],eax
        
        
        iterating_word:
        
        mov eax,0
        cmp [text+edx],eax
        je final_cuvant
        
        
        
        mov al,"a"
        mov ah,[text+edx]
        cmp ah,al
        je vocala
        
        mov al,"e"
        mov ah,[text+edx]
        cmp ah,al
        je vocala
        
        mov al,"o"
        mov ah,[text+edx]
        cmp ah,al
        je vocala
        
        mov al,"i"
        mov ah,[text+edx]
        cmp ah,al
        je vocala
        
        mov al,"u"
        mov ah,[text+edx]
        cmp ah,al
        je vocala
        
        jmp not_vocala
        
        vocala:
        inc ebx
        
        not_vocala:
        
        inc edx
        
        jmp iterating_word
        
        final_cuvant:
        
        cmp ebx,[n]
        jl nvm
        
        inc byte [cuvinte_pare]
         
       
        nvm:
        
        
        mov ecx,[counter]
        loop a_loop
   
   push dword [cuvinte_pare]
   push dword format_nr
   call [printf]
   add esp,4*2
   
  
    
    
	push   dword 0 ;se pune pe stiva codul de retur al functiei exit
	call   [exit] ;apelul functiei sistem exit pentru terminarea executiei programului
    
    
    