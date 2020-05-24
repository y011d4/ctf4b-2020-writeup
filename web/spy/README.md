# Spy

26人いる候補のうち、DB に登録されているユーザーが誰かを特定する問題 (最悪 2^26 なので総当りでもいける…？しないけど)。

`app.py` を読んでいると、挑発的なコメントを発見。なのでこの辺りがキモになっているのだと予想。

```
exists, account = db.get_account(name)

if not exists:
    return render_template("index.html", message="Login failed, try again.", sec="{:.7f}".format(time.perf_counter()-t))

# auth.calc_password_hash(salt, password) adds salt and performs stretching so many times.
# You know, it's really secure... isn't it? :-)
hashed_password = auth.calc_password_hash(app.SALT, password)
if hashed_password != account.password:
    return render_template("index.html", message="Login failed, try again.", sec="{:.7f}".format(time.perf_counter()-t))
```

ストレッチングはパスワード一致判定をするとき、総当り攻撃を防ぐためにハッシュ化を何回も行って計算時間を遅くする手法。なので、 db にユーザーがいるかどうかで `render_template` の実行までにかかる時間が異なる。画面下側に時間が書かれているので 26 人分ログインを試して時間を確認していけばよい。

`ctf4b{4cc0un7_3num3r4710n_by_51d3_ch4nn3l_4774ck}`

