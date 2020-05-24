# mask

実行してみると、 `Usage: ./mask [FLAG]` と表示される。flag を入力すると何かしら褒められるようなプログラムと予想。

radare2 を起動し、 `aaaaaa` で関数解析。 `iz` で string を見ると、

```
0   0x00002004 0x00002004 20  21   .rodata ascii Usage: ./mask [FLAG]
1   0x00002019 0x00002019 19  20   .rodata ascii Putting on masks...
2   0x0000202d 0x0000202d 29  30   .rodata ascii atd4`qdedtUpetepqeUdaaeUeaqau
3   0x0000204b 0x0000204b 29  30   .rodata ascii c`b bk`kj`KbababcaKbacaKiacki
4   0x00002069 0x00002069 26  27   .rodata ascii Correct! Submit your FLAG.
5   0x00002084 0x00002084 22  23   .rodata ascii Wrong FLAG. Try again.
```

`axt 0x00002069` で `Correct!` と表示する部分が表示される。

```
main 0x12cf [DATA] lea rdi, str.Correct__Submit_your_FLAG.
```

`s 0x12cf` で該当箇所に移動し前の辺りを見渡すと、 `rbp - 0x90` と `rbp - 0x50` があるバイト列に一致しているかをチェックしている。

```
│           0x0000129e      488d8570ffff.  lea rax, [s1]
│           0x000012a5      488d35810d00.  lea rsi, str.atd4_qdedtUpetepqeUdaaeUeaqau    ; 0x202d ; "atd4`qdedtUpetepqeUdaaeUeaqau" ; const char *s2
│           0x000012ac      4889c7         mov rdi, rax                ; const char *s1
│           0x000012af      e8bcfdffff     call sym.imp.strcmp         ;[3] ; int strcmp(const char *s1, const char *s2)
│           0x000012b4      85c0           test eax, eax
│       ┌─< 0x000012b6      7525           jne 0x12dd
│       │   0x000012b8      488d45b0       lea rax, [var_50h]
│       │   0x000012bc      488d35880d00.  lea rsi, str.c_b_bk_kj_KbababcaKbacaKiacki    ; 0x204b ; "c`b bk`kj`KbababcaKbacaKiacki" ; const char *s2
│       │   0x000012c3      4889c7         mov rdi, rax                ; const char *s1
│       │   0x000012c6      e8a5fdffff     call sym.imp.strcmp         ;[3] ; int strcmp(const char *s1, const char *s2)
```

もう少し上の部分を見ていくと、 `rbp - 0x90` と `rbp-0x50` の部分にそれぞれ `AND(FLAG, 0x75)` , `AND(FLAG, 0xffffffeb)` を代入している (各バイトごとに AND)。

```
│           0x00001200      c78528ffffff.  mov dword [var_d8h], 0
│       ┌─< 0x0000120a      eb4c           jmp 0x1258
│       │   ; CODE XREF from main @ 0x1264
│      ┌──> 0x0000120c      8b8528ffffff   mov eax, dword [var_d8h]
│      ╎│   0x00001212      4898           cdqe
│      ╎│   0x00001214      0fb6840530ff.  movzx eax, byte [rbp + rax - 0xd0]
│      ╎│   0x0000121c      83e075         and eax, 0x75
│      ╎│   0x0000121f      89c2           mov edx, eax
│      ╎│   0x00001221      8b8528ffffff   mov eax, dword [var_d8h]
│      ╎│   0x00001227      4898           cdqe
│      ╎│   0x00001229      88940570ffff.  mov byte [rbp + rax - 0x90], dl
│      ╎│   0x00001230      8b8528ffffff   mov eax, dword [var_d8h]
│      ╎│   0x00001236      4898           cdqe
│      ╎│   0x00001238      0fb6840530ff.  movzx eax, byte [rbp + rax - 0xd0]
│      ╎│   0x00001240      83e0eb         and eax, 0xffffffeb         ; 4294967275
│      ╎│   0x00001243      89c2           mov edx, eax
│      ╎│   0x00001245      8b8528ffffff   mov eax, dword [var_d8h]
│      ╎│   0x0000124b      4898           cdqe
│      ╎│   0x0000124d      885405b0       mov byte [rbp + rax - 0x50], dl
│      ╎│   0x00001251      838528ffffff.  add dword [var_d8h], 1
│      ╎│   ; CODE XREF from main @ 0x120a
│      ╎└─> 0x00001258      8b8528ffffff   mov eax, dword [var_d8h]
│      ╎    0x0000125e      3b852cffffff   cmp eax, dword [var_d4h]
│      └──< 0x00001264      7ca6           jl 0x120c
│           0x00001266      8b852cffffff   mov eax, dword [var_d4h]
│           0x0000126c      4898           cdqe
│           0x0000126e      c6840570ffff.  mov byte [rbp + rax - 0x90], 0
│           0x00001276      8b852cffffff   mov eax, dword [var_d4h]
│           0x0000127c      4898           cdqe
│           0x0000127e      c64405b000     mov byte [rbp + rax - 0x50], 0
```

以上の情報をもとにフラグを1文字ずつ決めていく (この条件だけで一意に決まるのかはわかっていない)

```python
s1 = "atd4`qdedtUpetepqeUdaaeUeaqau"
s2 = "c`b bk`kj`KbababcaKbacaKiacki"

result = []
for i in range(len(s1)):
    for j in range(32, 128):
        if chr(j & 0x75) == s1[i] and chr(j & 0xffffffeb) == s2[i]:
            result.append(chr(j))
print("".join(result))
```

`ctf4b{dont_reverse_face_mask}`