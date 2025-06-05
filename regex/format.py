import re

name = input ("What is your name? ").strip()
# Here () is used for capturing or returning values
# Whitespace is made optional with ?
if matches := re.search(r"^(.+), ?(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello,{name}")


# if "," in name:
   # last, first = name.split(", ") # split at comma with one whitespace after
