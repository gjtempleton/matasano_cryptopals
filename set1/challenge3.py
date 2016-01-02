import binascii
from challenge2 import fixed_xor
from itertools import cycle
# Source: http://www.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
REL_ENG_CHAR_FREQS = {
    'E': .1202,
    'T': .0910,
    'A': .0812,
    'O': .0768,
    'I': .0731,
    'N': .0695,
    'S': .0628,
    'R': .0602,
    'H': .0592,
    'D': .0432,
    'L': .0398,
    'U': .0288,
    'C': .0271,
    'M': .0261,
    'F': .0230,
    'Y': .0211,
    'W': .0209,
    'G': .0203,
    'P': .0182,
    'B': .0149,
    'V': .0111,
    'K': .0069,
    'X': .0017,
    'Q': .0011,
    'J': .0010,
    'Z': .0007
}

def single_byte_xor_reverse(hex_string):
    diff_score = 10000
    result = ""
    keyrange = [[byte] for byte in range(0, 255)]
    for key in keyrange:
        string, new_score = _score_key(hex_string, key)
        if new_score < diff_score:
            diff_score = new_score
            result = ""
    return result


def _score_key(byte_string, key):
    xored = fixed_xor(byte_string, cycle(binascii.b2a_hex(key)))

def main():
    print(single_byte_xor_reverse('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))


if __name__ == "__main__":
    main()
