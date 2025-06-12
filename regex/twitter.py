import re

# CRUDE
url = input("Enter URL: ").strip()

username1 = url.replace("https://twitter.com/", "")
print(f"Username One: {username1}")

# REGEX
username2 = re.sub(r"^https?://?(www\.)?twitter\.com/", "", url)
print(f"Username Two: {username2}")

# Cover instance where user doesn't enter twitter.com
# (?:) is used for www because we aren't using the group, hence (1) refers to username
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username Three: {matches.group(1)}")