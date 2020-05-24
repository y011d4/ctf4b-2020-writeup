import codecs
import base64


enc_flag = open("./encoded_flag", "r").read()

while True:
    if enc_flag[0] == "R":
        enc_flag = codecs.decode(enc_flag[1:], "rot_13")
    elif enc_flag[0] == "B":
        enc_flag = base64.b64decode(enc_flag[1:]).decode()
    else:
        break
print(enc_flag)
