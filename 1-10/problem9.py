import math

for b in range(500):
    for a in range(b):
        c = math.sqrt(pow(a, 2) + pow(b, 2))
        if c.is_integer() and a < b < c and a + b + c == 1000:
            print(int(a * b * c))
            exit(0)
