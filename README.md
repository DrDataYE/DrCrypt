# DrCrypt - Python Encryption Library

![PyPI](https://img.shields.io/pypi/v/drcrypt)
![License](https://img.shields.io/pypi/l/drcrypt)

DrCrypt is a Python encryption library that provides various cryptographic functions for your projects. It aims to simplify encryption tasks and provide a user-friendly interface for common encryption algorithms.

## Installation

You can install `DrCrypt` using pip:

```bash
pip install drcrypt
```

## Features

- Easy-to-use API for common encryption tasks.
- Supports various encryption algorithms, including MD5, SHA-256, SHA-3, and more.
- Provides functions for generating random strings and hashes.
- Well-documented and user-friendly interface.

## Usage

Here's a quick example of how to use `DrCrypt` to hash a password:

```python
from drcrypt import MD5Hash

password = "mysecretpassword"
hasher = MD5Hash()
hashed_password = hasher.hash_password(password)

print("Original Password:", password)
print("Hashed Password:", hashed_password)

if hasher.verify_password("mysecretpassword", hashed_password):
    print("Password Matched!")
else:
    print("Password Does Not Match!")
```

## Documentation

For detailed documentation and examples, please refer to the [official documentation](https://your-docs-link-here).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
