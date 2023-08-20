from drcrypt.hash import SHA256


data = "Hello, SHA-1!"
sha1_hash = SHA256()
sha1_hash.update(data.encode("utf-8"))
sha1_hash.finalize()
hashed = sha1_hash.hexdigest()

print("Data:", data)
print("SHA-1 Hash:", hashed)

