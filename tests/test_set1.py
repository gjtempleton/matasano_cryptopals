from set1.challenge_1 import hex_to_b64
from set1.challenge_2 import xor
from set1.challenge_3 import single_byte_xor_reverse

CHAL_1_INPUT = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
CHAL_1_OUTPUT = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

CHAL_2_INPUT_1 = '1c0111001f010100061a024b53535009181c'
CHAL_2_INPUT_2 = '686974207468652062756c6c277320657965'
CHAL_2_OUTPUT = '746865206b696420646f6e277420706c6179'

CHAL_3_INPUT = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
CHAL_3_OUTPUT = ''

def test_challenge_1():
    assert hex_to_b64(CHAL_1_INPUT) == CHAL_1_OUTPUT

def test_challenge_2():
    assert xor(CHAL_2_INPUT_1, CHAL_2_INPUT_2) == CHAL_2_OUTPUT

def test_challenge_3():
    assert single_byte_xor_reverse(CHAL_3_INPUT) == CHAL_3_INPUT

