import binascii


def string_to_bits(string_representation):
    bits_list = bin(int(binascii.hexlify(bytearray(string_representation, 'utf-8')), 16))[2:]
    return bits_list
