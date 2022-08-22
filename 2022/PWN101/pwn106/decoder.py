array = ["5F5530797B4D4854","5F3368745F6E3077","5961774133766947","3168745F446E615F","756F595F73315F73"]

flag = b""

try:
    for word in array:
        flag += bytes.fromhex(word.decode('utf-8'))[::-1]
except Exception:
    pass
print(flag)