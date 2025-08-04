import re

name = input("Enter your name: ").strip()

if match := re.search(r"^([a-z]+), *([a-z]+)$", name, re.IGNORECASE):
    name = match.group(2) + " " + match.group(1)

print(f"Your name is {name}.")
