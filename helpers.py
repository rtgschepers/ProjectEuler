def is_divisible(n: int, divider: int) -> bool:
    return n % divider == 0


def is_even(n: int) -> bool:
    return is_divisible(n, 2)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for x in range(2, n):
        if is_divisible(n, x):
            return False
    return True


def split_int(n: int) -> list[int]:
    list_n = []
    while n > 0:
        list_n.append(n % 10)
        n //= 10
    return list_n


def is_palindromic(arg) -> bool:
    if isinstance(arg, int):
        arg = split_int(arg)
    return arg == arg[::-1]
