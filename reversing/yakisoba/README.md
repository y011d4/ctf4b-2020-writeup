# yakisoba

[mask](https://github.com/y011d4/ctf4b-2020-writeup/tree/master/reversing/mask) の問題と同様に flag の一致判定結果を表示部分に飛ぶと、 `fcn.00000820` で一致判定をしていそう。中を見てみると条件分岐がたくさんある。ヒントに `You'd better automate your analysis` と書いてあったのはそういうことか。

自動化したいのはやまやまだが、いい方法を思いつかなかった (きっといいツールがあるのだろうけど) ので、がんばって読むことにした。一応 scanf の引数から flag は31文字以内であることがわかっていたので、それぐらいならいけるかなと。 `movzx edx, byte [rdi + N]` の部分を見るのと、 flag が leet で文章になることを意識して読めば人力でも読めるレベルだった。
(自動化したいですね…)

`ctf4b{sp4gh3tt1_r1pp3r1n0}`