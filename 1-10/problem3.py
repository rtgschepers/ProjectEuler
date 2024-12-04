from helpers import is_prime, is_divisible

start = 600851475143
factors = []

while start > 1:
    for x in range(2, start + 1):
        if is_prime(x) and is_divisible(start, x):
            factors.append(x)
            start //= x
            break
print(max(factors))
