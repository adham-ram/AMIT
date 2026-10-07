# def factorial(num: int) -> int:
#     """Calculates the factorial of a non-negative integer using recursion.

#     Args:
#         num (int): A non-negative integer whose factorial is to be calculated.

#     Returns:
#         int: The factorial of the given number. Returns 1 if num is 0 or 1.
#     """
#     # Base cases: Factorial of 0 and 1 is 1
#     if num == 0:
#         return 1
#     elif num == 1:
#         return 1
#     # Recursive case: Multiply num by the factorial of (num - 1)
#     else:
#         return num * factorial(num - 1)

# if __name__ == "__main__":
#     fact: int = factorial(5)
#     print(fact)  # Output: 120

from http.client import responses
import random
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm doing well, thanks!", "I'm just a bot, but I'm great!"],
}
def get_response(user_input):
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
def chatbot():
    print("Hello! I am a simple chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: I'm not sure how to respond to that.")
if __name__ == "__main__":  
    chatbot()