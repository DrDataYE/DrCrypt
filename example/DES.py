from drcrypt.crypt import SDES


key = "1100011110" # 10-bits 
plaintext = "00101000" # 8-bits 
cipher = SDES(key)
encrypted = cipher.encrypt(plaintext)
decrypted = cipher.decrypt(encrypted)

print('plaintext:', plaintext)
print('key:', key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
