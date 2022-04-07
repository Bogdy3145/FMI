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
	
   
     
     s    dw 2345h, 0a5h, 368h, 3990h
     s_w  equ ($-s)/2
     t    dw 4h,2651h,10
     t_w  equ ($-t)/2
     
     d    resb (s_w+t_w)
     
    
   
    
segment  code use32 class=code ; segmentul de cod
start: 
    
    mov esi,s
    mov edi,d
    mov ecx, s_w
    cld
    
    
    rep_1:
        lodsw   ; ax<-- <ds:esi>, esi<-esi+2
        stosb
        loop rep_1
    
    mov esi,t_w
    mov ecx, t_w
    
    rep_2:
        lodsw
        mov al,ah
        stosb
        loop rep_2
        
    ;sort string d in ascending order (signed interpretation)
    ;len=length of string
    ;
    ;changed = 1;
    ;while (changed==1){
    ;       changed=0;
    ;       for(int i=1; i<=len-1;i++{
    ;           if(d[i+1]<d[i]){
    ;               aux=d[i];
    ;               d[i]=d[i+1];
    ;               d[i+1]=aux;
    ;               changed=1;
    ;            }
    ;       }
    ;   }
      
    mov dx, 1;changed=1
    
    repeat_while:
        cmp dx,0
        je end_while
        
        mov esi,d
        mov dx,0
        mov ecx, (s_w+t_w)-1
        
        repeat_for:
            mov al,[esi]
            cmp al,[esi+1]
            jle next
                mov ah,[esi+1]
                mov [esi],ah
                mov [esi+1],al
                mov dx,1
            next:
            inc esi
            loop repeat_for
            jmp repeat_while
            
    end_while
    
    
            
    
    
    
	push   dword 0 ;se pune pe stiva codul de retur al functiei exit
	call   [exit] ;apelul functiei sistem exit pentru terminarea executiei programului
    
    
    