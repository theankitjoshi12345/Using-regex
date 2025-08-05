import re
url = input("Enter URL: ").strip()

'''
# Trying re.sub
username = re.sub(
    r"(?:https?://)?(?:www\.)?facebook\.com/", "", url
)
print(f"Your username is {username}")
'''

# Trying re.search
while True:
    if match := re.search(r"(?:https?://)?(?:www\.)?facebook\.com/([a-zA-Z0-9]+)", url, re.IGNORECASE):
        print(f"Your username is {match.group(1)}")
        break
    else:
        print("You did not enter it right. Try again.")
    url = input("Enter URL: ").strip()
