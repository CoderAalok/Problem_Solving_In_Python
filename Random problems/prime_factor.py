def prime_factors(n: int):
    if n <= 1:
        return -1
    
    x, i = n, 2
    factors = []
    while i <= x:
        if x % i == 0:
            factors.append(i)
            x //= i
        else:
            i += 1
    
    return factors
    
print(prime_factors(10))