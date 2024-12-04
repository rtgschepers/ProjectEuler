from sympy import nextprime

primes = []
cur = 2
while cur < 2000000:
    primes.append(cur)
    cur = nextprime(cur)
print(sum(primes))
