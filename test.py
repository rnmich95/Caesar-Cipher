# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:15:30 2024

@author: rnmic
"""

import unittest
from Caesar_Cipher import new_alphabet,new_message,encrypt

class GetExifTestCase(unittest.TestCase):
    def test_new_alphabet(self):
        self.assertEqual(new_alphabet(5),
                         'fghijklmnopqrstuvwxyzabcde')
    
    def test_new_message(self):
        alphabet = 'jklmnopqrstuvwxyzabcdefghi'
        message = 'Qualcuno che la sa lunga mi spieghi questo mistero:'
        
        self.assertEqual(new_message(alphabet,message,9),
                         'Zdjuldwx lqn uj bj udwpj vr byrnpqr zdnbcx vrbcnaxC')

    def test_encrypt(self):
        message = 'Zdjuldwx lqn uj bj udwpj vr byrnpqr zdnbcx vrbcnaxC'
        
        self.assertEqual(encrypt(-9,message),
                         'Qualcuno che la sa lunga mi spieghi questo mistero:')
if __name__ == '__main__':
    unittest.main()
        