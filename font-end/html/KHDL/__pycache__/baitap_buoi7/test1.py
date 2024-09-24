def exponent_to_binary_sum(exp):
    binary_sum = []
    current_exp = 0

    while exp > 0:
        if exp % 2 == 1:
            binary_sum.append(f"2^{current_exp}")
        exp //= 2
        current_exp += 1

    binary_sum.reverse()
    return binary_sum

# Test
exponent = 35
binary_sum_representation = exponent_to_binary_sum(exponent)
print(f"The binary sum representation of 2^{exponent} is:")
print(" + ".join(binary_sum_representation))
