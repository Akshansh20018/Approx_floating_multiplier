def float_to_ieee(num):
    # Check if the number is negative
    if num < 0:
        sign_bit = 1
        num *= -1
    else:
        sign_bit = 0
    
    # Convert the number to binary
    integer_part = int(num)
    fractional_part = num - integer_part
    
    integer_binary = bin(integer_part)[2:]
    fractional_binary = ''
    
    while fractional_part != 0:
        fractional_part *= 2
        if fractional_part >= 1:
            fractional_binary += '1'
            fractional_part -= 1
        else:
            fractional_binary += '0'
    
    # Combine the integer and fractional binary parts
    binary = integer_binary + '.' + fractional_binary
    
    # Calculate the exponent and mantissa
    exponent = 0
    
    if '.' in binary:
        integer_bits, fractional_bits = binary.split('.')
        exponent = len(integer_bits) - 1
        mantissa = fractional_bits
    else:
        mantissa = binary[1:]
    
    # Add the bias to the exponent
    bias = 127
    exponent += bias
    
    # Convert the exponent to binary
    exponent_binary = bin(exponent)[2:].zfill(8)
    
    # Convert the mantissa to binary
    mantissa_binary = ''
    for i in range(23):
        if i < len(mantissa):
            mantissa_binary += mantissa[i]
        else:
            mantissa_binary += '0'
    
    # Combine the sign bit, exponent, and mantissa
    binary_string = str(sign_bit) + exponent_binary + mantissa_binary
    
    # Convert the binary string to hexadecimal
    hex_string = hex(int(binary_string, 2))[2:].zfill(8)
    
    return binary_string

def bin_to_int(num):
    ans = 0
    for i in range(len(num)):
        ans += int(num[i])*(2**(len(num)-i-1))
    return ans
print(bin_to_int('111'))
