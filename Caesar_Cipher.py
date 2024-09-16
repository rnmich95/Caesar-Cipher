# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:47:19 2024

@author: rnmic
"""

import argparse
import traceback


def rotate(shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    n_alphabet = ''

    if shift < len(alphabet):
        n_alphabet = alphabet[-shift:] + alphabet[:-shift]
    else:
        shift = shift % len(alphabet)
        # print(f'Shift: {shift}')
        n_alphabet = alphabet[-shift:] + alphabet[:-shift]
        # print(f'Alphabet: {n_alphabet}')

    return n_alphabet
# print(rotate(-89))
# print(rotate(92))
# print(rotate(76))


def new_message(n_alphabet, message, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    n_message = ""

    if n_alphabet == alphabet:
        alphabet = rotate(-shift)

    for x in message:
        if x in alphabet:
            index = alphabet.index(x)
            n_message += n_alphabet[index]

        else:
            n_message += x
    return n_message


def encrypt(key, message):
    n_alphabet = rotate(key)
    n_message = new_message(n_alphabet, message, key)

    return n_message
# print(encrypt(89, 'helloo'))
# print(encrypt(92, 'helloo'))
# print(encrypt(39, 'helloo'))


def decrypt(key, message):
    key = -key
    n_message = encrypt(key, message)

    return n_message
# print(decrypt(89, 'QNUUXX'))
# print(decrypt(92, 'NKRRUU'))
# print(decrypt(39, 'EBIILL'))


def main(todo, key, message):
    if len(message) < 1:
        print("Nothing to do here. There is no message!")
        return
    try:
        if todo == 'encrypt':
            n_message = encrypt(key, message)
            print(n_message)
        else:
            n_message = decrypt(key, message)
            print(n_message)

    except Exception:
        traceback.print_exc()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--todo', type=str, choices=['decrypt'], default='encrypt',
                        help='If you want to decrypt a message type "--todo decrypt".')
    parser.add_argument('--key', type=int, default=0)
    parser.add_argument('--msg', type=str, default="")
    args = parser.parse_args()

    main(args.todo, args.key, args.msg)
