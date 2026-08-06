x = input("Enter your email: ")

if "@" in x and "." in x.split("@")[-1] and not x.startswith("@"):
    print("Valid email")
else:
    print("Invalid email")

if x.endswith(".com"):
    print("Commercial Domain")
elif x.endswith(".edu"):
    print("Educational Domain")
else:
    print("Other Domain")