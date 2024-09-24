def extended_gcd(a, N):
    x0, x1, b0, b1, i = N, a, 0, 1, 1

    while x1 > 1:
        y = x0 // x1
        x0, x1, b0, b1, i = x1, x0 - y * x1, b1, b0 - y * b1, i + 1

    if x0 == 0:
        return None
    else:
        return b1 if b1 > 0 else N + b1

# Test
a = 593
N = 7632
result = extended_gcd(a, N)

if result is None:
    print(f"Không tồn tại nghịch đảo modular cho {a} mod {N}")
else:
    print(f"Nghịch đảo modular của {a} mod {N} là {result}")
