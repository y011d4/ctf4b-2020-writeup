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
