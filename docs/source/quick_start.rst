Quick Start Guide: Using XOR Encryption with drcrypt
====================================================

Introduction
------------

This quick start guide demonstrates how to use the XOR encryption provided by the `drcrypt` library to encrypt and decrypt text. We'll show you a simple example using Python code.

Prerequisites
-------------

Before you begin, make sure you have the `drcrypt` library installed. You can install it using the following command:

.. code-block:: shell

   pip install drcrypt

Getting Started
---------------

Follow the steps below to encrypt and decrypt text using XOR encryption:

1. **Import the XOR Class:**

   In your Python code, start by importing the `XOR` class from the `drcrypt.crypt` module:

   .. code-block:: python

      from drcrypt.crypt import XOR

2. **Encrypting and Decrypting Text:**

   Define the text you want to encrypt. For example, let's use the text "Hello, World". Then, create an instance of the `XOR` class with a password and text encoding:

   .. code-block:: python

      text = "Hello, World"
      xor = XOR("MyPassword", "utf-8")

   Use the `encrypt` method to encrypt the text:

   .. code-block:: python

      en = xor.encrypt(text)

   You can now print the original text, the encrypted text, and decrypt the encrypted text to get the original text back:

   .. code-block:: python

      print("Original Text:", text, end="\n\n")
      print("Encrypted Text:", en)
      print("Decrypted Text:", xor.decrypt(en))

Summary
-------

You've successfully learned how to use XOR encryption with the `drcrypt` library to secure your text data. This is a simple example, and you can explore more advanced features of the library for more complex scenarios.
