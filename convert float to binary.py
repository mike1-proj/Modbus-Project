import struct
""" this code will convert a floating point value into a Binary equivalent value quite neat code for conversion"""
# 032b formats output as a 32-bit binary string
n = 4.725
output = struct.unpack('!I', struct.pack('!f', n))[0]
print(f"{output:032b}")
