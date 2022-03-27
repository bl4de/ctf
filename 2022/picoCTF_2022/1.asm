
run:	file format elf64-x86-64

Disassembly of section .init:

0000000000001000 <_init>:
    1000: f3 0f 1e fa                  	endbr64
    1004: 48 83 ec 08                  	sub	rsp, 8
    1008: 48 8b 05 d9 2f 00 00         	mov	rax, qword ptr [rip + 12249] # 0x3fe8 <_GLOBAL_OFFSET_TABLE_+0x30>
    100f: 48 85 c0                     	test	rax, rax
    1012: 74 02                        	je	0x1016 <_init+0x16>
    1014: ff d0                        	call	rax
    1016: 48 83 c4 08                  	add	rsp, 8
    101a: c3                           	ret

Disassembly of section .plt:

0000000000001020 <.plt>:
    1020: ff 35 9a 2f 00 00            	push	qword ptr [rip + 12186] # 0x3fc0 <_GLOBAL_OFFSET_TABLE_+0x8>
    1026: f2 ff 25 9b 2f 00 00         	repne		jmp	qword ptr [rip + 12187] # 0x3fc8 <_GLOBAL_OFFSET_TABLE_+0x10>
    102d: 0f 1f 00                     	nop	dword ptr [rax]
    1030: f3 0f 1e fa                  	endbr64
    1034: 68 00 00 00 00               	push	0
    1039: f2 e9 e1 ff ff ff            	repne		jmp	0x1020 <.plt>
    103f: 90                           	nop

Disassembly of section .plt.got:

0000000000001040 <.plt.got>:
    1040: f3 0f 1e fa                  	endbr64
    1044: f2 ff 25 ad 2f 00 00         	repne		jmp	qword ptr [rip + 12205] # 0x3ff8 <_GLOBAL_OFFSET_TABLE_+0x40>
    104b: 0f 1f 44 00 00               	nop	dword ptr [rax + rax]

Disassembly of section .plt.sec:

0000000000001050 <.plt.sec>:
    1050: f3 0f 1e fa                  	endbr64
    1054: f2 ff 25 75 2f 00 00         	repne		jmp	qword ptr [rip + 12149] # 0x3fd0 <_GLOBAL_OFFSET_TABLE_+0x18>
    105b: 0f 1f 44 00 00               	nop	dword ptr [rax + rax]

Disassembly of section .text:

0000000000001060 <_start>:
    1060: f3 0f 1e fa                  	endbr64
    1064: 31 ed                        	xor	ebp, ebp
    1066: 49 89 d1                     	mov	r9, rdx
    1069: 5e                           	pop	rsi
    106a: 48 89 e2                     	mov	rdx, rsp
    106d: 48 83 e4 f0                  	and	rsp, -16
    1071: 50                           	push	rax
    1072: 54                           	push	rsp
    1073: 4c 8d 05 76 01 00 00         	lea	r8, [rip + 374]         # 0x11f0 <__libc_csu_fini>
    107a: 48 8d 0d ff 00 00 00         	lea	rcx, [rip + 255]        # 0x1180 <__libc_csu_init>
    1081: 48 8d 3d c1 00 00 00         	lea	rdi, [rip + 193]        # 0x1149 <main>
    1088: ff 15 52 2f 00 00            	call	qword ptr [rip + 12114] # 0x3fe0 <_GLOBAL_OFFSET_TABLE_+0x28>
    108e: f4                           	hlt
    108f: 90                           	nop

0000000000001090 <deregister_tm_clones>:
    1090: 48 8d 3d 81 2f 00 00         	lea	rdi, [rip + 12161]      # 0x4018 <completed.8060>
    1097: 48 8d 05 7a 2f 00 00         	lea	rax, [rip + 12154]      # 0x4018 <completed.8060>
    109e: 48 39 f8                     	cmp	rax, rdi
    10a1: 74 15                        	je	0x10b8 <deregister_tm_clones+0x28>
    10a3: 48 8b 05 2e 2f 00 00         	mov	rax, qword ptr [rip + 12078] # 0x3fd8 <_GLOBAL_OFFSET_TABLE_+0x20>
    10aa: 48 85 c0                     	test	rax, rax
    10ad: 74 09                        	je	0x10b8 <deregister_tm_clones+0x28>
    10af: ff e0                        	jmp	rax
    10b1: 0f 1f 80 00 00 00 00         	nop	dword ptr [rax]
    10b8: c3                           	ret
    10b9: 0f 1f 80 00 00 00 00         	nop	dword ptr [rax]

00000000000010c0 <register_tm_clones>:
    10c0: 48 8d 3d 51 2f 00 00         	lea	rdi, [rip + 12113]      # 0x4018 <completed.8060>
    10c7: 48 8d 35 4a 2f 00 00         	lea	rsi, [rip + 12106]      # 0x4018 <completed.8060>
    10ce: 48 29 fe                     	sub	rsi, rdi
    10d1: 48 89 f0                     	mov	rax, rsi
    10d4: 48 c1 ee 3f                  	shr	rsi, 63
    10d8: 48 c1 f8 03                  	sar	rax, 3
    10dc: 48 01 c6                     	add	rsi, rax
    10df: 48 d1 fe                     	sar	rsi
    10e2: 74 14                        	je	0x10f8 <register_tm_clones+0x38>
    10e4: 48 8b 05 05 2f 00 00         	mov	rax, qword ptr [rip + 12037] # 0x3ff0 <_GLOBAL_OFFSET_TABLE_+0x38>
    10eb: 48 85 c0                     	test	rax, rax
    10ee: 74 08                        	je	0x10f8 <register_tm_clones+0x38>
    10f0: ff e0                        	jmp	rax
    10f2: 66 0f 1f 44 00 00            	nop	word ptr [rax + rax]
    10f8: c3                           	ret
    10f9: 0f 1f 80 00 00 00 00         	nop	dword ptr [rax]

0000000000001100 <__do_global_dtors_aux>:
    1100: f3 0f 1e fa                  	endbr64
    1104: 80 3d 0d 2f 00 00 00         	cmp	byte ptr [rip + 12045], 0 # 0x4018 <completed.8060>
    110b: 75 2b                        	jne	0x1138 <__do_global_dtors_aux+0x38>
    110d: 55                           	push	rbp
    110e: 48 83 3d e2 2e 00 00 00      	cmp	qword ptr [rip + 12002], 0 # 0x3ff8 <_GLOBAL_OFFSET_TABLE_+0x40>
    1116: 48 89 e5                     	mov	rbp, rsp
    1119: 74 0c                        	je	0x1127 <__do_global_dtors_aux+0x27>
    111b: 48 8b 3d e6 2e 00 00         	mov	rdi, qword ptr [rip + 12006] # 0x4008 <__dso_handle>
    1122: e8 19 ff ff ff               	call	0x1040 <.plt.got>
    1127: e8 64 ff ff ff               	call	0x1090 <deregister_tm_clones>
    112c: c6 05 e5 2e 00 00 01         	mov	byte ptr [rip + 12005], 1 # 0x4018 <completed.8060>
    1133: 5d                           	pop	rbp
    1134: c3                           	ret
    1135: 0f 1f 00                     	nop	dword ptr [rax]
    1138: c3                           	ret
    1139: 0f 1f 80 00 00 00 00         	nop	dword ptr [rax]

0000000000001140 <frame_dummy>:
    1140: f3 0f 1e fa                  	endbr64
    1144: e9 77 ff ff ff               	jmp	0x10c0 <register_tm_clones>

0000000000001149 <main>:
    1149: f3 0f 1e fa                  	endbr64
    114d: 55                           	push	rbp
    114e: 48 89 e5                     	mov	rbp, rsp
    1151: 48 83 ec 10                  	sub	rsp, 16
    1155: 89 7d fc                     	mov	dword ptr [rbp - 4], edi
    1158: 48 89 75 f0                  	mov	qword ptr [rbp - 16], rsi
    115c: 48 8b 05 ad 2e 00 00         	mov	rax, qword ptr [rip + 11949] # 0x4010 <flag>
    1163: 48 89 c6                     	mov	rsi, rax
    1166: 48 8d 3d c3 0e 00 00         	lea	rdi, [rip + 3779]       # 0x2030 <_IO_stdin_used+0x30>
    116d: b8 00 00 00 00               	mov	eax, 0
    1172: e8 d9 fe ff ff               	call	0x1050 <.plt.sec>
    1177: b8 00 00 00 00               	mov	eax, 0
    117c: c9                           	leave
    117d: c3                           	ret
    117e: 66 90                        	nop

0000000000001180 <__libc_csu_init>:
    1180: f3 0f 1e fa                  	endbr64
    1184: 41 57                        	push	r15
    1186: 4c 8d 3d 2b 2c 00 00         	lea	r15, [rip + 11307]      # 0x3db8 <__init_array_start>
    118d: 41 56                        	push	r14
    118f: 49 89 d6                     	mov	r14, rdx
    1192: 41 55                        	push	r13
    1194: 49 89 f5                     	mov	r13, rsi
    1197: 41 54                        	push	r12
    1199: 41 89 fc                     	mov	r12d, edi
    119c: 55                           	push	rbp
    119d: 48 8d 2d 1c 2c 00 00         	lea	rbp, [rip + 11292]      # 0x3dc0 <__do_global_dtors_aux_fini_array_entry>
    11a4: 53                           	push	rbx
    11a5: 4c 29 fd                     	sub	rbp, r15
    11a8: 48 83 ec 08                  	sub	rsp, 8
    11ac: e8 4f fe ff ff               	call	0x1000 <_init>
    11b1: 48 c1 fd 03                  	sar	rbp, 3
    11b5: 74 1f                        	je	0x11d6 <__libc_csu_init+0x56>
    11b7: 31 db                        	xor	ebx, ebx
    11b9: 0f 1f 80 00 00 00 00         	nop	dword ptr [rax]
    11c0: 4c 89 f2                     	mov	rdx, r14
    11c3: 4c 89 ee                     	mov	rsi, r13
    11c6: 44 89 e7                     	mov	edi, r12d
    11c9: 41 ff 14 df                  	call	qword ptr [r15 + 8*rbx]
    11cd: 48 83 c3 01                  	add	rbx, 1
    11d1: 48 39 dd                     	cmp	rbp, rbx
    11d4: 75 ea                        	jne	0x11c0 <__libc_csu_init+0x40>
    11d6: 48 83 c4 08                  	add	rsp, 8
    11da: 5b                           	pop	rbx
    11db: 5d                           	pop	rbp
    11dc: 41 5c                        	pop	r12
    11de: 41 5d                        	pop	r13
    11e0: 41 5e                        	pop	r14
    11e2: 41 5f                        	pop	r15
    11e4: c3                           	ret
    11e5: 66 66 2e 0f 1f 84 00 00 00 00 00     	nop	word ptr cs:[rax + rax]

00000000000011f0 <__libc_csu_fini>:
    11f0: f3 0f 1e fa                  	endbr64
    11f4: c3                           	ret

Disassembly of section .fini:

00000000000011f8 <_fini>:
    11f8: f3 0f 1e fa                  	endbr64
    11fc: 48 83 ec 08                  	sub	rsp, 8
    1200: 48 83 c4 08                  	add	rsp, 8
    1204: c3                           	ret
