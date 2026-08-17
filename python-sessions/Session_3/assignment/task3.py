def prime_factors(num):
    factors = []
    for i in range(2, num + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    return factors
print(prime_factors(56))  
