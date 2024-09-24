def modular_exponentiation(base, exponent, modulus):
    result = 1
    base = base % modulus  # Giảm bớt base nếu nó lớn hơn modulus

    while exponent > 0:
        # Nếu exponent lẻ, nhân result với base và lấy phần dư
        if exponent % 2 == 1:
            result = (result * base) % modulus

        # Chia exponent cho 2 và bình phương base, lấy phần dư
        exponent //= 2
        base = (base * base) % modulus

    return result

# Test
base = 475
exponent = 35
modulus = 893  # Số nguyên tố lớn, bạn có thể thay đổi theo nhu cầu

result = modular_exponentiation(base, exponent, modulus)
print(f"{base}^{exponent} mod {modulus} = {result}")
