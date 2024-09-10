# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:47:19 2024

@author: rnmic
"""

import argparse
import traceback


def new_alphabet(shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    n_alphabet = ""
    
    for x in alphabet:
        index = alphabet.index(x)+shift
        
        if index < len(alphabet):
            n_alphabet += alphabet[index]
        else:
            index = index%len(alphabet)
            n_alphabet += alphabet[index]
            
    return n_alphabet


def new_message(n_alphabet,message,shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    n_message = ""
    
    # message = message.lower()
    
    for x in message:
        if x in alphabet:
            index = alphabet.index(x)
            n_message += n_alphabet[index]
        else:
            if x != " ":
                ascii_code = ord(x) + shift
                x = chr(ascii_code)
                n_message += x
            else:
                n_message += x
    return n_message


def encrypt(key,message):
    n_alphabet = new_alphabet(key)
    n_message = new_message(n_alphabet,message,key)

    return n_message

   
def main(key,message):
    if len(message) < 1:
        print("Nothing to do here. There is no message!")
        return 
    try:
        n_message = encrypt(key,message)  
        print(n_message)
        
    except Exception:
        traceback.print_exc()   
       
           
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()  
    parser.add_argument('--key', type=int, default=0)
    parser.add_argument('--msg', type=str, default="")
    args = parser.parse_args()
    
    main(args.key,args.msg)




            
    