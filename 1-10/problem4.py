from helpers import is_palindromic

high_prod = 0
for x in range(999, 100, -1):
    for y in range(x, 100, -1):
        product = x * y
        if product > high_prod and is_palindromic(product):
            high_prod = product
print(high_prod)
