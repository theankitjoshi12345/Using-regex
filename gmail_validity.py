import re

gmail = input("Enter your gmail: ")

if re.search(r"^[A-Za-z0-9\._]+@gmail\.com$", gmail):
    print("Valid")
else:
    print("Invalid")
