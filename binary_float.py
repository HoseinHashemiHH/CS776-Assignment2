

import math


def binary_float(decimal_number):
    # Use math.frexp to split the decimal into its mantissa and exponent
    mantissa, exponent = math.frexp(decimal_number)
    # Convert the mantissa and exponent to binary strings
    mantissa_binary = bin(int(mantissa * 2**53))  # 53 is the mantissa length for a double-precision float
    exponent_binary = bin(exponent)

    # Combine the binary strings
    binary_representation = mantissa_binary + "e" + exponent_binary

    return (binary_representation)
