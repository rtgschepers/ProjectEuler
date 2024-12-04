from helpers import is_divisible

total = 0
for x in range(1000):
    if is_divisible(x, 3) or is_divisible(x, 5):
        total += x
print(total)
