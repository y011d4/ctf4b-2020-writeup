# unzip

`docker-compose.yml` を見ると、

```
    volumes:
      - ./public:/var/www/web
      - ./uploads:/uploads
      - ./flag.txt:/flag.txt
```

とあるので、 `flag.txt` をなんとかして読む問題だと予想。 `index.php` を読むと、 `"/uploads/" . session_id() . "/"` 以下にファイルが保存されていくらしい。

試しに `touch hoge; zip fuga.zip hoge` として `fuga.zip` を upload したら `hoge` というファイルを表示するようになった。ディレクトリトラバーサルかなと思い、 `touch ../../flag.txt; zip piyo.zip ../../flag.txt` でできた zip をアップロードして `../../flag.txt` を開いたらフラグが表示された。

`ctf4b{y0u_c4nn07_7ru57_4ny_1npu75_1nclud1n6_z1p_f1l3n4m35}`