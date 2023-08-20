from drcrypt.hash import MD5


data = "Hello, MD5!"
md5_hash = MD5Hash()
md5_hash.update(data.encode("utf-8"))
md5_hash.finalize()
hashed = md5_hash.hexdigest()

print("Data:", data)
print("MD5 Hash:", hashed)
