""" this is the full IEEE-754 floating point conversion steps process to produce a binary value from a floating point value"""
n = 9.87
#If n is greater than 0, sign is assigned as 0 else as 1
sign = '0' if n >= 0 else '1'
n= abs(n)

# Getting integer and fractional parts
int_part = int(n)
frac_part = n - int_part

# convert integer part to binary
int_bin = bin(int_part)[2:]

# convert fractional part to binary
frac_bin = []
while frac_part and len(frac_bin) < 23:
    frac_part *= 2
    bit = int(frac_part)
    frac_bin.append(str(bit))
    frac_part -= bit

# normalize
exponent = len(int_bin) - 1
mantissa = int_bin[1:] + ''.join(frac_bin)

# adjust mantissa to 23 bits
mantissa = (mantissa + '0' * 23)[:23]

# exponent with bias (127)
exponent_bin = f"{exponent + 127:08b}"

# IEEE 754 Binary Representation
output = sign + exponent_bin + mantissa
print(output)
