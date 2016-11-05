import base64


def hex_to_b64(hex_string):
    bytes_version = bytes.fromhex(hex_string)
    b64string = base64.b64encode(bytes_version).decode()
    return b64string


def main():
    print(hex_to_b64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))

if __name__ == "__main__": main()