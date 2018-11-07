"""
Angel Rodriguez

Project #2: ECIES

A command line python program that asks the user if he/she wants
to decrypt or encrypt a file using elliptic curves and chacha poly.

7 November 2018
"""
import os
from chacha20poly1305 import ChaCha20Poly1305
from fastecdsa import keys, curve
import argparse

#program description
parser = argparse.ArgumentParser(description="encrypt or decrypt a file using elliptic curves and chacha poly.")


#first group, to either decrypt or encrypt
group = parser.add_mutually_exclusive_group()
group.add_argument("-d", "--decrypt", action="store_true")
group.add_argument("-e", "--encrypt", action="store_true")

# for the file
parser.add_argument("filename", type=str, help="file")

args = parser.parse_args()

with open(args.filename) as file:
    text = file.read()

#creates a random nonce from the system
nonce = os.urandom(12)

#generates both a private and a public key
key, pub_key = keys.gen_keypair(curve.P256)

#converts that key intro a string and chops it to 32 characters
key = str(key)
key = key[0:32]

#encodes the key
encoded = str.encode(key)

#uses ChaCha20Poly1305 algorithm on it
cip = ChaCha20Poly1305(encoded)

#encrypts and saves in cipthertext variable
ciphertext = cip.encrypt(nonce, str.encode(text).strip())

def encrypt():
    #opens a file and saves the cipthertext
    f = open('my_file', 'wb')
    binary_format = bytearray(ciphertext)
    f.write(binary_format)
    f.close()
    print(ciphertext)

def decrypt():
    #decrypts the ciphertext into plaintext
    plaintext = cip.decrypt(nonce, text)
    print(plaintext.decode())

#user's choice on either decrypt or encrypt a file
if args.encrypt:
    encrypt()
else:
    decrypt()
