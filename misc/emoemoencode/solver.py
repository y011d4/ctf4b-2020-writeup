with open("./emoemoencode.txt-2586093c6d0bf61e0babf4d142c2418fb243b188", "r") as f:
    buf = f.read()

result = []
for c in buf[:-1]:
    h = c.encode("unicode-escape")[-2:].decode()
    result.append(chr(int(h, 16)))

print("".join(result))
