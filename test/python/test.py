# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:15:30 2024

@author: rnmic
"""


import unittest
import string
import random
from cipher import encrypt, decrypt


class CipherTestCase(unittest.TestCase):
    def test_cipher_with_random_data(self):
        s = random.randint(1, 100)

        l = string.ascii_letters
        d = string.digits

        m = ''.join(random.choice(l)for i in range(10)) + \
            ''.join(random.choice(d)for i in range(10))

        enc_outcome = encrypt(m, s)
        dec_outcome = decrypt(enc_outcome, s)

        self.assertEqual(dec_outcome, m)


    def test_the_entire_alphabet(self):
        s = random.randint(1, 200)
        m = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

        enc_outcome = encrypt(m, s)
        dec_outcome = decrypt(enc_outcome, s)

        self.assertEqual(m, dec_outcome)


if __name__ == '__main__':
    unittest.main()
