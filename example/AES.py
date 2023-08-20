from drcrypt.crypt import encrypt_aes, decrypt_aes


key = "MyTestPassword!!".encode("utf-8")
text = "Hello, world"
en = encrypt_aes(text,key)

print("Text:",text,end="\n\n")
print("Encrypt:",en.decode("utf-8"))
print("Decrypt:",decrypt_aes(en,key).decode("utf-8"))
