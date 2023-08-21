Using AES Encryption
==================================

Introduction
------------

In this guide, we'll explore how to use AES encryption and decryption functions from the `drcrypt` library. AES (Advanced Encryption Standard) is a widely used symmetric encryption algorithm that provides strong security for sensitive data.

Prerequisites
-------------

Before you begin, make sure you have the `drcrypt` library installed. If not, you can install it using the following command:

.. code-block:: shell

   pip install drcrypt

Understanding the Code
----------------------

Let's break down the code snippet you provided and understand each part:

1. **Importing the Encryption and Decryption Functions:**

   The first line of the code imports the `encrypt_aes` and `decrypt_aes` functions from the `drcrypt.crypt` module. These functions provide AES encryption and decryption capabilities.

   .. code-block:: python

      from drcrypt.crypt import encrypt_aes, decrypt_aes

2. **Using AES Encryption:**

   The code snippet defines a sample AES encryption scenario. A secret "key" is created by encoding the string `"MyTestPassword!!"` as bytes in UTF-8 format. The text to be encrypted is `"Hello, world"`.

   .. code-block:: python

      key = "MyTestPassword!!".encode("utf-8")
      text = "Hello, world"
      en = encrypt_aes(text, key)

   The `en` variable holds the encrypted data.

3. **Displaying Results:**

   The following lines print the original text, the encrypted data (decoded from bytes to UTF-8), and the decrypted text (decoded from bytes to UTF-8) after performing decryption:

   .. code-block:: python

      print("Original Text:", text, end="\n\n")
      print("Encrypted Text:", en.decode("utf-8"))
      print("Decrypted Text:", decrypt_aes(en, key).decode("utf-8"))

Conclusion
-----------

In this guide, you've learned how to use AES encryption and decryption functions from the `drcrypt` library. AES is a strong encryption algorithm that is widely used to secure sensitive information. Remember to keep your encryption keys secure to ensure the safety of your encrypted data.

Feel free to explore more features of the `drcrypt` library and different encryption scenarios!
