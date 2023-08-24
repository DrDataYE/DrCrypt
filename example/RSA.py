from drcrypt.crypt import RSA


# with using static keys.
message = "GDO developer."
encryption = RSA(
    text=message,
    public_key=61,
    private_key=53
)
print("Encoded:", encryption.encrypt())
print("Decoded:", encryption.decrypt())

# with using dynamic keys.
encryption = RSA(
    text=message,
    public_key=61,
    private_key=53
)
print("Encoded:", encryption.encrypt())
print("Decoded:", encryption.decrypt())
