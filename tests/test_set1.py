from set1.challenge_1 import hex_to_b64
from set1.challenge_2 import hex_xor
from set1.challenge_3 import single_byte_xor_reverse
from set1.challenge_5 import repeating_key_xor
from set1.challenge_6 import hanning_distance

CHAL_1_INPUT = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
CHAL_1_OUTPUT = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

CHAL_2_INPUT_1 = '1c0111001f010100061a024b53535009181c'
CHAL_2_INPUT_2 = '686974207468652062756c6c277320657965'
CHAL_2_OUTPUT = '746865206b696420646f6e277420706c6179'

CHAL_3_INPUT = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
CHAL_3_OUTPUT = ''

CHAL_4_INPUT = None
CHAL_4_OUTPUT = None

CHAL_5_PLAINTEXT = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
CHAL_5_KEY = 'ICE'
CHAL_5_OUTPUT = '''0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a2622632427276
5272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'''


def test_challenge_1():
    assert hex_to_b64(CHAL_1_INPUT) == CHAL_1_OUTPUT


def test_challenge_2():
    assert hex_xor(CHAL_2_INPUT_1, CHAL_2_INPUT_2) == CHAL_2_OUTPUT


def test_challenge_3():
    assert single_byte_xor_reverse(CHAL_3_INPUT) == CHAL_3_INPUT


def test_challenge_4():
    pass


def test_challenge_5():
    assert repeating_key_xor(CHAL_5_PLAINTEXT, CHAL_5_KEY) == CHAL_5_OUTPUT


def test_challenge_6():
    pass


def test_hanning_distance():
    assert hanning_distance("this is a test", "wokka wokka!!!") == 37


def test_challenge_7():
    pass


def test_challenge_8():
    pass
