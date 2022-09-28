
import math
import random

g = 666
p = 6661
m = 2000
bob_private_key = 66
bob_public_key = 2227


# 1
def encrypt_message(message):
    pk = bob_public_key

    r = random.randint(1, 6661)
    c1 = (g**r) % p
    c2 = message * ((pk**r) % p)
    c = (c1, c2)
    return c

# 2
def bruteforce_x():
    for i in range (1, 241):
        pk = 666 ** i % p
        if pk == 2227:
            print("Found x: " + str(i))
            return i

# 2
def decrypt_message():
    c1, c2 = encrypt_message(m)
    decrypted = c2 / (c1 ** (bob_private_key) % p)
    return decrypted


def main():
    # assignment 1
    print("Assignment 1")
    print(encrypt_message(2000))
    print()

    # assignment 2
    print("Assignment 2")
    bruteforce_x()
    print(decrypt_message())
    print()

    # assignment 3
    print("Assignment 3")
    # Encrypt the message 2000 to bob
    alice_to_bob_encrypted = encrypt_message(2000)

    # Catch Alice's message and change it to 6000 by multiplying with 3
    # deconstruct ciphertext c1 & c2
    mallory_c1, mallory_c2 = alice_to_bob_encrypted
    mallory_c2 = mallory_c2 * 3

    alice_to_bob_encrypted = (mallory_c1, mallory_c2);

    # Bob receives the message and decrypts it. He gets 6000
    decrypted = mallory_c2 / (mallory_c1 ** (bob_private_key) % p)
    print(str(decrypted))



main()
#decrypt_message()
#encrypt_message()
#bruteforce_x()
