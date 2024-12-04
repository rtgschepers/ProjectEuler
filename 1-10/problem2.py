from helpers import is_even

a = 1
b = 1
total = 0

while a < 4000000:
    b, a = a, a + b
    if is_even(a):
        total += a
print(total)
