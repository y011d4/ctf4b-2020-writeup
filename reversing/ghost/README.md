# ghost

`chall.gs` を眺めると、なんかしらの stack 操作で演算をするプログラムのように見える。拡張子や `chall.gs` に出てくる文字列や、題名などから調べると、 Ghostscript であることがわかった。

`chall.gs` を仕様書とにらめっこしながら読み解くのが想定解と思われるが、 Ghostscript をインストールすれば `$ gs chall.gs` で実行できるため、動作確認をしてみると以下のことがわかった。

* 入力した文字列と同じ長さの配列が返される
* `input + dummy_1 => output_1`, `input + dummy_2 => output_2` のとき、`output_1[:len(input)] == output_2[:len(input)]` となる
* `dummy_1 + input => output_1`, `dummy_2 + input => output_2` のとき、`output_1` と `output_2` はどこも一致しない

以上のことから、 flag の文字列を前方から1文字ずつ決定していけばよい。

```python
import subprocess

with open("./output.txt", "r") as f:
    buf = f.read()
output = list(map(int, buf.split()))

cmd = "gs chall.gs"
flag = "ctf4b"
while True:
    for i in range(32, 128):
        c = chr(i)
        with subprocess.Popen(
            cmd.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
        ) as proc:
            for _ in range(4):
                _ = proc.stdout.readline()
            print(f"{flag}{c}", file=proc.stdin, flush=True)
            result = proc.stdout.readline()
        if output[len(flag)] == int(result.split()[-1]):
            flag += c
            break
    if len(flag) == len(output):
        break
print(flag)
```

(夕食の時間にちょうどいいぐらいの実行時間がかかります)

`ctf4b{st4ck_m4ch1n3_1s_4_l0t_0f_fun!}`