def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, 9):
        if (num>i):     
            if num % i == 0:
                return False
    return True 
for i in range(1000):
    if is_prime(i):
        if is_prime(i+2):
            print(f"({i}, {i+2})")