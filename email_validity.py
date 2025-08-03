import re

email = input("Enter your email: ")

if re.search(r"^\w+@+\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
