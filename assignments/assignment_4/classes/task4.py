class prime_factors:
    def __init__(self, num):
        self.num = num

    def get_factors(self):
        factors = []
        for i in range(2, self.num + 1):
            while self.num % i == 0:
                factors.append(i)
                self.num //= i
        return factors
    
num_input = int(input("Enter a number: "))
instance = prime_factors(num_input)

result = instance.get_factors()
print(f"The prime factors of {num_input} are: {result}")