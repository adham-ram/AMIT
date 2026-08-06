x = input("Enter a string: ")

def check(x):
    if x.startswith('r') or x.startswith('R'):
        print(x + " plays banjo")
    else:
        print(x + " does not play banjo")

check(x)