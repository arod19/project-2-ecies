Project #2: ECIES

- Description:
A command line python program that asks the user if he/she wants
to decrypt or encrypt a file using elliptic curves and chacha poly.

- Features:
It features elliptic curve public and private key generation and chacha poly algorithm use to eother encrypt or decrypt a file.

- Python Version:
3.6.3

- Libraries used:
1. os: This module provides a portable way of using operating system dependent functionality. Generated random nonce in the program.
2. argparse: The argparse module makes it easy to write user-friendly command-line interfaces.
3. fastecdsa: elliptic curve generation of key pairs.
4. chacha20poly1305: use of chacha poly algorithm.

The reason for the implementation of these libraries are that they were required in order to accomplish the requirements of the assignments.

- Command line help:
. Must have either -d (to decrypt the file) or -e (to encrypt the file) as the first flag, then at the end, input the file of the plain text or encrypted text.
Note: It must be in the same directory as the python file.

- References:
1. https://pypi.org/project/chacha20poly1305/
2. https://www.ayrx.me/python-aead
3. https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ec/
4. https://github.com/AntonKueltz/fastecdsa#generating-keys
5. https://stackoverflow.com/questions/5552555/unicodedecodeerror-invalid-continuation-byte
