def xor_bytes(b1, b2):
    return bytes(a ^ b for (a, b) in zip(b1, b2))

def xor(x):
    return bytearray.fromhex(x)
    
key1 = xor("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
print(key1)

temp = xor("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key2 = xor_bytes(temp, key1)
print(key2)

temp = xor("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
key3 = xor_bytes(temp, key2)

flag = xor("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
flag = xor_bytes(flag, key3)
flag = xor_bytes(flag, key2)
flag = xor_bytes(flag, key1)

print(flag)