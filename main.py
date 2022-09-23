
import math
import random

g = 666
p = 6661
m = 2000
bob_private_key = 66
bob_public_key = 2227

# 1
def bruteforce_x():
    for i in range (1, 241):
        pk = 666 ** i % p
        if pk == 2227:
            print("Found x: " + str(i))
            return i

# 1
def encrypt_message(message):
    pk = bob_public_key

    r = random.randint(1, 1000)
    c1 = g**r
    c2 = message * ((pk**r) % p)
    c = (c1, c2)
    return c

# 2
def decrypt_message():
    c1, c2 = encrypt_message(m)
    decrypted = c2 / (c1 ** (bob_private_key) % p)
    return decrypted


#
def change_message_to(changed):
    return encrypt_message(changed)


def main():
    # assignment 1
    #bruteforce_x()
    #encrypt_message(2000)

    # assignment 2
    #decrypt_message()

    # assignment 3
    #Encrypt the message 2000 to bob
    alice_to_bob_encrypted = encrypt_message(2000)

    # Catch Alice's message and change it to 6000 using bobs public key
    alice_to_bob_encrypted = change_message_to(6000)

    # deconstruct ciphertext c1 & c2
    mallory_c1, mallory_c2 = alice_to_bob_encrypted

    # Bob receives the message and decrypts it. He gets 6000
    decrypted = mallory_c2 / (mallory_c1 ** (bob_private_key) % p)
    print(str(decrypted))



main()
#decrypt_message()
#encrypt_message()
#bruteforce_x()
