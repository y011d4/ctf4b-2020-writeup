# R&B

`problem.py` を眺めると、 `FORMAT` が [RB]+ で表され、R なら rot13、 B なら base64 で暗号化していることがわかる。

rot13 も base64 も復号可能なのと、R, B どちらで暗号化したかも親切に記録してくれているため、逆の操作を愚直に行えばよい。

`ctf4b{rot_base_rot_base_rot_base_base}`