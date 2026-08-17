def decimal_to_binary(num):
    if num < 0:
        return "Invalid input. Please enter a non-negative integer."
    elif num == 0:
        return "0"
    
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return binary

decimal_number = int(input("Enter a decimal number: "))
print(f"The binary representation of {decimal_number} is: {decimal_to_binary(decimal_number)}")