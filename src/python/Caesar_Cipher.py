# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:16:42 2024

@author: rnmic
"""

import argparse
import traceback


alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def rotate(c, s): return (alphabet.index(c) + s) % len(alphabet)


def msg_processing(msg, shift):
    outcome = ''
    for c in msg:
        if c in alphabet:
            enc = alphabet[rotate(c, shift)]
            outcome += enc
        else:
            outcome += c
    return outcome


def encrypt(msg, shift):
    outcome = msg_processing(msg, shift)
    return outcome


def decrypt(msg, shift):
    shift = -shift
    outcome = msg_processing(msg, shift)
    return outcome


def main(todo, msg, shift):
    if len(msg) < 1:
        print("Nothing to do here. There is no message!")
        return
    try:
        if todo == 'toencrypt':
            outcome = encrypt(msg, shift)
            print(outcome)
        else:
            outcome = decrypt(msg, shift)
            print(outcome)

    except Exception:
        traceback.print_exc()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--todo', type=str, choices=['todecrypt'], default='toencrypt',
                        help='If you want to decrypt a message type --todo "todecrypt".')
    parser.add_argument('--m', type=str, default="")
    parser.add_argument('--k', type=int, default=0)
    args = parser.parse_args()

    main(args.todo, args.m, args.k)
