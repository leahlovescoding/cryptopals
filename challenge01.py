from base64 import binascii
from base64 import b64encode

answer01= binascii.unhexlify('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
print (answer01)
answer02 = b64encode(answer01)
print(answer02)
