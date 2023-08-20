from drcrypt.crypt import MD5, compare_hash


data = "Hello, MD5!"
md5_hash = MD5()
md5_hash.update(data.encode("utf-8"))
md5_hash.finalize()
hashed = md5_hash.hexdigest()

result = compare_hash(MD5(), data, hashed)

if result:
    print("Hashes match! The data matches the target hash.")
else:
    print("Hashes do not match. The data does not match the target hash.")
