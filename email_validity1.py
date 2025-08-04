import re

email = input("Enter your email: ")

if match := re.match(r"^(\w+)@(\w+)\.edu$", email, re.IGNORECASE):
    print("Valid")
    print(
        f"Username: {match.group(1).title()} \nDomain: {match.group(2).title()} ")
else:
    print("Invalid")
