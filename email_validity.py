import re

email = input("Enter your email: ").strip()

if re.search(r"^\w+@+\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
