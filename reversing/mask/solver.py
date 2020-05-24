s1 = "atd4`qdedtUpetepqeUdaaeUeaqau"
s2 = "c`b bk`kj`KbababcaKbacaKiacki"

result = []
for i in range(len(s1)):
    for j in range(32, 128):
        if chr(j & 0x75) == s1[i] and chr(j & 0xffffffeb) == s2[i]:
            result.append(chr(j))
print("".join(result))
