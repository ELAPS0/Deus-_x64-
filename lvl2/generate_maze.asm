wdb> disassemble generate_maze_obstacles
0xea8 <+0>:    push    rbp
0xea9 <+1>:    mov     rbp, rsp
0xeac <+4>:    sub     rsp, 0x18
0xeb0 <+8>:    mov     dword [rbp-0x14], edi
0xeb3 <+11>:   mov     eax, dword [rbp-0x14]
0xeb6 <+14>:   mov     dword [rbp-0xc], eax
0xeb9 <+17>:   mov     dword [rbp-0x8], 0x1
0xec0 <+24>:   jmp     0xf2b
0xec2 <+26>:   mov     eax, dword [rbp-0xc]
0xec5 <+29>:   mov     edi, eax
0xec7 <+31>:   call    0xe91 <get_random_number>
0xecc <+36>:   mov     dword [rbp-0xc], eax
0xecf <+39>:   mov     dword [rbp-0x4], 0x1
0xed6 <+46>:   jmp     0xf21
0xed8 <+48>:   mov     eax, dword [rbp-0xc]
0xedb <+51>:   mov     edi, eax
0xedd <+53>:   call    0xe91 <get_random_number>
0xee2 <+58>:   mov     dword [rbp-0xc], eax
0xee5 <+61>:   mov     eax, dword [rbp-0xc]
0xee8 <+64>:   and     eax, 0x51
0xeeb <+67>:   cmp     eax, 0x51
0xeee <+70>:   jne     0xf1c
0xef0 <+72>:   mov     eax, dword [rbp-0x4]
0xef3 <+75>:   movsxd  rcx, eax
0xef6 <+78>:   mov     eax, dword [rbp-0x8]
0xef9 <+81>:   movsxd  rdx, eax
0xefc <+84>:   mov     rax, rdx
0xeff <+87>:   shl     rax, 0x3
0xf03 <+91>:   sub     rax, rdx
0xf06 <+94>:   add     rax, rax
0xf09 <+97>:   lea     rdx, [rax+rcx]
0xf0d <+101>:  lea     rax, [rel 0x203060]
0xf14 <+108>:  add     rax, rdx
0xf17 <+111>:  mov     byte [rax], 0x58
0xf1a <+114>:  jmp     0xf1d
0xf1c <+116>:  nop     
0xf1d <+117>:  add     dword [rbp-0x4], 0x1
0xf21 <+121>:  cmp     dword [rbp-0x4], 0xc
0xf25 <+125>:  jle     0xed8
0xf27 <+127>:  add     dword [rbp-0x8], 0x1
0xf2b <+131>:  cmp     dword [rbp-0x8], 0x1c
0xf2f <+135>:  jle     0xec2
0xf31 <+137>:  nop     
0xf32 <+138>:  leave   
0xf33 <+139>:  retn    