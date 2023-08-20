from drscan.hash import Bcrypt


# مثال على استخدام الكلاس
bcrypt_hasher = Bcrypt()
password = "mysecretpassword"
salt = bcrypt_hasher.generate_salt()
hashed_password = bcrypt_hasher.bcrypt_hash(password, salt)

input_password = "mysecretpassword"
if bcrypt_hasher.verify_password(input_password, hashed_password):
    print("Password Matched!")
else:
    print("Password Does Not Match!")
