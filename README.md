Project #2: ECIES

- Description:
A command line python program that asks the user if he/she wants
to decrypt or encrypt a file using elliptic curves and chacha poly.

- Features:
It features elliptic curve public and private key generation and chacha poly algorithm use to eother encrypt or decrypt a file.

- Python Version:
3.6.3

- Libraries used:
argparse: The argparse module makes it easy to write user-friendly command-line interfaces.
fastecdsa: elliptic curve generation of key pairs.
chacha20poly1305: use of chacha poly algorithm.

The reason for the implementation of these libraries are that they were required in order to accomplish the requirements of the assignments.

- Command line help:
. Must have either -d (to decrypt the file) or -e (to encrypt the file) as the first flag, then at the end, input the file of the plain text or encrypted text.
Note: It must be in the same directory as the python file.

- References:
1. "Elements of Cryptanalysis" by William F. Friedman
2. "Serious Cryptography" by Jean-Philippe Aumasson
3. Marcus Chong during TA office hours.
