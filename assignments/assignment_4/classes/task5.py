class NumberConverter:
    def __init__(self, decimal_num):
        self.decimal_num = decimal_num

    def decimal_to_binary(self):
        if self.decimal_num < 0:
            return "Invalid input. Please enter a non-negative integer."
        elif self.decimal_num == 0:
            return "0"
        
        binary = ""
        temp = self.decimal_num
        while temp > 0:
            binary = str(temp % 2) + binary
            temp //= 2
        return binary

user_input = int(input("Enter a decimal number: "))

converter = NumberConverter(user_input)

result = converter.decimal_to_binary()

print(f"The binary representation of {user_input} is: {result}")