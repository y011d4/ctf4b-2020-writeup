# Noisy equations

問題文を眺めると、
1. `coeffs` をランダムに生成
1. `FLAG` を 1byte の整数のベクトルとみなし、 `dot(coeffs, FLAG)`
1. **seed** を固定した上で* rand を生成して足す = `answers`

こうして得られた `coeffs` と `answers` が返される。式で書くとこんな感じ。
```
\sum_j coeffs_ij FLAG_j + rand_i = answers_i (for 0 <= i < 44)
```
`nc` を叩くたびに `coeffs` は変化するが、 rand は変化しないことに注意すると、2回 `nc` して得られた `coeffs` と `answers` の差を取れば ( `diff_coeffs`, `diff_answers` とする)、

```
\sum_j diff_coeffs_ij FLAG_j = diff_answers_i (for 0 <= i < 44)
```
となり、ただの行列計算になる。
大きな値の行列計算を扱うため、 `numpy` とかで適当にやろうとすると詰んでしまった。自分は [sage](https://sagecell.sagemath.org/) を使って解いた。 

`create_sage_code.py` でフラグ計算用のコード `sage.txt` を出力し、それを上記サイトに投げてフラグを得た。

`ctf4b{r4nd0m_533d_15_n3c3554ry_f0r_53cur17y}`
