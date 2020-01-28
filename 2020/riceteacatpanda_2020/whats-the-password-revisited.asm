
whats-the-password-revisited:     file format elf64-x86-64


Disassembly of section .init:

0000000000000718 <.init>:
 718:	48 83 ec 08          	sub    rsp,0x8
 71c:	48 8b 05 c5 08 20 00 	mov    rax,QWORD PTR [rip+0x2008c5]        # 200fe8 <exit@plt+0x200848>
 723:	48 85 c0             	test   rax,rax
 726:	74 02                	je     72a <strncpy@plt-0x16>
 728:	ff d0                	call   rax
 72a:	48 83 c4 08          	add    rsp,0x8
 72e:	c3                   	ret    

Disassembly of section .plt:

0000000000000730 <strncpy@plt-0x10>:
 730:	ff 35 5a 08 20 00    	push   QWORD PTR [rip+0x20085a]        # 200f90 <exit@plt+0x2007f0>
 736:	ff 25 5c 08 20 00    	jmp    QWORD PTR [rip+0x20085c]        # 200f98 <exit@plt+0x2007f8>
 73c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]

0000000000000740 <strncpy@plt>:
 740:	ff 25 5a 08 20 00    	jmp    QWORD PTR [rip+0x20085a]        # 200fa0 <exit@plt+0x200800>
 746:	68 00 00 00 00       	push   0x0
 74b:	e9 e0 ff ff ff       	jmp    730 <strncpy@plt-0x10>

0000000000000750 <puts@plt>:
 750:	ff 25 52 08 20 00    	jmp    QWORD PTR [rip+0x200852]        # 200fa8 <exit@plt+0x200808>
 756:	68 01 00 00 00       	push   0x1
 75b:	e9 d0 ff ff ff       	jmp    730 <strncpy@plt-0x10>

0000000000000760 <__stack_chk_fail@plt>:
 760:	ff 25 4a 08 20 00    	jmp    QWORD PTR [rip+0x20084a]        # 200fb0 <exit@plt+0x200810>
 766:	68 02 00 00 00       	push   0x2
 76b:	e9 c0 ff ff ff       	jmp    730 <strncpy@plt-0x10>

0000000000000770 <__fgets_chk@plt>:
 770:	ff 25 42 08 20 00    	jmp    QWORD PTR [rip+0x200842]        # 200fb8 <exit@plt+0x200818>
 776:	68 03 00 00 00       	push   0x3
 77b:	e9 b0 ff ff ff       	jmp    730 <strncpy@plt-0x10>

0000000000000780 <__strcpy_chk@plt>:
 780:	ff 25 3a 08 20 00    	jmp    QWORD PTR [rip+0x20083a]        # 200fc0 <exit@plt+0x200820>
 786:	68 04 00 00 00       	push   0x4
 78b:	e9 a0 ff ff ff       	jmp    730 <strncpy@plt-0x10>

0000000000000790 <__printf_chk@plt>:
 790:	ff 25 32 08 20 00    	jmp    QWORD PTR [rip+0x200832]        # 200fc8 <exit@plt+0x200828>
 796:	68 05 00 00 00       	push   0x5
 79b:	e9 90 ff ff ff       	jmp    730 <strncpy@plt-0x10>

00000000000007a0 <exit@plt>:
 7a0:	ff 25 2a 08 20 00    	jmp    QWORD PTR [rip+0x20082a]        # 200fd0 <exit@plt+0x200830>
 7a6:	68 06 00 00 00       	push   0x6
 7ab:	e9 80 ff ff ff       	jmp    730 <strncpy@plt-0x10>

Disassembly of section .plt.got:

00000000000007b0 <.plt.got>:
 7b0:	ff 25 42 08 20 00    	jmp    QWORD PTR [rip+0x200842]        # 200ff8 <exit@plt+0x200858>
 7b6:	66 90                	xchg   ax,ax

Disassembly of section .text:

00000000000007c0 <.text>:
 7c0:	55                   	push   rbp
 7c1:	53                   	push   rbx
 7c2:	ba 23 00 00 00       	mov    edx,0x23
 7c7:	48 83 ec 38          	sub    rsp,0x38
 7cb:	48 8b 35 9e 0e 20 00 	mov    rsi,QWORD PTR [rip+0x200e9e]        # 201670 <exit@plt+0x200ed0>
 7d2:	48 89 e3             	mov    rbx,rsp
 7d5:	48 89 df             	mov    rdi,rbx
 7d8:	48 8d 6b 0d          	lea    rbp,[rbx+0xd]
 7dc:	64 48 8b 04 25 28 00 	mov    rax,QWORD PTR fs:0x28
 7e3:	00 00 
 7e5:	48 89 44 24 28       	mov    QWORD PTR [rsp+0x28],rax
 7ea:	31 c0                	xor    eax,eax
 7ec:	e8 8f ff ff ff       	call   780 <__strcpy_chk@plt>
 7f1:	48 8d 35 5c 02 00 00 	lea    rsi,[rip+0x25c]        # a54 <exit@plt+0x2b4>
 7f8:	bf 01 00 00 00       	mov    edi,0x1
 7fd:	31 c0                	xor    eax,eax
 7ff:	e8 8c ff ff ff       	call   790 <__printf_chk@plt>
 804:	48 8b 0d 75 0e 20 00 	mov    rcx,QWORD PTR [rip+0x200e75]        # 201680 <stdin@@GLIBC_2.2.5>
 80b:	ba 1c 00 00 00       	mov    edx,0x1c
 810:	be 16 00 00 00       	mov    esi,0x16
 815:	48 89 ef             	mov    rdi,rbp
 818:	e8 53 ff ff ff       	call   770 <__fgets_chk@plt>
 81d:	48 8b 35 44 0e 20 00 	mov    rsi,QWORD PTR [rip+0x200e44]        # 201668 <exit@plt+0x200ec8>
 824:	48 8d 7b 05          	lea    rdi,[rbx+0x5]
 828:	ba 08 00 00 00       	mov    edx,0x8
 82d:	e8 0e ff ff ff       	call   740 <strncpy@plt>
 832:	31 d2                	xor    edx,edx
 834:	48 8d 35 e5 07 20 00 	lea    rsi,[rip+0x2007e5]        # 201020 <exit@plt+0x200880>
 83b:	48 89 ef             	mov    rdi,rbp
 83e:	eb 0a                	jmp    84a <exit@plt+0xaa>
 840:	48 83 c2 01          	add    rdx,0x1
 844:	48 83 fa 14          	cmp    rdx,0x14
 848:	74 38                	je     882 <exit@plt+0xe2>
 84a:	48 63 c2             	movsxd rax,edx
 84d:	48 8d 04 80          	lea    rax,[rax+rax*4]
 851:	48 c1 e0 04          	shl    rax,0x4
 855:	48 01 f0             	add    rax,rsi
 858:	0f be 08             	movsx  ecx,BYTE PTR [rax]
 85b:	0f b6 04 17          	movzx  eax,BYTE PTR [rdi+rdx*1]
 85f:	83 f0 32             	xor    eax,0x32
 862:	0f be c0             	movsx  eax,al
 865:	83 c0 01             	add    eax,0x1
 868:	83 f0 32             	xor    eax,0x32
 86b:	39 c1                	cmp    ecx,eax
 86d:	74 d1                	je     840 <exit@plt+0xa0>
 86f:	48 8d 3d f3 01 00 00 	lea    rdi,[rip+0x1f3]        # a69 <exit@plt+0x2c9>
 876:	e8 d5 fe ff ff       	call   750 <puts@plt>
 87b:	31 ff                	xor    edi,edi
 87d:	e8 1e ff ff ff       	call   7a0 <exit@plt>
 882:	48 8d 35 1f 02 00 00 	lea    rsi,[rip+0x21f]        # aa8 <exit@plt+0x308>
 889:	48 89 da             	mov    rdx,rbx
 88c:	31 c0                	xor    eax,eax
 88e:	bf 01 00 00 00       	mov    edi,0x1
 893:	66 c7 44 24 21 7d 00 	mov    WORD PTR [rsp+0x21],0x7d
 89a:	e8 f1 fe ff ff       	call   790 <__printf_chk@plt>
 89f:	31 c0                	xor    eax,eax
 8a1:	48 8b 5c 24 28       	mov    rbx,QWORD PTR [rsp+0x28]
 8a6:	64 48 33 1c 25 28 00 	xor    rbx,QWORD PTR fs:0x28
 8ad:	00 00 
 8af:	75 07                	jne    8b8 <exit@plt+0x118>
 8b1:	48 83 c4 38          	add    rsp,0x38
 8b5:	5b                   	pop    rbx
 8b6:	5d                   	pop    rbp
 8b7:	c3                   	ret    
 8b8:	e8 a3 fe ff ff       	call   760 <__stack_chk_fail@plt>
 8bd:	0f 1f 00             	nop    DWORD PTR [rax]
 8c0:	31 ed                	xor    ebp,ebp
 8c2:	49 89 d1             	mov    r9,rdx
 8c5:	5e                   	pop    rsi
 8c6:	48 89 e2             	mov    rdx,rsp
 8c9:	48 83 e4 f0          	and    rsp,0xfffffffffffffff0
 8cd:	50                   	push   rax
 8ce:	54                   	push   rsp
 8cf:	4c 8d 05 6a 01 00 00 	lea    r8,[rip+0x16a]        # a40 <exit@plt+0x2a0>
 8d6:	48 8d 0d f3 00 00 00 	lea    rcx,[rip+0xf3]        # 9d0 <exit@plt+0x230>
 8dd:	48 8d 3d dc fe ff ff 	lea    rdi,[rip+0xfffffffffffffedc]        # 7c0 <exit@plt+0x20>
 8e4:	ff 15 f6 06 20 00    	call   QWORD PTR [rip+0x2006f6]        # 200fe0 <exit@plt+0x200840>
 8ea:	f4                   	hlt    
 8eb:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]
 8f0:	48 8d 3d 81 0d 20 00 	lea    rdi,[rip+0x200d81]        # 201678 <exit@plt+0x200ed8>
 8f7:	55                   	push   rbp
 8f8:	48 8d 05 79 0d 20 00 	lea    rax,[rip+0x200d79]        # 201678 <exit@plt+0x200ed8>
 8ff:	48 39 f8             	cmp    rax,rdi
 902:	48 89 e5             	mov    rbp,rsp
 905:	74 19                	je     920 <exit@plt+0x180>
 907:	48 8b 05 ca 06 20 00 	mov    rax,QWORD PTR [rip+0x2006ca]        # 200fd8 <exit@plt+0x200838>
 90e:	48 85 c0             	test   rax,rax
 911:	74 0d                	je     920 <exit@plt+0x180>
 913:	5d                   	pop    rbp
 914:	ff e0                	jmp    rax
 916:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
 91d:	00 00 00 
 920:	5d                   	pop    rbp
 921:	c3                   	ret    
 922:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
 926:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
 92d:	00 00 00 
 930:	48 8d 3d 41 0d 20 00 	lea    rdi,[rip+0x200d41]        # 201678 <exit@plt+0x200ed8>
 937:	48 8d 35 3a 0d 20 00 	lea    rsi,[rip+0x200d3a]        # 201678 <exit@plt+0x200ed8>
 93e:	55                   	push   rbp
 93f:	48 29 fe             	sub    rsi,rdi
 942:	48 89 e5             	mov    rbp,rsp
 945:	48 c1 fe 03          	sar    rsi,0x3
 949:	48 89 f0             	mov    rax,rsi
 94c:	48 c1 e8 3f          	shr    rax,0x3f
 950:	48 01 c6             	add    rsi,rax
 953:	48 d1 fe             	sar    rsi,1
 956:	74 18                	je     970 <exit@plt+0x1d0>
 958:	48 8b 05 91 06 20 00 	mov    rax,QWORD PTR [rip+0x200691]        # 200ff0 <exit@plt+0x200850>
 95f:	48 85 c0             	test   rax,rax
 962:	74 0c                	je     970 <exit@plt+0x1d0>
 964:	5d                   	pop    rbp
 965:	ff e0                	jmp    rax
 967:	66 0f 1f 84 00 00 00 	nop    WORD PTR [rax+rax*1+0x0]
 96e:	00 00 
 970:	5d                   	pop    rbp
 971:	c3                   	ret    
 972:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
 976:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
 97d:	00 00 00 
 980:	80 3d 01 0d 20 00 00 	cmp    BYTE PTR [rip+0x200d01],0x0        # 201688 <stdin@@GLIBC_2.2.5+0x8>
 987:	75 2f                	jne    9b8 <exit@plt+0x218>
 989:	48 83 3d 67 06 20 00 	cmp    QWORD PTR [rip+0x200667],0x0        # 200ff8 <exit@plt+0x200858>
 990:	00 
 991:	55                   	push   rbp
 992:	48 89 e5             	mov    rbp,rsp
 995:	74 0c                	je     9a3 <exit@plt+0x203>
 997:	48 8b 3d 6a 06 20 00 	mov    rdi,QWORD PTR [rip+0x20066a]        # 201008 <exit@plt+0x200868>
 99e:	e8 0d fe ff ff       	call   7b0 <exit@plt+0x10>
 9a3:	e8 48 ff ff ff       	call   8f0 <exit@plt+0x150>
 9a8:	c6 05 d9 0c 20 00 01 	mov    BYTE PTR [rip+0x200cd9],0x1        # 201688 <stdin@@GLIBC_2.2.5+0x8>
 9af:	5d                   	pop    rbp
 9b0:	c3                   	ret    
 9b1:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
 9b8:	f3 c3                	repz ret 
 9ba:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
 9c0:	55                   	push   rbp
 9c1:	48 89 e5             	mov    rbp,rsp
 9c4:	5d                   	pop    rbp
 9c5:	e9 66 ff ff ff       	jmp    930 <exit@plt+0x190>
 9ca:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
 9d0:	41 57                	push   r15
 9d2:	41 56                	push   r14
 9d4:	49 89 d7             	mov    r15,rdx
 9d7:	41 55                	push   r13
 9d9:	41 54                	push   r12
 9db:	4c 8d 25 a6 03 20 00 	lea    r12,[rip+0x2003a6]        # 200d88 <exit@plt+0x2005e8>
 9e2:	55                   	push   rbp
 9e3:	48 8d 2d a6 03 20 00 	lea    rbp,[rip+0x2003a6]        # 200d90 <exit@plt+0x2005f0>
 9ea:	53                   	push   rbx
 9eb:	41 89 fd             	mov    r13d,edi
 9ee:	49 89 f6             	mov    r14,rsi
 9f1:	4c 29 e5             	sub    rbp,r12
 9f4:	48 83 ec 08          	sub    rsp,0x8
 9f8:	48 c1 fd 03          	sar    rbp,0x3
 9fc:	e8 17 fd ff ff       	call   718 <strncpy@plt-0x28>
 a01:	48 85 ed             	test   rbp,rbp
 a04:	74 20                	je     a26 <exit@plt+0x286>
 a06:	31 db                	xor    ebx,ebx
 a08:	0f 1f 84 00 00 00 00 	nop    DWORD PTR [rax+rax*1+0x0]
 a0f:	00 
 a10:	4c 89 fa             	mov    rdx,r15
 a13:	4c 89 f6             	mov    rsi,r14
 a16:	44 89 ef             	mov    edi,r13d
 a19:	41 ff 14 dc          	call   QWORD PTR [r12+rbx*8]
 a1d:	48 83 c3 01          	add    rbx,0x1
 a21:	48 39 dd             	cmp    rbp,rbx
 a24:	75 ea                	jne    a10 <exit@plt+0x270>
 a26:	48 83 c4 08          	add    rsp,0x8
 a2a:	5b                   	pop    rbx
 a2b:	5d                   	pop    rbp
 a2c:	41 5c                	pop    r12
 a2e:	41 5d                	pop    r13
 a30:	41 5e                	pop    r14
 a32:	41 5f                	pop    r15
 a34:	c3                   	ret    
 a35:	90                   	nop
 a36:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
 a3d:	00 00 00 
 a40:	f3 c3                	repz ret 

Disassembly of section .fini:

0000000000000a44 <.fini>:
 a44:	48 83 ec 08          	sub    rsp,0x8
 a48:	48 83 c4 08          	add    rsp,0x8
 a4c:	c3                   	ret    
