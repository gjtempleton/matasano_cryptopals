from .challenge_2 import hex_xor


def repeating_key_xor(plaintext, key):
    counter = 0
    ciphertext = ''
    for c in plaintext:
        e = hex_xor(bytes.tohex(c), bytes.tohex(key[counter%len(key)]))
        ciphertext += e
        counter += 1
    return ciphertext
