import binascii

from Crypto.Util.number import *
from pwn import *

# context.log_level = "DEBUG"

code = b"1337,F"  # % 2 == 0
code_num = bytes_to_long(code)

N = 104452494729225554355976515219434250315042721821732083150042629449067462088950256883215876205745135468798595887009776140577366427694442102435040692014432042744950729052688898874640941018896944459642713041721494593008013710266103709315252166260911167655036124762795890569902823253950438711272265515759550956133

s = remote("rsacalc.quals.beginners.seccon.jp", 10001)
s.sendlineafter("> ", "1")
s.sendlineafter("data> ", b"\x02")
s.recvuntil("Signature: ")
pow_2_d = int(s.recvline().strip(), 16)


s.sendlineafter("> ", "1")
s.sendlineafter("data> ", long_to_bytes(code_num // 2))
s.recvuntil("Signature: ")
pow_code_2_d = int(s.recvline().strip(), 16)


payload = pow_code_2_d * pow_2_d % N
payload = binascii.hexlify(long_to_bytes(payload)).decode()

s.sendlineafter("> ", "2")
s.sendlineafter("data> ", code)
s.sendlineafter("signature> ", payload)
print(s.recv())
