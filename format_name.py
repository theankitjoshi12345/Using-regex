import re

name = input("Enter your name: ").strip()

if match := re.match(r"^([a-z]+), *([a-z]+)$", name, re.IGNORECASE):
    name = match.group(2).title() + " " + match.group(1).title()

print(f"Your name is {name}.")
