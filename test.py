# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:15:30 2024

@author: rnmic
"""


import unittest
import string
import random
from Caesar_Cipher import encrypt, decrypt


class GetExifTestCase(unittest.TestCase):
    def test_cipher_with_random_data(self):
        key = random.randint(1, 100)
        
        l = string.ascii_letters
        d = string.digits
        
        msg = ''.join(random.choice(l)for i in range(10)) + ''.join(random.choice(d)for i in range(10))
        
        encrypt_msg = encrypt(key, msg)
        decrypt_msg = decrypt(key, encrypt_msg)
        
        print('* * * * * * * * * *')
        print(f'key: {key}')
        print(f'message: {msg}')
        print(f'encrypted message: {encrypt_msg}')
        print(f'decrypted message: {decrypt_msg}')
        
        self.assertEqual(decrypt_msg, msg)
        
        
if __name__ == '__main__':
    unittest.main()
    
    
        