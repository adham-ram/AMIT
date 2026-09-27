class multiply:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a * self.b
input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))
multiplication = multiply(input1, input2)
result = multiplication.calculate()
print(f"The result of multiplying {input1} and {input2} is: {result}")