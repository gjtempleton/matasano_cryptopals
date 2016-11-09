from .utils import string_to_bits


def break_repeating_key_xor(ciphertext):
    return ""

def hanning_distance(string1, string2):
    if len(string2) != len(string1):
        raise Exception("Two strings must be the same length")
    hanning_distance_score = 0
    i = 0
    string1_bits = string_to_bits(string1)
    string2_bits = string_to_bits(string2)
    print("{} rgikthrrgkghuk    {}".format(len(string1_bits), len(string2_bits)))
    while i < len(string1_bits):
        # print(i)
        # print(string1_bits[i])
        if string1_bits[i] != string2_bits[i]:
            hanning_distance_score += 1
        i += 1
    return hanning_distance_score



