from helpers import is_divisible

x = 0
while True:
    x += 20
    divisible = True

    for i in range(19, 10, -1):
        if not is_divisible(x, i):
            divisible = False
            break

    if divisible:
        print(x)
        break
