main:
        lea     ecx, [esp+4]
        and     esp, -16
        push    DWORD PTR [ecx-4]
        push    ebp
        mov     ebp, esp
        push    ebx
        push    ecx
        sub     esp, 32
        mov     ebx, ecx
        cmp     DWORD PTR [ebx], 2
        je      .L2
        mov     eax, 1
        jmp     .L3
.L2:
        mov     DWORD PTR [ebp-12], 0
        jmp     .L4
.L6:
        mov     eax, DWORD PTR [ebx+4]
        add     eax, 4
        mov     edx, DWORD PTR [eax]
        mov     eax, DWORD PTR [ebp-12]
        add     eax, edx
        movzx   eax, BYTE PTR [eax]
        test    al, al
        jne     .L5
        mov     eax, 1
        jmp     .L3
.L5:
        add     DWORD PTR [ebp-12], 1
.L4:
        cmp     DWORD PTR [ebp-12], 28
        jle     .L6
        sub     esp, 12
        push    29
        call    malloc
        add     esp, 16
        mov     DWORD PTR [ebp-32], eax
        mov     DWORD PTR [ebp-16], 0
        jmp     .L7
.L8:
        mov     eax, DWORD PTR [ebx+4]
        add     eax, 4
        mov     edx, DWORD PTR [eax]
        mov     eax, DWORD PTR [ebp-16]
        add     eax, edx
        mov     ecx, DWORD PTR [ebp-16]
        mov     edx, DWORD PTR [ebp-32]
        add     edx, ecx
        movzx   eax, BYTE PTR [eax]
        mov     BYTE PTR [edx], al
        mov     edx, DWORD PTR [ebp-16]
        mov     eax, DWORD PTR [ebp-32]
        add     eax, edx
        movzx   eax, BYTE PTR [eax]
        lea     ecx, [eax-49]
        mov     edx, DWORD PTR [ebp-16]
        mov     eax, DWORD PTR [ebp-32]
        add     eax, edx
        mov     edx, ecx
        mov     BYTE PTR [eax], dl
        add     DWORD PTR [ebp-16], 1
.L7:
        cmp     DWORD PTR [ebp-16], 28
        jle     .L8
        mov     eax, DWORD PTR [ebp-32]
        movzx   edx, BYTE PTR [eax]
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 2
        movzx   eax, BYTE PTR [eax]
        cmp     dl, al
        je      .L9
        mov     eax, 1
        jmp     .L3
.L9:
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 1
        movzx   eax, BYTE PTR [eax]
        cmp     al, 56
        je      .L10
        mov     eax, 1
        jmp     .L3
.L10:
        mov     eax, DWORD PTR [ebp-32]
        movzx   eax, BYTE PTR [eax]
        cmp     al, 54
        je      .L11
        mov     eax, 1
        jmp     .L3
.L11:
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 3
        movzx   eax, BYTE PTR [eax]
        cmp     al, 52
        je      .L12
        mov     eax, 1
        jmp     .L3
.L12:
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 28
        movzx   eax, BYTE PTR [eax]
        movsx   eax, al
        mov     edx, DWORD PTR [ebp-32]
        add     edx, 5
        movzx   edx, BYTE PTR [edx]
        movsx   edx, dl
        add     edx, 2
        cmp     eax, edx
        je      .L13
        mov     eax, 1
        jmp     .L3
.L13:
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 5
        movzx   eax, BYTE PTR [eax]
        cmp     al, 74
        je      .L14
        mov     eax, 1
        jmp     .L3
.L14:
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 4
        movzx   eax, BYTE PTR [eax]
        cmp     al, 60
        je      .L15
        mov     eax, 1
        jmp     .L3
.L15:
        mov     DWORD PTR [ebp-20], 0
        jmp     .L16
.L18:
        mov     eax, DWORD PTR [ebp-20]
        lea     edx, [eax+6]
        mov     eax, DWORD PTR [ebp-32]
        add     eax, edx
        movzx   eax, BYTE PTR [eax]
        cmp     al, 48
        je      .L17
        mov     eax, 1
        jmp     .L3
.L17:
        add     DWORD PTR [ebp-20], 1
.L16:
        cmp     DWORD PTR [ebp-20], 2
        jle     .L18
        mov     DWORD PTR [ebp-24], 0
        jmp     .L19
.L21:
        mov     eax, DWORD PTR [ebp-24]
        lea     edx, [eax+10]
        mov     eax, DWORD PTR [ebp-32]
        add     eax, edx
        movzx   eax, BYTE PTR [eax]
        cmp     al, 49
        je      .L20
        mov     eax, 1
        jmp     .L3
.L20:
        add     DWORD PTR [ebp-24], 1
.L19:
        cmp     DWORD PTR [ebp-24], 3
        jle     .L21
        mov     DWORD PTR [ebp-28], 0
        jmp     .L22
.L24:
        mov     eax, DWORD PTR [ebp-28]
        lea     edx, [eax+15]
        mov     eax, DWORD PTR [ebp-32]
        add     eax, edx
        movzx   eax, BYTE PTR [eax]
        cmp     al, 50
        je      .L23
        mov     eax, 1
        jmp     .L3
.L23:
        add     DWORD PTR [ebp-28], 1
.L22:
        cmp     DWORD PTR [ebp-28], 4
        jle     .L24
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 21
        movzx   eax, BYTE PTR [eax]
        movsx   eax, al
        mov     edx, DWORD PTR [ebp-32]
        add     edx, 15
        movzx   edx, BYTE PTR [edx]
        movsx   edx, dl
        add     edx, 1
        cmp     eax, edx
        je      .L25
        mov     eax, 1
        jmp     .L3
.L25:
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 9
        movzx   edx, BYTE PTR [eax]
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 14
        movzx   eax, BYTE PTR [eax]
        cmp     dl, al
        je      .L26
        mov     eax, 1
        jmp     .L3
.L26:
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 9
        movzx   edx, BYTE PTR [eax]
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 20
        movzx   eax, BYTE PTR [eax]
        cmp     dl, al
        je      .L27
        mov     eax, 1
        jmp     .L3
.L27:
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 9
        movzx   edx, BYTE PTR [eax]
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 22
        movzx   eax, BYTE PTR [eax]
        cmp     dl, al
        je      .L28
        mov     eax, 1
        jmp     .L3
.L28:
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 9
        movzx   eax, BYTE PTR [eax]
        cmp     al, 46
        je      .L29
        mov     eax, 1
        jmp     .L3
.L29:
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 27
        movzx   eax, BYTE PTR [eax]
        cmp     al, 1
        je      .L30
        mov     eax, 1
        jmp     .L3
.L30:
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 26
        movzx   eax, BYTE PTR [eax]
        cmp     al, 2
        je      .L31
        mov     eax, 1
        jmp     .L3
.L31:
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 23
        movzx   eax, BYTE PTR [eax]
        cmp     al, 3
        je      .L32
        mov     eax, 1
        jmp     .L3
.L32:
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 24
        movzx   eax, BYTE PTR [eax]
        cmp     al, 4
        je      .L33
        mov     eax, 1
        jmp     .L3
.L33:
        mov     eax, DWORD PTR [ebp-32]
        add     eax, 25
        movzx   eax, BYTE PTR [eax]
        movsx   eax, al
.L3:
        lea     esp, [ebp-8]
        pop     ecx
        pop     ebx
        pop     ebp
        lea     esp, [ecx-4]
        ret
