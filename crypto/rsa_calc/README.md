# RSA Calc

問題名の通り、 RSA の問題。 `server.py` を読むと、

* p, q, e は固定 (したがって N, d, phi なども固定)
* 任意の文字列 (ただし `F` や `1337` を含んでいない) を投げると、暗号化したものを得られる
* `1337,F`(以下 `code` と呼ぶ) を暗号化したものを投げつければフラグが得られる

ということがわかる。

```
code^d \equiv (code/2)^d * 2^d (mod N)
```

となることを利用し、 code/2 の暗号と 2 (\x02) の暗号の積を取ることで、 code の暗号が得られる。

`ctf4b{SIgn_n33ds_P4d&H4sh}`