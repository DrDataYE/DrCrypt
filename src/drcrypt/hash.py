import os
import struct


class SHA256:
    def __init__(self):
        self.buffer = b""
        self.h = [
            0x6A09E667, 0xBB67AE85, 0x3C6EF372, 0xA54FF53A,
            0x510E527F, 0x9B05688C, 0x1F83D9AB, 0x5BE0CD19
        ]

        self.k = [
            0x428A2F98, 0x71374491, 0xB5C0FBCF, 0xE9B5DBA5,
            0x3956C25B, 0x59F111F1, 0x923F82A4, 0xAB1C5ED5,
            0xD807AA98, 0x12835B01, 0x243185BE, 0x550C7DC3,
            0x72BE5D74, 0x80DEB1FE, 0x9BDC06A7, 0xC19BF174,
            0xE49B69C1, 0xEFBE4786, 0x0FC19DC6, 0x240CA1CC,
            0x2DE92C6F, 0x4A7484AA, 0x5CB0A9DC, 0x76F988DA,
            0x983E5152, 0xA831C66D, 0xB00327C8, 0xBF597FC7,
            0xC6E00BF3, 0xD5A79147, 0x06CA6351, 0x14292967,
            0x27B70A85, 0x2E1B2138, 0x4D2C6DFC, 0x53380D13,
            0x650A7354, 0x766A0ABB, 0x81C2C92E, 0x92722C85,
            0xA2BFE8A1, 0xA81A664B, 0xC24B8B70, 0xC76C51A3,
            0xD192E819, 0xD6990624, 0xF40E3585, 0x106AA070,
            0x19A4C116, 0x1E376C08, 0x2748774C, 0x34B0BCB5,
            0x391C0CB3, 0x4ED8AA4A, 0x5B9CCA4F, 0x682E6FF3,
            0x748F82EE, 0x78A5636F, 0x84C87814, 0x8CC70208,
            0x90BEFFFA, 0xA4506CEB, 0xBEF9A3F7, 0xC67178F2
        ]

    def right_rotate(self, x, c):
        return (x >> c) | (x << (32 - c))

    def process_block(self, block):
        w = list(struct.unpack(">16I", block)) + [0] * 48

        for i in range(16, 64):
            s0 = self.right_rotate(w[i - 15], 7) ^ self.right_rotate(w[i - 15], 18) ^ (w[i - 15] >> 3)
            s1 = self.right_rotate(w[i - 2], 17) ^ self.right_rotate(w[i - 2], 19) ^ (w[i - 2] >> 10)
            w[i] = (w[i - 16] + s0 + w[i - 7] + s1) & 0xFFFFFFFF

        a, b, c, d, e, f, g, h = self.h

        for i in range(64):
            s0 = self.right_rotate(a, 2) ^ self.right_rotate(a, 13) ^ self.right_rotate(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            t2 = (s0 + maj) & 0xFFFFFFFF
            s1 = self.right_rotate(e, 6) ^ self.right_rotate(e, 11) ^ self.right_rotate(e, 25)
            ch = (e & f) ^ ((~e) & g)
            t1 = (h + s1 + ch + self.k[i] + w[i]) & 0xFFFFFFFF

            h = g
            g = f
            f = e
            e = (d + t1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (t1 + t2) & 0xFFFFFFFF

        self.h[0] = (self.h[0] + a) & 0xFFFFFFFF
        self.h[1] = (self.h[1] + b) & 0xFFFFFFFF
        self.h[2] = (self.h[2] + c) & 0xFFFFFFFF
        self.h[3] = (self.h[3] + d) & 0xFFFFFFFF
        self.h[4] = (self.h[4] + e) & 0xFFFFFFFF
        self.h[5] = (self.h[5] + f) & 0xFFFFFFFF
        self.h[6] = (self.h[6] + g) & 0xFFFFFFFF
        self.h[7] = (self.h[7] + h) & 0xFFFFFFFF

    def update(self, data):
        self.buffer += data
        while len(self.buffer) >= 64:
            self.process_block(self.buffer[:64])
            self.buffer = self.buffer[64:]

    def finalize(self):
        message_length = len(self.buffer)
        bit_length = message_length * 8

        self.buffer += b"\x80"
        while len(self.buffer) % 64 != 56:
            self.buffer += b"\x00"

        self.buffer += struct.pack(">Q", bit_length)

        while len(self.buffer) > 0:
            self.process_block(self.buffer[:64])
            self.buffer = self.buffer[64:]

    def hexdigest(self):
        return "".join(f"{x:08x}" for x in self.h)

    def compare_hash(self, data, target_hash):
        self.update(data.encode("utf-8"))
        self.finalize()
        hashed = self.hexdigest()

        return hashed == target_hash

class SHA1:
    'SHA-1 (Secure Hash Algorithm 1)'
    def __init__(self):
        self.buffer = b""
        self.h = [
            0x67452301,
            0xEFCDAB89,
            0x98BADCFE,
            0x10325476,
            0xC3D2E1F0
        ]

    def left_rotate(self, x, c):
        return (x << c) | (x >> (32 - c))

    def process_block(self, block):
        w = list(struct.unpack(">16I", block)) + [0] * 64

        for i in range(16, 80):
            w[i] = self.left_rotate(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1)

        a, b, c, d, e = self.h

        for i in range(80):
            if i < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif i < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif i < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (self.left_rotate(a, 5) + f + e + k + w[i]) & 0xFFFFFFFF
            e = d
            d = c
            c = self.left_rotate(b, 30)
            b = a
            a = temp

        self.h[0] = (self.h[0] + a) & 0xFFFFFFFF
        self.h[1] = (self.h[1] + b) & 0xFFFFFFFF
        self.h[2] = (self.h[2] + c) & 0xFFFFFFFF
        self.h[3] = (self.h[3] + d) & 0xFFFFFFFF
        self.h[4] = (self.h[4] + e) & 0xFFFFFFFF

    def update(self, data):
        self.buffer += data
        while len(self.buffer) >= 64:
            self.process_block(self.buffer[:64])
            self.buffer = self.buffer[64:]

    def finalize(self):
        message_length = len(self.buffer)
        padded_data = self.buffer + b"\x80" + (b"\x00" * ((56 - message_length) % 64))

        message_bit_length = len(self.buffer) * 8
        padded_data += struct.pack(">Q", message_bit_length)

        self.update(padded_data)

    def hexdigest(self):
        return "".join(f"{x:08x}" for x in self.h)

    def compare_hash(self, data, target_hash):
        self.update(data.encode("utf-8"))
        self.finalize()
        hashed = self.hexdigest()

        return hashed == target_hash

class MD5:
    'MD5 (Message-Digest Algorithm 5)'
    def __init__(self):
        self.buffer = b""
        self.h = [
            0x67452301,
            0xEFCDAB89,
            0x98BADCFE,
            0x10325476
        ]

        self.k = [
            0x00000000, 0xd76aa478, 0xe8c7b756, 0x242070db,
            0xc1bdceee, 0xf57c0faf, 0x4787c62a, 0xa8304613,
            0xfd469501, 0x698098d8, 0x8b44f7af, 0xffff5bb1,
            0x895cd7be, 0x6b901122, 0xfd987193, 0xa679438e,
            0x49b40821, 0xf61e2562, 0xc040b340, 0x265e5a51,
            0xe9b6c7aa, 0xd62f105d, 0x02441453, 0xd8a1e681,
            0xe7d3fbc8, 0x21e1cde6, 0xc33707d6, 0xf4d50d87,
            0x455a14ed, 0xa9e3e905, 0xfcefa3f8, 0x676f02d9,
            0x8d2a4c8a, 0xfffa3942, 0x8771f681, 0x6d9d6122,
            0xfde5380c, 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60,
            0xbebfbc70, 0x289b7ec6, 0xeaa127fa, 0xd4ef3085,
            0x04881d05, 0xd9d4d039, 0xe6db99e5, 0x1fa27cf8,
            0xc4ac5665, 0xf4292244, 0x432aff97, 0xab9423a7,
            0xfc93a039, 0x655b59c3, 0x8f0ccc92, 0xffeff47d,
            0x85845dd1, 0x6fa87e4f, 0xfe2ce6e0, 0xa3014314,
            0x4e0811a1, 0xf7537e82, 0xbd3af235, 0x2ad7d2bb,
            0xeb86d391
        ]

    def left_rotate(self, x, c):
        return (x << c) | (x >> (32 - c))

    def process_block(self, block):
        a, b, c, d = self.h
        x = list(struct.unpack("<16I", block))

        # Round 1
        for i in range(16):
            f = (b & c) | ((~b) & d)
            g = i
            temp = d
            d = c
            c = b
            b = b + self.left_rotate((a + f + self.k[i] + x[g]) & 0xFFFFFFFF, 7)
            a = temp

        self.h[0] = (self.h[0] + a) & 0xFFFFFFFF
        self.h[1] = (self.h[1] + b) & 0xFFFFFFFF
        self.h[2] = (self.h[2] + c) & 0xFFFFFFFF
        self.h[3] = (self.h[3] + d) & 0xFFFFFFFF

    def update(self, data):
        self.buffer += data
        while len(self.buffer) >= 64:
            self.process_block(self.buffer[:64])
            self.buffer = self.buffer[64:]

    def finalize(self):
        message_length = len(self.buffer)
        padded_data = self.buffer + b"\x80" + (b"\x00" * ((56 - message_length) % 64))

        message_bit_length = len(self.buffer) * 8
        padded_data += struct.pack("<Q", message_bit_length)

        self.update(padded_data)

    def hexdigest(self):
        return "".join(f"{x:02x}" for x in self.h)

def compare_hash(md5_hash, data, target_hash):
    md5_hash.update(data.encode("utf-8"))
    md5_hash.finalize()
    hashed = md5_hash.hexdigest()
    print(hashed)
    return hashed == target_hash

class Bcrypt:
    def __init__(self, rounds=10):
        self.rounds = rounds
    
    def generate_salt(self):
        return os.urandom(16)
    
    def bytes_to_int(self, b):
        return int.from_bytes(b, byteorder="big")
    
    def int_to_bytes(self, n):
        return n.to_bytes((n.bit_length() + 7) // 8, byteorder="big")
    
    def bcrypt_hash(self, password, salt):
        key = password.encode()
        blocks = [0] * 18
        
        for i in range(8):
            blocks[i] = self.bytes_to_int(salt[i * 4 : i * 4 + 4])
        for i in range(len(key) // 4 + 1):
            blocks[i + 8] = self.bytes_to_int(key[i * 4 : i * 4 + 4])
        
        # تنفيذ تشفير Blowfish هنا
        
        result = b"".join([self.int_to_bytes(blocks[i]) for i in range(6)])
        
        return result
    
    def verify_password(self, entered_password, hashed_password):
        salt = hashed_password[:16]
        return hashed_password == self.bcrypt_hash(entered_password, salt)



