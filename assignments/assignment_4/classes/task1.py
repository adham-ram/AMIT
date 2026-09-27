class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error: Division by zero"

calculator1 = calculator(int(input("Enter first number: ")), int(input("Enter second number: ")))
operation = input("Select operation: 1. Add 2. Subtract 3. Multiply 4. Divide: ")

if operation == "1":
    print(calculator1.add())
elif operation == "2":
    print(calculator1.subtract())
elif operation == "3":
    print(calculator1.multiply())
elif operation == "4":
    print(calculator1.divide())
else:
    print("Invalid operation")