# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:15:30 2024

@author: rnmic
"""


import unittest
import string
import random
from Caesar_Cipher import encrypt, decrypt, rotate


class CipherTestCase(unittest.TestCase):
    def test_cipher_with_random_data(self):
        key = random.randint(1, 100)

        l = string.ascii_letters
        d = string.digits

        msg = ''.join(random.choice(l)for i in range(10)) + \
            ''.join(random.choice(d)for i in range(10))

        encrypt_msg = encrypt(key, msg)
        decrypt_msg = decrypt(key, encrypt_msg)

        print('* * * * * * * * * *')
        print(f'key: {key}')
        print(f'message: {msg}')
        print(f'encrypted message: {encrypt_msg}')
        print(f'decrypted message: {decrypt_msg}')

        self.assertEqual(decrypt_msg, msg)


    def test_does_rotate_work(self):
        standard_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        key = -68

        alphabet_for_encrypt = rotate(key)
        print(f'New alphabet: {alphabet_for_encrypt}')

        self.assertNotEqual(standard_alphabet, alphabet_for_encrypt)


    def test_broken_case(self):
        key = 68
        msg = 'Is it broken?'

        encrypt_msg = encrypt(key, msg)
        decrypt_msg = decrypt(key, encrypt_msg)

        self.assertEqual(msg, decrypt_msg)


if __name__ == '__main__':
    unittest.main()
