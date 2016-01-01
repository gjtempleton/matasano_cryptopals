import binascii


def fixed_xor(string1, string2):
    if not len(string1) == len(string2):
        raise Exception
    string1_bytes = bytes.fromhex(string1)
    string2_bytes = bytes.fromhex(string2)
    xored_bytes = bytes([b1 ^ b2 for b1, b2 in zip(string1_bytes, string2_bytes)])
    xored_hex = binascii.b2a_hex(xored_bytes).decode()
    return xored_hex

def main():
    print(fixed_xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965'))

if __name__ == "__main__":
    main()