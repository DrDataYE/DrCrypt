Using SHA-1 Hashing
===============================

Introduction
------------

In this guide, we'll delve into how to use the SHA-1 hashing functionality provided by the `drcrypt` library. SHA-1 (Secure Hash Algorithm 1) is a widely used cryptographic hash function that produces a fixed-size hash value, typically represented in hexadecimal.

Prerequisites
-------------

Before you start, make sure you have the `drcrypt` library installed. If not, you can install it using the following command:

.. code-block:: shell

   pip install drcrypt

Understanding the Code
----------------------

Let's break down the code snippet you provided and understand each part:

1. **Importing the SHA1 Class:**

   The first line of the code imports the `SHA1` class from the `drcrypt.hash` module. This class provides methods to compute the SHA-1 hash.

   .. code-block:: python

      from drcrypt.hash import SHA1

2. **Creating and Updating the Hash:**

   The code snippet defines a sample data string to hash, which is `"Hello, SHA-1!"`. An instance of the `SHA1` class is created:

   .. code-block:: python

      data = "Hello, SHA-1!"
      sha1_hash = SHA1()

   The `update` method is then used to feed the data into the hash algorithm. Note that the data needs to be encoded to bytes using UTF-8 before being passed to the `update` method:

   .. code-block:: python

      sha1_hash.update(data.encode("utf-8"))

3. **Finalizing the Hash and Getting the Hashed Value:**

   The `finalize` method is called to compute the final hash value based on the data provided:

   .. code-block:: python

      sha1_hash.finalize()

   The hashed value is retrieved in hexadecimal format using the `hexdigest` method:

   .. code-block:: python

      hashed = sha1_hash.hexdigest()

4. **Displaying Results:**

   The following lines print the original data and the computed SHA-1 hash value:

   .. code-block:: python

      print("Data:", data)
      print("SHA-1 Hash:", hashed)

Conclusion
-----------

In this guide, you've learned how to use the SHA-1 hash functionality from the `drcrypt` library. Hashing is commonly used to create a fixed-size representation of data, which is useful for data verification and security purposes.

Feel free to explore more hash functions and cryptographic features provided by the `drcrypt` library!
