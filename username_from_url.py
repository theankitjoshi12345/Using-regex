import re

url = input("Enter URL: ")

if match := re.sub(r"(\w+)", url):
    # incomplete
