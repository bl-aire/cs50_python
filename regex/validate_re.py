import re

email = input("Enter your email: ").strip()

# .+ || ..*
# r"" needed here because we are using \ to escape . in .edu
if re.search(r".+@.+\.edu", email):
    print("Valid email")
else:
    print("Invalid email")