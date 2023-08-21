Using XOR Encryption
==================================

Introduction
------------

Welcome to this guide that will introduce you to XOR encryption using the `drcrypt` library. XOR encryption is a simple method for securing data using a "password." In this guide, you'll see a step-by-step explanation of how to use it.

Prerequisites
-------------

Before you start, make sure you have the `drcrypt` library installed. If not, you can install it using the following command:

.. code-block:: shell

   pip install drcrypt

Understanding the Code
----------------------

Let's break down the code snippet you provided and understand each part:

1. **Importing the XOR Class:**

   The first line of the code imports the `XOR` class from the `drcrypt.crypt` module. This class provides methods for XOR encryption and decryption.

   .. code-block:: python

      from drcrypt.crypt import XOR

2. **Encrypting the Text:**

   Next, we define a sample text to encrypt, which is "Hello, World." We then create an instance of the `XOR` class by providing a "password" and specifying the text encoding (UTF-8 in this case).

   .. code-block:: python

      text = "Hello, World"
      xor = XOR("MyPassword", "utf-8")

   The `xor` instance is now ready to perform encryption and decryption operations.

3. **Encrypting and Decrypting:**

   The following lines perform the encryption. We use the `encrypt` method of the `xor` instance to encrypt the given text.

   .. code-block:: python

      en = xor.encrypt(text)

   After encryption, we print the original text, the encrypted text, and finally, we decrypt the encrypted text back to its original form:

   .. code-block:: python

      print("Original Text:", text, end="\n\n")
      print("Encrypted Text:", en)
      print("Decrypted Text:", xor.decrypt(en))

Conclusion
-----------

In this guide, you've learned how to use XOR encryption with the `drcrypt` library. Although XOR encryption is simple, it's important to note that it's not suitable for high-security applications. It's a starting point for understanding encryption concepts.

Feel free to explore the `drcrypt` library further and experiment with different encryption methods and scenarios!
