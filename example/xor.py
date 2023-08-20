from drcrypt.crypt import XOR


text = "Hello, World"
xor = XOR("MyPassword","utf-8")
en = xor.encrypt(text)

print("Text:",text,end="\n\n")
print("Encrypt:",en)
print("Decrypt:",xor.decrypt(en))
